from flask_restx import Namespace, fields, reqparse
from werkzeug.datastructures import FileStorage

category_api = Namespace('categories', description='Category operations', ordered=True)
course_api = Namespace('courses', description='Course operations', ordered=True)
lesson_api = Namespace('lessons', description='Lesson operations', ordered=True)
user_api = Namespace('users', description='User operations', ordered=True)
token_api = Namespace('token', description='Token operations', ordered=True)

base_model = category_api.model('Base Model', {
    'id': fields.Integer(readonly=True, description='Unique ID'),
    'is_active': fields.Boolean(description='Active'),
    'date_created': fields.DateTime(dt_format='iso8601'),
})

category = category_api.inherit('Category List', base_model, {
    'name': fields.String,
})

common_model = course_api.inherit('Common Model', base_model, {
    'subject': fields.String,
    'image': fields.String,
    'tags': fields.List(fields.String, description='List of tags')
})

courses = course_api.inherit('Course List', common_model, {
    'price': fields.Float,
    'category': fields.String
})

lessons = course_api.inherit('Lesson List', common_model, {
    'course': fields.String,
})

course = course_api.inherit('Course', courses, {
    'description': fields.String,
})

lesson = lesson_api.inherit('Lesson', common_model, {
    'content': fields.String,
})

login_model = token_api.model('Log In', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

user = user_api.inherit('User', login_model, {
    'username': fields.String(required=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'avatar': fields.String(required=False),
    'phone': fields.String(required=False)
})

current_user = user_api.inherit('Current User', user, {
    'last_seen': fields.String(required=False)
})

user_parser = user_api.parser()
user_parser.add_argument('email', type=str, help='Email', location='form')
user_parser.add_argument('password', type=str, help='Password', location='form')
user_parser.add_argument('username', type=str, help='Username', location='form')
user_parser.add_argument('first_name', type=str, help='First Name', location='form')
user_parser.add_argument('last_name', type=str, help='Last Name', location='form')
user_parser.add_argument('phone', type=int, help='Phone', location='form')
user_parser.add_argument('avatar', type=FileStorage, location='files')

course_parser = reqparse.RequestParser()
course_parser.add_argument('category', type=int, required=False, help='Category ID')
course_parser.add_argument('keyword', type=str, required=False, help='Search keyword')
course_parser.add_argument('from_price', type=float, required=False, help='Minimum price')
course_parser.add_argument('to_price', type=float, required=False, help='Maximum price')
course_parser.add_argument('page', type=int, required=False, default=1, help='Page number')
course_parser.add_argument('latest', type=bool, required=False, default=False, help='Filter by latest products (true/false)')
