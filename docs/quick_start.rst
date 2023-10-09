Quick start
===========

Installation
------------
.. code-block:: sh

    pip install faker-file[all]

Usage
-----
With ``Faker``
~~~~~~~~~~~~~~
**Imports and initialization**

.. literalinclude:: _static/examples/quick_start/import_and_init_1.py
    :language: python
    :lines: 2-78

**Usage examples**

.. literalinclude:: _static/examples/quick_start/import_and_init_1.py
    :language: python
    :lines: 87-121

If you just need bytes back (instead of creating the file), provide
the ``raw=True`` argument (works with all provider classes and inner
functions):

.. literalinclude:: _static/examples/quick_start/import_and_init_1.py
    :language: python
    :lines: 124-

*See the full example*
:download:`here <_static/examples/quick_start/import_and_init_1.py>`

----

With ``factory_boy``
~~~~~~~~~~~~~~~~~~~~
**Imports and initialization**

.. literalinclude:: _static/examples/quick_start/factory_import_and_init_1.py
    :language: python
    :lines: 3, 5-45, 49-78

**upload/models.py**

.. literalinclude:: _static/examples/quick_start/factory_models_1.py
    :language: python
    :lines: 1, 3-11

*See the full example*
:download:`here <_static/examples/quick_start/factory_models_1.py>`

**upload/factories.py**

.. literalinclude:: _static/examples/quick_start/factory_import_and_init_1.py
    :language: python
    :lines: 2-4, 46-49, 80-118

**Usage example**

.. literalinclude:: _static/examples/quick_start/factory_import_and_init_1.py
    :language: python
    :lines: 122-

*See the full example*
:download:`here <_static/examples/quick_start/factory_import_and_init_1.py>`
