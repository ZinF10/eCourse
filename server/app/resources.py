from flask_restx import Resource
from flask import abort, request
from app import dao, schemas, api, utils, cache
from flask_jwt_extended import jwt_required, current_user
from .modules import category_ns, course_ns, user_ns, user_parser, lesson_ns


@category_ns.route('/')
class Category(Resource):
    @cache.cached(timeout=(60*60*2))
    def get(self):
        schema = schemas.CategorySchema(many=True)
        return schema.dump(dao.load_categories()), 200


@course_ns.route('/')
class Course(Resource):
    @cache.cached(timeout=(60*60*2))
    @course_ns.doc(params={
        'keyword': 'Search keyword',
        'max_price': 'Maximum price',
        'min_price': 'Minimum price',
        'release_month': 'Filter by release month (1-12)',
        'release_month_after': 'Filter courses released after this month (1-12)',
        'release_month_before': 'Filter courses released before this month (1-12)',
        'latest': 'Filter by latest products (true/false)',
        'page': 'Page number',
        'category': 'Filter category id',
    })
    def get(self):
        category = request.args.get('category', type=int)
        keyword = request.args.get('keyword', type=str)
        from_price = request.args.get('min_price', type=float)
        to_price = request.args.get('max_price', type=float)
        release_month = request.args.get('release_month', type=int)
        release_month_after = request.args.get('release_month_after', type=int)
        release_month_before = request.args.get(
            'release_month_before', type=int)
        is_latest = request.args.get('latest', type=bool, default=False)
        page = request.args.get('page', type=int, default=1)

        courses = dao.load_courses(
            category=category,
            keyword=keyword,
            from_price=from_price,
            to_price=to_price,
            release_month=release_month,
            release_month_after=release_month_after,
            release_month_before=release_month_before,
            is_latest=is_latest,
            page=page
        )

        schema = schemas.CourseSchema(many=True)
        return schema.dump(courses['courses']), 200


@course_ns.route('/<int:id>/')
class CourseDetail(Resource):
    @cache.cached(timeout=(60*60*2))
    def get(self, id):
        course = dao.load_course(course_id=id)
        if not course:
            abort(404, description="Not found")
        return schemas.CourseDetailSchema().dump(course), 200
    

@course_ns.route('/<int:id>/lessons/')
class CourseLessons(Resource):
    @cache.cached(timeout=(60*60*2))
    def get(self, id):
        course = dao.load_course(course_id=id)
        if not course:
            abort(404, description="Not found")
        
        lessons = dao.load_lessons(course=id)        
        return schemas.LessonSchema(many=True).dump(lessons), 200


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
        data = user_parser.parse_args()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        avatar = request.files.get('avatar')

        if not all([username, email, password, first_name, last_name]):
            return {'message': 'Missing required fields'}, 400

        if dao.load_user(email=email):
            return {'message': 'Email already exists'}, 400

        if dao.load_user(username=username):
            return {'message': 'Username already exists'}, 400

        avatar_url = utils.upload_image(avatar)
        data['avatar'] = avatar_url

        user_schema = schemas.UserSchema()
        user = user_schema.load(data)

        return user_schema.dump(user), 201
            

@user_ns.route('/current-user/')
class CurrentUser(Resource):
    @cache.cached(timeout=(60*60*2))
    @jwt_required()
    def get(self):
        return schemas.CurrentUserSchema().dump(current_user), 200

api.add_namespace(user_ns)
api.add_namespace(category_ns)
api.add_namespace(course_ns)
api.add_namespace(lesson_ns)