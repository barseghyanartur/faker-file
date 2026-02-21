Testing with Docker
===================

Quick Start
-----------

Run tests in Docker (recommended for macOS)::

    make docker-test  # defaults to 3.12
    make docker-test PYTHON_VERSION=3.11
    make docker-test PYTHON_VERSION=3.13

This will:

- Build the Docker image with all dependencies (including wkhtmltopdf)
- Install the package with all extras
- Run the full test suite
- Generate coverage report in ``htmlcov/`` directory

View Coverage
-------------

Open the coverage report in your browser::

    open htmlcov/index.html

Interactive Shell
-----------------

For debugging or manual testing::

    make docker-shell

This drops you into a bash shell inside the container with all dependencies installed.

Clean Up
--------

Remove Docker containers and images::

    docker-compose down
    docker rmi faker-file
