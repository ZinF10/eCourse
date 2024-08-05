from app import create_app, dao
from .extensions import login_manager, db, oauth, jwt
from flask import flash, redirect, request, url_for, make_response
from flask_login import login_user, current_user
from datetime import datetime, timezone
from .models import User

app = create_app()

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return dao.load_user(id=identity)


@login_manager.user_loader
def load_user(user_id):
    return dao.load_user(id=user_id)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()


@app.route("/admin-login", methods=['POST'])
def admin_login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = dao.auth_user(email=email, password=password, role="admin")

    if user:
        flash(f"Welcome to {user.username} comeback!", category="success")
        login_user(user=user)
        return redirect(url_for('admin.index'))

    flash("Invalid email or password. Please try again.", category="warning")
    return redirect(url_for('admin.index'))


@app.route('/google-login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/google-auth')
def auth():
    token = oauth.google.authorize_access_token()
    response = make_response(redirect('http://localhost:5173/test'))
    response.set_cookie('access_token', token['access_token'], secure=True, samesite='Lax')
    return response