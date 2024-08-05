from flask import Flask
from .configs import LocalConfig, file_path
from .extensions import db, migrate, admin_manager, login_manager, babel, cors, api, toolbar, mail, bcrypt, oauth, jwt
from .admin import AdminView, LogoutView, UploadFileView, AnalyticsView, CategoryView, UserView, CourseView, TagView, LessonView
from .resources import category_ns, course_ns, user_ns, token_ns
from .models import Category, User, Course, Tag, Lesson
    
def create_app(config_class=LocalConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    cors.init_app(app=app, resources={r"/*": {"origins": "*"}})
    bcrypt.init_app(app=app)
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    jwt.init_app(app=app)
    toolbar.init_app(app=app)
    
    oauth.init_app(app=app)
    oauth.register(
        name='google',
        server_metadata_url=LocalConfig.CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        },
        client_id=LocalConfig.GOOGLE_CLIENT_ID,
        client_secret=LocalConfig.GOOGLE_CLIENT_SECRET,
        redirect_uri=LocalConfig.REDIRECT_URI
    )
        
    login_manager.init_app(app=app)
    babel.init_app(app=app)
    mail.init_app(app=app)

    api.init_app(app=app)
    api.add_namespace(category_ns)
    api.add_namespace(course_ns)
    api.add_namespace(user_ns)
    api.add_namespace(token_ns)
    
    from . import models

    admin_manager.init_app(app=app, index_view=AdminView())
    admin_manager.add_view(CategoryView(Category, db.session, category="Management"))
    admin_manager.add_view(UserView(User, db.session, category="Management"))
    admin_manager.add_view(CourseView(Course, db.session, category="Management"))
    admin_manager.add_view(LessonView(Lesson, db.session, category="Management"))
    admin_manager.add_view(TagView(Tag, db.session, category="Management"))
    admin_manager.add_view(AnalyticsView(name="Analytics & Statistics", endpoint="analytics-statistics"))
    admin_manager.add_view(UploadFileView(file_path, "/static/", name="Files", category="Settings", endpoint="files"))
    admin_manager.add_view(LogoutView(name="Log Out", category="Settings", endpoint="logout"))

    return app