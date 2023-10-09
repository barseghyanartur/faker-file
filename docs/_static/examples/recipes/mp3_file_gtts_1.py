from faker import Faker
from faker_file.providers.mp3_file import Mp3FileProvider
from faker_file.providers.mp3_file.generators.gtts_generator import (
    GttsMp3Generator,
)

FAKER = Faker()
FAKER.add_provider(Mp3FileProvider)

mp3_file = FAKER.mp3_file(mp3_generator_cls=GttsMp3Generator)
