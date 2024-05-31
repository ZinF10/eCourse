from app import db
from .models import User, Category, Course, Lesson
from sqlalchemy import func


def get_user(email):
    return User.query.filter_by(email=email).one_or_none()


def load_users():
    return User.query.filter(User.active.__eq__(True)).all()


def load_user(id):
    return User.query.get(int(id))


def load_categories():
    return Category.query.filter(Category.active.__eq__(True)).all()


def load_courses():
    return Course.query.filter(Course.active.__eq__(True)).all()


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
