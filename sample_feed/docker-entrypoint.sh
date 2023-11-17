#!/bin/bash

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

python manage.py makemigrations && python manage.py migrate

echo "from sample_feed.scripts import do_initial_gen;do_initial_gen();exit()" | python manage.py shell

gunicorn --config gunicorn_config.py wsgi:application