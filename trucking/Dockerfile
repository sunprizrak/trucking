FROM python:3.10.11-alpine

# set work directory
WORKDIR /usr/src/trucking

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/

# copy project
COPY . .

ENTRYPOINT ["sh", "/usr/src/trucking/entrypoint.sh"]