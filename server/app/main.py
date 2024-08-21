
from app import create_app, login_manager, dao, jwt
from .models import db
from .admin.views import admin_login
from flask_login import current_user
from datetime import datetime, timezone

app = create_app()
            
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


app.add_url_rule('/admin-login', view_func=admin_login, methods=['POST'])