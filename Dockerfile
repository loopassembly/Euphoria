FROM python:3.8-alpine
LABEL maintainer "Euphoria team India"
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

# RUN apk add --update --no-cache postgresql-client
# RUN apk add --update --no-cache --virtual .tmp-build-deps \
#     gcc libc-dev linux-headers postgresql-dev

RUN apk update && apk upgrade
RUN apk add gcc
RUN apk add  musl-dev\
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg 
    


RUN pip install --trusted-host pypi.python.org -r /requirements.txt

# RUN apk del .tmp-build-deps
RUN mkdir /app
WORKDIR /app

# collect static files

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python", "manage.py", "runserver"]
CMD ["gunicorn" ,"app.wsgi:application","--bind 0.0.0.0:$PORT"]
COPY ./app /app
RUN  python manage.py collectstatic --noinput 
RUN adduser -D user
USER user