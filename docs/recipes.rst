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

    file = ZipFileProvider(FAKER).zip_file(
        options={"create_inner_file_args": {"content": "Lorem ipsum"}}
    )

Create a ZIP file consisting of 3 DOCX files with dynamically generated content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 3 DOCX files in the ZIP archive.
- Content is generated dynamically.
- Content is limited to 1024 chars.
- Prefix the filenames in archive with ``xxx_``.
- Prefix the filename of the archive itself with ``zzz``.
- Inside the ZIP, put all files in directory ``yyy``.

.. code-block:: python

    from faker_file.providers.helpers.inner import create_inner_docx_file
    file = ZipFileProvider(FAKER).zip_file(
        prefix="zzz",
        options={
            "count": 3,
            "create_inner_file_func": create_inner_docx_file,
            "create_inner_file_args": {
                "prefix": "xxx_",
                "max_nb_chars": 1_024,
            },
            "directory": "yyy",
        }
    )

Create a ZIP file of 9 DOCX files with content generated from template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 9 DOCX files in the ZIP archive.
- Content is generated dynamically from given template.

.. code-block:: python

    from faker_file.providers.helpers.inner import create_inner_docx_file

    TEMPLATE = "Hey {{name}},\n{{text}},\nBest regards\n{{name}}"

    file = ZipFileProvider(FAKER).zip_file(
        options={
            "count": 9,
            "create_inner_file_func": create_inner_docx_file,
            "create_inner_file_args": {
                "content": TEMPLATE,
            },
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

    from faker_file.providers.helpers.inner import (
        create_inner_docx_file,
        create_inner_zip_file,
    )

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

Create a ZIP file with variety of different file types within
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 50 files in the ZIP archive (limited to DOCX, EPUB and TXT types).
- Content is generated dynamically.
- Prefix the filename of the archive itself with ``zzz_archive_``.
- Inside the ZIP, put all files in directory ``zzz``.

.. code-block:: python

    from faker import Faker
    from faker_file.providers.helpers.inner import (
        create_inner_docx_file,
        create_inner_epub_file,
        create_inner_txt_file,
        fuzzy_choice_create_inner_file,
    )
    from faker_file.providers.zip_file import ZipFileProvider
    from faker_file.storages.filesystem import FileSystemStorage

    FAKER = Faker()
    STORAGE = FileSystemStorage()

    kwargs = {"storage": STORAGE, "generator": FAKER}
    file = ZipFileProvider(FAKER).zip_file(
        prefix="zzz_archive_",
        options={
            "count": 50,
            "create_inner_file_func": fuzzy_choice_create_inner_file,
            "create_inner_file_args": {
                "func_choices": [
                    (create_inner_docx_file, kwargs),
                    (create_inner_epub_file, kwargs),
                    (create_inner_txt_file, kwargs),
                ],
            },
            "directory": "zzz",
        }
    )

Create a EML file consisting of TXT files with static content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 5 TXT files in the EML email (default value is 5).
- Content of all files is ``Lorem ipsum``.

.. code-block:: python

    from faker import Faker
    from faker_file.providers.eml_file import EmlFileProvider

    FAKER = Faker()

    file = EmlFileProvider(FAKER).eml_file(
        options={"create_inner_file_args": {"content": "Lorem ipsum"}}
    )

Create a EML file consisting of 3 DOCX files with dynamically generated content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 3 DOCX files in the EML email.
- Content is generated dynamically.
- Content is limited to 1024 chars.
- Prefix the filenames in email with ``xxx_``.
- Prefix the filename of the email itself with ``zzz``.

.. code-block:: python

    from faker import Faker
    from faker_file.providers.eml_file import EmlFileProvider
    from faker_file.providers.helpers.inner import create_inner_docx_file

    FAKER = Faker()

    file = EmlFileProvider(FAKER).eml_file(
        prefix="zzz",
        options={
            "count": 3,
            "create_inner_file_func": create_inner_docx_file,
            "create_inner_file_args": {
                "prefix": "xxx_",
                "max_nb_chars": 1_024,
            },
        }
    )

Create a nested EML file
~~~~~~~~~~~~~~~~~~~~~~~~
Create a EML file which contains 5 EML files which contain 5 EML files which
contain 5 DOCX files.

- 5 EML files in the EML file.
- Content is generated dynamically.
- Prefix the filenames in EML email with ``nested_level_1_``.
- Prefix the filename of the EML email itself with ``nested_level_0_``.
- Each of the EML files inside the EML file in their turn contains 5 other EML
  files, prefixed with ``nested_level_2_``, which in their turn contain 5
  DOCX files.

.. code-block:: python

    from faker import Faker
    from faker_file.providers.eml_file import EmlFileProvider
    from faker_file.providers.helpers.inner import (
        create_inner_docx_file,
        create_inner_eml_file,
    )

    FAKER = Faker()

    file = EmlFileProvider(FAKER).eml_file(
        prefix="nested_level_0_",
        options={
            "create_inner_file_func": create_inner_eml_file,
            "create_inner_file_args": {
                "prefix": "nested_level_1_",
                "options": {
                    "create_inner_file_func": create_inner_eml_file,
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

Create an EML file with variety of different file types within
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 10 files in the EML file (limited to DOCX, EPUB and TXT types).
- Content is generated dynamically.
- Prefix the filename of the EML itself with ``zzz``.

.. code-block:: python

    from faker import Faker
    from faker_file.providers.helpers.inner import (
        create_inner_docx_file,
        create_inner_epub_file,
        create_inner_txt_file,
        fuzzy_choice_create_inner_file,
    )
    from faker_file.providers.eml_file import EmlFileProvider
    from faker_file.storages.filesystem import FileSystemStorage

    FAKER = Faker()
    STORAGE = FileSystemStorage()

    kwargs = {"storage": STORAGE, "generator": FAKER}

    file = EmlFileProvider(FAKER).eml_file(
        prefix="zzz",
        options={
            "count": 10,
            "create_inner_file_func": fuzzy_choice_create_inner_file,
            "create_inner_file_args": {
                "func_choices": [
                    (create_inner_docx_file, kwargs),
                    (create_inner_epub_file, kwargs),
                    (create_inner_txt_file, kwargs),
                ],
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

    TEMPLATE = """
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

    file = FAKER.pdf_file(content=TEMPLATE, wrap_chars_after=80)

Create a PDF using `reportlab` generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    from faker_file.providers.pdf_file.generators.reportlab_generator import (
        ReportlabPdfGenerator,
    )

    file = FAKER.pdf_file(pdf_generator_cls=ReportlabPdfGenerator)

Create a PDF using `pdfkit` generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Note, that at the moment, ``pdfkit`` is the default generator. However,
you could set it explicitly as follows:

.. code-block:: python

    from faker_file.providers.pdf_file.generators.pdfkit_generator import (
        PdfkitPdfGenerator,
    )

    file = FAKER.pdf_file(pdf_generator_cls=PdfkitPdfGenerator)

Create a MP3 file
~~~~~~~~~~~~~~~~~
.. code-block:: python

    file = FAKER.mp3_file()

Create a MP3 file by explicitly specifying MP3 generator class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Google Text-to-Speech
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    from faker import Faker
    from faker_file.providers.mp3_file import Mp3FileProvider
    from faker_file.providers.mp3_file.generators.gtts_generator import (
        GttsMp3Generator,
    )

    FAKER = Faker()

    file = Mp3FileProvider(FAKER).mp3_file(mp3_generator_cls=GttsMp3Generator)

You can tune arguments too:

.. code-block:: python

    from faker import Faker
    from faker_file.providers.mp3_file import Mp3FileProvider
    from faker_file.providers.mp3_file.generators.gtts_generator import (
        GttsMp3Generator,
    )

    FAKER = Faker()

    file = Mp3FileProvider(FAKER).mp3_file(
        mp3_generator_cls=GttsMp3Generator,
        mp3_generator_kwargs={
            "lang": "en",
            "tld": "co.uk",
        }
    )

Refer to https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang
for list of accepted values for ``lang`` argument.

Refer to https://gtts.readthedocs.io/en/latest/module.html#localized-accents
for list of accepted values for ``tld`` argument.

Microsoft Edge Text-to-Speech
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    from faker import Faker
    from faker_file.providers.mp3_file import Mp3FileProvider
    from faker_file.providers.mp3_file.generators.edge_tts_generator import (
        EdgeTtsMp3Generator,
    )

    FAKER = Faker()

    file = Mp3FileProvider(FAKER).mp3_file(mp3_generator_cls=EdgeTtsMp3Generator)

You can tune arguments too:

.. code-block:: python

    from faker import Faker
    from faker_file.providers.mp3_file import Mp3FileProvider
    from faker_file.providers.mp3_file.generators.edge_tts_generator import (
        EdgeTtsMp3Generator,
    )

    FAKER = Faker()

    file = Mp3FileProvider(FAKER).mp3_file(
        mp3_generator_cls=EdgeTtsMp3Generator,
        mp3_generator_kwargs={
            "voice": "en-GB-LibbyNeural",
        }
    )

Run ``edge-tts -l`` from terminal for list of available voices.

Create a MP3 file with custom MP3 generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Default MP3 generator class is ``GttsMp3Generator`` which uses Google
Text-to-Speech services to generate an MP3 file from given or
randomly generated text. It does not require additional services to
run and the only dependency here is the ``gtts`` package. You can
however implement your own custom MP3 generator class and pass it to
te ``mp3_file`` method in ``mp3_generator_cls`` argument instead of the
default ``GttsMp3Generator``. Read about quotas of Google Text-to-Speech
services `here <https://cloud.google.com/text-to-speech/quotas>`_.

Usage with custom MP3 generator class.

.. code-block:: python

    # Imaginary `marytts` Python library
    from marytts import MaryTTS

    # Import BaseMp3Generator
    from faker_file.providers.base.mp3_generator import (
        BaseMp3Generator,
    )

    # Define custom MP3 generator
    class MaryTtsMp3Generator(BaseMp3Generator):

        locale: str = "cmu-rms-hsmm"
        voice: str = "en_US"

        def handle_kwargs(self, **kwargs) -> None:
            # Since it's impossible to unify all TTS systems it's allowed
            # to pass arbitrary arguments to the `BaseMp3Generator`
            # constructor. Each implementation class contains its own
            # additional tuning arguments. Check the source code of the
            # implemented MP3 generators as an example.
            if "locale" in kwargs:
                self.locale = kwargs["locale"]
            if "voice" in kwargs:
                self.voice = kwargs["voice"]

        def generate(self) -> bytes:
            # Your implementation here. Note, that `self.content`
            # in this context is the text to make MP3 from.
            # `self.generator` would be the `Faker` or `Generator`
            # instance from which you could extract information on
            # active locale.
            # What comes below is pseudo implementation.
            mary_tts = MaryTTS(locale=self.locale, voice=self.voice)
            return mary_tts.synth_mp3(self.content)

    # Generate MP3 file from random text
    file = FAKER.mp3_file(
        mp3_generator_cls=MaryTtsMp3Generator,
    )

See exact implementation of
`marytts_mp3_generator <https://github.com/barseghyanartur/faker-file/tree/main/examples/customizations/marytts_mp3_generator>`_
in the examples.

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

Generate a lot of files using multiprocessing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generate 100 DOCX files
^^^^^^^^^^^^^^^^^^^^^^^
- Use template.
- Generate 100 DOCX files.

.. code-block:: python

    from multiprocessing import Pool
    from faker import Faker
    from faker_file.providers.helpers.inner import create_inner_docx_file
    from faker_file.storages.filesystem import FileSystemStorage

    FAKER = Faker()
    STORAGE = FileSystemStorage()

    # Document template
    TEMPLATE = "Hey {{name}},\n{{text}},\nBest regards\n{{name}}"

    with Pool(processes=8) as pool:
        for _ in range(100):  # Number of times we want to run our function
            pool.apply_async(
                create_inner_docx_file,
                # Apply async doesn't support kwargs. We have to pass all
                # arguments.
                [STORAGE, "mp", FAKER, None, None, TEMPLATE],
            )
        pool.close()
        pool.join()

Randomize the file format
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    from multiprocessing import Pool

    from faker import Faker
    from faker_file.providers.helpers.inner import (
        create_inner_docx_file,
        create_inner_epub_file,
        create_inner_pdf_file,
        create_inner_txt_file,
        fuzzy_choice_create_inner_file,
    )
    from faker_file.storages.filesystem import FileSystemStorage

    FAKER = Faker()
    STORAGE = FileSystemStorage()

    # Document template
    TEMPLATE = """
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

    kwargs = {"storage": STORAGE, "generator": FAKER, "content": TEMPLATE}

    with Pool(processes=8) as pool:
        for _ in range(100):  # Number of times we want to run our function
            pool.apply_async(
                fuzzy_choice_create_inner_file,
                [
                    [
                        (create_inner_docx_file, kwargs),
                        (create_inner_epub_file, kwargs),
                        (create_inner_pdf_file, kwargs),
                        (create_inner_txt_file, kwargs),
                    ]
                ],
            )
        pool.close()
        pool.join()

Generating files from existing documents using NLP augmentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
See the following example:

.. code-block:: python

    from faker import Faker
    from faker_file.providers.augment_file_from_dir import (
        AugmentFileFromDirProvider,
    )

    FAKER = Faker()

    file = AugmentFileFromDirProvider(FAKER).augment_file_from_dir(
        source_dir_path="/path/to/source/",
    )

Generated file will resemble text of the original document, but
will not be the same. This is useful when you don't want to
test on text generated by ``Faker``, but rather something that
makes more sense for your use case, still want to ensure
uniqueness of the documents.

The following file types are supported:

- ``DOCX``
- ``EML``
- ``EPUB``
- ``ODT``
- ``PDF``
- ``RTF``
- ``TXT``

By default, all supported files are eligible for random selection. You could
however narrow that list by providing ``extensions`` argument:

.. code-block:: python

    file = AugmentFileFromDirProvider(FAKER).augment_file_from_dir(
        source_dir_path="/path/to/source/",
        extensions={"docx", "pdf"},  # Pick only DOCX or PDF
    )

By default ``bert-base-multilingual-cased`` model is used, which is
pretrained on the top 104 languages with the largest Wikipedia using a
masked language modeling (MLM) objective. If you want to use a different
model, specify the proper identifier in the ``model_path`` argument.
Some well working options for ``model_path`` are:

- ``bert-base-multilingual-cased``
- ``bert-base-multilingual-uncased``
- ``bert-base-cased``
- ``bert-base-uncased``
- ``bert-base-german-cased``
- ``GroNLP/bert-base-dutch-cased``

.. code-block:: python

    from faker_file.providers.augment_file_from_dir.augmenters import (
        nlpaug_augmenter
    )

    file = AugmentFileFromDirProvider(FAKER).augment_file_from_dir(
        text_augmenter_cls=(
            nlpaug_augmenter.ContextualWordEmbeddingsAugmenter
        ),
        text_augmenter_kwargs={
            "model_path": "bert-base-cased",
            "action": "substitute",  # or "insert"
        }
    )

Refer to ``nlpaug``
`docs <https://nlpaug.readthedocs.io/en/latest/example/example.html>`__
and check `Textual augmenters` examples.

Using `raw=True` features in tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you pass ``raw=True`` argument to any provider or inner function,
instead of creating a file, you will get ``bytes`` back (or to be
totally correct, ``bytes``-like object ``BytesValue``, which is basically
bytes enriched with meta-data). You could then use the ``bytes`` content
of the file to build a test payload as shown in the example test below:

.. code-block:: python

    import os
    from io import BytesIO

    from django.test import TestCase
    from django.urls import reverse
    from faker import Faker
    from faker_file.providers.docx_file import DocxFileProvider
    from rest_framework.status import HTTP_201_CREATED
    from upload.models import Upload

    FAKER = Faker()
    FAKER.add_provider(DocxFileProvider)

    class UploadTestCase(TestCase):
        """Upload test case."""

        def test_create_docx_upload(self) -> None:
            """Test create an Upload."""
            url = reverse("api:upload-list")

            raw = FAKER.docx_file(raw=True)
            test_file = BytesIO(raw)
            test_file.name = os.path.basename(raw.data["filename"])

            payload = {
                "name": FAKER.word(),
                "description": FAKER.paragraph(),
                "file": test_file,
            }

            response = self.client.post(url, payload, format="json")

            # Test if request is handled properly (HTTP 201)
            self.assertEqual(response.status_code, HTTP_201_CREATED)

            test_upload = Upload.objects.get(id=response.data["id"])

            # Test if the name is properly recorded
            self.assertEqual(str(test_upload.name), payload["name"])

            # Test if file name recorded properly
            self.assertEqual(str(test_upload.file.name), test_file.name)

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

        # File
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
    from faker_file.providers.bin_file import BinFileProvider
    from faker_file.providers.csv_file import CsvFileProvider
    from faker_file.providers.docx_file import DocxFileProvider
    from faker_file.providers.eml_file import EmlFileProvider
    from faker_file.providers.epub_file import EpubFileProvider
    from faker_file.providers.ico_file import IcoFileProvider
    from faker_file.providers.jpeg_file import JpegFileProvider
    from faker_file.providers.mp3_file import Mp3FileProvider
    from faker_file.providers.ods_file import OdsFileProvider
    from faker_file.providers.odt_file import OdtFileProvider
    from faker_file.providers.pdf_file import PdfFileProvider
    from faker_file.providers.png_file import PngFileProvider
    from faker_file.providers.pptx_file import PptxFileProvider
    from faker_file.providers.rtf_file import RtfFileProvider
    from faker_file.providers.svg_file import SvgFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.webp_file import WebpFileProvider
    from faker_file.providers.xlsx_file import XlsxFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    # Import file storage, because we need to customize things in order for it
    # to work with Django.
    from faker_file.storages.filesystem import FileSystemStorage

    from upload.models import Upload

    # Add all providers we want to use
    Faker.add_provider(BinFileProvider)
    Faker.add_provider(CsvFileProvider)
    Faker.add_provider(DocxFileProvider)
    Faker.add_provider(EmlFileProvider)
    Faker.add_provider(EpubFileProvider)
    Faker.add_provider(IcoFileProvider)
    Faker.add_provider(JpegFileProvider)
    Faker.add_provider(Mp3FileProvider)
    Faker.add_provider(OdsFileProvider)
    Faker.add_provider(OdtFileProvider)
    Faker.add_provider(PdfFileProvider)
    Faker.add_provider(PngFileProvider)
    Faker.add_provider(PptxFileProvider)
    Faker.add_provider(RtfFileProvider)
    Faker.add_provider(SvgFileProvider)
    Faker.add_provider(TxtFileProvider)
    Faker.add_provider(WebpFileProvider)
    Faker.add_provider(XlsxFileProvider)
    Faker.add_provider(ZipFileProvider)

    # Define a file storage. When working with Django and FileSystemStorage
    # you need to set the value of `root_path` argument to
    # `settings.MEDIA_ROOT`.
    STORAGE = FileSystemStorage(
        root_path=settings.MEDIA_ROOT,
        rel_path="tmp"
    )

    class UploadFactory(DjangoModelFactory):
        """Upload factory."""

        name = Faker("text", max_nb_chars=100)
        description = Faker("text", max_nb_chars=1000)

        class Meta:
            model = Upload

        class Params:
            bin_file = Trait(file=Faker("bin_file", storage=STORAGE))
            csv_file = Trait(file=Faker("csv_file", storage=STORAGE))
            docx_file = Trait(file=Faker("docx_file", storage=STORAGE))
            eml_file = Trait(file=Faker("eml_file", storage=STORAGE))
            epub_file = Trait(file=Faker("epub_file", storage=STORAGE))
            ico_file = Trait(file=Faker("ico_file", storage=STORAGE))
            jpeg_file = Trait(file=Faker("jpeg_file", storage=STORAGE))
            mp3_file = Trait(file=Faker("mp3_file", storage=STORAGE))
            ods_file = Trait(file=Faker("ods_file", storage=STORAGE))
            odt_file = Trait(file=Faker("odt_file", storage=STORAGE))
            pdf_file = Trait(file=Faker("pdf_file", storage=STORAGE))
            png_file = Trait(file=Faker("png_file", storage=STORAGE))
            pptx_file = Trait(file=Faker("pptx_file", storage=STORAGE))
            rtf_file = Trait(file=Faker("rtf_file", storage=STORAGE))
            svg_file = Trait(file=Faker("svg_file", storage=STORAGE))
            txt_file = Trait(file=Faker("txt_file", storage=STORAGE))
            webp_file = Trait(file=Faker("webp_file", storage=STORAGE))
            xlsx_file = Trait(file=Faker("xlsx_file", storage=STORAGE))
            zip_file = Trait(file=Faker("zip_file", storage=STORAGE))

And then somewhere in your code:

.. code-block:: python

    UploadFactory(bin_file=True)  # Upload with BIN file
    UploadFactory(docx_file=True)  # Upload with DOCX file
    UploadFactory(jpeg_file=True)  # Upload with JPEG file
    UploadFactory(zip_file=True)  # Upload with ZIP file

Randomize provider choice
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from factory import LazyAttribute
    from faker import Faker
    from random import choice

    FAKER = Faker()

    PROVIDER_CHOICES = [
        lambda: BinFileProvider(FAKER).bin_file(storage=STORAGE),
        lambda: CsvFileProvider(FAKER).csv_file(storage=STORAGE),
        lambda: DocxFileProvider(FAKER).docx_file(storage=STORAGE),
        lambda: EmlFileProvider(FAKER).eml_file(storage=STORAGE),
        lambda: EpubFileProvider(FAKER).epub_file(storage=STORAGE),
        lambda: IcoFileProvider(FAKER).ico_file(storage=STORAGE),
        lambda: JpegFileProvider(FAKER).jpeg_file(storage=STORAGE),
        lambda: Mp3FileProvider(FAKER).mp3_file(storage=STORAGE),
        lambda: OdsFileProvider(FAKER).ods_file(storage=STORAGE),
        lambda: OdtFileProvider(FAKER).odt_file(storage=STORAGE),
        lambda: PdfFileProvider(FAKER).pdf_file(storage=STORAGE),
        lambda: PngFileProvider(FAKER).png_file(storage=STORAGE),
        lambda: PptxFileProvider(FAKER).pptx_file(storage=STORAGE),
        lambda: RtfFileProvider(FAKER).rtf_file(storage=STORAGE),
        lambda: SvgFileProvider(FAKER).svg_file(storage=STORAGE),
        lambda: TxtFileProvider(FAKER).txt_file(storage=STORAGE),
        lambda: XlsxFileProvider(FAKER).xlsx_file(storage=STORAGE),
        lambda: ZipFileProvider(FAKER).zip_file(storage=STORAGE),
    ]

    def pick_random_provider(*args, **kwargs):
        return choice(PROVIDER_CHOICES)()

    class UploadFactory(DjangoModelFactory):
        """Upload factory that randomly picks a file provider."""

        # ...
        class Params:
            # ...
            random_file = Trait(file=LazyAttribute(pick_random_provider))
            # ...

And then somewhere in your code:

.. code-block:: python

    UploadFactory(random_file=True)  # Upload with randon file

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

Other Django usage examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Faker example with AWS S3 storage**

.. code-block:: python

    from django.conf import settings
    from faker import Faker
    from faker_file.providers.pdf_file import PdfFileProvider
    from faker_file.storages.aws_s3 import AWSS3Storage

    FAKER = Faker()
    STORAGE = AWSS3Storage(
        bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
        root_path="",
        rel_path="",
    )
    FAKER.add_provider(PdfFileProvider)

    file = PdfFileProvider(FAKER).pdf_file(storage=STORAGE)

**factory-boy example with AWS S3 storage**

.. code-block:: python

    import factory

    from django.conf import settings
    from factory import Faker
    from factory.django import DjangoModelFactory
    from faker_file.storages.aws_s3 import AWSS3Storage

    from upload.models import Upload

    STORAGE = AWSS3Storage(
        bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
        root_path="",
        rel_path="",
    )

    Faker.add_provider(PdfFileProvider)

    class UploadFactory(DjangoModelFactory):
        name = Faker('word')
        description = Faker('text')
        file = Faker("pdf_file", storage=STORAGE)

        class Meta:
            model = Upload

    upload = UploadFactory()

**Flexible storage selection**

.. code-block:: python

    from django.conf import settings
    from django.core.files.storage import default_storage
    from faker_file.storages.aws_s3 import AWSS3Storage
    from faker_file.storages.filesystem import FileSystemStorage
    from storages.backends.s3boto3 import S3Boto3Storage

    # Faker doesn't know anything about Django. That's why, if we want to
    # support remote storages, we need to manually check which file storage
    # backend is used. If `Boto3` storage backend (of the `django-storages`
    # package) is used we use the correspondent `AWSS3Storage` class of the
    # `faker-file`.
    # Otherwise, fall back to native file system storage (`FileSystemStorage`)
    # of the `faker-file`.
    if isinstance(default_storage, S3Boto3Storage):
        STORAGE = AWSS3Storage(
            bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
            credentials={
                "key_id": settings.AWS_ACCESS_KEY_ID,
                "key_secret": settings.AWS_SECRET_ACCESS_KEY,
            },
            rel_path="tmp",
        )
    else:
        STORAGE = FileSystemStorage(
            root_path=settings.MEDIA_ROOT,
            rel_path="tmp",
        )
