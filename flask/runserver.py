import os
from notejam import app

from logging.config import dictConfig

host = '127.0.0.1'
env_config = os.environ.get("APP_SETTINGS")
if env_config:
    host = '0.0.0.0'

if __name__ == '__main__':
    app.run(host=host)
