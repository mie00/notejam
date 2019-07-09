import os
from notejam import app

from logging.config import dictConfig

host = '127.0.0.1'
config = 'notejam.config.DevelopmentConfig'
env_config = os.environ.get("APP_SETTINGS")
if env_config:
    config = env_config
    host = '0.0.0.0'

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



if __name__ == '__main__':
    app.run(host=host)
