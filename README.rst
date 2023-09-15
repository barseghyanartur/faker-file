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

.. _faker-file: https://github.com/barseghyanartur/faker-file/
.. _Read the Docs: http://faker-file.readthedocs.io/
.. _Quick start: https://faker-file.readthedocs.io/en/latest/quick_start.html
.. _Recipes: https://faker-file.readthedocs.io/en/latest/recipes.html
.. _Creating PDF: https://faker-file.readthedocs.io/en/latest/creating_pdf.html
.. _Creating DOCX: https://faker-file.readthedocs.io/en/latest/creating_docx.html
.. _Creating ODT: https://faker-file.readthedocs.io/en/latest/creating_odt.html
.. _Creating images: https://faker-file.readthedocs.io/en/latest/creating_images.html
.. _CLI: https://faker-file.readthedocs.io/en/latest/cli.html
.. _Methodology: https://faker-file.readthedocs.io/en/latest/methodology.html
.. _Contributor guidelines: https://faker-file.readthedocs.io/en/latest/contributor_guidelines.html

.. Related projects

.. _faker-file-api: https://github.com/barseghyanartur/faker-file-api
.. _faker-file-ui: https://github.com/barseghyanartur/faker-file-ui
.. _faker-file-wasm: https://github.com/barseghyanartur/faker-file-wasm
.. _faker-file-qt: https://github.com/barseghyanartur/faker-file-qt

.. Demos

.. _REST API demo: https://faker-file-api.onrender.com/docs/
.. _UI frontend demo: https://faker-file-ui.vercel.app/
.. _WASM frontend demo: https://faker-file-wasm.vercel.app/

.. External references

.. _Apache Tika: https://tika.apache.org/
.. _Django: https://www.djangoproject.com/
.. _Faker: https://faker.readthedocs.io/
.. _Jinja2: https://jinja.palletsprojects.com/
.. _Pillow: https://pypi.org/project/Pillow/
.. _PyQT5: https://pypi.org/project/PyQt5/
.. _PyTorch: https://pytorch.org/
.. _WeasyPrint: https://pypi.org/project/weasyprint/
.. _azure-storage-blob: https://pypi.org/project/azure-storage-blob/
.. _boto3: https://pypi.org/project/boto3/
.. _edge-tts: https://pypi.org/project/edge-tts/
.. _factory_boy: https://factoryboy.readthedocs.io/
.. _gTTS: https://gtts.readthedocs.io/
.. _google-cloud-storage: https://pypi.org/project/google-cloud-storage/
.. _imgkit: https://pypi.org/project/imgkit/
.. _nlpaug: https://nlpaug.readthedocs.io/
.. _numpy: https://numpy.org/
.. _odfpy: https://pypi.org/project/odfpy/
.. _openpyxl: https://openpyxl.readthedocs.io/
.. _pandas: https://pandas.pydata.org/
.. _pdf2image: https://pypi.org/project/pdf2image/
.. _paramiko: http://paramiko.org/
.. _pathy: https://pypi.org/project/pathy/
.. _pdfkit: https://pypi.org/project/pdfkit/
.. _poppler: https://poppler.freedesktop.org/
.. _python-docx: https://python-docx.readthedocs.io/
.. _python-pptx: https://python-pptx.readthedocs.io/
.. _reportlab: https://pypi.org/project/reportlab/
.. _tablib: https://tablib.readthedocs.io/
.. _tika: https://pypi.org/project/tika/
.. _transformers: https://pypi.org/project/transformers/
.. _wkhtmltopdf: https://wkhtmltopdf.org/
.. _xml2epub: https://pypi.org/project/xml2epub/

.. Licenses

.. _GPL 2.0: https://opensource.org/license/gpl-2-0/
.. _BSD 3 clause: https://opensource.org/license/bsd-3-clause/

Prerequisites
=============
All of core dependencies of this package are `MIT` licensed.
Most of optional dependencies of this package are `MIT` licensed, while
a few are `BSD`-, `Apache 2`-, `GPL` or `HPND` licensed.

All licenses are mentioned below between the brackets.

- Core package requires Python 3.7, 3.8, 3.9, 3.10 or 3.11.
- `Faker`_ (`MIT`) is the only required dependency.
- `Django`_ (`BSD`) integration with `factory_boy`_ (`MIT`) has
  been tested with ``Django`` starting from version 2.2 to 4.2 (although only
  maintained versions of Django are currently being tested against).
- ``BMP``, ``GIF`` and ``TIFF`` file support requires either just
  `Pillow`_ (`HPND`), or a combination of `WeasyPrint`_ (`BSD`),
  `pdf2image`_ (`MIT`), `Pillow`_ (`HPND`) and `poppler`_ (`GPLv2`).
- ``DOCX`` file support requires `python-docx`_ (`MIT`).
- ``EPUB`` file support requires `xml2epub`_ (`MIT`) and `Jinja2`_ (`BSD`).
- ``ICO``, ``JPEG``, ``PNG``, ``SVG`` and ``WEBP`` files support
  requires either just `Pillow`_ (`HPND`), or a combination of
  `imgkit`_ (`MIT`) and `wkhtmltopdf`_ (`LGPLv3`).
