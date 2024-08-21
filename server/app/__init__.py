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

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

api.init_app(app=app)
db.init_app(app=app)
babel.init_app(app=app)

jwt = JWTManager(app=app)
cors = CORS(app=app, resources={r"/*": {"origins": "*"}})
login_manager = LoginManager(app=app)
migrate = Migrate(app=app, db=db, render_as_batch=False)

admin_manager.init_app(app=app)
cache.init_app(app=app)
toolbar = DebugToolbarExtension(app=app)

from .models import (
    Category, Course, Lesson, Tag, 
    lesson_tag, course_tag, User, Order,
    Order, OrderDetail, Like, Comment, 
    Resource, Rating
)