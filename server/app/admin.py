import os
import os.path as op
from flask import session, request, g
from flask_admin import Admin
from flask_babel import Babel
from app import app, db
from .views import (
    CategoryView, TagView, AdminView, AnalyticsView, 
    UploadFileView, UserView, InstructorView, CourseView,
    CommentView, LessonView, LikeView, LogoutView,
    OrderView, RatingView, ResourceView
)
from .models import (
    Category, Course, Tag, Lesson, User, Instructor,
    Resource, Order, Like, Rating, Comment
)

path = op.join(op.dirname(__file__), "static")

try:
    os.mkdir(path)
except OSError:
    pass


def get_locale():
    if request.args.get("lang"):
        session["lang"] = request.args.get("lang")
    return session.get("lang", "en")


def get_timezone():
    user = getattr(g, "user", None)
    if user is not None:
        return user.timezone


babel = Babel(app=app, locale_selector=get_locale, timezone_selector=get_timezone)
admin = Admin(app=app, name="eCourse", template_mode="bootstrap4",
              index_view=AdminView())

admin.add_view(UserView(User, db.session, category="Management"))
admin.add_view(InstructorView(Instructor, db.session, category="Management"))
admin.add_view(CategoryView(Category, db.session, category="Management"))
admin.add_view(CourseView(Course, db.session, category="Management"))
admin.add_view(LessonView(Lesson, db.session, category="Management"))
admin.add_view(ResourceView(Resource, db.session, category="Management"))
admin.add_view(TagView(Tag, db.session, category="Management"))
admin.add_view(OrderView(Order, db.session, category="Management"))
admin.add_view(CommentView(Comment, db.session, category="Management"))
admin.add_view(RatingView(Rating, db.session, category="Management"))
admin.add_view(LikeView(Like, db.session, category="Management"))
admin.add_view(AnalyticsView(name="Analytics & Statistics",
               endpoint="analytics-statistics"))
admin.add_view(UploadFileView(path, "/static/", name="Files",
               category="Settings", endpoint="files"))
admin.add_view(LogoutView(
    name="Log Out", category="Settings", endpoint="logout"))
