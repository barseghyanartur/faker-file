Contributor guidelines
======================

.. _documentation: https://faker-file.readthedocs.io/#writing-documentation
.. _testing: https://faker-file.readthedocs.io/#testing
.. _pre-commit: https://pre-commit.com/#installation
.. _black: https://black.readthedocs.io/
.. _isort: https://pycqa.github.io/isort/
.. _doc8: https://doc8.readthedocs.io/
.. _ruff: https://beta.ruff.rs/docs/
.. _pip-tools: https://pip-tools.readthedocs.io/
.. _uv: https://docs.astral.sh/uv/
.. _issues: https://github.com/barseghyanartur/faker-file/issues
.. _discussions: https://github.com/barseghyanartur/faker-file/discussions
.. _pull request: https://github.com/barseghyanartur/faker-file/pulls
.. _support: https://faker-file.readthedocs.io/#support
.. _installation: https://faker-file.readthedocs.io/#installation
.. _features: https://faker-file.readthedocs.io/#features
.. _recipes: https://faker-file.readthedocs.io/en/latest/recipes.html
.. _quick start: https://faker-file.readthedocs.io/en/latest/quick_start.html
.. _prerequisites: https://faker-file.readthedocs.io/#prerequisites

Developer prerequisites
-----------------------
pre-commit
~~~~~~~~~~
Refer to `pre-commit`_ for installation instructions.

TL;DR:

.. code-block:: sh

    pip install pipx --user  # Install pipx
    pipx install pre-commit  # Install pre-commit
    pre-commit install  # Install pre-commit hooks

Installing `pre-commit`_ will ensure you adhere to the project code quality
standards.

Code standards
--------------
`ruff`_ and `doc8`_ will be automatically triggered by `pre-commit`_.

`ruff`_ is configured to do the job of `black`_ and `isort`_ as well, so
all the standards apply.

Still, if you want to run checks manually:

.. code-block:: sh

    make pre-commit

Requirements
------------
Requirements are compiled using `uv`_.

.. code-block:: sh

    make compile_requirements
    make compile_requirements_upgrade

Virtual environment
-------------------
You are advised to work in virtual environment.

TL;DR:

.. code-block:: sh

    python -m venv env
    make install

Documentation
-------------
Check `documentation`_.

Testing
-------
Check `testing`_.

If you introduce changes or fixes, make sure to test them locally using
all supported environments. For that use tox.

.. code-block:: sh

    tox

For quick testing in current environment only:

.. code-block:: sh

    make test

In any case, GitHub Actions will catch potential errors, but using tox speeds
things up.

Pull requests
-------------
You can contribute to the project by making a `pull request`_.

For example:

- To fix documentation typos.
- To improve documentation (for instance, to add new recipe or fix
  an existing recipe that doesn't seem to work).
- To introduce a new feature (for instance, add support for a non-supported
  file type).

**Good to know:**

- Test suite makes extensive use of parametrization. Make sure you have added
  your changes in the right place.

**General list to go through:**

- Does your change require documentation update?
- Does your change require update to tests?
- Did you test both Latin and Unicode characters?
- Does your change rely on third-party cloud based service? If so, please
  make sure it's added to tests that should be retried a couple of times.
  Example: ``@pytest.mark.flaky(reruns=5)``.

**When fixing bugs (in addition to the general list):**

- Make sure to add regression tests.

**When adding a new feature (in addition to the general list):**

- Check the licenses of added dependencies carefully and make sure to list them
  in `prerequisites`_.
- Make sure to update the documentation (check whether the `installation`_,
  `features`_, `recipes`_ and `quick start`_ require changes).

Questions
---------
Questions can be asked on GitHub `discussions`_.

Issues
------
For reporting a bug or filing a feature request use GitHub `issues`_.

**Do not report security issues on GitHub**. Check the `support`_ section.
