from app import db
from .models import User, Instructor, Category, Course, Role


def create_data():
    admin = User(
        username='admin',
        email='admin@gmail.com',
        first_name='Admin',
        last_name='User',
        role=Role.ADMIN
    )

    instructor = User(
        username='duccuong.instr',
        email='nguyenduccuong@gmail.com',
        first_name='Duc Cuong',
        last_name='Nguyen',
        role=Role.INSTRUCTOR
    )

    student = User(
        username='zin.it.dev',
        email='zin.it.dev@gmail.com',
        first_name='Hien Vinh',
        last_name='Le'
    )

    admin.set_password(password='admin')
    instructor.set_password(password='123')
    student.set_password(password='123')

    teach = Instructor(user=instructor, bio="Good teach")
    
    category1 = Category(name='Programming')
    category2 = Category(name='Mathematics')
        
    course1 = Course(
        subject='Introduction to Python',
        description='Learn Python programming language from scratch.',
        price=49.99,
        category=category1,
        instructor=teach
    )
    course2 = Course(
        subject='Calculus I',
        description='Basic concepts of calculus for beginners.',
        price=39.99,
        category=category2,
        instructor=teach
    )
    db.session.add_all([admin, instructor, student, teach,
                       category1, category2, course1, course2])
    
    db.session.commit()

    print("Data created successfully!")
