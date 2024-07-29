import cloudinary.uploader
from flask import request, session, g

def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'en')


def get_timezone():
    user = getattr(g, 'current_user', None)
    if user is not None:
        return user.timezone


def format_price(amount, currency="$"):
    return f"{amount:.2f}{currency}"


def upload_image(file_data):
    result = cloudinary.uploader.upload(file_data)
    return result.get('secure_url')