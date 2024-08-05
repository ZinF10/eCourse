from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from flask_babel import Babel
from flask_restx import Api
from flask_cors import CORS
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from authlib.integrations.flask_client import OAuth
from .utils import get_locale
from .configs import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

bcrypt = Bcrypt()
login_manager = LoginManager()
cors = CORS()
authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    },
    'oauth2': {
        'type': 'oauth2',
        'flow': 'implicit',
        'authorizationUrl': 'https://idp.example.com/authorize?audience=https://app.example.com',
        'clientId': Config.SWAGGER_UI_OAUTH_CLIENT_ID,
        'scopes': {
            'openid': 'Get ID token',
            'profile': 'Get identity',
            'read': 'Grant read-only access',
            'write': 'Grant read-write access',
        }
    }
}
api = Api(
    contact="zin.it.dev@gmail.com",
    contact_email="zin.it.dev@gmail.com",
    version='1.0',
    title=Config.SWAGGER_UI_OAUTH_APP_NAME,
    description='APIs for eCourse 🎓',
    license='Apache 2.0',
    terms_url='https://www.google.com/policies/terms/',
    security=['apikey', {'oauth2': ['read', 'write']}],
    authorizations=authorizations,
    validate=True,
    ordered=True
)
admin_manager = Admin(name=Config.SWAGGER_UI_OAUTH_APP_NAME, template_mode='bootstrap4')
babel = Babel(locale_selector=get_locale)
toolbar = DebugToolbarExtension()
mail = Mail()
oauth = OAuth()