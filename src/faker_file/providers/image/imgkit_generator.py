import contextlib
import io
import logging
from typing import Any, Dict, Union

import imgkit
from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider

from ...constants import DEFAULT_FILE_ENCODING
from ..base.image_generator import BaseImageGenerator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("ImgkitImageGenerator",)

LOGGER = logging.getLogger(__name__)


class ImgkitImageGenerator(BaseImageGenerator):
    """Imgkit image generator.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.png_file import PngFileProvider
        from faker_file.providers.images.generators import imgkit_generator

        FAKER = Faker()
        FAKER.add_provider(PngFileProvider)

        file = FAKER.png_file(
            img_generator_cls=imgkit_generator.ImgkitImageGenerator
        )
    """

    encoding: str = DEFAULT_FILE_ENCODING

    def handle_kwargs(self: "ImgkitImageGenerator", **kwargs) -> None:
        """Handle kwargs."""

    def generate(
        self: "ImgkitImageGenerator",
        content: str,
        data: Dict[str, Any],
        provider: Union[Faker, Generator, Provider],
        **kwargs,
    ) -> bytes:
        """Generate image."""
        with contextlib.redirect_stdout(io.StringIO()):
            return imgkit.from_string(
                f"<pre>{content}</pre>",
                False,
                options={"format": provider.extension},
            )
