from flask_restx import fields, reqparse
from werkzeug.datastructures import FileStorage
from .extensions import api

base_model = api.model('Base Model', {
    'id': fields.Integer(readonly=True, description='Unique ID'),
    'active': fields.Boolean(description='Active'),
    'date_created': fields.DateTime(dt_format='iso8601'),
})

category_model = api.inherit('Category', base_model, {
    'name': fields.String,
})

common_model = api.inherit('Common Model', base_model, {
    'subject': fields.String,
    'image': fields.String,
    'tags': fields.List(fields.String, description='List of tags')
})

course_model = api.inherit('Course', common_model, {
    'price': fields.Float,
    'category': fields.String
})

lesson_model = api.inherit('Lesson', common_model, {
    'course': fields.String,
})

course_details_model = api.inherit('Course Details', course_model, {
    'description': fields.String,
})

login_model = api.inherit('Log In', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

user_model = api.inherit('User', login_model, {
    'username': fields.String(required=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'avatar': fields.String(required=False),
    'phone': fields.String(required=False),
    'last_seen': fields.String(required=False)
})

user_parser = api.parser()
user_parser.add_argument('username', type=str, help='Username', location='form')
user_parser.add_argument('first_name', type=str, help='First Name', location='form')
user_parser.add_argument('last_name', type=str, help='Last Name', location='form')
user_parser.add_argument('phone', type=int, help='Phone', location='form')
# user_parser.add_argument('avatar', type=FileStorage, location='files')

course_parser = reqparse.RequestParser()
course_parser.add_argument('category', type=int, required=False, help='Category ID')
course_parser.add_argument('keyword', type=str, required=False, help='Search keyword')
course_parser.add_argument('from_price', type=float, required=False, help='Minimum price')
course_parser.add_argument('to_price', type=float, required=False, help='Maximum price')
course_parser.add_argument('page', type=int, required=False, default=1, help='Page number')
course_parser.add_argument('latest', type=bool, required=False, default=False, help='Filter by latest products (true/false)')
