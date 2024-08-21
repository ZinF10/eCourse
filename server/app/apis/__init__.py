from flask_restx import Api
from .categories import category_api
from .coures import course_api
from .lessons import lesson_api
from .users import user_api
from .token import token_api
from ..config import Config

authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
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

api.add_namespace(category_api)
api.add_namespace(course_api)
api.add_namespace(lesson_api)
api.add_namespace(user_api)
api.add_namespace(token_api)