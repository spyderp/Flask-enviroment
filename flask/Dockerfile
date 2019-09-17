FROM python:3

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

# Create a uwsgi log directory and files
RUN mkdir /var/log/uwsgi
RUN touch /var/log/uwsgi/uwsgi_access.log
RUN touch /var/log/uwsgi/uwsgi_error.log

CMD ["uwsgi", "app.ini"]

