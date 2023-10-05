from faker import Faker
from faker_file.providers.image.pil_generator import PilImageGenerator
from faker_file.providers.png_file import PngFileProvider

FAKER = Faker()
FAKER.add_provider(PngFileProvider)

png_file = FAKER.png_file(image_generator_cls=PilImageGenerator)
