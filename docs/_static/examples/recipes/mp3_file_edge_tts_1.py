from faker import Faker
from faker_file.providers.mp3_file import Mp3FileProvider
from faker_file.providers.mp3_file.generators.edge_tts_generator import (
    EdgeTtsMp3Generator,
)

FAKER = Faker()
FAKER.add_provider(Mp3FileProvider)

mp3_file = FAKER.mp3_file(mp3_generator_cls=EdgeTtsMp3Generator)
