from flask import Flask, jsonify, request, Response, json
import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from Configs import *


app = Flask(__name__)


app.config.from_object(Production)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


# from books.views import book_blueprint
# app.register_blueprint(book_blueprint)
from book_store.authentication.views import authentication_blueprint
from book_store.books.views import book_blueprint

app.register_blueprint(authentication_blueprint)
app.register_blueprint(book_blueprint)

app.run(host='0.0.0.0',port='5000', debug=True)