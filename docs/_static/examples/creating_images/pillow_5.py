from faker import Faker
from faker_file.providers.png_file import GraphicPngFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(GraphicPngFileProvider)  # Register provider

png_file = FAKER.graphic_png_file(size=(800, 800))
