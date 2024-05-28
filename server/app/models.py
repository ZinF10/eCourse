from app import db
from sqlalchemy import Column, Integer, Boolean, DateTime, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=datetime.utcnow())


class Category(Base):
    name = Column(String(80), unique=True)
    courses = relationship('Course', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Course(Base):
    subject = Column(String(100), unique=True)
    description = Column(Text)
    image = Column(String(255), default=None)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.subject