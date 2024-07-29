from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from flask_babel import Babel
from flask_restx import Api
from flask_cors import CORS
from .utils import get_locale, get_timezone
from .configs import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
cors = CORS()
api = Api(
    contact="zin.it.dev@gmail.com",
    contact_email="zin.it.dev@gmail.com",
    version='1.0',
    title=Config.SWAGGER_UI_OAUTH_APP_NAME,
    description='APIs for eCourse 🎓',
    license='Apache 2.0',
    terms_url='https://www.google.com/policies/terms/',
    security={'OAuth2': ['read', 'write']},
    authorizations={
        'OAuth2': {
            'type': 'oauth2',
            'flow': 'implicit',
            'authorizationUrl': 'https://idp.example.com/authorize?audience=https://app.example.com',
            'clientId': Config.SWAGGER_UI_OAUTH_CLIENT_ID,
            'scopes': {
                'openid': 'Get ID token',
                'profile': 'Get identity',
            }
        }
    },
    validate=True,
    ordered=True
)
admin_manager = Admin(name='eCourse', template_mode='bootstrap4')
babel = Babel(locale_selector=get_locale, timezone_selector=get_timezone)