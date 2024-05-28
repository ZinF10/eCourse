from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from .models import Category, Course


class BaseView(ModelView):
    column_list = ["active", "date_created"]
    column_filters = ["active", "date_created"]
    create_modal = True
    edit_modal = True
    can_view_details = True
    can_export = True
    page_size = 10
    column_editable_list = ["active"]


class CategoryView(BaseView):
    column_list = ["name", "courses"] + BaseView.column_list
    inline_models = [Course]
    column_searchable_list = ["name"]
    column_editable_list = ["name", "courses"] + BaseView.column_editable_list


class CourseView(BaseView):
    column_list = ["subject", "category"] + BaseView.column_list
    column_searchable_list = ["subject"]
    column_editable_list = ["subject", "category"] + \
        BaseView.column_editable_list


admin = Admin(app, name="eCourse", template_mode="bootstrap4")

admin.add_view(CategoryView(Category, db.session, category="Management"))
admin.add_view(CourseView(Course, db.session, category="Management"))
