import enum
from app import db
from sqlalchemy import Column, Integer, Boolean, DateTime, String, ForeignKey, Text, Float, Enum, Date
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Role(enum.Enum):
    ADMIN = 'Administrator'
    USER = 'User'
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
    password = Column(String(100))
    first_name = Column(String(80))
    last_name = Column(String(80))
    phone = Column(String(10), nullable=True)
    role = Column(Enum(Role), default=Role.USER)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_admin(self):
        return self.role == Role.ADMIN

    def __str__(self):
        return self.username


class Instructor(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), unique=True, nullable=False)
    bio = Column(Text, nullable=True)
    user = relationship(User, backref='instructor', uselist=False)
    courses = relationship('Course', backref='instructor', lazy=True)


class Student(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), unique=True, nullable=False)
    user = relationship(User, backref='student', uselist=False)
    address = Column(String(125), nullable=True)
    date_of_birth = Column(Date)


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
