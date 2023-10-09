from faker import Faker
from faker_file.providers.mp3_file import Mp3FileProvider

FAKER = Faker()
FAKER.add_provider(Mp3FileProvider)

mp3_file = FAKER.mp3_file()
