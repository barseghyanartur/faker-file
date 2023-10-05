from faker import Faker
from faker_file.providers.image.imgkit_generator import ImgkitImageGenerator
from faker_file.providers.png_file import PngFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(PngFileProvider)  # Register PngFileProvider

# Generate PNG file using `imgkit`
pdf_file = FAKER.png_file(image_generator_cls=ImgkitImageGenerator)
