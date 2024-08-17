#!/bin/sh

until cd /app/backend/src
do
    echo "Waiting for server volume..."
done


until python manage.production.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


python manage.production.py collectstatic --noinput

# python manage.py createsuperuser --noinput

gunicorn core.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

#python manage.py runserver 0.0.0.0:8000