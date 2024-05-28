from app import app, admin, login_manager, dao
from flask_login import login_user, current_user
from flask import flash, redirect, request


@login_manager.user_loader
def load_user(user_id):
    return dao.load_user(id=user_id)


@app.get('/')
def index():
    return app.send_static_file('data/categories.json')


@app.route("/admin-login", methods=['POST'])
def admin_login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = dao.auth_user(email=email, password=password)

    if user:
        flash(f"Welcome to {user.username} comeback!", category="success")
        login_user(user=user, remember=True)
        return redirect('/admin')

    flash("Invalid email or password. Please try again.", category="warning")
    return redirect('/admin')
