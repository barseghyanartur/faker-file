import io
import logging
import random
from copy import deepcopy
from typing import Any, Callable, Dict, List, Optional, Tuple

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

LOGGER = logging.getLogger(__name__)


# Default methods
def resize_width(
    img: Image.Image, lower: float = 0.5, upper: float = 1.5
) -> Image.Image:
    """Resize the image in width by a random percentage.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random resize.
        Default is 0.5.
    :param upper: Upper bound for the random resize.
        Default is 1.5.
    :return: Adjusted image.
    """
    width_percent = random.uniform(lower, upper)
    return img.resize((int(img.width * width_percent), img.height))


def resize_height(
    img: Image.Image, lower: float = 0.5, upper: float = 1.5
) -> Image.Image:
    """Resize the image in height by a random percentage.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random resize.
        Default is 0.5.
    :param upper: Upper bound for the random resize.
        Default is 1.5.
    :return: Adjusted image.
    """
    height_percent = random.uniform(lower, upper)
    return img.resize((img.width, int(img.height * height_percent)))


def grayscale(img: Image.Image) -> Image.Image:
    """Convert the image to grayscale."""
    return img.convert("L")


def add_contrast(
    img: Image.Image, lower: float = 1, upper: float = 2
) -> Image.Image:
    """Enhance the image's contrast by a random factor.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random enhancement.
        Default is 0.5.
    :param upper: Upper bound for the random enhancement.
        Default is 1.5.
    :return: Adjusted image.
    """
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(random.uniform(lower, upper))


def decrease_contrast(
    img: Image.Image, lower: float = 0.5, upper: float = 1
) -> Image.Image:
    """Reduce the image's contrast by a random factor.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random enhancement.
        Default is 0.5.
    :param upper: Upper bound for the random enhancement.
        Default is 1.5.
    :return: Adjusted image.
    """
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(random.uniform(lower, upper))


def add_saturation(
    img: Image.Image, lower: float = 1, upper: float = 2
) -> Image.Image:
    """Enhance the image's color saturation by a random factor.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random enhancement.
        Default is 0.5.
    :param upper: Upper bound for the random enhancement.
        Default is 1.5.
    :return: Adjusted image.
    """
    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(random.uniform(lower, upper))


def add_brightness(
    img: Image.Image, lower: float = 1, upper: float = 2
) -> Image.Image:
    """Increase the image's brightness by a random factor.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random enhancement.
        Default is 0.5.
    :param upper: Upper bound for the random enhancement.
        Default is 1.5.
    :return: Adjusted image.
    """
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(random.uniform(lower, upper))


def add_darkness(
    img: Image.Image, lower: float = 0.5, upper: float = 1
) -> Image.Image:
    """Decrease the image's brightness by a random factor.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random enhancement.
        Default is 0.5.
    :param upper: Upper bound for the random enhancement.
        Default is 1.5.
    :return: Adjusted image.
    """
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(random.uniform(lower, upper))


def flip_vertical(img: Image.Image) -> Image.Image:
    """Flip the image vertically."""
    return img.transpose(method=Image.FLIP_TOP_BOTTOM)


def flip_horizontal(img: Image.Image) -> Image.Image:
    """Flip the image horizontally."""
    return img.transpose(method=Image.FLIP_LEFT_RIGHT)


def rotate(
    img: Image.Image,
    lower: int = -45,
    upper: int = 45,
) -> Image.Image:
    """Rotate the image by a random angle.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random rotation.
        Default is 0.5.
    :param upper: Upper bound for the random rotation.
        Default is 1.5.
    :return: Adjusted image.
    """
    angle = random.randint(lower, upper)
    return img.rotate(angle)


def gaussian_blur(
    img: Image.Image, lower: float = 0.5, upper: float = 3
) -> Image.Image:
    """Apply Gaussian blur to the image using a random radius.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random radius.
        Default is 0.5.
    :param upper: Upper bound for the random radius.
        Default is 1.5.
    :return: Adjusted image.
    """
    return img.filter(
        ImageFilter.GaussianBlur(radius=random.uniform(lower, upper))
    )


def solarize(img: Image.Image, threshold: int = 128) -> Image.Image:
    """Invert pixel values above a specified threshold."""
    if img.mode == "RGBA":
        # Split the image into RGB and alpha
        rgb, alpha = img.split()[0:3], img.split()[3]

        # Convert the RGB tuple back to an image
        rgb_img = Image.merge("RGB", rgb)

        # Solarize the RGB image
        solarized_rgb = ImageOps.solarize(rgb_img, threshold=threshold)

        # Merge back with the alpha channel
        solarized_img = Image.merge("RGBA", (*solarized_rgb.split(), alpha))

        return solarized_img
    else:
        return ImageOps.solarize(img, threshold=threshold)


