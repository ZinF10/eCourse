from app import db
from sqlalchemy import Column, Integer, Boolean, DateTime, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=datetime.utcnow())


class Category(BaseModel):
    name = Column(String(80), unique=True)
    courses = relationship('Course', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = Column(String(100), unique=True)
    description = Column(Text)
    image = Column(String(255), default=None)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    tags = relationship('Tag', secondary='course_tag', backref='courses')

    def __str__(self):
        return self.subject


class Tag(BaseModel):
    name = Column(String(80), unique=True)

    def __str__(self):
        return self.name


course_tag = db.Table('course_tag',
                      Column('course_id', Integer, ForeignKey(
                          Course.id), nullable=False),
                      Column('tag_id', Integer, ForeignKey(
                          Tag.id), nullable=False)
                      )
