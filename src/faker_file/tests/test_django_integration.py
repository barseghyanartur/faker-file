import os

import factories
from django.test import TestCase
from faker import Faker
from parametrize import parametrize

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
    def test_file(self, factory) -> None:
        """Test DOCX file."""
        _upload = factory()
        self.assertTrue(os.path.exists(_upload.file.path))
