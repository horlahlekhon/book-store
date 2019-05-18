from flask import Flask
import json
from book_store import db ,bcrypt, app
import datetime
import jwt



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin):
        self.email = email
        self.password = bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS')).decode()
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    @staticmethod
    def json(user):
        return {'email':user.email, 'password': user.password,'is_admin':user.admin}


    def encode_auth_token(self, user_id, is_admin=False):
        try :
            payload = {
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10000),
                'iat' :datetime.datetime.utcnow(),
                'sub' : user_id,
                'is_admin': is_admin
            }
            print("payload ==>> ", payload)
            return jwt.encode(
                payload,
               app.config.get('PRIVATE'),
               algorithm='RS256'
            )
        except Exception as e :
            return e

    @staticmethod
    def get_user(id):
        user = User.query.filter_by(id=id).first()
        if user:
            return User.json(user)
        else:
            return None

    @staticmethod
    def get_all_users():
        return [User.json(user) for user in User.query.all()]
    
    @staticmethod
    def decode_auth_token(token):

        try:
            payload = jwt.decode(token, app.config.get('PUBLIC'), algorithms='RS256')
            return payload['sub'], payload["is_admin"]
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.',False
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.',False
    
class Book(db.Model):
    __tablename__ = 'books'  # name of the table the model will be stored

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isbn = db.Column(db.Integer)

    def __init__(self, name, price, isbn):
        self.name = name
        self.price = price
        self.isbn = isbn
        
    @staticmethod
    def json(book):
        return {'name': book.name, 'price': book.price, 'isbn': book.isbn}

    @staticmethod
    def add_book(name, price, isbn):
        new_book = Book(name=name, isbn=isbn, price=price)
        db.session.add(new_book)
        db.session.commit()

    @staticmethod
    def get_all_books():
        return [Book.json(book) for book in Book.query.all()]

    def __repr__(self):
        bok_object = {
            'name': self.name,
            'price': self.price,
            'isbn': self.isbn
        }
        return json.dumps(bok_object)

    @staticmethod
    def get_book(isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            return Book.json(book)
        return  None

    @staticmethod
    def delete_book(isbn):
        Book.query.filter_by(isbn=isbn).delete()
        db.session.commit()

    @staticmethod
    def update_book(isbn, data):
        book = Book.query.filter_by(isbn=isbn).first()
        if data['name'] != '':
            book.name = data['name']
        if data['price'] != 0:
            book.name = data['price']
        db.session.commit()


