#!/bin/sh

until cd /app/backend/src
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A core worker --loglevel=info --concurrency 1 -E
