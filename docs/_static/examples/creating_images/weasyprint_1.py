from faker import Faker
from faker_file.providers.image.weasyprint_generator import (
    WeasyPrintImageGenerator,
)
from faker_file.providers.png_file import PngFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(PngFileProvider)  # Register provider

# Generate image file using `WeasyPrint`
png_file = FAKER.png_file(image_generator_cls=WeasyPrintImageGenerator)
