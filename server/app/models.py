import enum 
from .extensions import db
from .utils import hash_avatar_url
from sqlalchemy import Column, Integer, Boolean, DateTime, String, ForeignKey, Text, Float, Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime, timezone
from flask_bcrypt import generate_password_hash, check_password_hash


class Role(enum.Enum):
    ADMIN = 'Administrator'
    STUDENT = 'Student'
    INSTRUCTOR = 'Instructor'


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'active': self.active,
            'date_created': self.date_created
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        

class User(UserMixin, BaseModel):
    username = Column(String(80), unique=True)
    email = Column(String(125), unique=True)
    password = Column(String(255))
    avatar = Column(String(225), default=None)
    first_name = Column(String(80), nullable=True)
    last_name = Column(String(80), nullable=True)
    phone = Column(String(10), nullable=True)
    last_seen = Column(DateTime, default=datetime.now(timezone.utc))
    role = Column(Enum(Role), default=Role.STUDENT)
    orders = relationship('Order', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)
    ratings = relationship('Rating', backref='user', lazy=True)
    likes = relationship('Like', backref='user', lazy=True)
    
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        if not self.avatar:
            self.avatar = hash_avatar_url(email=self.email)
            
        if self.role == Role.INSTRUCTOR and not self.password:
            self.set_password('123')
            
        if self.role == Role.ADMIN and not self.password:
            self.set_password('admin')

    def set_password(self, password):
        self.password = generate_password_hash(password, 10)

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
    name = Column(String(80), unique=True, nullable=False)
    courses = relationship('Course', backref='category', lazy=True)

    def __str__(self):
        return self.name
    
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'name': self.name,
        })
        return base_dict


class Course(BaseModel):
    subject = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    image = Column(String(255), default=None)
    price = Column(Float, default=0.00)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    instructor_id = Column(Integer, ForeignKey(Instructor.id), nullable=True)
    lessons = relationship('Lesson', backref='course', lazy=True)
    tags = relationship('Tag', secondary='course_tag', backref='courses', lazy=True)
    details = relationship('OrderDetail', backref='course', lazy=True)
    comments = relationship('Comment', backref='course', lazy=True)
    ratings = relationship('Rating', backref='course', lazy=True)
    likes = relationship('Like', backref='course', lazy=True)

    def __str__(self):
        return self.subject


class Lesson(BaseModel):
    subject = Column(String(100), unique=True, nullable=False)
    content = Column(Text)
    image = Column(String(255), default=None)
    course_id = Column(Integer, ForeignKey(Course.id), nullable=False)
    tags = relationship('Tag', secondary='lesson_tag', backref='lessons')
    resources = relationship('Resource', backref='lesson', lazy=True)

    def __str__(self):
        return self.subject


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
    unit_price = Column(Float, default=0.0)
    course_id = Column(Integer, ForeignKey(Course.id), nullable=False)
    order_id = Column(Integer, ForeignKey(Order.id), nullable=False)

    def __str__(self):
        return f'<Details: #{self.course_id}{self.unit_price}">'


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


class Like(InteractionModel):
    liked = Column(Boolean, default=False)

    def __str__(self):
        return self.liked

