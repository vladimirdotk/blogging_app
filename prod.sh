#!/bin/bash

./manage.py collectstatic --noinput
./manage.py migrate
gunicorn --workers=4 -b 0.0.0.0:8100 blogging_app.wsgi
