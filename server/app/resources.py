from flask_restx import Resource
from flask import abort, request
from app import dao, schemas, api, utils
from flask_jwt_extended import jwt_required, current_user
from .modules import category_ns, course_ns, lesson_ns, user_ns, user_parser


@category_ns.route('/')
class Category(Resource):
    def get(self):
        schema = schemas.CategorySchema(many=True)
        return schema.dump(dao.load_categories()), 200


@course_ns.route('/')
class Course(Resource):
    def get(self):
        schema = schemas.CourseSchema(many=True)
        return schema.dump(dao.load_courses()), 200


@course_ns.route('/<int:id>')
class CourseDetail(Resource):
    def get(self, id):
        course = dao.load_course(course_id=id)
        if not course:
            abort(404, description="Not found")
        return schemas.CourseDetailSchema().dump(course), 200


@lesson_ns.route('/')
class Lesson(Resource):
    def get(self):
        schema = schemas.LessonSchema(many=True)
        return schema.dump(dao.load_lessons()), 200


@lesson_ns.route('/<int:id>')
class LessonDetail(Resource):
    def get(self, id):
        lesson = dao.load_lesson(lesson_id=id)
        if not lesson:
            abort(404, description="Not found")
        return schemas.LessonDetailSchema().dump(lesson), 200


@user_ns.route('/')
class User(Resource):
    @user_ns.expect(user_parser)
    def post(self):
        try:
            data = user_parser.parse_args()
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            avatar = request.files.get('avatar')

            if not all([username, email, password, first_name, last_name]):
                return {'message': 'Missing required fields'}, 400

            if dao.exist_user(email=email):
                return {'message': 'Email already exists'}, 400

            if dao.exist_user(username=username):
                return {'message': 'Username already exists'}, 400

            avatar_url = utils.upload_image(avatar)
            data['avatar'] = avatar_url

            user = schemas.UserSchema().load(data)

            return schemas.UserSchema().dump(user), 201
        except Exception as e:
            return {'error': str(e)}, 500


@user_ns.route('/current-user/')
class CurrentUser(Resource):
    @jwt_required()
    def get(self):
        return schemas.CurrentUserSchema().dump(current_user), 200


api.add_namespace(user_ns)
api.add_namespace(category_ns)
api.add_namespace(course_ns)
api.add_namespace(lesson_ns)
