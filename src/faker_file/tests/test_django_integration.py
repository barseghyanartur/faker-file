import os

from django.test import TestCase
from faker import Faker
from parametrize import parametrize

import factories

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
    def test_file(self: "DjangoIntegrationTestCase", factory: callable) -> None:
        """Test DOCX file."""
        _upload = factory()
        self.assertTrue(os.path.exists(_upload.file.path))
