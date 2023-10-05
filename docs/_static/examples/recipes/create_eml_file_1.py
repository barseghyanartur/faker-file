from faker import Faker
from faker_file.providers.eml_file import EmlFileProvider

FAKER = Faker()
FAKER.add_provider(EmlFileProvider)

eml_file = FAKER.eml_file(
    options={"create_inner_file_args": {"content": "Lorem ipsum"}}
)
