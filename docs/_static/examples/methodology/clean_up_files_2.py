from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.registry import FILE_REGISTRY  # Import instance at once

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)

# Create a file to remove
txt_file = FAKER.txt_file()

# We assume that there's an initialized `txt_file` instance to remove.
FILE_REGISTRY.remove(txt_file)  # Where file is an instance of ``StringValue``
