.PHONY: clean_up another_script

alembic_migrate:
	cd examples/sqlalchemy_example/faker_file_admin/
	alembic upgrade head

benchmark_test:
	pytest -vvrx --durations=0

black:
	black .

build_docs:
	sphinx-build -n -a -b html docs builddocs
	cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..

check_release:
	python setup.py sdist bdist_wheel
	twine check dist/* --verbose

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.py,cover" -exec rm -rf {} \;
	find . -name "*.orig" -exec rm -rf {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
	rm -rf build/
	rm -rf builddocs/
	rm -rf dist/
	rm -rf src/faker-file.egg-info/
	rm -rf src/faker-file/var/
	rm -rf .cache/
	rm -rf .idea/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/

compile_requirements:
	echo "common.in"
	pip-compile examples/requirements/common.in "$$@"

	echo "debug.in"
	pip-compile examples/requirements/debug.in "$$@"

	echo "deployment.in"
	pip-compile examples/requirements/deployment.in "$$@"

	echo "dev.in"
	pip-compile examples/requirements/dev.in "$$@"

	echo "django_2_2.in"
	pip-compile examples/requirements/django_2_2.in "$$@"

	echo "django_3_2.in"
	pip-compile examples/requirements/django_3_2.in "$$@"

	echo "django_4_0.in"
	pip-compile examples/requirements/django_4_0.in "$$@"

	echo "django_4_1.in"
	pip-compile examples/requirements/django_4_1.in "$$@"

	echo "django_4_2.in"
	pip-compile examples/requirements/django_4_2.in "$$@"

	echo "django_2_2_and_flask.in"
	pip-compile examples/requirements/django_2_2_and_flask.in "$$@"

	echo "django_3_2_and_flask.in"
	pip-compile examples/requirements/django_3_2_and_flask.in "$$@"

	echo "django_4_0_and_flask.in"
	pip-compile examples/requirements/django_4_0_and_flask.in "$$@"

	echo "django_4_1_and_flask.in"
	pip-compile examples/requirements/django_4_1_and_flask.in "$$@"

	echo "django_4_2_and_flask.in"
	pip-compile examples/requirements/django_4_2_and_flask.in "$$@"

	echo "docs.in"
	pip-compile examples/requirements/docs.in "$$@"

	echo "flask.in"
	pip-compile examples/requirements/flask.in "$$@"

	echo "ml.in"
	pip-compile examples/requirements/ml.in "$$@"

	echo "style_checkers.in"
	pip-compile examples/requirements/style_checkers.in "$$@"

	echo "test.in"
	pip-compile examples/requirements/test.in "$$@"

	echo "testing.in"
	pip-compile examples/requirements/testing.in "$$@"

detect_secrets_create_baseline:
	detect-secrets scan > .secrets.baseline

detect_secrets_update_baseline:
	detect-secrets scan --baseline .secrets.baseline

doc8:
	doc8

flask_runserver:
	python examples/sqlalchemy_example/run_server.py

install:
	pip-compile examples/requirements/dev.in
	pip install -r examples/requirements/dev.txt
	pip install -e .
	mkdir -p var/logs examples/db examples/media examples/media/static
	python examples/django_example/manage.py collectstatic --noinput
	python examples/django_example/manage.py migrate --noinput

isort:
	isort . --overwrite-in-place

jupyter:
	cd examples/django_example/
	TOKENIZERS_PARALLELISM=true ./manage.py shell_plus --notebook

make_migrations:
	echo 'Making messages for faker-file...'
	cd examples/django_example/
	./manage.py makemigrations faker-file

	echo 'Making messages for example projects...'
	./manage.py makemigrations

	echo 'Applying migrations...'
	./manage.py migrate

make_release:
	python setup.py sdist bdist_wheel
	twine upload dist/* --verbose

migrate:
	cd examples/django_example/
	./manage.py migrate "$$@"

mypy:
	mypy src/

rebuild_docs: clean_up
	sphinx-apidoc src/faker_file --full -o docs -H 'faker-file' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
	cp docs/conf.py.distrib docs/conf.py
	cp docs/index.rst.distrib docs/index.rst

ruff:
	ruff conftest.py
	ruff setup.py
	ruff examples/
	ruff src/

runserver:
	cd examples/django_example/
	./manage.py runserver 0.0.0.0:8000 --traceback -v 3 "$$@"

serve_docs:
	cd builddocs/
	python -m http.server 5000

shell:
	cd examples/django_example/ && ./manage.py shell --traceback -v 3 "$$@"

sqlalchemy_shell:
	cd examples/sqlalchemy_example/
	ipython

test:
	pytest

test_with_local_tika:
	TIKA_SERVER_JAR="file:///$(shell pwd)/tika-server.jar" pytest

test_rst_docs:
	pytest *.rst docs/*.rst

test_tests:
	pytest --cov-config=tests.coveragerc

uninstall:
	pip uninstall faker-file -y
	rm build -rf
	rm dist -rf
	rm src/faker-file.egg-info -rf
	rm builddocs.zip
	rm builddocs/ -rf

upgrade_requirements:
	echo "common.in"
	pip-compile examples/requirements/common.in --upgrade "$$@"

	echo "debug.in"
	pip-compile examples/requirements/debug.in --upgrade "$$@"

	echo "deployment.in"
	pip-compile examples/requirements/deployment.in --upgrade "$$@"

	echo "dev.in"
	pip-compile examples/requirements/dev.in --upgrade "$$@"

	echo "django_3_2.in"
	pip-compile examples/requirements/django_3_2.in --upgrade "$$@"

	echo "django_4_1.in"
	pip-compile examples/requirements/django_4_1.in --upgrade "$$@"

	echo "django_4_2.in"
	pip-compile examples/requirements/django_4_2.in --upgrade "$$@"

	echo "django_3_2_and_flask.in"
	pip-compile examples/requirements/django_3_2_and_flask.in --upgrade "$$@"

	echo "django_4_1_and_flask.in"
	pip-compile examples/requirements/django_4_1_and_flask.in --upgrade "$$@"

	echo "django_4_2_and_flask.in"
	pip-compile examples/requirements/django_4_2_and_flask.in --upgrade "$$@"

	echo "docs.in"
	pip-compile examples/requirements/docs.in --upgrade "$$@"

	echo "flask.in"
	pip-compile examples/requirements/flask.in --upgrade "$$@"

	echo "ml.in"
	pip-compile examples/requirements/ml.in --upgrade "$$@"

	echo "style_checkers.in"
	pip-compile examples/requirements/style_checkers.in --upgrade "$$@"

	echo "test.in"
	pip-compile examples/requirements/test.in --upgrade "$$@"

	echo "testing.in"
	pip-compile examples/requirements/testing.in --upgrade "$$@"
