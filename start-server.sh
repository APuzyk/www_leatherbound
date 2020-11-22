#!/usr/bin/env bash
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd leatherbound_www; python manage.py createsuperuser --no-input)
fi
(cd leatherbound_www; gunicorn leatherbound.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"