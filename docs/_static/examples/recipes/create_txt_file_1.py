from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)

txt_file = FAKER.txt_file(content="Lorem ipsum")
