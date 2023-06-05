#!/usr/bin/env bash
#cd examples/requirements/
echo "common.in"
pip-compile examples/requirements/common.in "$@"

echo "debug.in"
pip-compile examples/requirements/debug.in "$@"

echo "deployment.in"
pip-compile examples/requirements/deployment.in "$@"

echo "dev.in"
pip-compile examples/requirements/dev.in "$@"

echo "django_2_2.in"
pip-compile examples/requirements/django_2_2.in "$@"

#echo "django_3_0.in"
#pip-compile examples/requirements/django_3_0.in "$@"
#
#echo "django_3_1.in"
#pip-compile examples/requirements/django_3_1.in "$@"

echo "django_3_2.in"
pip-compile examples/requirements/django_3_2.in "$@"

echo "django_4_0.in"
pip-compile examples/requirements/django_4_0.in "$@"

echo "django_4_1.in"
pip-compile examples/requirements/django_4_1.in "$@"

echo "django_4_2.in"
pip-compile examples/requirements/django_4_2.in "$@"

echo "django_2_2_and_flask.in"
pip-compile examples/requirements/django_2_2_and_flask.in "$@"

#echo "django_3_0_and_flask.in"
#pip-compile examples/requirements/django_3_0_and_flask.in "$@"
#
#echo "django_3_1_and_flask.in"
#pip-compile examples/requirements/django_3_1_and_flask.in "$@"

echo "django_3_2_and_flask.in"
pip-compile examples/requirements/django_3_2_and_flask.in "$@"

echo "django_4_0_and_flask.in"
pip-compile examples/requirements/django_4_0_and_flask.in "$@"

echo "django_4_1_and_flask.in"
pip-compile examples/requirements/django_4_1_and_flask.in "$@"

echo "django_4_2_and_flask.in"
pip-compile examples/requirements/django_4_2_and_flask.in "$@"

echo "docs.in"
pip-compile examples/requirements/docs.in "$@"

echo "flask.in"
pip-compile examples/requirements/flask.in "$@"

echo "ml.in"
pip-compile examples/requirements/ml.in "$@"

echo "style_checkers.in"
pip-compile examples/requirements/style_checkers.in "$@"

echo "test.in"
pip-compile examples/requirements/test.in "$@"

echo "testing.in"
pip-compile examples/requirements/testing.in "$@"
