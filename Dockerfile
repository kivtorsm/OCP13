# pull the official base image
FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app
RUN #python manage.py collectstatic --noinput

#EXPOSE 8000
#   \1111\  \\\\1\1
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
