import os
from dotenv import load_dotenv
from pathlib import Path 
basedir = os.path.abspath(os.path.dirname(__file__))

dot_env_path = Path('.')/'.env'
load_dotenv(dotenv_path=dot_env_path)

class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# class DevelopmentConfig(BaseConfig):
#     """Development configuration."""

#     user = os.getenv('POSTGRES_USER')
#     password = os.getenv('POSTGRES_PASSWORD')
#     database = os.getenv('POSTGRES_DB')
#     port = os.getenv('POSTGRES_PORT')
#     host = '127.0.0.1'
#     DEBUG = True
#     PRIVATE = open(Path('../keys/private'), 'rb').read()
#     PUBLIC = open(Path('../keys/private.pub'), 'rb').read()
#     BCRYPT_LOG_ROUNDS = 4
#     SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://{user}:{pw}@{url}:{port}/{db}'.format(
#     user=user, pw=password, url=host,port=port, db=database)

class Production(BaseConfig):
    """Production configuration."""

    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    database = os.getenv('POSTGRES_DB')
    port = os.getenv('POSTGRES_PORT')
    host = os.getenv('HOST')
    DEBUG = True
    PRIVATE = open(Path('/data/ubanquity/conf/private'), 'rb').read()
    PUBLIC = open(Path('/data/ubanquity/conf/private.pub'), 'rb').read()
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://{user}:{pw}@{url}:{port}/{db}'.format(
    user=user, pw=password, url=host,port=port, db=database)

