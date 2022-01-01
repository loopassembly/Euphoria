FROM python:3.8-alpine
LABEL maintainer "Euphoria team India"
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN apk update && apk upgrade
RUN apk add gcc
RUN apk add  musl-dev
RUN pip install --trusted-host pypi.python.org -r /requirements.txt
RUN mkdir /app
WORKDIR /app
COPY ./app /app
RUN adduser -D user
USER user