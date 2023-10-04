from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)

from faker_file.storages.aws_s3 import AWSS3Storage

AWS_S3_STORAGE = AWSS3Storage(
    bucket_name="your-bucket-name",
    root_path="",
    rel_path="",
)

# txt_file = FAKER.txt_file(storage=AWS_S3_STORAGE)
