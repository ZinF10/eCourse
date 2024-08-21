from .dao import create_user

def create_admin():
    try:
        admin = create_user(username="ADMIN", email="admin@gmail.com", password="admin", is_admin=True)
        print(f"Admin with email {admin.email} created successfully!")
    except Exception:
        print("Couldn't create admin user.")
