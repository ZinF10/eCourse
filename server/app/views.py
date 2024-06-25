from flask import redirect, flash
from flask_admin import expose, AdminIndexView, BaseView
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_login import current_user, logout_user
from flask_babel import gettext
from flask_admin.actions import action
from app import db, dao, decorators
from .models import (
    Resource, Course, Lesson, Tag
)
from .widgets import CKTextAreaField


cdn_ckeditor = ['//cdn.ckeditor.com/4.6.0/full-all/ckeditor.js']

class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()


class BaseModelView(ModelView):
    column_list = ["active", "date_created"]
    column_filters = ["active", "date_created"]
    column_editable_list = ["active"]
    column_sortable_list = ["date_created"]
    create_modal = True
    edit_modal = True
    can_view_details = True
    can_export = True
    page_size = 10
    can_delete = True

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()
    
    def __init__(self, model, session, *args, **kwargs):
        super(BaseModelView, self).__init__(model, session, *args, **kwargs)
    
    def render(self, *args, **kwargs):
        return super(BaseModelView, self).render(*args, **kwargs)


class ActionsView(BaseModelView):
    @action('change_active', 'Change Active', 'Are you sure you want to change the active status of selected models?')
    def action_change_active(self, ids):
        try:
            query = self.get_query().filter(self.model.id.in_(ids))

            for model in query.all():
                model.active = not model.active if model else True

            db.session.commit()
            flash(gettext('Successfully to change active.'), category='success')
        except Exception as e:
            flash(gettext(f'Failed to change activate. {
                  str(e)}'), category='error')

class UserView(ActionsView):
    column_list = ["username", "role"] + ActionsView.column_list
    column_searchable_list = ["username", "email"]
    column_editable_list = ["username", "role"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["username"] + \
        ActionsView.column_sortable_list
    column_filters = ["role"] + ActionsView.column_filters
    

class InstructorView(BaseModelView):
    column_list = ["user", "bio"]
    column_filters = ["user"]
    column_editable_list = ["user"]
    column_sortable_list = ["user"]


class CategoryView(ActionsView):
    column_list = ["name"] + ActionsView.column_list
    inline_models = [Course]
    column_searchable_list = ["name"]
    column_editable_list = ["name"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["name"] + ActionsView.column_sortable_list


class CourseView(ActionsView):
    column_list = ["subject", "price", "category"
            ] + ActionsView.column_list
    inline_models = [Lesson, Tag]
    column_searchable_list = ["subject"]
    column_editable_list = ["subject", "price", "category"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["subject", "price"] + \
        ActionsView.column_sortable_list
    column_filters = ["price"] + ActionsView.column_filters
    extra_js = cdn_ckeditor
    
    form_overrides = {
        'description': CKTextAreaField
    }


class TagView(ActionsView):
    column_list = ["name", "course", "lesson"] + ActionsView.column_list
    column_searchable_list = ["name"]
    column_editable_list = ["name"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["name"] + ActionsView.column_sortable_list


class LessonView(ActionsView):
    column_list = ["subject", "course"] + ActionsView.column_list
    inline_models = [Tag, Resource]
    column_searchable_list = ["subject"]
    column_editable_list = ["subject", "course",
                    ] + ActionsView.column_editable_list
    column_sortable_list = ["subject"] + ActionsView.column_sortable_list
    extra_js = cdn_ckeditor
    form_overrides = {
        'content': CKTextAreaField
    }


class ResourceView(ActionsView):
    column_list = ["url", "name", "lesson"] + ActionsView.column_list
    column_searchable_list = ["url", "name"]
    column_editable_list = ["url", "name", "lesson"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["url", "name", "lesson"] + \
        ActionsView.column_sortable_list


class OrderView(ActionsView):
    column_list = ["user", "details"] + ActionsView.column_list
    column_editable_list = ["user"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["user"] + \
        ActionsView.column_sortable_list


class OrderDetailView(ActionsView):
    column_list = ["order", "course"] + ActionsView.column_list
    column_editable_list = ["order", "course"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["order", "course"] + \
        ActionsView.column_sortable_list


class CommentView(ActionsView):
    column_list = ["user", "course", "content"] + ActionsView.column_list
    column_editable_list = ["user", "course", "content"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["user", "course", "content"] + \
        ActionsView.column_sortable_list


class RatingView(ActionsView):
    column_list = ["user", "course", "rate"] + ActionsView.column_list
    column_editable_list = ["user", "course", "rate"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["user", "course", "rate"] + \
        ActionsView.column_sortable_list


class LikeView(BaseModelView):
    column_list = ["user", "course", "liked", "date_created"]
    column_editable_list = ["user", "course", "liked", "date_created"]
    column_sortable_list = ["user", "course", "liked", "date_created"]
    column_filters = ["liked", "date_created"]


class UploadFileView(FileAdmin, AuthenticatedView):
    def is_accessible(self):
        return AuthenticatedView.is_accessible(self=self)


class AnalyticsView(AuthenticatedView):
    @expose("/")
    def index(self):
        return self.render("admin/analytics.html")


class AdminView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html', categories=dao.stats_courses())


class LogoutView(AuthenticatedView):
    @decorators.admin_member_required
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')
