==========
faker-file
==========
**Generate files with fake data**

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

- Core package requires Python 3.7, 3.8, 3.9, 3.10 or 3.11.
- ``Faker`` (`MIT`) is the only required dependency.
- ``Django`` (`BSD`) integration with ``factory_boy`` (`MIT`) has
  been tested with ``Django`` 2.2, 3.0, 3.1, 3.2, 4.0 and 4.1.
- ``DOCX`` file support requires ``python-docx`` (`MIT`).
- ``EPUB`` file support requires ``xml2epub`` (`MIT`) and ``jinja2`` (`BSD`).
- ``ICO``, ``JPEG``, ``PNG``, ``SVG`` and ``WEBP`` files support
  requires ``imgkit`` (`MIT`).
- ``MP3`` file support requires ``gtts`` (`MIT`).
- ``PDF`` file support requires ``pdfkit`` (`MIT`).
- ``PPTX`` file support requires ``python-pptx`` (`MIT`).
- ``ODS`` file support requires ``tablib`` (`MIT`) and ``odfpy`` (`Apache 2`).
- ``XLSX`` file support requires ``tablib`` (`MIT`) and ``openpyxl`` (`MIT`).
- ``PathyFileSystemStorage`` storage support requires ``pathy`` (`Apache 2`).
- ``AWSS3Storage`` storage support requires ``pathy`` (`Apache 2`)
  and ``boto3`` (`Apache 2`).
- ``AzureCloudStorage`` storage support requires ``pathy`` (`Apache 2`)
  and ``azure-storage-blob`` (`MIT`).
- ``GoogleCloudStorage`` storage support requires ``pathy`` (`Apache 2`)
  and ``google-cloud-storage`` (`Apache 2`).

Documentation
=============
Documentation is available on `Read the Docs
<http://faker-file.readthedocs.io/>`_.

Installation
============
Latest stable version from PyPI
-------------------------------
**WIth all dependencies**

.. code-block:: sh

    pip install faker-file[all]

**Only core**

.. code-block:: sh

    pip install faker-file

**With DOCX support**

.. code-block:: sh

    pip install faker-file[docx]

**With EPUB support**

.. code-block:: sh

    pip install faker-file[epub]

**With images support**

.. code-block:: sh

    pip install faker-file[images]

**With MP3 support**

.. code-block:: sh

    pip install faker-file[mp3]

**With XLSX support**

.. code-block:: sh

    pip install faker-file[xlsx]

**With ODS support**

.. code-block:: sh

    pip install faker-file[ods]

Or development version from GitHub
----------------------------------

.. code-block:: sh

    pip install https://github.com/barseghyanartur/faker-file/archive/main.tar.gz

Features
========

Supported file types
--------------------
- ``BIN``
- ``CSV``
- ``DOCX``
- ``EML``
- ``EPUB``
- ``ICO``
- ``JPEG``
- ``MP3``
- ``ODS``
- ``PDF``
- ``PNG``
- ``RTF``
- ``PPTX``
- ``SVG``
- ``TXT``
- ``WEBP``
- ``XLSX``
- ``ZIP``

Additional providers
--------------------
- ``RandomFileFromDirProvider``: Pick a random file from given directory.

Supported file storages
-----------------------
- Native file system storage
- AWS S3 storage
- Azure Cloud Storage
- Google Cloud Storage

Usage examples
==============
With ``Faker``
--------------
**One way**

.. code-block:: python

    from faker import Faker
    from faker_file.providers.txt_file import TxtFileProvider

    FAKER = Faker()

    file = TxtFileProvider(FAKER).txt_file()

**Or another**

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

upload/factories.py
~~~~~~~~~~~~~~~~~~~
Note, that when using ``faker-file`` with ``Django`` and native file system
storages, you need to pass your ``MEDIA_ROOT`` setting as ``root_path`` value
to the chosen file storage as show below.

.. code-block:: python

    import factory
    from django.conf import settings
    from factory import Faker
    from factory.django import DjangoModelFactory
    from faker_file.providers.docx_file import DocxFileProvider
    from faker_file.storages.filesystem import FileSystemStorage

    from upload.models import Upload

    FS_STORAGE = FileSystemStorage(
        root_path=settings.MEDIA_ROOT,
        rel_path="tmp"
    )
    factory.Faker.add_provider(DocxFileProvider)

    class UploadFactory(DjangoModelFactory):

        # ...
        file = Faker("docx_file", storage=FS_STORAGE)

        class Meta:
            model = Upload

File storages
=============
All file operations are delegated to a separate abstraction layer of storages.

The following storages are implemented:

- ``FileSystemStorage``: Does not have additional requirements.
- ``PathyFileSystemStorage``: Requires `pathy`.
- ``AzureCloudStorage``: Requires `pathy` and `Azure` related dependencies.
- ``GoogleCloudStorage``: Requires `pathy` and `Google Cloud` related
  dependencies.
- ``AWSS3Storage``: Requires `pathy` and `AWS S3` related dependencies.

Usage example with storages
---------------------------
`FileSystemStorage` example
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Native file system storage. Does not have dependencies.

.. code-block:: python

    import tempfile
    from faker import Faker
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.storages.filesystem import FileSystemStorage

    FS_STORAGE = FileSystemStorage(
        root_path=tempfile.gettempdir(),  # Use settings.MEDIA_ROOT for Django
        rel_path="tmp",
    )

    FAKER = Faker()

    file = TxtFileProvider(FAKER).txt_file(storage=FS_STORAGE)

    FS_STORAGE.exists(file)

`PathyFileSystemStorage` example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Native file system storage. Requires `pathy`.

.. code-block:: python

    import tempfile
    from pathy import use_fs
    from faker import Faker
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.storages.cloud import PathyFileSystemStorage

    use_fs(tempfile.gettempdir())
    PATHY_FS_STORAGE = PathyFileSystemStorage(
        bucket_name="bucket_name",
        root_path="tmp"
        rel_path="sub-tmp",
    )

    FAKER = Faker()

    file = TxtFileProvider(FAKER).txt_file(storage=PATHY_FS_STORAGE)

    PATHY_FS_STORAGE.exists(file)

`AWSS3Storage` example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AWS S3 storage. Requires `pathy`.

.. code-block:: python

    import tempfile
    from pathy import use_fs
    from faker import Faker
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.storages.aws_s3 import AWSS3Storage

    S3_STORAGE = AWSS3Storage(
        bucket_name="bucket_name",
        root_path="tmp",  # Optional
        rel_path="sub-tmp",  # Optional
        # Credentials are optional too. If your AWS credentials are properly
        # set in the ~/.aws/credentials, you don't need to send them
        # explicitly.
        credentials={
            "key_id": "YOUR KEY ID",
            "key_secret": "YOUR KEY SECRET"
        },
    )

    FAKER = Faker()

    file = TxtFileProvider(FAKER).txt_file(storage=S3_STORAGE)

    S3_STORAGE.exists(file)

Testing
=======
Simply type:

.. code-block:: sh

    pytest -vrx

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
For security issues contact me at the e-mail given in the `Author`_ section.

For overall issues, go to `GitHub <https://github.com/barseghyanartur/faker-file/issues>`_.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
