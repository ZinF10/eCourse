from app import app, resources, admin, login_manager, dao, jwt
from flask import flash, redirect, request, jsonify, url_for
from flask_login import login_user
from flask_jwt_extended import create_access_token

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
        return redirect('/admin')

    flash("Invalid email or password. Please try again.", category="warning")
    return redirect('/admin')


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    return dao.load_user(id=jwt_data["sub"])


@app.route("/token/", methods=["POST"])
def get_token():
    email = request.json.get("email")
    password = request.json.get("password")

    user = dao.load_user(email=email)
    if not user or not user.check_password(password=password):
        return jsonify(message="Wrong email or password"), 401

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)
