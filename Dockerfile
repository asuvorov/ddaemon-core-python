FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt ./

RUN apt update && apt install -y python3-dev wget gcc make g++ libc-dev libffi-dev build-essential default-libmysqlclient-dev pkg-config python3-psycopg2 memcached gettext nodejs npm
RUN npm install -g bower less recess

RUN pip install --upgrade pip
RUN pip install --upgrade --no-cache-dir -r requirements.txt

RUN pip uninstall PyJWT -y
RUN pip install PyJWT

COPY ./ddcore ./ddcore
# RUN mkdir -p ./src/logs
# RUN mkdir -p ./src/media

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
