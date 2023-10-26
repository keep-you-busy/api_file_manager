#!/bin/sh

cd /usr/src/app/api_file_manager
python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000 &

celery -A api_file_manager worker --loglevel=info --logfile=logs/celery.log &

tail -f /dev/null
