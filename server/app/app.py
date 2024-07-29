from app import create_app, dao
from .extensions import login_manager
from flask import flash, redirect, request, url_for
from flask_login import login_user

app = create_app()

@login_manager.user_loader
def load_user(user_id):
    return dao.load_user(id=user_id)


@app.route("/admin-login", methods=['POST'])
def admin_login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = dao.auth_user(email=email, password=password)

    if user:
        flash(f"Welcome to {user.username} comeback!", category="success")
        login_user(user=user)
        return redirect(url_for('admin.index'))

    flash("Invalid email or password. Please try again.", category="warning")
    return redirect(url_for('admin.index'))