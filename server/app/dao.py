from app import db
from .configs import Config
from .models import User, Category, Course, Lesson
from sqlalchemy import func, extract


def get_user(email):
    return User.query.filter_by(email=email).one_or_none()


def load_users():
    return User.query.filter(User.active.__eq__(True)).all()


def load_user(id):
    return User.query.get(int(id))


def load_categories():
    return Category.query.filter(Category.active.__eq__(True)).all()


def load_courses(
    category=None, keyword=None,
    from_price=None, to_price=None,
    is_latest=False, release_month=None,
    release_month_after=None, release_month_before=None,
    page=1, per_page=Config.PAGE_SIZE
):
    queries = Course.query.filter(Course.active.__eq__(True))

    if category:
        queries = queries.filter(Course.category_id.__eq__(category))

    if keyword:
        queries = queries.filter(Course.subject.contains(keyword))

    if from_price:
        queries = queries.filter(Course.price.__ge__(from_price))

    if to_price:
        queries = queries.filter(Course.price.__le__(to_price))

    if release_month:
        queries = queries.filter(
            extract('month', Course.date_created).__eq__(release_month))

    if release_month_after:
        queries = queries.filter(
            extract('month', Course.date_created).__gt__(release_month_after))

    if release_month_before:
        queries = queries.filter(
            extract('month', Course.date_created).__lt__(release_month_before))

    if is_latest:
        queries = queries.order_by(Course.date_created)
    else:
        queries = queries.order_by(Course.subject)

    pagination = queries.paginate(
        page=page, per_page=per_page)

    return {
        'courses': pagination.items,
        'total_pages': pagination.pages,
        'total_items': pagination.total,
        'current_page': page,
        'per_page': per_page
    }


def load_course(course_id):
    return Course.query.get(int(course_id))


def load_lessons():
    return Lesson.query.filter(Lesson.active.__eq__(True)).all()


def load_lesson(lesson_id):
    return Lesson.query.get(int(lesson_id))


def auth_user(email, password):
    user = User.query.filter(User.email.__eq__(email)).first()
    return user if user and user.check_password(password=password) and user.is_admin() else None


def stats_courses():
    """
        SELECT c.id, c.name, COUNT(b.id)
        FROM category c
        LEFT OUTER JOIN Course b ON c.id = b.category_id
        GROUP BY c.id;
    """
    return db.session.query(Category.id, Category.name, func.count(Course.id))\
        .join(Course, Course.category_id.__eq__(Category.id), isouter=True)\
        .group_by(Category.id).all()


def exist_user(email=None, username=None):
    query = User.query

    if email:
        query = query.filter_by(email=email)

    if username:
        query = query.filter_by(username=username)

    return query.first()
