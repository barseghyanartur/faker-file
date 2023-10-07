from faker import Faker
from faker_file.providers.bin_file import BinFileProvider

FAKER = Faker()
FAKER.add_provider(BinFileProvider)

bin_file = FAKER.bin_file(length=1024**2)  # 1 Mb
bin_file = FAKER.bin_file(length=3 * 1024**2)  # 3 Mb
bin_file = FAKER.bin_file(length=10 * 1024**2)  # 10 Mb

bin_file = FAKER.bin_file(length=1024)  # 1 Kb
bin_file = FAKER.bin_file(length=3 * 1024)  # 3 Kb
bin_file = FAKER.bin_file(length=10 * 1024)  # 10 Kb
