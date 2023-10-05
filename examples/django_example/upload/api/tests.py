from io import BytesIO
from uuid import uuid4

from django.test import TestCase
from django.urls import reverse
from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.registry import FILE_REGISTRY
from rest_framework.status import HTTP_201_CREATED

from upload.models import Upload

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)

__all__ = ("UploadTestCase",)


class UploadTestCase(TestCase):
    """Upload test case."""

    def tearDown(self, *args, **kwargs) -> None:
        super().tearDown(*args, **kwargs)
        FILE_REGISTRY.clean_up()

    def test_create_docx_upload(self) -> None:
        """Test create an Upload."""
        url = reverse("api:upload-list")

        raw = FAKER.docx_file(raw=True)
        test_file = BytesIO(raw)
        test_file.name = f"test{uuid4()}.docx"

        payload = {
            "name": FAKER.word(),
            "description": FAKER.paragraph(),
            "file": test_file,
        }

        response = self.client.post(url, payload, format="json")

        # Test if request is handled properly (HTTP 201)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

        test_upload = Upload.objects.get(id=response.data["id"])

        # Test if the name is properly recorded
        self.assertEqual(str(test_upload.name), payload["name"])

        # Test if file name recorded properly
        self.assertEqual(str(test_upload.file.name), test_file.name)
