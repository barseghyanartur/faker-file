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
    from faker_file.providers.augment_file_from_dir import AugmentFileFromDirProvider
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
    from faker_file.providers.random_file_from_dir import RandomFileFromDirProvider
    from faker_file.providers.rtf_file import RtfFileProvider
    from faker_file.providers.svg_file import SvgFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.webp_file import WebpFileProvider
    from faker_file.providers.xlsx_file import XlsxFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    FAKER = Faker()
    FAKER.add_provider(AugmentFileFromDirProvider)
    FAKER.add_provider(BinFileProvider)
    FAKER.add_provider(CsvFileProvider)
    FAKER.add_provider(DocxFileProvider)
    FAKER.add_provider(EmlFileProvider)
    FAKER.add_provider(EpubFileProvider)
    FAKER.add_provider(IcoFileProvider)
    FAKER.add_provider(JpegFileProvider)
    FAKER.add_provider(Mp3FileProvider)
    FAKER.add_provider(OdsFileProvider)
    FAKER.add_provider(OdtFileProvider)
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

    augmented_file = FAKER.augment_file_from_dir(source_dir_path="/path/to/source/",)
    bin_file = FAKER.bin_file()
    csv_file = FAKER.csv_file()
    docx_file = FAKER.docx_file()
    eml_file = FAKER.eml_file()
    epub_file = FAKER.epub_file()
    ico_file = FAKER.ico_file()
    jpeg_file = FAKER.jpeg_file()
    mp3_file = FAKER.mp3_file()
    ods_file = FAKER.ods_file()
    odt_file = FAKER.odt_file()
    pdf_file = FAKER.pdf_file()
    png_file = FAKER.png_file()
    pptx_file = FAKER.pptx_file()
    random_file = FAKER.random_file_from_dir(source_dir_path="/path/to/source/",)
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

    from faker_file.providers.augment_file_from_dir import AugmentFileFromDirProvider
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
    from faker_file.providers.random_file_from_dir import RandomFileFromDirProvider
    from faker_file.providers.rtf_file import RtfFileProvider
    from faker_file.providers.svg_file import SvgFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.webp_file import WebpFileProvider
    from faker_file.providers.xlsx_file import XlsxFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    Faker.add_provider(AugmentFileFromDirProvider)
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

        # File
        file = models.FileField(null=True)

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

    from factory import Faker

    # Import all needed providers
    from faker_file.providers.augment_file_from_dir import (
        AugmentFileFromDirProvider,
    )
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
    from faker_file.providers.random_file_from_dir import (
        RandomFileFromDirProvider,
    )
    from faker_file.providers.rtf_file import RtfFileProvider
    from faker_file.providers.svg_file import SvgFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.webp_file import WebpFileProvider
    from faker_file.providers.xlsx_file import XlsxFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    # Import file storage, because we need to customize things in
    # order for it to work with Django.
    from faker_file.storages.filesystem import FileSystemStorage

    from upload.models import Upload

    # Add all needed providers
    Faker.add_provider(AugmentFileFromDirProvider)
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
    Faker.add_provider(RandomFileFromDirProvider)
    Faker.add_provider(RtfFileProvider)
    Faker.add_provider(SvgFileProvider)
    Faker.add_provider(TxtFileProvider)
    Faker.add_provider(WebpFileProvider)
    Faker.add_provider(XlsxFileProvider)
    Faker.add_provider(ZipFileProvider)

    # Define a file storage.
    STORAGE = FileSystemStorage(
        root_path=settings.MEDIA_ROOT,
        rel_path="tmp"
    )

    # Define the upload factory
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

Usage example
^^^^^^^^^^^^^
.. code-block:: python

    UploadFactory(bin_file=True)  # Upload with BIN file
    UploadFactory(docx_file=True)  # Upload with DOCX file
    UploadFactory(jpeg_file=True)  # Upload with JPEG file
    UploadFactory(zip_file=True)  # Upload with ZIP file
