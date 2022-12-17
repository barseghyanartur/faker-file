Recipes
=======
When using with ``Faker``
-------------------------
When using with ``Faker``, there are two ways of using the providers.

Imports and initializations
~~~~~~~~~~~~~~~~~~~~~~~~~~~
**One way**

.. code-block:: python

    from faker import Faker
    from faker_file.providers.bin_file import BinFileProvider
    from faker_file.providers.docx_file import DocxFileProvider
    from faker_file.providers.pdf_file import PdfFileProvider
    from faker_file.providers.pptx_file import PptxFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    FAKER = Faker()

    # Usage example
    file = TxtFileProvider(FAKER).txt_file(content="Lorem ipsum")

**Or another**

.. code-block:: python

    from faker import Faker
    from faker_file.providers.docx_file import DocxFileProvider
    from faker_file.providers.pdf_file import PdfFileProvider
    from faker_file.providers.pptx_file import PptxFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    FAKER = Faker()
    FAKER.add_provider(DocxFileProvider)
    FAKER.add_provider(PdfFileProvider)
    FAKER.add_provider(PptxFileProvider)
    FAKER.add_provider(TxtFileProvider)
    FAKER.add_provider(ZipFileProvider)

    # Usage example
    file = FAKER.txt_file(content="Lorem ipsum")

Throughout documentation we will be mixing these approaches.

Create a TXT file with static content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Content of the file is ``Lorem ipsum``.

.. code-block:: python

    file = TxtFileProvider(FAKER).txt_file(content="Lorem ipsum")

Create a DOCX file with dynamically generated content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Content is generated dynamically.
- Content is limited to 1024 chars.
- Wrap lines after 80 chars.
- Prefix the filename with ``zzz``.

.. code-block:: python

    file = DocxFileProvider(FAKER).docx_file(
        prefix="zzz",
        max_nb_chars=1_024,
        wrap_chars_after=80,
    )

Create a ZIP file consisting of TXT files with static content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 5 TXT files in the ZIP archive (default value is 5).
- Content of all files is ``Lorem ipsum``.

.. code-block:: python

    file = ZipFileProvider(FAKER).zip_file(options={"content": "Lorem ipsum"})

Create a ZIP file consisting of 3 DOCX files with dynamically generated content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 3 DOCX files in the ZIP archive.
- Content is generated dynamically.
- Content is limited to 1024 chars.
- Prefix the filenames in archive with ``xxx_``.
- Prefix the filename of the archive itself with ``zzz``.
- Inside the ZIP, put all files in directory ``yyy``.

.. code-block:: python

    from faker_file.providers.zip_file import create_inner_docx_file
    file = ZipFileProvider(FAKER).zip_file(
        prefix="zzz",
        options={
            "count": 3,
            "create_inner_file_func": create_inner_docx_file,
            "create_inner_file_args": {
                "prefix": "xxx_",
                "max_nb_chars": 1_024,
            }
            "directory": "yyy",
        }
    )

Create a nested ZIP file
~~~~~~~~~~~~~~~~~~~~~~~~
Create a ZIP file which contains 5 ZIP files which contain 5 ZIP files which
contain 5 DOCX files.

- 5 ZIP files in the ZIP archive.
- Content is generated dynamically.
- Prefix the filenames in archive with ``nested_level_1_``.
- Prefix the filename of the archive itself with ``nested_level_0_``.
- Each of the ZIP files inside the ZIP file in their turn contains 5 other ZIP
  files, prefixed with ``nested_level_2_``, which in their turn contain 5
  DOCX files.

.. code-block:: python

    from faker_file.providers.zip_file import create_inner_docx_file, create_inner_zip_file
    file = ZipFileProvider(FAKER).zip_file(
        prefix="nested_level_0_",
        options={
            "create_inner_file_func": create_inner_zip_file,
            "create_inner_file_args": {
                "prefix": "nested_level_1_",
                "options": {
                    "create_inner_file_func": create_inner_zip_file,
                    "create_inner_file_args": {
                        "prefix": "nested_level_2_",
                        "options": {
                            "create_inner_file_func": create_inner_docx_file,
                        }
                    },
                }
            },
        }
    )

Create a TXT file with static content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    file = FAKER.txt_file(content="Lorem ipsum dolor sit amet")

Create a DOCX file with dynamically generated content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Content is generated dynamically.
- Content is limited to 1024 chars.
- Wrap lines after 80 chars.
- Prefix the filename with ``zzz``.

.. code-block:: python

    file = FAKER.docx_file(
        prefix="zzz",
        max_nb_chars=1_024,
        wrap_chars_after=80,
    )

Create a PDF file with predefined template containing dynamic fixtures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Content template is predefined and contains dynamic fixtures.
- Wrap lines after 80 chars.

.. code-block:: python

    template = """
    {{date}} {{city}}, {{country}}

    Hello {{name}},

    {{text}} {{text}} {{text}}

    {{text}} {{text}} {{text}}

    {{text}} {{text}} {{text}}

    Address: {{address}}

    Best regards,

    {{name}}
    {{address}}
    {{phone_number}}
    """

    file = FAKER.pdf_file(content=template, wrap_chars_after=80)

Pick a random file from a directory given
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Create an exact copy of the randomly picked file under a different name.
- Prefix of the destination file would be ``zzz``.
- ``source_dir_path`` is the absolute path to the directory to pick files from.

.. code-block:: python

    from faker_file.providers.random_file_from_dir import (
        RandomFileFromDirProvider,
    )

    file = RandomFileFromDirProvider(FAKER).random_file_from_dir(
        source_dir_path="/tmp/tmp/",
        prefix="zzz",
    )


