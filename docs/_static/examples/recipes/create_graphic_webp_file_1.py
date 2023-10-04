from faker import Faker

FAKER = Faker()

from faker_file.providers.webp_file import GraphicWebpFileProvider

FAKER.add_provider(GraphicWebpFileProvider)

webp_file = FAKER.graphic_webp_file(size=(800, 800))
