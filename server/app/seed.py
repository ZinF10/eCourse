from .models import User, Role

def create_data():
    admin = User(
            username='Admin',
            email='admin@gmail.com',
            role=Role.ADMIN
        )
    admin.save()
    print("Data created successfully!")