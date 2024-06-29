from flask_restx import Namespace, fields, reqparse
from werkzeug.datastructures import FileStorage

token_ns = Namespace(
    name='token',
    description='Operations related to token'
)
category_ns = Namespace(
    name='categories',
    description='Operations related to categories'
)
course_ns = Namespace(
    name='courses',
    description='Operations related to courses'
)
lesson_ns = Namespace(
    name='lessons',
    description='Operations related to lessons'
)
user_ns = Namespace(
    name='users',
    description='Operations related to users'
)
order_ns = Namespace(
    name='orders',
    description='Operations related to orders of current user'
)

user_model = user_ns.model('User', {
    'username': fields.String(required=True, description='The username'),
    'email': fields.String(required=True, description='The email'),
    'password': fields.String(required=True, description='The password'),
    'first_name': fields.String(required=True, description='The first name'),
    'last_name': fields.String(required=True, description='The last name'),
    'avatar': fields.String(required=False, description='The avatar')
})

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True)
user_parser.add_argument('email', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)
user_parser.add_argument('first_name', type=str, required=True)
user_parser.add_argument('last_name', type=str, required=True)
user_parser.add_argument('avatar', location='files',
                         type=FileStorage, required=False)
