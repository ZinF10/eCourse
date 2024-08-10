from flask_restx import Resource
from flask_jwt_extended import jwt_required, current_user
from ..dao import fetch_user, create_user
from .serializers import user_parser, user_api, user
from ..utils.helpers import upload_image

@user_api.route('/')
class UserResource(Resource):
    @user_api.expect(user_parser)
    @user_api.marshal_with(user, code=201)
    def post(self):
        avatar_url = None
        args = user_parser.parse_args()
        avatar = args['avatar']
        
        if avatar:
            avatar_url = upload_image(file_data=avatar)
        
        new_user = create_user(
            username=args['username'],
            email=args['email'], 
            password=args['password'], 
            first_name=args['first_name'],
            last_name=args['last_name'],
            avatar=avatar_url,
            phone=args['phone']
        )
        # send_email(to=new_user.email, subject="Thank", content="hello")
        return new_user
    
    
@user_api.route('/current-user/')
class CurrentUserResource(Resource):
    method_decorators = [jwt_required()]
    @user_api.doc(security="jwt")
    @user_api.marshal_with(user, code=200)
    def get(self):
        return fetch_user(current_user.id)

