import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config(object):
    
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'postgres'
    DB_HOST = os.environ.get('DB_HOST') or '127.0.0.1'
    DB_PORT = os.environ.get('DB_PORT') or 5432
    DB_NAME = os.environ.get('DB_NAME') or 'steam_db'
    DB_USER = os.environ.get('DB_USER') or 'postgres'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_HOST}:{DB_PORT}/{DB_NAME}?user={DB_USER}&password={DB_PASSWORD}"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = False
    DB_NAME = os.environ.get('DB_NAME') or 'steam.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class StagingConfig(DevelopmentConfig):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(DevelopmentConfig):
    TESTING = True