FROM python:3.7.4-buster
RUN pip install Django
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install mysqlclient
COPY . /app
