from random import choice

from django.conf import settings
from factory import Faker, LazyAttribute
from factory.django import DjangoModelFactory
from upload.models import Upload

from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.pptx_file import PptxFileProvider
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.providers.zip_file import ZipFileProvider
from faker_file.storages.filesystem import FileSystemStorage

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
    "UploadFactory",
    "ZipUploadFactory",
)

FS_STORAGE = FileSystemStorage(root_path=settings.MEDIA_ROOT)


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

    file = Faker("txt_file", storage=FS_STORAGE)


class DocxUploadFactory(AbstractUploadFactory):
    """DOCX Upload factory."""

    file = Faker("docx_file", storage=FS_STORAGE)


class PptxUploadFactory(AbstractUploadFactory):
    """PPTX Upload factory."""

    file = Faker("pptx_file", storage=FS_STORAGE)


class PdfUploadFactory(AbstractUploadFactory):
    """PDF Upload factory."""

    file = Faker("pdf_file", storage=FS_STORAGE)


class ZipUploadFactory(AbstractUploadFactory):
    """ZIP Upload factory."""

    file = Faker("zip_file", storage=FS_STORAGE)


PROVIDER_CHOICES = [
    lambda: DocxFileProvider(None).docx_file(storage=FS_STORAGE),
    lambda: PdfFileProvider(None).pdf_file(storage=FS_STORAGE),
    lambda: PptxFileProvider(None).pptx_file(storage=FS_STORAGE),
    lambda: TxtFileProvider(None).txt_file(storage=FS_STORAGE),
    lambda: ZipFileProvider(None).zip_file(storage=FS_STORAGE),
]


def pick_random_provider(*args, **kwargs):
    return choice(PROVIDER_CHOICES)()


class UploadFactory(AbstractUploadFactory):
    """Upload factory that randomly picks a file provider."""

    file = LazyAttribute(pick_random_provider)
