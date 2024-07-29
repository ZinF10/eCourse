from flask_restx import Resource, Namespace
from flask import abort, request
from .dao import load_categories, load_courses, load_course
from .serializers import category_model, course_model, user_model, course_parser, course_details_model

category_ns = Namespace('categories', description='Category operations', ordered=True)
course_ns = Namespace('courses', description='Course operations', ordered=True)
user_ns = Namespace('users', description='User operations', ordered=True)


@user_ns.route('/')
class UserResource(Resource):
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        pass


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
    })
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