Generate a file of a certain size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The only two file types for which it is easy to foresee the file size are BIN
and TXT. Note, that size of BIN files is always exact, while for TXT it is
approximate.

BIN
^^^
.. code-block:: python

    file = BinFileProvider(FAKER).bin_file(length=1024**2)  # 1 Mb
    file = BinFileProvider(FAKER).bin_file(length=3*1024**2)  # 3 Mb
    file = BinFileProvider(FAKER).bin_file(length=10*1024**2)  # 10 Mb

    file = BinFileProvider(FAKER).bin_file(length=1024)  # 1 Kb
    file = BinFileProvider(FAKER).bin_file(length=3*1024)  # 3 Kb
    file = BinFileProvider(FAKER).bin_file(length=10*1024)  # 10 Kb

TXT
^^^
.. code-block:: python

    file = TxtFileProvider(FAKER).txt_file(max_nb_chars=1024**2)  # 1 Mb
    file = TxtFileProvider(FAKER).txt_file(max_nb_chars=3*1024**2)  # 3 Mb
    file = TxtFileProvider(FAKER).txt_file(max_nb_chars=10*1024**2)  # 10 Mb

    file = TxtFileProvider(FAKER).txt_file(max_nb_chars=1024)  # 1 Kb
    file = TxtFileProvider(FAKER).txt_file(max_nb_chars=3*1024)  # 3 Kb
    file = TxtFileProvider(FAKER).txt_file(max_nb_chars=10*1024)  # 10 Kb

When using with ``Django`` (and ``factory_boy``)
------------------------------------------------
When used with Django (to generate fake data with ``factory_boy`` factories),
the ``root_path`` argument of the correspondent file storage shall be provided.
Otherwise (although no errors will be triggered) the generated files will
reside outside the ``MEDIA_ROOT`` directory (by default in ``/tmp/`` on
Linux) and further operations with those files through Django will cause
``SuspiciousOperation`` exception.

Basic example
~~~~~~~~~~~~~

Imaginary ``Django`` model
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from django.db import models

    class Upload(models.Model):
        """Upload model."""

        name = models.CharField(max_length=255, unique=True)
        description = models.TextField(null=True, blank=True)

        # Files
        docx_file = models.FileField(null=True)
        pdf_file = models.FileField(null=True)
        pptx_file = models.FileField(null=True)
        txt_file = models.FileField(null=True)
        zip_file = models.FileField(null=True)
        file = models.FileField(null=True)

        class Meta:
            verbose_name = "Upload"
            verbose_name_plural = "Upload"

        def __str__(self):
            return self.name

Correspondent ``factory_boy`` factory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from django.conf import settings

    from factory import Faker
    from factory.django import DjangoModelFactory

    # Import all providers we want to use
    from faker_file.providers.docx_file import DocxFileProvider
    from faker_file.providers.pdf_file import PdfFileProvider
    from faker_file.providers.pptx_file import PptxFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    # Import file storage, because we need to customize things in order for it
    # to work with Django.
    from faker_file.storages.filesystem import FileSystemStorage

    from upload.models import Upload

    # Add all providers we want to use
    Faker.add_provider(DocxFileProvider)
    Faker.add_provider(PdfFileProvider)
    Faker.add_provider(PptxFileProvider)
    Faker.add_provider(TxtFileProvider)
    Faker.add_provider(ZipFileProvider)

    # Define a file storage.
    FS_STORAGE = FileSystemStorage(
        root_path=settings.MEDIA_ROOT,
        rel_path="tmp"
    )

    class UploadFactory(DjangoModelFactory):
        """Upload factory."""

        name = Faker("text", max_nb_chars=100)
        description = Faker("text", max_nb_chars=1000)

        # Files
        docx_file = Faker("docx_file", storage=FS_STORAGE)
        pdf_file = Faker("pdf_file", storage=FS_STORAGE)
        pptx_file = Faker("pptx_file", storage=FS_STORAGE)
        txt_file = Faker("txt_file", storage=FS_STORAGE)
        zip_file = Faker("zip_file", storage=FS_STORAGE)
        file = Faker("txt_file", storage=FS_STORAGE)

        class Meta:
            model = Upload

Randomize provider choice
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from random import choice

    from factory import LazyAttribute
    from faker import Faker as FakerFaker

    FAKER = FakerFaker()

    PROVIDER_CHOICES = [
        lambda: DocxFileProvider(FAKER).docx_file(storage=FS_STORAGE),
        lambda: PdfFileProvider(FAKER).pdf_file(storage=FS_STORAGE),
        lambda: PptxFileProvider(FAKER).pptx_file(storage=FS_STORAGE),
        lambda: TxtFileProvider(FAKER).txt_file(storage=FS_STORAGE),
        lambda: ZipFileProvider(FAKER).zip_file(storage=FS_STORAGE),
    ]

    def pick_random_provider(*args, **kwargs):
        return choice(PROVIDER_CHOICES)()

    class UploadFactory(DjangoModelFactory):
        """Upload factory that randomly picks a file provider."""

        # ...
        file = LazyAttribute(pick_random_provider)
        # ...

Use a different locale
~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    from factory import Faker
    from factory.django import DjangoModelFactory
    from faker_file.providers.ods_file import OdsFileProvider

    Faker._DEFAULT_LOCALE = "hy_AM"  # Set locale to Armenian

    Faker.add_provider(OdsFileProvider)

    class UploadFactory(DjangoModelFactory):
        """Base Upload factory."""

        name = Faker("text", max_nb_chars=100)
        description = Faker("text", max_nb_chars=1000)
        file = Faker("ods_file")

        class Meta:
            """Meta class."""

            model = Upload
