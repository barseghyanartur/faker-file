from faker import Faker
from faker_file.providers.image.pil_generator import PilImageGenerator
from faker_file.providers.png_file import PngFileProvider

FAKER = Faker()
FAKER.add_provider(PngFileProvider)

png_file = FAKER.png_file(
    image_generator_cls=PilImageGenerator,
    image_generator_kwargs={
        "encoding": "utf8",
        "font_size": 14,
        "page_width": 800,
        "page_height": 1200,
        "line_height": 16,
        "spacing": 5,
    },
    wrap_chars_after=100,
)
