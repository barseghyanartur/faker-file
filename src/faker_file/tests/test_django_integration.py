from typing import Callable

import factories
from django.conf import settings
from django.core.files.storage import default_storage
from django.test import TestCase
from faker import Faker
from parametrize import parametrize
from storages.backends.s3boto3 import S3Boto3Storage

from ..storages.aws_s3 import AWSS3Storage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("DjangoIntegrationTestCase",)


# Faker doesn't know anything about Django. That's why, if we want to support
# remove storages, we need to manually check which file storage backend is
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
    )
else:
    STORAGE = FileSystemStorage(root_path=settings.MEDIA_ROOT, rel_path="tmp")


class DjangoIntegrationTestCase(TestCase):
    """Django integration test case."""

    FAKER: Faker

    @parametrize(
        "factory",
        [
            (factories.DocxUploadFactory,),
            (factories.PdfUploadFactory,),
            (factories.PptxUploadFactory,),
            (factories.TxtUploadFactory,),
            (factories.ZipUploadFactory,),
        ],
    )
    def test_file(self: "DjangoIntegrationTestCase", factory: Callable) -> None:
        """Test file."""
        _upload = factory()
        self.assertTrue(STORAGE.exists(_upload.file.name))
