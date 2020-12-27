#!/usr/bin/env bash
cd leatherbound_www; python manage.py makemigrations; python manage.py migrate;
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)
fi
gunicorn leatherbound.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 -p gunicorn_pids
