from django.conf import settings
from faker import Faker
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.storages.aws_s3 import AWSS3Storage

STORAGE = AWSS3Storage(
    bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
    root_path="",
    rel_path="",
)

FAKER = Faker()
FAKER.add_provider(PdfFileProvider)

pdf_file = FAKER.pdf_file(storage=STORAGE)
