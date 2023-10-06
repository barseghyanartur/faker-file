from faker import Faker

FAKER = Faker()

from faker_file.providers.generic_file import GenericFileProvider

FAKER.add_provider(GenericFileProvider)

generic_file = FAKER.generic_file(
    content="<html><body><p>{{text}}</p></body></html>",
    extension="html",
)
