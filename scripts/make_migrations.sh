#!/usr/bin/env bash
echo 'Making messages for faker-file...'
cd examples/django_example/
./manage.py makemigrations faker-file

echo 'Making messages for example projects...'
./manage.py makemigrations

echo 'Applying migrations...'
./manage.py migrate
