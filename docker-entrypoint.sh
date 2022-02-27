#!/bin/sh
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "runserver"
gunicorn --bind 0.0.0.0:8000 drf_assignment.wsgi
