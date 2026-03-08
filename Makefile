.PHONY: clean_up another_script

# Update version ONLY here
VERSION := 0.19
SHELL := /bin/bash
VENV := .venv/bin/activate
UNAME_S := $(shell uname -s)

# ----------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------

benchmark-test:
	source $(VENV) && pytest -vvrx --durations=0

# ----------------------------------------------------------------------------
# Documentation
# ----------------------------------------------------------------------------

build-docs:
	source $(VENV) && python scripts/generate_project_source_tree.py
	source $(VENV) && sphinx-build -n -b text docs builddocs
	source $(VENV) && sphinx-build -n -a -b html docs builddocs
	cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..

check-release:
	source $(VENV) && python -m build
	source $(VENV) && twine check dist/*

auto-build-docs:
	sphinx-autobuild docs docs/_build/html

rebuild-docs: clean
	sphinx-apidoc src/faker_file --full -o docs -H 'faker-file' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
	cp docs/conf.py.distrib docs/conf.py
	cp docs/index.rst.distrib docs/index.rst

serve-docs:
	source $(VENV) && cd builddocs/ && python -m http.server 5001

# ----------------------------------------------------------------------------
# Development
# ----------------------------------------------------------------------------

flask-runserver:
	source $(VENV) && python examples/sqlalchemy_example/run_server.py

create-venv:
	uv venv

install:
	source $(VENV) && uv pip install -e .'[all]'
	source $(VENV) && uv pip install -r examples/requirements/django_4_2.in
	mkdir -p var/logs examples/db examples/media examples/media/static
	source $(VENV) && python examples/django_example/manage.py collectstatic --noinput
	source $(VENV) && python examples/django_example/manage.py migrate --noinput

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

# ----------------------------------------------------------------------------
# Security
# ----------------------------------------------------------------------------

detect-secrets-create-baseline:
	source $(VENV) && detect-secrets scan > .secrets.baseline

detect-secrets-update-baseline:
	source $(VENV) && detect-secrets scan --baseline .secrets.baseline

# ----------------------------------------------------------------------------
# Docker test
# ----------------------------------------------------------------------------

docker-build:
	docker compose build

# List all available environments in the Docker container
docker-list-envs: docker-build
	docker compose run --rm tox -l

docker-test: docker-build
	@if [ -n "$(ENV)" ]; then \
		docker compose run --rm tox -e $(ENV); \
	else \
		docker compose run --rm tox; \
	fi

# Usage:
#  make docker-test-env ENV=py312-django42-pathy0110-sqlalchemy
#  make docker-test-env ENV=py313-django42-pathy0110-sqlalchemy
docker-test-env: docker-build
	@if [ -z "$(ENV)" ]; then \
		echo "Usage: make docker-test-env ENV=py312-django42-pathy0110-sqlalchemy"; \
		exit 1; \
	fi
	docker compose run --rm tox -e $(ENV)

docker-test-docs: docker-build
	docker compose run --rm tox -e py310-docs,py311-docs,py312-docs,py313-docs

# Usage:
#  make docker-test-docs-env ENV=py313-docs
docker-test-docs-env: docker-build
	@if [ -z "$(ENV)" ]; then \
		echo "Usage: make docker-test-docs-env ENV=py313-docs"; \
		exit 1; \
	fi
	docker compose run --rm tox -e $(ENV)

docker-test-xml: docker-build
	docker compose run --rm tox -e py313-django42-pathy0110-sqlalchemy -- -k XMLFileProviderTestCase

docker-shell: docker-build
	docker compose run --rm --entrypoint bash tox

# Usage: make docker-shell-env ENV=py312-django42-pathy0110-sqlalchemy
docker-shell-env: docker-build
	@if [ -z "$(ENV)" ]; then \
		echo "Usage: make docker-shell-env ENV=py312-django42-pathy0110-sqlalchemy"; \
		exit 1; \
	fi
	docker compose run --rm --entrypoint bash tox -e $(ENV)

# ----------------------------------------------------------------------------
# Linting
# ----------------------------------------------------------------------------

doc8:
	source $(VENV) && doc8

mypy:
	source $(VENV) && mypy src/


ruff:
	source $(VENV) && ruff check conftest.py --fix
	source $(VENV) && ruff check examples/ --fix
	source $(VENV) && ruff check src/ --fix

# ----------------------------------------------------------------------------
# Pre-commit
# ----------------------------------------------------------------------------

pre-commit:
	pre-commit run --all-files

jupyter:
	source $(VENV) && cd examples/django_example/ && TOKENIZERS_PARALLELISM=true ./manage.py shell_plus --notebook

make-migrations:
	echo 'Making messages for faker-file...'
	source $(VENV) && cd examples/django_example/ && ./manage.py makemigrations faker-file

	echo 'Making messages for example projects...'
	source $(VENV) && ./manage.py makemigrations

	echo 'Applying migrations...'
	source $(VENV) && ./manage.py migrate

migrate:
	source $(VENV) && cd examples/django_example/ && ./manage.py migrate "$$@"

runserver:
	source $(VENV) && cd examples/django_example/ && ./manage.py runserver 0.0.0.0:8000 --traceback -v 3 "$$@"

shell:
	source $(VENV) && cd examples/django_example/ && ./manage.py shell --traceback -v 3 "$$@"

sqlalchemy-shell:
	source $(VENV) && cd examples/sqlalchemy_example/ && ipython

alembic-migrate:
	source $(VENV) && cd examples/sqlalchemy_example/faker_file_admin/ && alembic upgrade head

uninstall:
	source $(VENV) && uv pip uninstall faker-file -y
	rm build -rf
	rm dist -rf
	rm src/faker-file.egg-info -rf
	rm builddocs.zip
	rm builddocs/ -rf

upgrade-requirements: compile-requirements-upgrade

# ----------------------------------------------------------------------------
# Release
# ----------------------------------------------------------------------------

build:
	source $(VENV) && python -m build

release:
	source $(VENV) && twine upload dist/* --verbose

test-release:
	source $(VENV) && twine upload --repository testpypi dist/* --verbose

update-version:
	@echo "Updating version in pyproject.toml and __init__.py"
	@if [ "$(UNAME_S)" = "Darwin" ]; then \
		gsed -i 's/^version = "[0-9.]\+"/version = "$(VERSION)"/' pyproject.toml; \
		gsed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' src/faker_file/__init__.py; \
	else \
		sed -i 's/^version = "[0-9.]\+"/version = "$(VERSION)"/' pyproject.toml; \
		sed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' src/faker_file/__init__.py; \
	fi
