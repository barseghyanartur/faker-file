#!/usr/bin/env bash
echo "common.in"
pip-compile examples/requirements/common.in --upgrade

echo "debug.in"
pip-compile examples/requirements/debug.in --upgrade

echo "deployment.in"
pip-compile examples/requirements/deployment.in --upgrade

echo "dev.in"
pip-compile examples/requirements/dev.in --upgrade
#pip-compile examples/requirements/django_2_2.in --upgrade
#pip-compile examples/requirements/django_3_0.in --upgrade
#pip-compile examples/requirements/django_3_1.in --upgrade

echo "django_3_2.in"
pip-compile examples/requirements/django_3_2.in --upgrade

echo "django_4_1.in"
pip-compile examples/requirements/django_4_1.in --upgrade

echo "django_4_2.in"
pip-compile examples/requirements/django_4_2.in --upgrade

echo "django_3_2_and_flask.in"
pip-compile examples/requirements/django_3_2_and_flask.in --upgrade

echo "django_4_1_and_flask.in"
pip-compile examples/requirements/django_4_1_and_flask.in --upgrade

echo "django_4_2_and_flask.in"
pip-compile examples/requirements/django_4_2_and_flask.in --upgrade

echo "docs.in"
pip-compile examples/requirements/docs.in --upgrade

echo "flask.in"
pip-compile examples/requirements/flask.in --upgrade

echo "ml.in"
pip-compile examples/requirements/ml.in --upgrade

echo "style_checkers.in"
pip-compile examples/requirements/style_checkers.in --upgrade

echo "test.in"
pip-compile examples/requirements/test.in --upgrade

echo "testing.in"
pip-compile examples/requirements/testing.in --upgrade
