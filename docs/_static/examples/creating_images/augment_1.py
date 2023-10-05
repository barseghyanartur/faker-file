from faker import Faker
from faker_file.providers.augment_image_from_path import (
    AugmentImageFromPathProvider,
)
from faker_file.providers.augment_random_image_from_dir import (
    AugmentRandomImageFromDirProvider,
)
from faker_file.providers.image.augment import (
    add_brightness,
    decrease_contrast,
    flip_horizontal,
    flip_vertical,
    resize_height,
    resize_width,
)
from faker_file.providers.png_file import GraphicPngFileProvider

FAKER = Faker()
FAKER.add_provider(AugmentImageFromPathProvider)
FAKER.add_provider(AugmentRandomImageFromDirProvider)
FAKER.add_provider(GraphicPngFileProvider)

# Create a couple of graphic images to augment later on.
FAKER.graphic_png_file(basename="01")  # One named 01.png
# And 5 more with random names.
for __ in range(5):
    FAKER.graphic_png_file()

# We assumed that directory "/tmp/tmp/" exists and contains
# image files, among which "01.png". Augmentations will be applied
# sequentially, one by one until all fulfilled. If you wish to apply only
# a random number of augmentations, but not all, pass the `num_steps`
# argument, with value less than the number of `augmentations` provided.
augmented_image_file = FAKER.augment_image_from_path(
    path="/tmp/tmp/01.png",
    augmentations=[
        (flip_horizontal, {}),
        (flip_vertical, {}),
        (decrease_contrast, {}),
        (add_brightness, {}),
        (resize_width, {"lower": 0.9, "upper": 1.1}),
        (resize_height, {"lower": 0.9, "upper": 1.1}),
    ],
    prefix="augmented_image_01_",
    # num_steps=3,
)

augmented_random_image_file = FAKER.augment_random_image_from_dir(
    source_dir_path="/tmp/tmp/",
    augmentations=[
        (flip_horizontal, {}),
        (flip_vertical, {}),
        (decrease_contrast, {}),
        (add_brightness, {}),
        (resize_width, {"lower": 0.9, "upper": 1.1}),
        (resize_height, {"lower": 0.9, "upper": 1.1}),
    ],
    prefix="augmented_random_image_",
    # num_steps=3,
)
