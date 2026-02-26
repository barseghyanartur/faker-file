Testing with Docker
===================

Quick Start
-----------

Run all tests::

    make docker-test

Run specific environment::

    make docker-test ENV=py312-django42-pathy0110

List available environments::

    make docker-list-envs

View Coverage
-------------

Coverage report is generated in ``htmlcov/`` directory::

    open htmlcov/index.html

Interactive Shell
-----------------

Open shell in container::

    make docker-shell

Clean Up
--------

Remove Docker containers and images::

    docker compose down
    docker rmi faker-file-tox
