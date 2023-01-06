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

.. code-block:: python

    from faker import Faker
    from faker_file.providers.bin_file import BinFileProvider
    from faker_file.providers.csv_file import CsvFileProvider
    from faker_file.providers.docx_file import DocxFileProvider
    from faker_file.providers.eml_file import EmlFileProvider
    from faker_file.providers.epub_file import EpubFileProvider
    from faker_file.providers.ico_file import IcoFileProvider
    from faker_file.providers.jpeg_file import JpegFileProvider
    from faker_file.providers.mp3_file import Mp3FileProvider
    from faker_file.providers.ods_file import OdsFileProvider
    from faker_file.providers.pdf_file import PdfFileProvider
    from faker_file.providers.png_file import PngFileProvider
    from faker_file.providers.pptx_file import PptxFileProvider
    from faker_file.providers.random_file_from_dir import RandomFileFromDirProvider
    from faker_file.providers.rtf_file import RtfFileProvider
    from faker_file.providers.svg_file import SvgFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.webp_file import WebpFileProvider
    from faker_file.providers.xlsx_file import XlsxFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    FAKER = Faker()
    FAKER.add_provider(BinFileProvider)
    FAKER.add_provider(CsvFileProvider)
    FAKER.add_provider(DocxFileProvider)
    FAKER.add_provider(EmlFileProvider)
    FAKER.add_provider(EpubFileProvider)
    FAKER.add_provider(IcoFileProvider)
    FAKER.add_provider(JpegFileProvider)
    FAKER.add_provider(Mp3FileProvider)
    FAKER.add_provider(OdsFileProvider)
    FAKER.add_provider(PdfFileProvider)
    FAKER.add_provider(PngFileProvider)
    FAKER.add_provider(PptxFileProvider)
    FAKER.add_provider(RandomFileFromDirProvider)
    FAKER.add_provider(RtfFileProvider)
    FAKER.add_provider(SvgFileProvider)
    FAKER.add_provider(TxtFileProvider)
    FAKER.add_provider(WebpFileProvider)
    FAKER.add_provider(XlsxFileProvider)
    FAKER.add_provider(ZipFileProvider)

**Usage examples**

.. code-block:: python

    bin_file = FAKER.bin_file()
    csv_file = FAKER.csv_file()
    docx_file = FAKER.docx_file()
    eml_file = FAKER.eml_file()
    epub_file = FAKER.epub_file()
    ico_file = FAKER.ico_file()
    jpeg_file = FAKER.jpeg_file()
    mp3_file = FAKER.mp3_file()
    ods_file = FAKER.ods_file()
    pdf_file = FAKER.pdf_file()
    png_file = FAKER.png_file()
    pptx_file = FAKER.pptx_file()
    rtf_file = FAKER.rtf_file()
    svg_file = FAKER.svg_file()
    txt_file = FAKER.txt_file()
    webp_file = FAKER.webp_file()
    xlsx_file = FAKER.xlsx_file()
    zip_file = FAKER.zip_file()

With ``factory_boy``
~~~~~~~~~~~~~~~~~~~~
**Imports and initialization**

.. code-block:: python

    from factory import Faker
    from faker_file.providers.bin_file import BinFileProvider
    from faker_file.providers.csv_file import CsvFileProvider
    from faker_file.providers.docx_file import DocxFileProvider
    from faker_file.providers.eml_file import EmlFileProvider
    from faker_file.providers.epub_file import EpubFileProvider
    from faker_file.providers.ico_file import IcoFileProvider
    from faker_file.providers.jpeg_file import JpegFileProvider
    from faker_file.providers.mp3_file import Mp3FileProvider
    from faker_file.providers.ods_file import OdsFileProvider
    from faker_file.providers.pdf_file import PdfFileProvider
    from faker_file.providers.png_file import PngFileProvider
    from faker_file.providers.pptx_file import PptxFileProvider
    from faker_file.providers.random_file_from_dir import RandomFileFromDirProvider
    from faker_file.providers.rtf_file import RtfFileProvider
    from faker_file.providers.svg_file import SvgFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.webp_file import WebpFileProvider
    from faker_file.providers.xlsx_file import XlsxFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    Faker.add_provider(BinFileProvider)
    Faker.add_provider(CsvFileProvider)
    Faker.add_provider(DocxFileProvider)
    Faker.add_provider(EmlFileProvider)
    Faker.add_provider(EpubFileProvider)
    Faker.add_provider(IcoFileProvider)
    Faker.add_provider(JpegFileProvider)
    Faker.add_provider(Mp3FileProvider)
    Faker.add_provider(OdsFileProvider)
    Faker.add_provider(PdfFileProvider)
    Faker.add_provider(PngFileProvider)
    Faker.add_provider(PptxFileProvider)
    Faker.add_provider(RandomFileFromDirProvider)
    Faker.add_provider(RtfFileProvider)
    Faker.add_provider(SvgFileProvider)
    Faker.add_provider(TxtFileProvider)
    Faker.add_provider(WebpFileProvider)
    Faker.add_provider(XlsxFileProvider)
    Faker.add_provider(ZipFileProvider)

upload/models.py
^^^^^^^^^^^^^^^^
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

        class Meta:
            verbose_name = "Upload"
            verbose_name_plural = "Upload"

        def __str__(self):
            return self.name

upload/factories.py
^^^^^^^^^^^^^^^^^^^

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

        class Meta:
            model = Upload
