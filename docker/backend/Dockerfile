FROM python:3.12.5-alpine

RUN apk update && apk add python3-dev gcc libc-dev

ENV APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $APP_HOME

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./backend/src/requirements/base.txt $APP_HOME
ADD ./backend/src/requirements/production.txt $APP_HOME
RUN pip install -r production.txt

ADD ./backend $APP_HOME/backend
ADD ./docker $APP_HOME/docker

RUN chmod +x /app/docker/backend/server-entrypoint.sh
RUN chmod +x /app/docker/backend/worker-entrypoint.sh