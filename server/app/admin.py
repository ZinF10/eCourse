import os
import os.path as op
from flask import session, request, g, redirect, flash, url_for
from flask_admin import Admin, expose, AdminIndexView, BaseView, form
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_login import current_user, logout_user
from flask_admin.form.upload import ImageUploadField
from markupsafe import Markup
from flask_babel import Babel, gettext
from flask_admin.actions import action
from app import app, db, dao, decorators
from .models import (
    Category, Course, Tag, Lesson, User, Instructor,
    Resource, Order, Like, Rating, Comment, OrderDetail
)


path = op.join(op.dirname(__file__), "static")
images_path = op.join(op.dirname(__file__),
                      f"static/uploads/images/")

try:
    os.mkdir(path)
    os.mkdir(images_path)
except OSError:
    pass


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

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()


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
    column_list = ["username", "email", "role"] + ActionsView.column_list
    column_searchable_list = ["username", "email"]
    column_editable_list = ["username", "email", "role"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["username", "email"] + \
        ActionsView.column_sortable_list
    column_filters = ["role"] + ActionsView.column_filters
    

class InstructorView(BaseModelView):
    column_list = ["user", "bio"]
    column_filters = ["user"]
    column_editable_list = ["user"]
    column_sortable_list = ["user"]


class CategoryView(ActionsView):
    column_list = ["name", "courses"] + ActionsView.column_list
    inline_models = [Course]
    column_searchable_list = ["name"]
    column_editable_list = ["name", "courses"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["name"] + ActionsView.column_sortable_list


class ImageView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return '-Empty-'
        return Markup(f'<img src="{url_for('static', filename=f"uploads/images/{form.thumbgen_filename(model.image)}")}" alt="{model.subject}" width="80" height="80" class="img-thumbnail rounded-circle shadow" />')

    column_formatters = {
        'image': _list_thumbnail
    }

    form_extra_fields = {
        'image': ImageUploadField('Image',
                                  base_path=images_path,
                                  thumbnail_size=(100, 100, True)
                                )
    }

class CourseView(ActionsView, ImageView):
    column_list = ["subject", "image", "price", "category",
                   "tags"] + ActionsView.column_list
    inline_models = [Lesson, Tag]
    column_searchable_list = ["subject"]
    column_editable_list = ["subject", "price", "category", "tags"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["subject", "price"] + \
        ActionsView.column_sortable_list
    column_filters = ["price"] + ActionsView.column_filters


class TagView(ActionsView):
    column_list = ["name", "courses"] + ActionsView.column_list
    column_searchable_list = ["name"]
    column_editable_list = ["name", "courses"] + \
        ActionsView.column_editable_list
    column_sortable_list = ["name"] + ActionsView.column_sortable_list


class LessonView(ActionsView):
    column_list = ["title", "course", "tags",
                   "resources"] + ActionsView.column_list
    inline_models = [Tag, Resource]
    column_searchable_list = ["title"]
    column_editable_list = ["title", "course",
                            "tags", "resources"] + ActionsView.column_editable_list
    column_sortable_list = ["title"] + ActionsView.column_sortable_list


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
    pass


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


def get_locale():
    if request.args.get("lang"):
        session["lang"] = request.args.get("lang")
    return session.get("lang", "en")


def get_timezone():
    user = getattr(g, "user", None)
    if user is not None:
        return user.timezone


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)
admin = Admin(app, name="eCourse", template_mode="bootstrap4",
              index_view=AdminView())

admin.add_view(UserView(User, db.session, category="Management"))
admin.add_view(InstructorView(Instructor, db.session, category="Management"))
admin.add_view(CategoryView(Category, db.session, category="Management"))
admin.add_view(CourseView(Course, db.session, category="Management"))
admin.add_view(LessonView(Lesson, db.session, category="Management"))
admin.add_view(ResourceView(Resource, db.session, category="Management"))
admin.add_view(TagView(Tag, db.session, category="Management"))
admin.add_view(OrderView(Order, db.session, category="Management"))
admin.add_view(OrderDetailView(OrderDetail, db.session, category="Management"))
admin.add_view(CommentView(Comment, db.session, category="Management"))
admin.add_view(RatingView(Rating, db.session, category="Management"))
admin.add_view(LikeView(Like, db.session, category="Management"))
admin.add_view(AnalyticsView(name="Analytics & Statistics",
               endpoint="analytics-statistics"))
admin.add_view(UploadFileView(path, "/static/", name="Files",
               category="Settings", endpoint="upload-file"))
admin.add_view(LogoutView(
    name="Log Out", category="Settings", endpoint="logout"))
