from faker import Faker

FAKER = Faker()

from faker_file.providers.jpeg_file import GraphicJpegFileProvider

FAKER.add_provider(GraphicJpegFileProvider)

jpeg_file = FAKER.graphic_jpeg_file(size=(800, 800))
