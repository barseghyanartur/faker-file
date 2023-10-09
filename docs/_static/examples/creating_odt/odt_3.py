# Required imports
from faker import Faker
from faker_file.providers.odt_file import OdtFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(OdtFileProvider)  # Register OdtFileProvider

# Generate ODT file, wrapping each line after 80 characters
odt_file = FAKER.odt_file(wrap_chars_after=80)
