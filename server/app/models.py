import enum
from app import db
from sqlalchemy import Column, Integer, Boolean, DateTime, String, ForeignKey, Text, Float, Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Role(enum.Enum):
    ADMIN = 'Administrator'
    STUDENT = 'Student'
    INSTRUCTOR = 'Instructor'


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=datetime.utcnow())


class User(UserMixin, BaseModel):
    avatar = Column(String(225), default=None)
    username = Column(String(80), unique=True)
    email = Column(String(125), unique=True)
    password = Column(String(255))
    first_name = Column(String(80))
    last_name = Column(String(80))
    phone = Column(String(10), nullable=True)
    role = Column(Enum(Role), default=Role.STUDENT)
    orders = relationship('Order', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)
    ratings = relationship('Rating', backref='user', lazy=True)
    likes = relationship('Like', backref='user', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_admin(self):
        return self.role == Role.ADMIN

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Instructor(BaseModel):
    user_id = Column(Integer, ForeignKey(User.id), unique=True, nullable=False)
    bio = Column(Text, nullable=True)
    user = relationship(User, backref='instructor', uselist=False)
    courses = relationship('Course', backref='instructor', lazy=True)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'


class Category(BaseModel):
    name = Column(String(80), unique=True)
    courses = relationship('Course', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = Column(String(100), unique=True)
    description = Column(Text)
    image = Column(String(255), default=None)
    price = Column(Float, default=0.00)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    instructor_id = Column(Integer, ForeignKey(Instructor.id), nullable=False)
    lessons = relationship('Lesson', backref='course', lazy=True)
    tags = relationship('Tag', secondary='course_tag', backref='courses')
    details = relationship('OrderDetail', backref='course', lazy=True)
    comments = relationship('Comment', backref='course', lazy=True)
    ratings = relationship('Rating', backref='course', lazy=True)
    likes = relationship('Like', backref='course', lazy=True)

    def __str__(self):
        return self.subject


class Lesson(BaseModel):
    title = Column(String(100), unique=True)
    content = Column(Text)
    image = Column(String(255), default=None)
    course_id = Column(Integer, ForeignKey(Course.id), nullable=False)
    tags = relationship('Tag', secondary='lesson_tag', backref='lessons')
    resources = relationship('Resource', backref='lesson', lazy=True)

    def __str__(self):
        return self.title


class Resource(BaseModel):
    url = Column(String(125))
    name = Column(String(100), unique=True)
    lesson_id = Column(Integer, ForeignKey(Lesson.id), nullable=False)

    def __str__(self):
        return f"{self.title}-{self.url[:20]}"


class Tag(BaseModel):
    name = Column(String(80), unique=True)

    def __str__(self):
        return f"#{self.name}"


course_tag = db.Table('course_tag',
                      Column('course_id', Integer, ForeignKey(
                          Course.id), nullable=False),
                      Column('tag_id', Integer, ForeignKey(
                          Tag.id), nullable=False)
                      )


lesson_tag = db.Table('lesson_tag',
                      Column('lesson_id', Integer, ForeignKey(
                          Lesson.id), nullable=False),
                      Column('tag_id', Integer, ForeignKey(
                          Tag.id), nullable=False)
                      )


class Order(BaseModel):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    details = relationship('OrderDetail', backref='order', lazy=True)

    def __str__(self):
        return self.user_id


class OrderDetail(BaseModel):
    quantity = Column(Integer, default=1)
    unit_price = Column(Float, default=0.0)
    course_id = Column(Integer, ForeignKey(Course.id), nullable=False)
    order_id = Column(Integer, ForeignKey(Order.id), nullable=False)

    def __str__(self):
        return f'<Details "{self.quantity} * {self.unit_price}">'


class InteractionModel(BaseModel):
    __abstract__ = True

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    course_id = Column(Integer, ForeignKey(Course.id), nullable=False)


class Comment(InteractionModel):
    content = Column(Text)

    def __str__(self):
        return self.content[:20]


class Rating(InteractionModel):
    rate = Column(Integer, default=0)

    def __str__(self):
        return self.rate


class Like(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    course_id = Column(Integer, ForeignKey(Course.id), nullable=False)
    liked = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())

    def __str__(self):
        return self.liked
