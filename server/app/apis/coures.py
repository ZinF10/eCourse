from flask_restx import Resource
from flask import abort
from ..dao import load_courses, load_course, load_lessons
from .dto import course_api, courses, course, course_parser, lessons


@course_api.route('/')
class CourseListResource(Resource):
    @course_api.doc(params={
        'category': 'An Category ID',
        'keyword': 'Keyword to search for',
        'from_price': 'Minimum price',
        'to_price': 'Maximum price',
        'page': 'Page number',
        'latest': 'Filter by latest products (true/false)',
    }, security="jwt")
    @course_api.expect(course_parser)
    @course_api.marshal_with(courses, code=200, envelope="results", as_list=True)
    def get(self):
        """ Get all courses """
        args = course_parser.parse_args()
        return load_courses(**args)
    
    
@course_api.route('/<int:id>/')
@course_api.param('id', 'An ID')
@course_api.response(404, 'Not found')
class CourseResource(Resource):
    @course_api.marshal_with(course, code=200)
    def get(self, id):
        """ Get course """
        return load_course(course_id=id) or abort(404, 'Not found')
    
    
@course_api.route('/<int:id>/lessons/')
@course_api.param('id', 'An ID')
@course_api.response(404, 'Not found')
class CourseLessonsResource(Resource):
    @course_api.marshal_with(lessons, code=200, envelope="results", as_list=True)
    def get(self, id):
        """ Get all lessons by course """
        lessons = load_lessons(course=id)
        if lessons is None:
            abort(404, 'Not found')
        return lessons
    