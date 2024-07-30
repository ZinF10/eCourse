from .configs import Config
from .models import db, User, Category, Course, Lesson, Order
from sqlalchemy import func, extract

def load_user(id=None, email=None, username=None):
    queries = User.query.filter(User.active.__eq__(True))

    if id:
        queries = queries.filter(User.id.__eq__(id))
    
    if email:
        queries = queries.filter(User.email.__eq__(email))

    if username:
        queries = queries.filter(User.username.__eq__(username))

    return queries.one_or_none()


def load_categories():
    return Category.query.filter(Category.active.__eq__(True)).all()
        

def load_courses(
    per_page=Config.PAGE_SIZE,
    **kwargs
):
    queries = Course.query.filter(Course.active.__eq__(True))

    category = kwargs.get('category')
    keyword = kwargs.get('keyword')
    from_price = kwargs.get('from_price')
    to_price = kwargs.get('to_price')
    release_month = kwargs.get('release_month')
    release_month_after = kwargs.get('release_month_after')
    release_month_before = kwargs.get('release_month_before')
    page = kwargs.get('page')
    
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

    pagination = queries.paginate(page=page, per_page=per_page)
    
    return pagination.items
    

def load_course(course_id):
    return Course.query.get(int(course_id))


def load_lessons(course=None, lesson=None):
    queries = Lesson.query.filter(Lesson.active.__eq__(True))

    if course:
        queries = queries.filter(Lesson.course_id.__eq__(course))
        
    return queries.all()


def load_lesson(lesson_id):
    return Lesson.query.get(int(lesson_id))


def load_order(order_id):
    return Order.query.get(int(order_id))


def load_orders(user=None):
    queries = Order.query
    
    if user:
        queries = queries.filter(Order.user_id.__eq__(user))
    
    return queries.all()


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
        

def count_courses():
    """
        SELECT COUNT(*) AS total_courses FROM course;
    """
    return Course.query.count()