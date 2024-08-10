from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, Integer, Boolean, DateTime, String, ForeignKey, Text, Float, Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime, timezone
from flask_bcrypt import generate_password_hash, check_password_hash
from .utils.helpers import hash_avatar_url

db = SQLAlchemy()
migrate = Migrate()
class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'is_active': self.is_active,
            'date_created': self.date_created
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        

class User(BaseModel, UserMixin):
    username = Column(String(80), unique=True)
    email = Column(String(125), unique=True)
    password = Column(String(255))
    avatar = Column(String(225), default=None)
    first_name = Column(String(80), nullable=True)
    last_name = Column(String(80), nullable=True)
    phone = Column(String(10), nullable=True)
    last_seen = Column(DateTime, default=datetime.now(timezone.utc))
    is_admin = Column(Boolean, default=False)
    orders = relationship('Order', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)
    ratings = relationship('Rating', backref='user', lazy=True)
    likes = relationship('Like', backref='user', lazy=True)
    
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.password = generate_password_hash(kwargs.get('password'), 10)
        if not self.avatar:
            self.avatar = hash_avatar_url(email=self.email)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'avatar': self.avatar,
            'phone': self.phone,
            'is_admin': self.is_admin,
            'last_seen': self.last_seen
        })
        return base_dict

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

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'name': self.name,
        })
        return base_dict

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
    is_liked = Column(Boolean, default=False)

    def __str__(self):
        return self.is_liked