- ``MP3`` file support requires `gTTS`_ (`MIT`) or `edge-tts`_ (`GPLv3`).
- ``PDF`` file support requires either combination of `pdfkit`_ (`MIT`)
  and `wkhtmltopdf`_ (`LGPLv3`), or `reportlab`_ (`BSD`).
- ``PPTX`` file support requires `python-pptx`_ (`MIT`).
- ``ODP`` and ``ODT`` file support requires `odfpy`_ (`Apache 2`).
- ``ODS`` file support requires `tablib`_ (`MIT`) and `odfpy`_ (`Apache 2`).
- ``XLSX`` file support requires `tablib`_ (`MIT`) and `openpyxl`_ (`MIT`).
- ``PathyFileSystemStorage`` storage support requires `pathy`_ (`Apache 2`).
- ``AWSS3Storage`` storage support requires `pathy`_ (`Apache 2`)
  and `boto3`_ (`Apache 2`).
- ``AzureCloudStorage`` storage support requires `pathy`_ (`Apache 2`)
  and `azure-storage-blob`_ (`MIT`).
- ``GoogleCloudStorage`` storage support requires `pathy`_ (`Apache 2`)
  and `google-cloud-storage`_ (`Apache 2`).
- ``SFTPStorage`` storage support requires `paramiko`_ (`LGLPv2.1`).
- ``AugmentFileFromDirProvider`` provider requires `nlpaug`_ (`MIT`),
  `PyTorch`_ (`BSD`), `transformers`_ (`Apache 2`), `numpy`_ (`BSD`),
  `pandas`_ (`BSD`), `tika`_ (`Apache 2`) and `Apache Tika`_ (`Apache 2`).

Documentation
=============
- Documentation is available on `Read the Docs`_.
- For bootstrapping check the `Quick start`_.
- For various ready to use code examples see the `Recipes`_.
- For tips on ``PDF`` creation see `Creating PDF`_.
- For tips on ``DOCX`` creation see `Creating DOCX`_.
- For tips on ``ODT`` creation see `Creating ODT`_.
- For tips on images creation see `Creating images`_.
- For CLI options see the `CLI`_.
- Read the `Methodology`_.
- For guidelines on contributing check the `Contributor guidelines`_.

Online demos and related projects
=================================
Check the demo(s) and related projects below:

- `REST API demo`_ (based on `faker-file-api`_ REST API)
- `UI frontend demo`_ (based on `faker-file-ui`_ UI frontend)
- `WASM frontend demo`_ (based on `faker-file-wasm`_ WASM frontend)
- `faker-file-qt`_ GUI application (based on `PyQT5`_).

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

**With GoogleCloudStorage support**

.. code-block:: sh

    pip install faker-file[gcs]

**With AzureCloudStorage support**

.. code-block:: sh

    pip install faker-file[azure]

**With AWSS3Storage support**

.. code-block:: sh

    pip install faker-file[s3]

Or development version from GitHub
----------------------------------

.. code-block:: sh

    pip install https://github.com/barseghyanartur/faker-file/archive/main.tar.gz

Features
========

Supported file types
--------------------
- ``BIN``
- ``BMP``
- ``CSV``
- ``DOCX``
- ``EML``
- ``EPUB``
- ``ICO``
- ``GIF``
- ``JPEG``
- ``JSON``
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
- ``TIFF``
- ``TXT``
- ``WEBP``
- ``XLSX``
- ``XML``
- ``ZIP``

For all image formats (``BMP``, ``ICO``, ``GIF``, ``JPEG``, ``PNG``, ``SVG``,
``TIFF`` and ``WEBP``) and ``PDF``, there are both graphic-only and
mixed-content file providers (that also have text-to-image capabilities).

Additional providers
--------------------
- ``AugmentFileFromDirProvider``: Make an augmented copy of randomly picked
  file from given directory. The following types are supported : ``DOCX``,
  ``EML``, ``EPUB``, ``ODT``,  ``PDF``, ``RTF`` and ``TXT``.
- ``AugmentRandomImageFromDirProvider``: Augment a random image file from
  given directory. The following types are supported : ``BMP``, ``GIF``,
  ``JPEG``, ``PNG``,  ``TIFF`` and ``WEBP``.
- ``AugmentImageFromPathProvider``: Augment an image file from given path.
  Supported file types are the same as for
  ``AugmentRandomImageFromDirProvider`` provider.
- ``GenericFileProvider``: Create files in any format from raw bytes or a
  predefined template.
- ``RandomFileFromDirProvider``: Pick a random file from given directory.
- ``FileFromPathProvider``: File from given path.

Supported file storages
-----------------------
- Native file system storage
- AWS S3 storage
- Azure Cloud Storage
- Google Cloud Storage
- SFTP storage

Usage examples
==============
With ``Faker``
--------------
**Recommended way**

