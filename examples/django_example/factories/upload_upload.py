from django.conf import settings
from factory import Faker
from factory.django import DjangoModelFactory
from upload.models import Upload

from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.pptx_file import PptxFileProvider
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.providers.zip_file import ZipFileProvider

Faker.add_provider(DocxFileProvider)
Faker.add_provider(PdfFileProvider)
Faker.add_provider(PptxFileProvider)
Faker.add_provider(TxtFileProvider)
Faker.add_provider(ZipFileProvider)

__all__ = (
    "DocxUploadFactory",
    "PdfUploadFactory",
    "PptxUploadFactory",
    "TxtUploadFactory",
    "ZipUploadFactory",
)


class AbstractUploadFactory(DjangoModelFactory):
    """Base Upload factory."""

    name = Faker("text", max_nb_chars=100)
    description = Faker("text", max_nb_chars=1000)

    class Meta:
        """Meta class."""

        model = Upload
        abstract = True


class TxtUploadFactory(AbstractUploadFactory):
    """TXT Upload factory."""

    file = Faker("txt_file", root_path=settings.MEDIA_ROOT)


class DocxUploadFactory(AbstractUploadFactory):
    """DOCX Upload factory."""

    file = Faker("docx_file", root_path=settings.MEDIA_ROOT)


class PptxUploadFactory(AbstractUploadFactory):
    """PPTX Upload factory."""

    file = Faker("pptx_file", root_path=settings.MEDIA_ROOT)


class PdfUploadFactory(AbstractUploadFactory):
    """PDF Upload factory."""

    file = Faker("pdf_file", root_path=settings.MEDIA_ROOT)


class ZipUploadFactory(AbstractUploadFactory):
    """ZIP Upload factory."""

    file = Faker("zip_file", root_path=settings.MEDIA_ROOT)
