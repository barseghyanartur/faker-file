# Required imports
from faker import Faker
from faker_file.providers.odt_file import OdtFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(OdtFileProvider)  # Register OdtFileProvider

# Generate ODT file
odt_file = FAKER.odt_file()
