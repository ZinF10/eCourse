from .models import db, User, Role

def create_data():
    admin = User(
            username='admin',
            email='admin@gmail.com',
            first_name='Admin',
            last_name='User',
            role=Role.ADMIN
        )
    admin.set_password(password='admin')
    db.session.add(admin)
    db.session.commit()
    print("Data created successfully!")