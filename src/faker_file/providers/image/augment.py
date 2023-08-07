import io
import random
from copy import deepcopy
from typing import Callable, List, Optional

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

from ...helpers import random_pop

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "add_brightness",
    "add_contrast",
    "add_darkness",
    "add_saturation",
    "augment_image",
    "augment_image_file",
    "color_jitter",
    "decrease_contrast",
    "equalize",
    "flip_horizontal",
    "flip_vertical",
    "gaussian_blur",
    "grayscale",
    "random_crop",
    "resize_height",
    "resize_width",
    "rotate",
    "solarize",
)


# Default methods
def resize_width(
    img: Image.Image, lower: float = 0.5, upper: float = 1.5
) -> Image.Image:
    width_percent = random.uniform(lower, upper)
    return img.resize((int(img.width * width_percent), img.height))


def resize_height(
    img: Image.Image, lower: float = 0.5, upper: float = 1.5
) -> Image.Image:
    height_percent = random.uniform(lower, upper)
    return img.resize((img.width, int(img.height * height_percent)))


def grayscale(img: Image.Image) -> Image.Image:
    return img.convert("L")


def add_contrast(
    img: Image.Image, lower: float = 1, upper: float = 2
) -> Image.Image:
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(random.uniform(lower, upper))


def decrease_contrast(
    img: Image.Image, lower: float = 0.5, upper: float = 1
) -> Image.Image:
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(random.uniform(lower, upper))


def add_saturation(
    img: Image.Image, lower: float = 1, upper: float = 2
) -> Image.Image:
    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(random.uniform(lower, upper))


def add_brightness(
    img: Image.Image, lower: float = 1, upper: float = 2
) -> Image.Image:
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(random.uniform(lower, upper))


def add_darkness(
    img: Image.Image, lower: float = 0.5, upper: float = 1
) -> Image.Image:
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(random.uniform(lower, upper))


def flip_vertical(img: Image.Image) -> Image.Image:
    return img.transpose(method=Image.FLIP_TOP_BOTTOM)


def flip_horizontal(img: Image.Image) -> Image.Image:
    return img.transpose(method=Image.FLIP_LEFT_RIGHT)


def rotate(img: Image.Image, lower: int = -45, upper: int = 45) -> Image.Image:
    angle = random.randint(lower, upper)
    return img.rotate(angle)


def gaussian_blur(
    img: Image.Image, lower: float = 0.5, upper: float = 3
) -> Image.Image:
    return img.filter(
        ImageFilter.GaussianBlur(radius=random.uniform(lower, upper))
    )


def random_crop(
    img: Image.Image, lower: float = 0.6, upper: float = 0.9
) -> Image.Image:
    width, height = img.size
    crop_size = random.uniform(lower, upper)
    new_width, new_height = int(width * crop_size), int(height * crop_size)

    left = random.randint(0, width - new_width)
    top = random.randint(0, height - new_height)
    right = left + new_width
    bottom = top + new_height

    return img.crop((left, top, right, bottom))


def solarize(img: Image.Image, threshold: int = 128) -> Image.Image:
    return ImageOps.solarize(img, threshold=threshold)


def equalize(img: Image.Image) -> Image.Image:
    return ImageOps.equalize(img)


def color_jitter(
    img: Image.Image, lower: float = 0.5, upper: float = 1.5
) -> Image.Image:
    img = ImageEnhance.Brightness(img).enhance(random.uniform(lower, upper))
    img = ImageEnhance.Contrast(img).enhance(random.uniform(lower, upper))
    img = ImageEnhance.Color(img).enhance(random.uniform(lower, upper))
    return img


DEFAULT_METHODS = [
    add_brightness,
    add_contrast,
    add_darkness,
    add_saturation,
    decrease_contrast,
    flip_horizontal,
    flip_vertical,
    grayscale,
    resize_height,
    resize_width,
    rotate,
    solarize,
]


def augment_image(
    image_bytes: bytes,
    methods: Optional[List[Callable]] = None,
    num_steps: Optional[int] = None,
) -> bytes:
    # Load the image using PIL
    image = Image.open(io.BytesIO(image_bytes))
    counter = 0

    if not methods:
        _methods = deepcopy(DEFAULT_METHODS)
    else:
        _methods = deepcopy(methods)

    if not num_steps:
        num_steps = len(_methods)

    while counter < num_steps:
        method = random_pop(_methods)
        image = method(image)
        counter += 1

    # Convert the image back to bytes
    byte_array = io.BytesIO()
    image.save(byte_array, format=image.format)
    return byte_array.getvalue()


def augment_image_file(
    image_path: str,
    methods: Optional[List[Callable]] = None,
    num_steps: Optional[int] = None,
) -> bytes:
    with open(image_path, "rb") as image_bytes:
        return augment_image(
            image_bytes=image_bytes.read(),
            methods=methods,
            num_steps=num_steps,
        )
