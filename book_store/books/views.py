from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
import jwt

from book_store.models import Book 
from book_store.models import User

from book_store import app



book_blueprint = Blueprint('book', __name__)

def retriev_header_and_verify(auth_header):
    if auth_header:
        tk = auth_header.split(' ')[1]
        toke, is_admin = User.decode_auth_token(tk)
        if isinstance(toke, int):
            user = User.query.filter_by(id=toke).first()
            if user : 
                return toke, is_admin
        else:
            return toke, is_admin
    else:
        response = {
            "status" : " Fail",
            "Message": "Please either register or make th authentication token avilable"
        }
        return  response, False
        
    

class BookAPI(MethodView):

    def post(self):
        post_data = request.get_json()
        auth_header = request.headers.get("Authentication")
        toke, _ = retriev_header_and_verify(auth_header)
        if isinstance(toke, int):
            Book.add_book(post_data.get('name'), post_data.get('price'), post_data.get('isbn'))
            response = {
                "status" : "success",
                "message" : "book created"
            }
            return make_response(jsonify(response)), 200
        else :
            return make_response(jsonify(toke)), 404


    def get(self, isbn):
        header = request.headers.get("Authentication")
        toke , _ = retriev_header_and_verify(header)
        if isinstance(toke, int):
            if isbn == None :
                books = Book.get_all_books()
                return make_response(jsonify(books)), 200
            else :
                book = Book.get_book(isbn)
                if book:
                    return make_response(jsonify(book)), 200
                else :
                    return make_response(jsonify({
                        "status" : "fail",
                        "Message" : " Book with isbn {} not found".format(isbn)
                    })), 404
        else :
            return make_response(jsonify(toke)), 500
    
    def delete(self, isbn):
        header = request.headers.get("Authentication")
        toke, _ = retriev_header_and_verify(header)
        if isinstance(toke, int):
            Book.delete_book(isbn)
            return make_response(jsonify({
                "status" : " Success",
                "Message" : " Book with isbn {} successfully deleted".format(isbn)
            })), 200 
        else :
            return make_response(jsonify(toke)), 500
    
    def patch(self , isbn):
        post_data = request.get_json()
        toke, _ = retriev_header_and_verify(request.headers.get("Authentication"))
        if isinstance(toke, int):
            Book.update_book(isbn, post_data)
            return make_response(jsonify({
                "status" : " Success",
                "Message" : "Book successfully updated"
            })), 200
        else : 
            return make_response(jsonify(toke)), 500 

book_api = BookAPI.as_view('book_view')

add_book_blueprint = book_blueprint.add_url_rule(
    '/api/books/',
    view_func=book_api,
    methods=['POST']
)


book_blueprint.add_url_rule(
    '/api/books/',
    defaults={'isbn' : None},
    view_func= book_api,
    methods = ['GET']
)
book_blueprint.add_url_rule(
    '/api/books/<isbn>',
    view_func=book_api,
    methods = ['GET', 'DELETE','PATCH']
)
