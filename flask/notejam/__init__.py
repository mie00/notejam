import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail

from logging.config import dictConfig

# @TODO use application factory approach
app = Flask(__name__)

config = 'notejam.config.DevelopmentConfig'
env_config = os.environ.get("APP_SETTINGS")
if env_config:
    config = env_config

app.config.from_object(config)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default'
        }
    },
    'loggers': {
        '': {
            'level': app.config['LOG_LEVEL'],
            'handlers': ['wsgi']
        }
    }
})

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "signin"
login_manager.init_app(app)

mail = Mail()
mail.init_app(app)

from notejam import views
