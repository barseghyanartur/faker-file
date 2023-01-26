from io import BytesIO

# import pytest
from django.test import TestCase
from django.urls import reverse
from faker import Faker

# from upload.api import API, UploadsController
from upload.models import Upload

from faker_file.providers.docx_file import DocxFileProvider

from .. import factories

# from ninja.testing import TestClient
# from ninja_extra.testing import TestClient


FAKER = Faker()
FAKER.add_provider(DocxFileProvider)

__all__ = ("UploadTestCase",)


class UploadTestCase(TestCase):
    """Upload test case."""

    # @pytest.mark.django_db
    def test_create_docx_upload(self) -> None:
        """Test create an Upload."""
        # client = TestClient(UploadsController)
        factories.UserFactory(super_admin=True, test_user=True)
        # self.client.login(
        #     username=factories.auth_user.TEST_USERNAME,
        #     password=factories.auth_user.TEST_PASSWORD
        # )
        url = reverse("api:create_upload")

        raw = FAKER.docx_file(raw=True)
        test_file = BytesIO(raw)
        test_file.name = "test.docx"

        payload = {
            "payload": {
                "name": FAKER.word(),
                "description": FAKER.paragraph(),
            },
            "file": test_file,
        }

        response = self.client.post(url, data=payload)
        import IPython

        IPython.embed()
        # Test if request is handled properly (HTTP 201)
        self.assertEqual(response.status_code, 200)
        # assert response.status_code == 200

        test_upload = Upload.objects.get(id=response.data["id"])

        # Test if the name is properly recorded
        self.assertEqual(str(test_upload.name), payload["payload"]["name"])
        # assert str(test_upload.name) == payload["name"]
