=============================================
SQLAlchemy example project for ``faker-file``
=============================================
*Used mainly for SQLAlchemy/Flask-Admin integration show-off.*

Migrate
=======
.. code-block:: shell

    cd admin
    alembic upgrade head

Run server
==========
.. code-block:: shell

    python examples/sqlalchemy_example/run_server.py

Testing
=======
.. code-block:: shell

    pytest -c pytest_sqlalchemy.ini src/faker_file/
