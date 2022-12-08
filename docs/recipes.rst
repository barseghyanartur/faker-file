Recipes
=======
When using standalone
---------------------
Prerequisites
~~~~~~~~~~~~~
**Imports and initializations**

.. code-block:: python

    import Faker
    from faker_file.providers.docx_file import DocxFileProvider
    from faker_file.providers.pdf_file import PdfFileProvider
    from faker_file.providers.pptx_file import PptxFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    FAKER = Faker()

Create a TXT file with static content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Content of the file is ``Lorem ipsum``.

.. code-block:: python

    file = TxtFileProvider(FAKER).txt_file(content="Lorem ipsum")

Create a DOCX file with dynamically generated content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- 5 TXT files in the ZIP archive (default value is 5).
- Content of all files is ``Lorem ipsum``.

.. code-block:: python

    file = ZipFileProvider(FAKER).zip_file(options={"content": "Lorem ipsum"})

Create a ZIP file consisting of 3 DOCX files with dynamically generated content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
            "max_nb_chars": 1_024,
            "prefix": "xxx_",
            "directory": "yyy",
        }
    )

When using with ``Faker``
-------------------------
**Imports and initializations**

.. code-block:: python

    import Faker
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

Create a TXT file with static content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    file = FAKER("txt_file", content="Lorem ipsum dolor sit amet")

Create a DOCX file with dynamically generated content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Content is generated dynamically.
- Content is limited to 1024 chars.
- Wrap lines after 80 chars.
- Prefix the filename with ``zzz``.

.. code-block:: python

    file = FAKER(
        "docx_file",
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
    file = FAKER("pdf_file", content=template, wrap_chars_after=80)

When using with ``Django``
--------------------------
When used with Django (to generate fake data with ``factory_boy`` factories),
the ``root_path`` argument shall be provided. Otherwise (although no errors
will be triggered) the generated files will reside outside the ``MEDIA_ROOT``
directory (by default in ``/tmp/tmp/`` on Linux) and further operations with
those files through Django will cause ``SuspiciousOperation`` exception.

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

    from upload.models import Upload

    # Add all providers we want to use
    Faker.add_provider(DocxFileProvider)
    Faker.add_provider(PdfFileProvider)
    Faker.add_provider(PptxFileProvider)
    Faker.add_provider(TxtFileProvider)
    Faker.add_provider(ZipFileProvider)

    class UploadFactory(DjangoModelFactory):
        """Upload factory."""

        name = Faker("text", max_nb_chars=100)
        description = Faker("text", max_nb_chars=1000)

        # Files
        docx_file = Faker("docx_file", root_path=settings.MEDIA_ROOT)
        pdf_file = Faker("pdf_file", root_path=settings.MEDIA_ROOT)
        pptx_file = Faker("pptx_file", root_path=settings.MEDIA_ROOT)
        txt_file = Faker("txt_file", root_path=settings.MEDIA_ROOT)
        zip_file = Faker("zip_file", root_path=settings.MEDIA_ROOT)
        file = Faker("txt_file", root_path=settings.MEDIA_ROOT)

        class Meta:
            model = Upload

Randomise provider choice
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from random import choice

    from factory import LazyAttribute

    PROVIDER_CHOICES = [
        lambda: DocxFileProvider(None).docx_file(root_path=settings.MEDIA_ROOT),
        lambda: PdfFileProvider(None).pdf_file(root_path=settings.MEDIA_ROOT),
        lambda: PptxFileProvider(None).pptx_file(root_path=settings.MEDIA_ROOT),
        lambda: TxtFileProvider(None).txt_file(root_path=settings.MEDIA_ROOT),
        lambda: ZipFileProvider(None).zip_file(root_path=settings.MEDIA_ROOT),
    ]

    def pick_random_provider(*args, **kwargs):
        return choice(PROVIDER_CHOICES)()

    class UploadFactory(DjangoModelFactory):
        """Upload factory that randomly picks a file provider."""

        # ...
        file = LazyAttribute(pick_random_provider)
        # ...
