from .dao import fetch_user
from datetime import datetime, timezone
from flask import Flask, redirect, request, flash, url_for
from flask_login import LoginManager, current_user, login_user
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail
from .configs import DevelopmentConfig
from .models import db, migrate
from .apis import api
from .admin import admin_manager, babel

mail = Mail()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app=app)
    migrate.init_app(app=app, db=db, render_as_batch=True)
    babel.init_app(app=app)
    admin_manager.init_app(app=app)
    api.init_app(app=app)

    mail.init_app(app=app)
    cors = CORS(app=app)
    jwt = JWTManager(app=app)
    bcrypt = Bcrypt(app=app)
    login_manager = LoginManager(app=app)


    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id


    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return dao.fetch_user(id=identity)


    @login_manager.user_loader
    def load_user(user_id):
        return dao.fetch_user(id=user_id)


    @app.before_request
    def before_request():
        if current_user.is_authenticated:
            current_user.last_seen = datetime.now(timezone.utc)
            db.session.commit()
            

    @app.route("/admin-login", methods=['POST'])
    def admin_login():
        email = request.form.get('email')
        password = request.form.get('password')
        user = dao.auth_user(email=email, password=password)

        if user and user.is_admin:
            flash(f"Welcome to {user.username} comeback!", category="success")
            login_user(user=user)
            return redirect(url_for('admin.index'))

        flash("Invalid email or password. Please try again.", category="warning")
        return redirect(url_for('admin.index'))
        
    return app