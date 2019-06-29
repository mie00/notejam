From python:2

Add flask /app
WORKDIR /app
RUN source .env/bin/activate && python runserver.py
