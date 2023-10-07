from faker import Faker
from faker_file.providers.jpeg_file import GraphicJpegFileProvider

FAKER = Faker()
FAKER.add_provider(GraphicJpegFileProvider)

jpeg_file = FAKER.graphic_jpeg_file(size=(800, 800))
