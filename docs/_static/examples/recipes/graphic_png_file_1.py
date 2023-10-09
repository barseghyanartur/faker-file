from faker import Faker
from faker_file.providers.png_file import GraphicPngFileProvider

FAKER = Faker()
FAKER.add_provider(GraphicPngFileProvider)

png_file = FAKER.graphic_png_file(size=(800, 800))
