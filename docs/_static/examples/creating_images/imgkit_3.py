from faker import Faker
from faker_file.providers.image.imgkit_generator import ImgkitImageGenerator
from faker_file.providers.png_file import PngFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(PngFileProvider)  # Register PngFileProvider

# Generate an image file of 20,000 characters
png_file = FAKER.png_file(
    image_generator_cls=ImgkitImageGenerator, max_nb_chars=20_000
)
