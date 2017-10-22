#!/bin/bash

./manage.py collectstatic --noinput
./manage.py migrate
gunicorn -b 0.0.0.0:8100 blogging_app.wsgi