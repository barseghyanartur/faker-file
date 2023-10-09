from faker import Faker
from faker_file.providers.ico_file import GraphicIcoFileProvider

FAKER = Faker()
FAKER.add_provider(GraphicIcoFileProvider)

ico_file = FAKER.graphic_ico_file(size=(800, 800))
