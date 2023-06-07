# base image
FROM python:3.9-slim

#maintainer
LABEL Author="Daniel Tesfai"


# The environment variable ensures that the python
# output to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# switch to the app directory so that everything runs from here
COPY . /app/
COPY requirements.txt /app/
WORKDIR /app/src


# #installs the requirements
RUN pip install -r ../requirements.txt
EXPOSE 8000
# CMD python manage.py runserver 0.0.0.0:8000
CMD exec gunicorn --bind 0.0.0.0:8000 --workers 1 --threads 8 --timeout 0 --log-level=debug core.wsgi:application
#CMD exec gunicorn --bind 0.0.0.0:8000 --workers 1 --threads 8 --timeout 0 --log-level=debug --access-logfile=/logs/access.log --error-logfile=/logs/error.log core.wsgi:application

# FROM python:3.9-slim

# # maintainer
# LABEL Author="Daniel Tesfai"

# # The environment variable ensures that the python
# # output to the terminal without buffering it first
# ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1

# # switch to the app directory so that everything runs from here
# COPY . /app/
# COPY requirements.txt /app/
# WORKDIR /app/

# # install the requirements
# RUN pip install -r requirements.txt

# # install gunicorn
# RUN pip install gunicorn

# # expose port 8000
# EXPOSE 8000

# # run gunicorn with the app:app application
# CMD exec gunicorn --bind 0.0.0.0:8000 --workers 1 --threads 8 --timeout 0 src/core.wsgi:application




# FROM python:3.8-slim

# COPY ./requirements.txt /requirements.txt
# RUN pip install -r requirements.txt
# RUN pip install gunicorn
# COPY ./src /app
# WORKDIR /app


# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

#CMD exec gunicorn --bind 0.0.0.0:8000 --workers 1 --threads 8 --timeout 0 core.wsgi:application