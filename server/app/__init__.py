from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_jwt_extended import JWTManager
from .config import DevelopmentConfig
from .models import db
from .apis import api
from .admin import admin_manager, babel
from .services.caching import cache

jwt = JWTManager()
login_manager = LoginManager()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app=app)
    cache.init_app(app=app)
    babel.init_app(app=app)
    
    Migrate(app=app, db=db, render_as_batch=False)
    CORS(app=app, resources={r"/*": {"origins": "*"}})
    
    jwt.init_app(app=app)
    login_manager.init_app(app=app)
    api.init_app(app=app)
    admin_manager.init_app(app=app)
    
    DebugToolbarExtension(app=app)
    
    from .models import (
        Category, Course, Lesson, Tag, 
        lesson_tag, course_tag, User, Order,
        Order, OrderDetail, Like, Comment, 
        Resource, Rating
    )
    
    return app