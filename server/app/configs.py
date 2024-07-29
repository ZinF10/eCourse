import os, os.path as op, cloudinary
from dotenv import load_dotenv

load_dotenv()
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')

base_path = op.join(op.dirname(__file__), "static")

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{
        DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_ADMIN_SWATCH = 'lux'
    PAGE_SIZE = 10
    SWAGGER_UI_OAUTH_APP_NAME = 'eCourse 🎓'
    SWAGGER_UI_OAUTH_CLIENT_ID = ''
    BUNDLE_ERRORS = True
    
    cloudinary.config(
        cloud_name=os.environ.get('CLOUD_NAME'),
        api_key=os.environ.get('API_KEY'),
        api_secret=os.environ.get('API_SECRET')
    )
    
class LocalConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
