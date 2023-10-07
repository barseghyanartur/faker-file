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
    :lines: 2-61

**Usage examples**

.. literalinclude:: _static/examples/quick_start/import_and_init_1.py
    :language: python
    :lines: 70-100

If you just need bytes back (instead of creating the file), provide
the ``raw=True`` argument (works with all provider classes and inner
functions):

.. literalinclude:: _static/examples/quick_start/import_and_init_1.py
    :language: python
    :lines: 103-

*See the full example*
:download:`here <_static/examples/recipes/import_and_init_1.py>`

With ``factory_boy``
~~~~~~~~~~~~~~~~~~~~
**Imports and initialization**

.. code-block:: python
    :name: test_usage_with_factory_boy_imports_and_init

    from factory import Faker

    from faker_file.providers.augment_file_from_dir import AugmentFileFromDirProvider
    from faker_file.providers.bin_file import BinFileProvider
    from faker_file.providers.bmp_file import BmpFileProvider
    from faker_file.providers.csv_file import CsvFileProvider
    from faker_file.providers.docx_file import DocxFileProvider
    from faker_file.providers.eml_file import EmlFileProvider
    from faker_file.providers.epub_file import EpubFileProvider
    from faker_file.providers.ico_file import GraphicIcoFileProvider, IcoFileProvider
    from faker_file.providers.jpeg_file import GraphicJpegFileProvider, JpegFileProvider
    from faker_file.providers.mp3_file import Mp3FileProvider
    from faker_file.providers.odp_file import OdpFileProvider
    from faker_file.providers.ods_file import OdsFileProvider
    from faker_file.providers.odt_file import OdtFileProvider
    from faker_file.providers.pdf_file import GraphicPdfFileProvider, PdfFileProvider
    from faker_file.providers.png_file import GraphicPngFileProvider, PngFileProvider
    from faker_file.providers.pptx_file import PptxFileProvider
    from faker_file.providers.random_file_from_dir import RandomFileFromDirProvider
    from faker_file.providers.rtf_file import RtfFileProvider
    from faker_file.providers.svg_file import SvgFileProvider
    from faker_file.providers.tar_file import TarFileProvider
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.providers.webp_file import GraphicWebpFileProvider, WebpFileProvider
    from faker_file.providers.xlsx_file import XlsxFileProvider
    from faker_file.providers.zip_file import ZipFileProvider

    Faker.add_provider(AugmentFileFromDirProvider)
    Faker.add_provider(BinFileProvider)
    Faker.add_provider(BmpFileProvider)
    Faker.add_provider(CsvFileProvider)
    Faker.add_provider(DocxFileProvider)
    Faker.add_provider(EmlFileProvider)
    Faker.add_provider(EpubFileProvider)
    Faker.add_provider(GraphicIcoFileProvider)
    Faker.add_provider(GraphicJpegFileProvider)
    Faker.add_provider(GraphicPdfFileProvider)
    Faker.add_provider(GraphicPngFileProvider)
    Faker.add_provider(GraphicWebpFileProvider)
    Faker.add_provider(IcoFileProvider)
    Faker.add_provider(JpegFileProvider)
    Faker.add_provider(Mp3FileProvider)
    Faker.add_provider(OdpFileProvider)
    Faker.add_provider(OdsFileProvider)
    Faker.add_provider(OdtFileProvider)
    Faker.add_provider(PdfFileProvider)
    Faker.add_provider(PngFileProvider)
    Faker.add_provider(PptxFileProvider)
    Faker.add_provider(RandomFileFromDirProvider)
    Faker.add_provider(RtfFileProvider)
    Faker.add_provider(SvgFileProvider)
    Faker.add_provider(TarFileProvider)
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
    from faker_file.providers.bmp_file import BmpFileProvider
    from faker_file.providers.csv_file import CsvFileProvider
    from faker_file.providers.docx_file import DocxFileProvider
    from faker_file.providers.eml_file import EmlFileProvider
    from faker_file.providers.epub_file import EpubFileProvider
    from faker_file.providers.ico_file import IcoFileProvider
    from faker_file.providers.jpeg_file import JpegFileProvider
    from faker_file.providers.mp3_file import Mp3FileProvider
    from faker_file.providers.odp_file import OdpFileProvider
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
    from faker_file.providers.tar_file import TarFileProvider
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
    Faker.add_provider(BmpFileProvider)
    Faker.add_provider(CsvFileProvider)
    Faker.add_provider(DocxFileProvider)
    Faker.add_provider(EmlFileProvider)
    Faker.add_provider(EpubFileProvider)
    Faker.add_provider(IcoFileProvider)
    Faker.add_provider(JpegFileProvider)
    Faker.add_provider(Mp3FileProvider)
    Faker.add_provider(OdpFileProvider)
    Faker.add_provider(OdsFileProvider)
    Faker.add_provider(OdtFileProvider)
    Faker.add_provider(PdfFileProvider)
    Faker.add_provider(PngFileProvider)
    Faker.add_provider(PptxFileProvider)
    Faker.add_provider(RandomFileFromDirProvider)
    Faker.add_provider(RtfFileProvider)
    Faker.add_provider(SvgFileProvider)
    Faker.add_provider(TarFileProvider)
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
            bmp_file = Trait(file=Faker("bmp_file", storage=STORAGE))
            csv_file = Trait(file=Faker("csv_file", storage=STORAGE))
            docx_file = Trait(file=Faker("docx_file", storage=STORAGE))
            eml_file = Trait(file=Faker("eml_file", storage=STORAGE))
            epub_file = Trait(file=Faker("epub_file", storage=STORAGE))
            ico_file = Trait(file=Faker("ico_file", storage=STORAGE))
            jpeg_file = Trait(file=Faker("jpeg_file", storage=STORAGE))
            mp3_file = Trait(file=Faker("mp3_file", storage=STORAGE))
            odp_file = Trait(file=Faker("odp_file", storage=STORAGE))
            ods_file = Trait(file=Faker("ods_file", storage=STORAGE))
            odt_file = Trait(file=Faker("odt_file", storage=STORAGE))
            pdf_file = Trait(file=Faker("pdf_file", storage=STORAGE))
            png_file = Trait(file=Faker("png_file", storage=STORAGE))
            pptx_file = Trait(file=Faker("pptx_file", storage=STORAGE))
            rtf_file = Trait(file=Faker("rtf_file", storage=STORAGE))
            svg_file = Trait(file=Faker("svg_file", storage=STORAGE))
            tar_file = Trait(file=Faker("tar_file", storage=STORAGE))
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
