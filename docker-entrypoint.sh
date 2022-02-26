#!/bin/sh
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "runserver"
gunicorn drf_assignment.wsgi:application --bind 0.0.0.0:$PORT