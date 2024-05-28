from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import configs

app = Flask(__name__)
app.config.from_object(configs.Config)
db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)

with app.app_context():
    from app import models