#!/usr/bin/env bash
cd examples/requirements/
echo "common.in"
pip-compile common.in "$@"

echo "debug.in"
pip-compile debug.in "$@"

echo "deployment.in"
pip-compile deployment.in "$@"

echo "dev.in"
pip-compile dev.in "$@"

echo "flask.in"
pip-compile flask.in "$@"

echo "django_2_2.in"
pip-compile django_2_2.in "$@"

echo "django_3_0.in"
pip-compile django_3_0.in "$@"

echo "django_3_1.in"
pip-compile django_3_1.in "$@"

echo "django_3_2.in"
pip-compile django_3_2.in "$@"

echo "django_4_0.in"
pip-compile django_4_0.in "$@"

echo "django_4_1.in"
pip-compile django_4_1.in "$@"
#pip-compile django_2_2_and_flask.in "$@"
#pip-compile django_3_0_and_flask.in "$@"
#pip-compile django_3_1_and_flask.in "$@"
#pip-compile django_3_2_and_flask.in "$@"

echo "docs.in"
pip-compile docs.in "$@"

echo "style_checkers.in"
pip-compile style_checkers.in "$@"

echo "test.in"
pip-compile test.in "$@"

echo "testing.in"
pip-compile testing.in "$@"
