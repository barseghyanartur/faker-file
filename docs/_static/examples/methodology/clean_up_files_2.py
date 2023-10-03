# Import instance at once
from faker_file.registry import FILE_REGISTRY

# Create a file to remove
from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider
FAKER = Faker()
FAKER.add_provider(TxtFileProvider)
file = FAKER.txt_file()

# We assume that there's an initialized `file` instance to remove.
FILE_REGISTRY.remove(file)  # Where file is an instance of ``StringValue``
