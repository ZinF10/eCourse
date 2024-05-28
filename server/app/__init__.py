from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app import configs

app = Flask(__name__)
app.config.from_object(configs.Config)
db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)
login_manager = LoginManager(app=app)

with app.app_context():
    from app import models