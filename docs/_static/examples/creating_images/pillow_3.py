from faker import Faker
from faker_file.base import DynamicTemplate
from faker_file.contrib.image.pil_snippets import (
    add_paragraph,
    add_picture,
    add_table,
)
from faker_file.providers.image.pil_generator import PilImageGenerator
from faker_file.providers.png_file import PngFileProvider

FAKER = Faker()
FAKER.add_provider(PngFileProvider)

# Create an image file with paragraph, picture and table.
# The ``DynamicTemplate`` simply accepts a list of callables (such as
# ``add_paragraph``, ``add_picture``) and dictionary to be later on fed
# to the callables as keyword arguments for customising the default
# values.
png_file = FAKER.png_file(
    image_generator_cls=PilImageGenerator,
    content=DynamicTemplate(
        [
            (add_paragraph, {}),  # Add paragraph
            (add_picture, {}),  # Add picture
            (add_table, {}),  # Add table
        ]
    ),
)

# You could make the list as long as you like or simply multiply for
# easier repetition as follows:
png_file = FAKER.png_file(
    image_generator_cls=PilImageGenerator,
    content=DynamicTemplate(
        [
            (add_paragraph, {}),  # Add paragraph
            (add_picture, {}),  # Add picture
            (add_table, {}),  # Add table
        ]
        * 5  # Will repeat your config 5 times
    ),
)
