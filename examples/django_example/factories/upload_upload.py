from random import choice

from django.conf import settings
from django.core.files.storage import default_storage
from factory import Faker, LazyAttribute
from factory.django import DjangoModelFactory
from storages.backends.s3boto3 import S3Boto3Storage
from upload.models import Upload

from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.ods_file import OdsFileProvider
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.pptx_file import PptxFileProvider
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.providers.zip_file import ZipFileProvider
from faker_file.storages.aws_s3 import AWSS3Storage
from faker_file.storages.filesystem import FileSystemStorage

__all__ = (
    "DocxUploadFactory",
    "OdsUploadFactory",
    "PdfUploadFactory",
    "PptxUploadFactory",
    "TxtUploadFactory",
    "UploadFactory",
    "ZipUploadFactory",
)

# Faker._DEFAULT_LOCALE = "hy_AM"
Faker.add_provider(DocxFileProvider)
Faker.add_provider(OdsFileProvider)
Faker.add_provider(PdfFileProvider)
Faker.add_provider(PptxFileProvider)
Faker.add_provider(TxtFileProvider)
Faker.add_provider(ZipFileProvider)

# Faker doesn't know anything about Django. That's why, if we want to support
# remote storages, we need to manually check which file storage backend is
# used. If `Boto3` storage backend (of the `django-storages` package) is used
# we use the correspondent `AWSS3Storage` class of the `faker-file`.
# Otherwise, fall back to native file system storage (`FileSystemStorage`) of
# the `faker-file`.
if isinstance(default_storage, S3Boto3Storage):
    STORAGE = AWSS3Storage(
        bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
        credentials={
            "key_id": settings.AWS_ACCESS_KEY_ID,
            "key_secret": settings.AWS_SECRET_ACCESS_KEY,
        },
        rel_path="tmp",
        check_bucket=False,
    )
else:
    STORAGE = FileSystemStorage(root_path=settings.MEDIA_ROOT, rel_path="tmp")


class AbstractUploadFactory(DjangoModelFactory):
    """Base Upload factory."""

    name = Faker("text", max_nb_chars=100)
    description = Faker("text", max_nb_chars=1000)

    class Meta:
        """Meta class."""

        model = Upload
        abstract = True


class DocxUploadFactory(AbstractUploadFactory):
    """DOCX Upload factory."""

    file = Faker("docx_file", storage=STORAGE)


class OdsUploadFactory(AbstractUploadFactory):
    """ODS Upload factory."""

    file = Faker("ods_file", storage=STORAGE)


class PptxUploadFactory(AbstractUploadFactory):
    """PPTX Upload factory."""

    file = Faker("pptx_file", storage=STORAGE)


class PdfUploadFactory(AbstractUploadFactory):
    """PDF Upload factory."""

    file = Faker("pdf_file", storage=STORAGE)


class TxtUploadFactory(AbstractUploadFactory):
    """TXT Upload factory."""

    file = Faker("txt_file", storage=STORAGE)


class ZipUploadFactory(AbstractUploadFactory):
    """ZIP Upload factory."""

    file = Faker("zip_file", storage=STORAGE)


PROVIDER_CHOICES = [
    lambda: DocxFileProvider(None).docx_file(storage=STORAGE),
    lambda: PdfFileProvider(None).pdf_file(storage=STORAGE),
    lambda: PptxFileProvider(None).pptx_file(storage=STORAGE),
    lambda: TxtFileProvider(None).txt_file(storage=STORAGE),
    lambda: ZipFileProvider(None).zip_file(storage=STORAGE),
]


def pick_random_provider(*args, **kwargs):
    return choice(PROVIDER_CHOICES)()


class UploadFactory(AbstractUploadFactory):
    """Upload factory that randomly picks a file provider."""

    file = LazyAttribute(pick_random_provider)
