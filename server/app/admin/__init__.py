from flask_admin import Admin
from flask_babel import Babel
from ..configs import file_path, Config
from ..models import db, Category, Course, Lesson, Tag, User
from .admin import (
    AdminView, CategoryAdmin, AnalyticsAdmin, CourseAdmin, UserAdmin,
    LessonAdmin, TagAdmin, LogoutView, UploadFileView, ProfileView
)
from ..utils.helpers import get_locale

babel = Babel(locale_selector=get_locale)

admin_manager = Admin(name=Config.SWAGGER_UI_OAUTH_APP_NAME, template_mode='bootstrap4', index_view=AdminView())
admin_manager.add_view(CategoryAdmin(Category, db.session, category="Management"))
admin_manager.add_view(CourseAdmin(Course, db.session, category="Management"))
admin_manager.add_view(LessonAdmin(Lesson, db.session, category="Management"))
admin_manager.add_view(UserAdmin(User, db.session, category="Management"))
admin_manager.add_view(TagAdmin(Tag, db.session, category="Management"))
admin_manager.add_view(AnalyticsAdmin(name="Analytics & Statistics", endpoint="analytics-statistics"))
admin_manager.add_view(UploadFileView(file_path, "/static/", name="Files", category="Settings", endpoint="files"))
admin_manager.add_view(ProfileView(name="Profile", category="Settings", endpoint="profile"))
admin_manager.add_view(LogoutView(name="Log Out", category="Settings", endpoint="logout"))