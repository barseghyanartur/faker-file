from faker import Faker

FAKER = Faker()

from faker_file.providers.mp3_file import Mp3FileProvider

FAKER.add_provider(Mp3FileProvider)

mp3_file = FAKER.mp3_file()
