==========
faker-file
==========
**Create files with fake data**. In many formats. With no efforts.

.. image:: https://img.shields.io/pypi/v/faker-file.svg
   :target: https://pypi.python.org/pypi/faker-file
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/faker-file.svg
    :target: https://pypi.python.org/pypi/faker-file/
    :alt: Supported Python versions

.. image:: https://github.com/barseghyanartur/faker-file/workflows/test/badge.svg?branch=main
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

.. Internal references

.. _Read the Docs: http://faker-file.readthedocs.io/
.. _Quick start: https://faker-file.readthedocs.io/en/latest/quick_start.html
.. _Recipes: https://faker-file.readthedocs.io/en/latest/recipes.html
.. _CLI: https://faker-file.readthedocs.io/en/latest/cli.html
.. _Contributor guidelines: https://faker-file.readthedocs.io/en/latest/contributor_guidelines.html

.. Related projects

.. _faker-file-api: https://github.com/barseghyanartur/faker-file-api
.. _faker-file-ui: https://github.com/barseghyanartur/faker-file-ui
.. _faker-file-wasm: https://github.com/barseghyanartur/faker-file-wasm

.. Demos

.. _REST API demo: https://faker-file-api.onrender.com/docs/
.. _UI frontend demo: https://faker-file-ui.vercel.app/
.. _WASM frontend demo: https://faker-file-wasm.vercel.app/

.. External references

.. _Faker: https://faker.readthedocs.io/
.. _Django: https://www.djangoproject.com/
.. _factory_boy: https://factoryboy.readthedocs.io/
.. _python-docx: https://python-docx.readthedocs.io/
.. _xml2epub: https://pypi.org/project/xml2epub/
.. _Jinja2: https://jinja.palletsprojects.com/
.. _imgkit: https://pypi.org/project/imgkit/
.. _wkhtmltopdf: https://wkhtmltopdf.org/
.. _gTTS: https://gtts.readthedocs.io/
.. _edge-tts: https://pypi.org/project/edge-tts/
.. _reportlab: https://pypi.org/project/reportlab/
.. _pdfkit: https://pypi.org/project/pdfkit/
.. _python-pptx: https://python-pptx.readthedocs.io/
.. _odfpy: https://pypi.org/project/odfpy/
.. _tablib: https://tablib.readthedocs.io/
.. _openpyxl: https://openpyxl.readthedocs.io/
.. _pathy: https://pypi.org/project/pathy/
.. _boto3: https://pypi.org/project/boto3/
.. _azure-storage-blob: https://pypi.org/project/azure-storage-blob/
.. _google-cloud-storage: https://pypi.org/project/google-cloud-storage/
.. _nlpaug: https://nlpaug.readthedocs.io/
.. _PyTorch: https://pytorch.org/
.. _transformers: https://pypi.org/project/transformers/
.. _numpy: https://numpy.org/
.. _pandas: https://pandas.pydata.org/
.. _tika: https://pypi.org/project/tika/
.. _Apache Tika: https://tika.apache.org/

Prerequisites
=============
All of core dependencies of this package are `MIT` licensed.
Most of optional dependencies of this package are `MIT` licensed, while
a few are `BSD`-, `Apache 2`- or `GPLv3` licensed. All licenses are mentioned
below between the brackets.

- Core package requires Python 3.7, 3.8, 3.9, 3.10 or 3.11.
- `Faker`_ (`MIT`) is the only required dependency.
- `Django`_ (`BSD`) integration with `factory_boy`_ (`MIT`) has
  been tested with ``Django`` 2.2, 3.0, 3.1, 3.2, 4.0 and 4.1.
- ``DOCX`` file support requires `python-docx`_ (`MIT`).
- ``EPUB`` file support requires `xml2epub`_ (`MIT`) and `Jinja2`_ (`BSD`).
- ``ICO``, ``JPEG``, ``PNG``, ``SVG`` and ``WEBP`` files support
  requires `imgkit`_ (`MIT`) and `wkhtmltopdf`_ (`LGPLv3`).
- ``MP3`` file support requires `gTTS`_ (`MIT`) or `edge-tts`_ (`GPLv3`).
- ``PDF`` file support requires either combination of `pdfkit`_ (`MIT`)
  and `wkhtmltopdf`_ (`LGPLv3`), or `reportlab`_ (`BSD`).
