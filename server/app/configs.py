import os, os.path as op, cloudinary, secrets
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

base_dir = op.abspath(op.dirname(__file__))
file_path = op.join(op.dirname(__file__), "static")

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
    
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = secrets.token_hex(32)
    JWT_SECRET_KEY = secrets.token_urlsafe(32)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    FLASK_ADMIN_SWATCH = 'lux'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_SIZE = 10
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SWAGGER_UI_OAUTH_APP_NAME = 'eCourse 🎓'
    
    cloudinary.config(
        cloud_name=os.environ.get('CLOUD_NAME'),
        api_key=os.environ.get('API_KEY'),
        api_secret=os.environ.get('API_SECRET')
    )

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4'
    DEVELOPMENT = True
    DEBUG = True
    DEBUG_TB_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    BUNDLE_ERRORS = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'database', 'ecourse.sqlite3')
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False