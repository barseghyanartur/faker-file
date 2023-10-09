from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.registry import FILE_REGISTRY  # Import instance at once

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)

# Create a file to remove
filename = str(FAKER.txt_file())

# We assume that there's an initialized `filename` (str) to remove.
txt_file = FILE_REGISTRY.search(filename)
if txt_file:
    FILE_REGISTRY.remove(txt_file)
