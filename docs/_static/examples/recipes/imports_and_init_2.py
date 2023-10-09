from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider

FAKER = Faker()

# Usage example
txt_file = TxtFileProvider(FAKER).txt_file(content="Lorem ipsum")