def random_crop(
    img: Image.Image, lower: float = 0.6, upper: float = 0.9
) -> Image.Image:
    """Randomly crop a portion of the image.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random crop.
        Default is 0.5.
    :param upper: Upper bound for the random crop.
        Default is 1.5.
    :return: Adjusted image.
    """
    width, height = img.size
    crop_size = random.uniform(lower, upper)
    new_width, new_height = int(width * crop_size), int(height * crop_size)

    left = random.randint(0, width - new_width)
    top = random.randint(0, height - new_height)
    right = left + new_width
    bottom = top + new_height

    return img.crop((left, top, right, bottom))


def equalize(img: Image.Image) -> Image.Image:
    """Equalize the image's histogram."""
    return ImageOps.equalize(img)


def color_jitter(
    img: Image.Image, lower: float = 0.5, upper: float = 1.5
) -> Image.Image:
    """Randomly adjust the image's brightness, contrast, saturation, and hue.

    :param img: Input image to be adjusted.
    :param lower: Lower bound for the random enhancement multiplier.
        Default is 0.5.
    :param upper: Upper bound for the random enhancement multiplier.
        Default is 1.5.
    :return: Adjusted image.
    """
    img = ImageEnhance.Brightness(img).enhance(random.uniform(lower, upper))
    img = ImageEnhance.Contrast(img).enhance(random.uniform(lower, upper))
    img = ImageEnhance.Color(img).enhance(random.uniform(lower, upper))
    return img


DEFAULT_AUGMENTATIONS: List[Tuple[Callable, Dict[str, Any]]] = [
    (add_brightness, {}),
    (add_contrast, {}),
    (add_darkness, {}),
    (add_saturation, {}),
    (decrease_contrast, {}),
    (flip_horizontal, {}),
    (flip_vertical, {}),
    (grayscale, {}),
    (resize_height, {}),
    (resize_width, {}),
    (rotate, {}),
    (solarize, {}),
    (gaussian_blur, {}),
    # Additional
    # (equalize, {}),
    # (color_jitter, {}),
    # (random_crop, {}),
]


def augment_image(
    image_bytes: bytes,
    augmentations: Optional[List[Tuple[Callable, Dict[str, Any]]]] = None,
    num_steps: Optional[int] = None,
    pop_func: Callable = random_pop,
) -> bytes:
    """Augment the input image with a series of random augmentation methods.

    Read an image provided in bytes format, applies a specified number
    of random augmentation methods from a given list, and then returns the
    augmented image in bytes format. If no list of methods is provided, a
    default list is used. If no number of steps (methods) is specified, all
    methods will be applied.

    :param image_bytes: Input image in bytes format.
    :param augmentations: List of tuples of callable augmentation
        functions and their respective keyword arguments. If not
        provided, the default augmentation functions will be used.
    :param num_steps: Number of augmentation steps (functions) to be
        applied. If not specified, the length of the `augmentations` list
        will be used.
    :param pop_func: Callable to pop items from `augmentations` list. By
        default, the `random_pop` is used, which pops items in random
        order. If you want the order of augmentations to be constant and
        as given, replace it with `list.pop` (`pop_func=list.pop`).
    :return: Augmented image in bytes format.
    """
    # Load the image using PIL
    image = Image.open(io.BytesIO(image_bytes))
    # Original file format somehow gets lots during conversion.
    # We save it for later.
    image_format = image.format

    # Convert to RGB if the image is in palette mode. If we don't do so,
    # some formats (namely GIF) will certainly break on this.
    if image.mode == "P":
        image = image.convert("RGB")

    counter = 0

    if not augmentations:
        _augmentations = deepcopy(DEFAULT_AUGMENTATIONS)
    else:
        _augmentations = deepcopy(augmentations)

    if not num_steps:
        num_steps = len(_augmentations)

    while counter < num_steps:
        func_and_kwargs = pop_func(_augmentations)
        if func_and_kwargs:
            func, kwargs = func_and_kwargs
            # LOGGER.debug(f"Applying {func} to {id(image_bytes)}")
            try:
                image = func(image, **kwargs)
            except Exception as err:
                # Some combination of filters may not work correctly together.
                # Therefore, we silence the errors here.
                LOGGER.warning(f"Failed to apply {func} to {id(image_bytes)}")
                LOGGER.exception(err)
            counter += 1

    # Convert the image back to bytes
    byte_array = io.BytesIO()
    image.save(byte_array, format=image_format)
    return byte_array.getvalue()


def augment_image_file(
    image_path: str,
    augmentations: Optional[List[Tuple[Callable, Dict[str, Any]]]] = None,
    num_steps: Optional[int] = None,
    pop_func: Callable = random_pop,
) -> bytes:
    """Augment image from path.

    Augment the input image with a series of random augmentation functions.
    """
    with open(image_path, "rb") as image_bytes:
        return augment_image(
            image_bytes=image_bytes.read(),
            augmentations=augmentations,
            num_steps=num_steps,
            pop_func=pop_func,
        )
