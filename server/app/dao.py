from app import db
from .models import User, Category, Course
from sqlalchemy import func

def load_user(id):
    return User.query.get(int(id))


def auth_user(email, password):
    user = User.query.filter(User.email.__eq__(email)).first()
    return user if user and user.check_password(password=password) and user.is_admin() else None


def stats_courses():
    """
        SELECT c.id, c.name, COUNT(b.id)
        FROM category c
        LEFT OUTER JOIN book b ON c.id = b.category_id
        GROUP BY c.id;
    """
    return db.session.query(Category.id, Category.name, func.count(Course.id))\
        .join(Course, Course.category_id.__eq__(Category.id), isouter=True)\
        .group_by(Category.id).all()
