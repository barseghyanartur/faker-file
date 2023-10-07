from faker import Faker
from faker_file.providers.webp_file import GraphicWebpFileProvider

FAKER = Faker()
FAKER.add_provider(GraphicWebpFileProvider)

webp_file = FAKER.graphic_webp_file(size=(800, 800))
