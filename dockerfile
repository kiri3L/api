FROM python:3.7.4-buster
RUN pip install Django
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install mysqlclient
COPY . /app
# RUN rm -rf /app/db.sqlite3
#RUN python3 /app/manage.py migrate
#CMD ["python3", "/app/manage.py", "runserver", "127.0.0.1:8080"]