from faker import Faker
from faker_file.providers.zip_file import ZipFileProvider

FAKER = Faker()
FAKER.add_provider(ZipFileProvider)

zip_file = FAKER.zip_file(
    options={"create_inner_file_args": {"content": "Lorem ipsum"}}
)
