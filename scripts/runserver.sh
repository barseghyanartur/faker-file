#!/usr/bin/env bash
cd examples/django_example/
./manage.py runserver 0.0.0.0:8000 --traceback -v 3 "$@"
