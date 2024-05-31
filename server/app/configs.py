import os
import cloudinary
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    load_dotenv()

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, 'database', 'ecourse.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_ADMIN_SWATCH = 'lux'

    cloudinary.config(
        cloud_name=os.environ.get('CLOUD_NAME'),
        api_key=os.environ.get('API_KEY'),
        api_secret=os.environ.get('API_SECRET')
    )
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')
