from ..dao import load_lesson
from flask_restx import Resource
from flask import abort
from .dto import lesson_api, lesson

@lesson_api.route('/<int:id>/')
@lesson_api.param('id', 'An ID')
@lesson_api.response(404, 'Not found')
class LessonResource(Resource):
    @lesson_api.marshal_with(lesson, code=200)
    def get(self, id):
        """ Get lesson """
        return load_lesson(course_id=id) or abort(404, 'Not found')