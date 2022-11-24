# base image
FROM python:3.10.6-alpine

WORKDIR /usr/src/trucking

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/trucking

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]