#!/bin/bash

# Dump auth data
pipenv run python manage.py dumpdata auth > /tmp/auth.json

# Remove db file
rm db.sqlite3

# Remove migration files

for item in $(find ./**/migrations/ -type f)
do
    if [[ $item != *__init__.py ]]; then
        rm "$item"
    fi
done

# Generate Migrations
pipenv run python manage.py makemigrations 
pipenv run python manage.py migrate

# Load auth data
pipenv run python manage.py loaddata /tmp/auth.json