.PHONY: clean_up another_script

# Update version ONLY here
VERSION := 0.18.2

alembic-migrate:
	cd examples/sqlalchemy_example/faker_file_admin/ && alembic upgrade head

benchmark-test:
	pytest -vvrx --durations=0

build-docs:
	sphinx-build -n -a -b html docs builddocs
	cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..

check-release:
	python setup.py sdist bdist_wheel
	twine check dist/*

clean-dev:
	find . -name "*.orig" -exec rm -rf {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
	rm -rf dist/
	rm -rf src/faker-file.egg-info/
	rm -rf src/faker-file/var/
	rm -rf .cache/
	rm -rf .idea/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/

clean-docs:
	rm -rf build/
	rm -rf builddocs/
	rm -rf docs/_build/

clean-test:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.py,cover" -exec rm -rf {} \;
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf htmlcov/

clean: clean-dev clean-docs clean-test

compile-requirements:
	echo "common.in"
	uv pip compile --no-strip-extras examples/requirements/common.in -o examples/requirements/common.txt

	echo "debug.in"
	uv pip compile --no-strip-extras examples/requirements/debug.in -o examples/requirements/debug.txt

	echo "deployment.in"
	uv pip compile --no-strip-extras examples/requirements/deployment.in -o examples/requirements/deployment.txt

	echo "dev.in"
	uv pip compile --no-strip-extras examples/requirements/dev.in -o examples/requirements/dev.txt

	echo "django_5_0.in"
	uv pip compile --no-strip-extras examples/requirements/django_5_0.in -o examples/requirements/django_5_0.txt

	echo "django_5_1.in"
	uv pip compile --no-strip-extras examples/requirements/django_5_1.in -o examples/requirements/django_5_1.txt

	echo "django_4_2.in"
	uv pip compile --no-strip-extras examples/requirements/django_4_2.in -o examples/requirements/django_4_2.txt

	echo "django_5_0_and_flask.in"
	uv pip compile --no-strip-extras examples/requirements/django_5_0_and_flask.in -o examples/requirements/django_5_0_and_flask.txt

	echo "django_5_1_and_flask.in"
	uv pip compile --no-strip-extras examples/requirements/django_5_1_and_flask.in -o examples/requirements/django_5_1_and_flask.txt

	echo "django_4_2_and_flask.in"
	uv pip compile --no-strip-extras examples/requirements/django_4_2_and_flask.in -o examples/requirements/django_4_2_and_flask.txt

	echo "docs.in"
	uv pip compile --no-strip-extras examples/requirements/docs.in -o examples/requirements/docs.txt

	echo "flask.in"
	uv pip compile --no-strip-extras examples/requirements/flask.in -o examples/requirements/flask.txt

	echo "ml.in"
	uv pip compile --no-strip-extras examples/requirements/ml.in -o examples/requirements/ml.txt

	echo "style_checkers.in"
	uv pip compile --no-strip-extras examples/requirements/style_checkers.in -o examples/requirements/style_checkers.txt

	echo "test.in"
	uv pip compile --no-strip-extras examples/requirements/test.in -o examples/requirements/test.txt

	echo "testing.in"
	uv pip compile --no-strip-extras examples/requirements/testing.in -o examples/requirements/testing.txt

compile-requirements-upgrade:
	echo "common.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/common.in -o examples/requirements/common.txt

	echo "debug.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/debug.in -o examples/requirements/debug.txt

	echo "deployment.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/deployment.in -o examples/requirements/deployment.txt

	echo "dev.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/dev.in -o examples/requirements/dev.txt

	echo "django_5_0.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/django_5_0.in -o examples/requirements/django_5_0.txt

	echo "django_5_1.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/django_5_1.in -o examples/requirements/django_5_1.txt

	echo "django_4_2.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/django_4_2.in -o examples/requirements/django_4_2.txt

	echo "django_5_0_and_flask.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/django_5_0_and_flask.in -o examples/requirements/django_5_0_and_flask.txt

	echo "django_5_1_and_flask.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/django_5_1_and_flask.in -o examples/requirements/django_5_1_and_flask.txt

	echo "django_4_2_and_flask.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/django_4_2_and_flask.in -o examples/requirements/django_4_2_and_flask.txt

	echo "docs.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/docs.in -o examples/requirements/docs.txt

	echo "flask.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/flask.in -o examples/requirements/flask.txt

	echo "ml.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/ml.in -o examples/requirements/ml.txt

	echo "style_checkers.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/style_checkers.in -o examples/requirements/style_checkers.txt

	echo "test.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/test.in -o examples/requirements/test.txt

	echo "testing.in"
	uv pip compile --upgrade --no-strip-extras examples/requirements/testing.in -o examples/requirements/testing.txt

detect-secrets-create-baseline:
	detect-secrets scan > .secrets.baseline

detect-secrets-update-baseline:
	detect-secrets scan --baseline .secrets.baseline

doc8:
	doc8

flask-runserver:
	python examples/sqlalchemy_example/run_server.py

pre-commit:
	pre-commit run --all-files

install: compile_requirements
	pip install -r examples/requirements/dev.txt
	pip install -e .'[all]'
	mkdir -p var/logs examples/db examples/media examples/media/static
	python examples/django_example/manage.py collectstatic --noinput
	python examples/django_example/manage.py migrate --noinput

jupyter:
	cd examples/django_example/ && TOKENIZERS_PARALLELISM=true ./manage.py shell_plus --notebook

make-migrations:
	echo 'Making messages for faker-file...'
	cd examples/django_example/ && ./manage.py makemigrations faker-file

	echo 'Making messages for example projects...'
	./manage.py makemigrations

	echo 'Applying migrations...'
	./manage.py migrate

release:
	python setup.py sdist bdist_wheel
	twine upload dist/* --verbose

test-release:
	python setup.py sdist bdist_wheel
	twine upload --repository testpypi dist/* --verbose

migrate:
	cd examples/django_example/ && ./manage.py migrate "$$@"

mypy:
	mypy src/

auto-build-docs:
	sphinx-autobuild docs docs/_build/html

rebuild-docs: clean
	sphinx-apidoc src/faker_file --full -o docs -H 'faker-file' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
	cp docs/conf.py.distrib docs/conf.py
	cp docs/index.rst.distrib docs/index.rst

ruff:
	ruff check conftest.py --fix
	ruff check setup.py --fix
	ruff check examples/ --fix
	ruff check src/ --fix

runserver:
	cd examples/django_example/ && ./manage.py runserver 0.0.0.0:8000 --traceback -v 3 "$$@"

serve-docs:
	cd builddocs/ && python -m http.server 5001

shell:
	cd examples/django_example/ && ./manage.py shell --traceback -v 3 "$$@"

sqlalchemy-shell:
	cd examples/sqlalchemy_example/ && ipython

test-main:
	pytest -vrx -m "not optional" --ignore src/faker_file/tests/test_sqlalchemy_integration.py --ignore src/faker_file/tests/test_augment_file_from_dir_provider.py

test-main-collect-only:
	pytest -vrx -m "not optional" --ignore src/faker_file/tests/test_sqlalchemy_integration.py --ignore src/faker_file/tests/test_augment_file_from_dir_provider.py --collect-only

test-sqlalchemy-integration:
	pytest -vrx src/faker_file/tests/test_sqlalchemy_integration.py

test-sqlalchemy-integration-collect-only:
	pytest -vrx src/faker_file/tests/test_sqlalchemy_integration.py --collect-only

test-augmented-file-from-dir-provider:
	pytest -vrx src/faker_file/tests/test_augment_file_from_dir_provider.py

test:
	pytest

test-with-local-tika:
	TIKA_SERVER_JAR="file:///$(shell pwd)/tika-server.jar" pytest

test-rst-docs:
	pytest *.rst docs/*.rst

test-tests:
	pytest --cov-config=tests.coveragerc

uninstall:
	pip uninstall faker-file -y
	rm build -rf
	rm dist -rf
	rm src/faker-file.egg-info -rf
	rm builddocs.zip
	rm builddocs/ -rf

upgrade-requirements: compile-requirements-upgrade

update-version:
	@echo "Updating version in setup.py and __init__.py"
	@if [ "$(UNAME_S)" = "Darwin" ]; then \
		gsed -i 's/version = "[0-9.]\+"/version = "$(VERSION)"/' setup.py; \
		gsed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' src/faker_file/__init__.py; \
	else \
		sed -i 's/version = "[0-9.]\+"/version = "$(VERSION)"/' setup.py; \
		sed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' src/faker_file/__init__.py; \
	fi
