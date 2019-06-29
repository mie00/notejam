From python:2

Add flask /app
WORKDIR /app
RUN . .env/bin/activate && python runserver.py
