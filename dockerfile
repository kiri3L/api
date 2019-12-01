FROM python:3.7.4-buster
RUN pip install Django
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install mysqlclient
COPY . /app
#ENTRYPOINT ['python3', '']
# RUN rm -rf /app/db.sqlite3
#RUN python3 /app/manage.py migrate
EXPOSE 8888
#ENTRYPOINT ["python3", "/app/manage.py", "runserver", "172.105.77.74:8888"]
#CMD 
