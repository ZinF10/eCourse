from flask import redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_admin import expose, AdminIndexView, BaseView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.actions import action
from flask_admin.form import SecureForm
from wtforms import FileField
from flask_login import current_user, logout_user
from markupsafe import Markup
from ..config import DevelopmentConfig
from ..dao import stats_courses, count_courses
from ..utils.decorators import admin_member_required
from .widgets import CKTextAreaField
from ..models import Tag, Lesson, Order
from ..utils.helpers import upload_image
from .actions import view_json, change_active

cdn_ckeditor = ['//cdn.ckeditor.com/4.6.0/full-all/ckeditor.js']

class AuthView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin_login', next=request.url)) 


class AdminView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html', 
                        categories=stats_courses(),
                        total_courses=count_courses())


class LogoutView(AuthView):
    @admin_member_required
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


class AnalyticsAdmin(AuthView):
    @expose("/")
    def index(self):
        return self.render("admin/analytics.html", 
                        categories=stats_courses(),
                        total_courses=count_courses())


class ProfileView(AuthView):
    @expose("/")
    def index(self):
        return self.render("admin/profile.html")


class UploadFileView(FileAdmin, AuthView):
    pass
    
class BaseModelView(AuthView, ModelView):
    form_base_class = SecureForm
    column_labels = {
        "is_active": "Active",
    }
    column_list = ["is_active", "date_created"]
    column_filters = ["is_active"]
    column_editable_list = ["is_active"]
    column_sortable_list = ["date_created"]
    create_modal = True
    edit_modal = True
    can_view_details = True
    can_export = True
    can_delete = True
    page_size = DevelopmentConfig.PAGE_SIZE   
    
    @action('change_active', 'Change Active', 'Are you sure you want to change the active status of selected models?')
    def action_active(self, ids):
        return change_active(self=self, ids=ids)
    
    @action('view_json', 'View JSON', 'Are you sure you want to view JSON data for the selected items?')
    def view_json(self, ids):
        return view_json(self=self, ids=ids)
       
        
class CategoryAdmin(BaseModelView):
    column_list = ["name", "courses"] + BaseModelView.column_list
    column_sortable_list = ["name"] + BaseModelView.column_sortable_list
    column_editable_list = ["name"] + BaseModelView.column_editable_list
    

class BaseCustomView(BaseModelView):
    extra_js = cdn_ckeditor
    
    form_overrides = {
        'description': CKTextAreaField,
        'image': FileField
    }

    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return '-Empty-'
        return Markup(f'<img src="{model.image}" alt="{model.subject}" width="80" height="80" class="img-thumbnail rounded-circle shadow" />')

    column_formatters = {'image': _list_thumbnail}

    def on_model_change(self, form, model, is_created):
        if form.image.data:
            file_data = form.image.data
            if file_data and hasattr(file_data, 'filename') and file_data.filename != '':
                try:
                    file_data.seek(0)
                    model.image = upload_image(file_data=file_data)
                except:
                    model.image = None
        super(BaseCustomView, self).on_model_change(form, model, is_created)


class CourseAdmin(BaseCustomView):
    column_list = ["subject", "image", "price", "category"
            ] + BaseCustomView.column_list
    inline_models = [Lesson, Tag]
    column_searchable_list = ["subject"]
    column_editable_list = ["subject", "price", "category"] + \
        BaseCustomView.column_editable_list
    column_sortable_list = ["subject", "price"] + \
        BaseCustomView.column_sortable_list
    column_filters = ["price"] + BaseCustomView.column_filters


class LessonAdmin(BaseCustomView):
    column_list = ["subject", "image", "course"
            ] + BaseCustomView.column_list
    column_searchable_list = ["subject"]
    column_editable_list = ["subject", "course"] + \
        BaseCustomView.column_editable_list
    column_sortable_list = ["subject"] + \
        BaseCustomView.column_sortable_list
        
    
class TagAdmin(BaseModelView):
    column_list = ["name", "courses"] + BaseModelView.column_list
    column_sortable_list = ["name"] + BaseModelView.column_sortable_list
    column_editable_list = ["name"] + BaseModelView.column_editable_list


class UserAdmin(BaseModelView):
    column_labels = {
        **BaseCustomView.column_labels,
        "is_admin": "Admin",
    }
    column_list = ["username", "email", 'password', "is_admin"] + BaseModelView.column_list
    inline_models = [Order]
    column_searchable_list = ["username", "email"]
    column_editable_list = ["username", "is_admin"] + \
        BaseModelView.column_editable_list
    column_sortable_list = ["username"] + \
        BaseModelView.column_sortable_list
    column_filters = ["is_admin"] + BaseModelView.column_filters
    column_exclude_list = ['password']