.. code-block:: python
    :name: test_usage_examples_with_faker_recommended_way

    from faker import Faker
    # Import the file provider we want to use
    from faker_file.providers.txt_file import TxtFileProvider

    FAKER = Faker()  # Initialise Faker instance
    FAKER.add_provider(TxtFileProvider)  # Register the TXT file provider

    file = FAKER.txt_file()  # Generate a TXT file

    # Meta-data is stored inside a ``data`` attribute (``dict``).
    # The following line would produce something like /tmp/tmp/tmphzzb8mot.txt
    print(file.data["filename"])
    # The following line would produce a text generated by Faker, used as
    # the content of the generated file.
    print(file.data["content"])

.. note::

    Note, that in this case ``file`` value is a ``StringValue`` instance,
    which inherits from ``str`` but contains meta-data such as absolute
    path to the generated file, and text used to generate the file, stored
    in ``filename`` and ``content`` keys of the ``data`` attribute
    respectively. See `Meta-data`_ for more information.

If you just need ``bytes`` back (instead of creating the file), provide
the ``raw=True`` argument (works with all provider classes and inner
functions):

.. code-block:: python

    raw = FAKER.txt_file(raw=True)

.. note::

    Note, that in this case ``file`` value is a ``BytesValue`` instance,
    which inherits from ``bytes`` but contains meta-data such as absolute
    path to the generated file, and text used to generate the file, stored
    in ``filename`` and ``content`` keys of the ``data`` attribute
    respectively. See `Meta-data`_ for more information.

**But this works too**

.. code-block:: python
    :name: test_rst_readme_usage_examples_with_faker_but_this_works_too

    from faker import Faker
    from faker_file.providers.txt_file import TxtFileProvider

    FAKER = Faker()

    file = TxtFileProvider(FAKER).txt_file()

If you just need ``bytes`` back:

.. code-block:: python

    raw = TxtFileProvider(FAKER).txt_file(raw=True)

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

Meta-data
=========
The return value of any file provider file generator function is either
``StringValue`` or ``BytesValue``, which inherit from ``str`` and ``bytes``
respectively.

Both ``StringValue`` and ``BytesValue`` instances have a meta data attribute
named ``data`` (type ``dict``). Various file providers use ``data`` to
store meta-data, such as ``filename`` (absolute path to the generated file;
valid for all file providers), or ``content`` (text used when generating the
file; valid for most file providers, except ``FileFromPathProvider``,
``RandomFileFromDirProvider``, ``TarFileProvider`` and ``ZipFileProvider``).

All file providers store an absolute path to the generated file in ``filename``
key of the ``data`` attribute and instance of the storage used in ``storage``
key. See the table below.

+-----------+-----------------------------------------------------------------+
| Key name  | File provider                                                   |
+===========+=================================================================+
| filename  | all                                                             |
+-----------+-----------------------------------------------------------------+
| storage   | all                                                             |
+-----------+-----------------------------------------------------------------+
| content   | all except FileFromPathProvider, RandomFileFromDirProvider,     |
|           | TarFileProvider, ZipFileProvider and all graphic file providers |
|           | such as GraphicBmpFileProvider, GraphicGifFileProvider,         |
|           | GraphicIcoFileProvider, GraphicJpegFileProvider,                |
|           | GraphicPdfFileProvider, GraphicPngFileProvider,                 |
|           | GraphicTiffFileProvider and GraphicWebpFileProvider             |
+-----------+-----------------------------------------------------------------+
| inner     | only EmlFileProvider, TarFileProvider and ZipFileProvider       |
+-----------+-----------------------------------------------------------------+

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
- ``SFTPStorage``: Requires `paramiko`_ and related dependencies.

Usage example with storages
---------------------------
`FileSystemStorage` example
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Native file system storage. Does not have dependencies.

- ``root_path``: Path to the root directory. Given the example of Django,
  this would be the path to the ``MEDIA_ROOT`` directory. It's important
  to know, that ``root_path`` will not be embedded into the string
  representation of the file. Only ``rel_path`` will.
- ``rel_path``: Relative path from the root directory. Given the example of
  Django, this would be the rest of the path to the file.

.. code-block:: python
    :name: test_usage_examples_example_with_storages_filesystemstorage

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
    :name: test_usage_examples_example_with_storages_pathyfilesystemstorage

    import tempfile
    from pathy import use_fs
    from faker import Faker
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.storages.cloud import PathyFileSystemStorage

    use_fs(tempfile.gettempdir())
    PATHY_FS_STORAGE = PathyFileSystemStorage(
        bucket_name="bucket_name",
        root_path="tmp",
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

Citation
========
Please, use the following entry when citing `faker-file`_ in your research:

.. code-block:: latex

    @software{faker-file,
      author = {Artur Barseghyan},
      title = {faker-file: Create files with fake data. In many formats. With no efforts.},
      year = {2023},
      publisher = {GitHub},
      journal = {GitHub repository},
      howpublished = {https://github.com/barseghyanartur/faker-file},
    }
