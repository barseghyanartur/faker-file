from django.conf import settings
from factory import Faker
from factory.django import DjangoModelFactory
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.storages.aws_s3 import AWSS3Storage

from upload.models import Upload

STORAGE = AWSS3Storage(
    bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
    root_path="",
    rel_path="",
)

Faker.add_provider(PdfFileProvider)


class UploadFactory(DjangoModelFactory):
    name = Faker("word")
    description = Faker("text")
    file = Faker("pdf_file", storage=STORAGE)

    class Meta:
        model = Upload


# Usage example
upload = UploadFactory()
