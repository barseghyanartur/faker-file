from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.storages.aws_s3 import AWSS3Storage

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)

AWS_S3_STORAGE = AWSS3Storage(
    bucket_name="your-bucket-name",
    root_path="",
    rel_path="",
)

txt_file = FAKER.txt_file(storage=AWS_S3_STORAGE)
