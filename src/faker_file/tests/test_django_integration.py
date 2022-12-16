from typing import Callable

import factories
from django.conf import settings
from django.test import TestCase
from faker import Faker
from parametrize import parametrize

from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("DjangoIntegrationTestCase",)


class DjangoIntegrationTestCase(TestCase):
    """Django integration test case."""

    FAKER: Faker
    FS_STORAGE = FileSystemStorage(root_path=settings.MEDIA_ROOT)

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
        self.assertTrue(self.FS_STORAGE.exists(_upload.file.path))