- ``PPTX`` file support requires `python-pptx`_ (`MIT`).
- ``ODP`` file support requires `odfpy`_ (`Apache 2`).
- ``ODS`` file support requires `tablib`_ (`MIT`) and `odfpy`_ (`Apache 2`).
- ``ODT`` file support requires `odfpy`_ (`Apache 2`).
- ``XLSX`` file support requires `tablib`_ (`MIT`) and `openpyxl`_ (`MIT`).
- ``PathyFileSystemStorage`` storage support requires `pathy`_ (`Apache 2`).
- ``AWSS3Storage`` storage support requires `pathy`_ (`Apache 2`)
  and `boto3`_ (`Apache 2`).
- ``AzureCloudStorage`` storage support requires `pathy`_ (`Apache 2`)
  and `azure-storage-blob`_ (`MIT`).
- ``GoogleCloudStorage`` storage support requires `pathy`_ (`Apache 2`)
  and `google-cloud-storage`_ (`Apache 2`).
- ``AugmentFileFromDirProvider`` provider requires `nlpaug`_ (`MIT`),
  `PyTorch`_ (`BSD`), `transformers`_ (`Apache 2`), `numpy`_ (`BSD`),
  `pandas`_ (`BSD`), `tika`_ (`Apache 2`) and `Apache Tika`_ (`Apache 2`).

Documentation
=============
- Documentation is available on `Read the Docs`_.
- For bootstrapping check the `Quick start`_.
- For various ready to use code examples see the `Recipes`_.
- For CLI options see the `CLI`_.
- For guidelines on contributing check the `Contributor guidelines`_.

Online demos
============
Check the demo(s):

- `REST API demo`_ (based on `faker-file-api`_ REST API)
- `UI frontend demo`_ (based on `faker-file-ui`_ UI frontend)
- `WASM frontend demo`_ (based on `faker-file-wasm`_ WASM frontend)

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

**With most common dependencies**

*Everything, except ML libraries which are required for data augmentation only*

.. code-block:: sh

    pip install faker-file[common]

**With DOCX support**

.. code-block:: sh

    pip install faker-file[docx]

**With EPUB support**

.. code-block:: sh

    pip install faker-file[epub]

**With images support**

.. code-block:: sh

    pip install faker-file[images]

**With PDF support**

.. code-block:: sh

    pip install faker-file[pdf]

**With MP3 support**

.. code-block:: sh

    pip install faker-file[mp3]

**With XLSX support**

.. code-block:: sh

    pip install faker-file[xlsx]

**With ODS support**

.. code-block:: sh

    pip install faker-file[ods]

**With ODT support**

.. code-block:: sh

    pip install faker-file[odt]

**With data augmentation support**

.. code-block:: sh

    pip install faker-file[data-augmentation]

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
- ``ODT``
- ``ODP``
- ``PDF``
- ``PNG``
- ``RTF``
- ``PPTX``
- ``SVG``
- ``TAR``
- ``TXT``
- ``WEBP``
- ``XLSX``
- ``ZIP``

Additional providers
--------------------
- ``AugmentFileFromDirProvider``: Make an augmented copy of randomly picked
  file from given directory. The following types are supported : ``DOCX``,
  ``EML``, ``EPUB``, ``ODT``,  ``PDF``, ``RTF`` and ``TXT``.
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

If you just need ``bytes`` back (instead of creating the file), provide
the ``raw=True`` argument (works with all provider classes and inner
functions):

.. code-block:: python

    raw = TxtFileProvider(FAKER).txt_file(raw=True)

**Or another**

.. code-block:: python

    from faker import Faker
    from faker_file.providers.txt_file import TxtFileProvider

    FAKER = Faker()
    FAKER.add_provider(TxtFileProvider)

    file = FAKER.txt_file()

If you just need ``bytes`` back:

.. code-block:: python

    raw = FAKER.txt_file(raw=True)

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
- ``PathyFileSystemStorage``: Requires `pathy`_.
- ``AzureCloudStorage``: Requires `pathy`_ and `Azure` related dependencies.
- ``GoogleCloudStorage``: Requires `pathy`_ and `Google Cloud` related
  dependencies.
- ``AWSS3Storage``: Requires `pathy`_ and `AWS S3` related dependencies.

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
Native file system storage. Requires ``pathy``.

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
AWS S3 storage. Requires ``pathy`` and ``boto3``.

.. code-block:: python

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
