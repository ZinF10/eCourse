from flask import Flask
from .configs import LocalConfig, file_path
from .extensions import migrate, admin_manager, login_manager, babel, cors, api, toolbar, mail
from .admin import AdminView, LogoutView, UploadFileView, AnalyticsView, CategoryView, UserView, CourseView, TagView
from .models import db, Category, User, Course, Tag
from .resources import category_ns, course_ns, user_ns

def create_app(config_class=LocalConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    cors.init_app(app=app, resources={r"/*": {"origins": "*"}})
    
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    toolbar.init_app(app=app)
    
    login_manager.init_app(app=app)
    babel.init_app(app=app)
    mail.init_app(app=app)

    api.init_app(app=app)
    api.add_namespace(category_ns)
    api.add_namespace(course_ns)
    api.add_namespace(user_ns)

    with app.app_context():
        from . import models
        
    admin_manager.init_app(app=app, index_view=AdminView())
    admin_manager.add_view(CategoryView(Category, db.session, category="Management"))
    admin_manager.add_view(UserView(User, db.session, category="Management"))
    admin_manager.add_view(CourseView(Course, db.session, category="Management"))
    admin_manager.add_view(TagView(Tag, db.session, category="Management"))
    admin_manager.add_view(AnalyticsView(name="Analytics & Statistics", endpoint="analytics-statistics"))
    admin_manager.add_view(UploadFileView(file_path, "/static/", name="Files", category="Settings", endpoint="files"))
    admin_manager.add_view(LogoutView(name="Log Out", category="Settings", endpoint="logout"))

    return app