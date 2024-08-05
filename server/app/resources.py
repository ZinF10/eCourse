from datetime import datetime, timezone
from flask_restx import Resource, Namespace
from flask import abort, jsonify
from flask_jwt_extended import create_access_token, jwt_required, current_user, create_refresh_token
from .dao import load_categories, load_courses, load_course, load_lessons, create_user, auth_user, load_user
from .serializers import category_model, course_model, user_model, course_parser, user_parser, course_details_model, lesson_model, login_model

category_ns = Namespace('categories', description='Category operations', ordered=True)
course_ns = Namespace('courses', description='Course operations', ordered=True)
user_ns = Namespace('users', description='User operations', ordered=True)
token_ns = Namespace('token', description='Token operations', ordered=True)

@user_ns.route('/')
class UserResource(Resource):
    @user_ns.expect(user_parser, validate=True)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        args = user_parser.parse_args()
        avatar_file = args.get('avatar')
        
        return create_user(
            username=user_ns.payload['username'],
            email=user_ns.payload['email'], 
            password=user_ns.payload['password'], 
            first_name=user_ns.payload['first_name'],
            last_name=user_ns.payload['last_name'],
            avatar=user_ns.payload['avatar'],
            phone=user_ns.payload['phone']
        )

@user_ns.route('/current-user/')
class CurrentUserResource(Resource):
    method_decorators = [jwt_required()]
    @user_ns.doc(security="jwt")
    @user_ns.marshal_with(user_model, code=200)
    def get(self):
        return load_user(current_user.id)


@category_ns.route('/')
@category_ns.doc(responses={404: 'Not Found'})
class CategoryResource(Resource):
    @category_ns.marshal_with(category_model, code=200, as_list=True)
    def get(self):
        """ Get all categories """
        return load_categories()
    
    
@course_ns.route('/')
class CourseResource(Resource):
    @course_ns.doc(params={
        'category': 'An Category ID',
        'keyword': 'Keyword to search for',
        'from_price': 'Minimum price',
        'to_price': 'Maximum price',
        'page': 'Page number',
        'latest': 'Filter by latest products (true/false)',
    }, security="jwt")
    @course_ns.expect(course_parser)
    @course_ns.marshal_with(course_model, code=200, envelope="results", as_list=True)
    def get(self):
        """ Get all courses """
        args = course_parser.parse_args()
        return load_courses(**args)
    
    
@course_ns.route('/<int:id>/')
@course_ns.param('id', 'An ID')
@course_ns.response(404, 'Not found')
class CourseDetailsResource(Resource):
    @course_ns.marshal_with(course_details_model, code=200)
    def get(self, id):
        """ Get details course """
        return load_course(course_id=id) or abort(404, 'Not found')


@course_ns.route('/<int:id>/lessons/')
@course_ns.param('id', 'An ID')
@course_ns.response(404, 'Not found')
class CourseLessonsResource(Resource):
    @course_ns.marshal_with(lesson_model, code=200, envelope="results", as_list=True)
    def get(self, id):
        """ Get all lessons by course """
        lessons = load_lessons(course=id)
        if lessons is None:
            abort(404, 'Not found')
        return lessons
    
    
@token_ns.route('/')
class TokenResource(Resource):
    @token_ns.expect(login_model)
    def post(self):
        user = auth_user(email=token_ns.payload['email'], password=token_ns.payload['password'])
        if not user:
            return jsonify(message='Invalid email or password'), 401
        user.last_seen = datetime.now(timezone.utc)
        user.save()
        access_token = create_access_token(identity=user, fresh=True)
        refresh_token = create_refresh_token(identity=user)
        return jsonify(access_token=access_token, refresh_token=refresh_token)