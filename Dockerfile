FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONNUNBUFFERED = 1

WORKDIR /app

COPY requirements.txt /app/

RUN apk update
RUN apk add musl-dev mariadb-dev gcc
RUN python3 -m pip install --upgrade pip
RUN pip install mysqlclient

RUN pip3 install -r requirements.txt

COPY ./core /app

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]