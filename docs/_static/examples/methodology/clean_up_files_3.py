# Import instance at once
# Create a file to remove
from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.registry import FILE_REGISTRY

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)
filename = str(FAKER.txt_file())

# We assume that there's an initialized `filename` (str) to remove.
file = FILE_REGISTRY.search(filename)
if file:
    FILE_REGISTRY.remove(file)
