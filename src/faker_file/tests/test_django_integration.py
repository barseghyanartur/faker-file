import os
from typing import Callable

import factories
from django.test import TestCase
from faker import Faker
from parametrize import parametrize

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("DjangoIntegrationTestCase",)


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
        """Test DOCX file."""
        _upload = factory()
        self.assertTrue(os.path.exists(_upload.file.path))
