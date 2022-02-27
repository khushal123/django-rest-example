#!/bin/sh
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "runserver"
gunicorn --bind 0.0.0.0:$PORT drf_assignment.wsgi
# python manage.py runserver