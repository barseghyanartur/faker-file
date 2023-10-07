from faker import Faker
from faker_file.providers.generic_file import GenericFileProvider

FAKER = Faker()
FAKER.add_provider(GenericFileProvider)

generic_file = FAKER.generic_file(
    content="<html><body><p>{{text}}</p></body></html>",
    extension="html",
)
