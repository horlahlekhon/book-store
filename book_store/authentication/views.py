from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

 
from book_store.models import User
from book_store import db
import jwt
from book_store.books.views import retriev_header_and_verify



authentication_blueprint = Blueprint('auth', __name__)


class Register(MethodView):


    def post(self):
        data = request.get_json()
        
        user = User.query.filter_by(email=data.get('email')).first()
        if user:
            reaponse = {
                'status' : 'fail',
                'message' : 'User already exist'
            }
            return make_response(jsonify(reaponse)), 202
        else :
            try :
                user = User(data.get("email"),password=data.get("password"),admin=data.get('admin'))
                
                db.session.add(user)
                db.session.commit()
                auth_token = user.encode_auth_token(user.id, user.admin)
                response = {
                    "status": "success",
                    "message" :'successfully registered',
                    "auth_token": auth_token.decode()
                }
                return make_response(jsonify(response)), 200
            except Exception as e:
                print("error === {}".format(e))
                response = {
                    'status' : 'failed',
                    'message' : 'some error occured, try again' + str(e),
                }
                return make_response(jsonify(response)), 401
class Login(MethodView):

    def post(self):
        data = request.get_json()

        user = User.query.filter_by(email=data.get("email")).first()
        if user :
            try:
                response = {
                "status" : "success",
                "message": "Welcome, never forget to leave a tip for the librarian",
                "token" : user.encode_auth_token(user.id, user.admin).decode()
                }
                return make_response(jsonify(response)),200
            except Exception as e :
                response = {
                "status" : "failed",
                "message" : "something baroque happened, please try again",
                }
                return make_response(jsonify(response)), 500
        else :
            response = {
                "status" : "failed",
                "message" : "user does not exist",
            }
            return make_response(jsonify(response)), 401

class UserAPi(MethodView):
    def get(self):
        header = request.headers.get("Authentication")
        toke , is_admin = retriev_header_and_verify(header)
        if isinstance(toke, int):
            if is_admin:
                users = User.get_all_users()
                print(users)
                return make_response(jsonify(users)), 200
            user = User.get_user(toke)
            return make_response(jsonify(user)), 200
        return make_response(jsonify(toke)), 500 

login_api = Login.as_view('login')
register_api = Register.as_view('register')
user_api = UserAPi.as_view('user_view')
authentication_blueprint.add_url_rule(
    '/api/register',
     view_func=register_api,
    methods=['POST'])

authentication_blueprint.add_url_rule(
    '/api/user/login', 
    view_func=login_api, 
    methods=['POST'])

authentication_blueprint.add_url_rule(
    '/api/users',
    view_func=user_api,
    methods=['GET']
)



