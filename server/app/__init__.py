from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from app import configs
from .api import Api

app = Flask(__name__)
app.config.from_object(configs.LocalConfig)
CORS(app=app, resources={r"/*": {"origins": "*"}})
cache = Cache(app=app)
mail = Mail(app=app)
api = Api(
    app=app,
    contact="zin.it.dev@gmail.com",
    contact_email="zin.it.dev@gmail.com",
    version='3.0.0',
    title='eCourse - Swagger UI',
    description='RESTful APIs for eCourse application 🌶️',
    doc="/",
    license='Apache 2.0',
    terms_url='https://www.google.com/policies/terms/'
)
jwt = JWTManager(app=app)
ma = Marshmallow(app)
db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)
login_manager = LoginManager(app=app)

toolbar = DebugToolbarExtension(app=app)

with app.app_context():
    from app import models
