#!/usr/bin/env bash
cd examples/django_example/
./manage.py shell --traceback -v 3 "$@"
