#!/bin/sh

until cd /app/backend/src
do
    echo "Waiting for server volume..."
done


# until python manage.production.py migrate
# do
#     echo "Waiting for db to be ready..."
#     sleep 2
# done


python manage.production.py collectstatic --noinput

gunicorn core.wsgi.production --bind 0.0.0.0:8000 --workers 4 --threads 4
