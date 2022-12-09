==========
faker-file
==========
**Generate fake files**

.. image:: https://img.shields.io/pypi/v/faker-file.svg
   :target: https://pypi.python.org/pypi/faker-file
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/faker-file.svg
    :target: https://pypi.python.org/pypi/faker-file/
    :alt: Supported Python versions

.. image:: https://github.com/barseghyanartur/faker-file/workflows/test/badge.svg
   :target: https://github.com/barseghyanartur/faker-file/actions
   :alt: Build Status

.. image:: https://readthedocs.org/projects/faker-file/badge/?version=latest
    :target: http://faker-file.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/barseghyanartur/faker-file/#License
   :alt: MIT

.. image:: https://coveralls.io/repos/github/barseghyanartur/faker-file/badge.svg?branch=main&service=github
    :target: https://coveralls.io/github/barseghyanartur/faker-file?branch=main
    :alt: Coverage

Prerequisites
=============
All of core dependencies of this package are `MIT` licensed.
Most of optional dependencies of this package are `MIT` licensed, while
a few are `BSD`- or `Apache 2` licensed. All licenses are mentioned
below between the brackets.

- Core package requires Python 3.7, 3.8, 3.9, 3.10 and 3.11.
- ``Django`` (`BSD`) integration with ``factory_boy`` (`MIT`) has
  been tested with ``Django`` 2.2, 3.0, 3.1, 3.2, 4.0 and 4.1.
- ``DOCX`` file support requires ``python-docx`` (`MIT`).
- ``ICO``, ``JPEG``, ``PNG``, ``SVG`` and ``WEBP`` files support
  requires ``imgkit`` (`MIT`).
- ``PDF`` file support requires ``pdfkit`` (`MIT`).
- ``PPTX`` file support requires ``python-pptx`` (`MIT`).
- ``ODS`` file support requires ``tablib`` (`MIT`) and ``odfpy`` (`Apache 2`).
- ``XLSX`` file support requires ``tablib`` (`MIT`) and ``openpyxl`` (`MIT`).

Documentation
=============
Documentation is available on `Read the Docs
<http://faker-file.readthedocs.io/>`_.

Installation
============
Latest stable version on PyPI:

.. code-block:: sh

    pip install faker-file[all]

Or development version from GitHub:

.. code-block:: sh

    pip install https://github.com/barseghyanartur/faker-file/archive/main.tar.gz

Supported file types
====================

- BIN
- CSV
- DOCX
- ICO
- JPEG
- ODS
- PDF
- PNG
- PPTX
- SVG
- TXT
- WEBP
- XLSX
- ZIP

Usage examples
==============
With ``Faker``
--------------
One way
~~~~~~~

.. code-block:: python

    from faker import Faker
    from faker_file.providers.txt_file import TxtFileProvider

    FAKER = Faker()

    file = TxtFileProvider(FAKER).txt_file()

Or another
~~~~~~~~~~

.. code-block:: python

    from faker import Faker
    from faker_file.providers.txt_file import TxtFileProvider

    FAKER = Faker()
    FAKER.add_provider(TxtFileProvider)

    file = FAKER.txt_file()

With ``factory_boy``
--------------------
upload/models.py
~~~~~~~~~~~~~~~~
.. code-block:: python

    from django.db import models

    class Upload(models.Model):

        # ...
        file = models.FileField()

upload/factory.py
~~~~~~~~~~~~~~~~~
Note, that when using ``faker-file`` with ``Django``, you need to pass your
``MEDIA_ROOT`` setting as ``root_path`` value (which is by default set
to ``tempfile.gettempdir()``).

.. code-block:: python

    import factory
    from django.conf import settings
    from factory import Faker
    from factory.django import DjangoModelFactory
    from faker_file.providers.docx_file import DocxFileProvider

    from upload.models import Upload

    factory.Faker.add_provider(DocxFileProvider)

    class UploadFactory(DjangoModelFactory):

        # ...
        file = Faker("docx_file", root_path=settings.MEDIA_ROOT)

        class Meta:
            model = Upload

Testing
=======
Simply type:

.. code-block:: sh

    pytest -vvv

Or use tox:

.. code-block:: sh

    tox

Or use tox to check specific env:

.. code-block:: sh

    tox -e py310-django41

Writing documentation
=====================

Keep the following hierarchy.

.. code-block:: text

    =====
    title
    =====

    header
    ======

    sub-header
    ----------

    sub-sub-header
    ~~~~~~~~~~~~~~

    sub-sub-sub-header
    ^^^^^^^^^^^^^^^^^^

    sub-sub-sub-sub-header
    ++++++++++++++++++++++

    sub-sub-sub-sub-sub-header
    **************************

License
=======
MIT

Support
=======
For any security issues contact me at the e-mail given in the `Author`_ section.

For overall issues, go to `GitHub <https://github.com/barseghyanartur/faker-file/issues>`_.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
