#!/bin/sh

cd /usr/src/app/api_file_manager
python manage.py makemigrations
python manage.py migrate

gunicorn api_file_manager.wsgi

celery -A api_file_manager worker --loglevel=info --logfile=logs/celery.log &

tail -f /dev/null
