import os
basedir = os.path.abspath(os.path.dirname(__file__))



class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    user = "postgres"
    password = "postgres"
    host = 'postgres' # since we are using docker compose, docker will create an alias for the host using the db name
    database = "bookstore"
    port = 5432
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=user, pw=password, url=host, db=database)
