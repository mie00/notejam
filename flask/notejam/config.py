import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'notejam-flask-secret-key'
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'notejam-flask-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql://notejam:tYoSZlT&Bf^YLn<HiuOj@mysql.storage/notejam'


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']
    CSRF_SESSION_KEY = os.environ['CSRF_SESSION_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
