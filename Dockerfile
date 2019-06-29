From python:2

Add flask /app
WORKDIR /app

CMD . .env/bin/activate && python runserver.py
