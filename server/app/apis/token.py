from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restx import Resource
from flask import jsonify
from datetime import datetime, timezone
from .serializers import token_api, login_model
from ..dao import auth_user

@token_api.route('/')
class TokenResource(Resource):
    @token_api.expect(login_model)
    def post(self):
        user = auth_user(email=token_api.payload['email'], password=token_api.payload['password'])
        if not user:
            return jsonify(message='Invalid email or password'), 401
        user.last_seen = datetime.now(timezone.utc)
        user.save()
        access_token = create_access_token(identity=user, fresh=True)
        refresh_token = create_refresh_token(identity=user)
        return jsonify(access_token=access_token, refresh_token=refresh_token)
