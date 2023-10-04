from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)

# Create files to test `random_file_from_dir` with
for __i in range(5):
    FAKER.txt_file()

from faker_file.providers.random_file_from_dir import (
    RandomFileFromDirProvider,
)

FAKER.add_provider(RandomFileFromDirProvider)

random_file = FAKER.random_file_from_dir(
    source_dir_path="/tmp/tmp/",
    prefix="zzz",
)
