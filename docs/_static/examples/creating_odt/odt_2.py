# Required imports
from faker import Faker
from faker_file.providers.odt_file import OdtFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(OdtFileProvider)  # Register OdtFileProvider

# Generate ODT file of 20,000 characters
odt_file = FAKER.odt_file(max_nb_chars=20_000)
