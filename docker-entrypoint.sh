#!/bin/sh
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "runserver"
python manage.py runserver