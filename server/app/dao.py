from .models import User


def load_user(id):
    return User.query.get(int(id))


def auth_user(email, password):
    user = User.query.filter(User.email.__eq__(email)).first()
    return user if user and user.check_password(password=password) and user.is_admin() else None
