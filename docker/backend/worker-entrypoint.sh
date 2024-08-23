#!/bin/sh

until cd /app/backend/src
do
    echo "Waiting for server volume..."
done

DJANGO_SETTINGS_MODULE='core.settings.production' celery -A core worker --loglevel=info --concurrency 1 -E
