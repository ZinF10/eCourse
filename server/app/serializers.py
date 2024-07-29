from flask_restx import fields, reqparse
from .extensions import api

base_model = api.model('Models', {
    'id': fields.Integer(readonly=True, description='Unique ID'),
    'active': fields.Boolean(description='Active'),
    'date_created': fields.DateTime(dt_format='iso8601'),
})

category_model = api.inherit('Category', base_model, {
    'name': fields.String,
})

course_model = api.inherit('Course', base_model, {
    'subject': fields.String,
    'price': fields.Float,
    'image': fields.String,
    'category': fields.String,
    'tags': fields.List(fields.String, description='List of tags associated with the course')
})

course_details_model = api.inherit('Course Details', course_model, {
    'description': fields.String,
})

user_model = api.inherit('User', base_model, {
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'avatar': fields.String,
    'phone': fields.String,
    'role': fields.String,
})

course_parser = reqparse.RequestParser()
course_parser.add_argument('category', type=int, required=False, help='Category ID')
course_parser.add_argument('keyword', type=str, required=False, help='Search keyword')
course_parser.add_argument('from_price', type=float, required=False, help='Minimum price')
course_parser.add_argument('to_price', type=float, required=False, help='Maximum price')
course_parser.add_argument('page', type=int, required=False, default=1, help='Page number')