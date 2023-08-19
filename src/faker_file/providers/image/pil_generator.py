import logging
from io import BytesIO
from pathlib import Path
from typing import Any, Dict, Union

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider
from PIL import Image, ImageDraw, ImageFont

from ...constants import DEFAULT_FILE_ENCODING
from ..base.image_generator import BaseImageGenerator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("PilImageGenerator",)

LOGGER = logging.getLogger(__name__)


class PilImageGenerator(BaseImageGenerator):
    """PIL image generator.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.png_file import PngFileProvider
        from faker_file.providers.image.pil_generator import PilImageGenerator

        FAKER = Faker()
        FAKER.add_provider(PngFileProvider)

        file = FAKER.png_file(
            image_generator_cls=PilImageGenerator,
        )

    With options:

    .. code-block:: python

        file = FAKER.png_file(
            image_generator_cls=PilImageGenerator,
            image_generator_kwargs={
                "spacing": 6,
            },
            wrap_chars_after=119,
        )
    """

    encoding: str = DEFAULT_FILE_ENCODING
    font: str = str(Path("Pillow") / "Tests" / "fonts" / "DejaVuSans.ttf")
    font_size: int = 12
    page_width: int = 794  # A4 size at 96 DPI
    page_height: int = 1123  # A4 size at 96 DPI
    line_height: int = 14
    spacing: int = 6

    def handle_kwargs(self: "PilImageGenerator", **kwargs) -> None:
        """Handle kwargs."""
        if "encoding" in kwargs:
            self.encoding = kwargs["encoding"]
        if "font_size" in kwargs:
            self.font_size = kwargs["font_size"]
        if "page_width" in kwargs:
            self.page_width = kwargs["page_width"]
        if "page_height" in kwargs:
            self.page_height = kwargs["page_height"]
        if "line_height" in kwargs:
            self.line_height = kwargs["line_height"]
        if "spacing" in kwargs:
            self.spacing = kwargs["spacing"]

    def generate(
        self: "PilImageGenerator",
        content: str,
        data: Dict[str, Any],
        provider: Union[Faker, Generator, Provider],
        **kwargs,
    ) -> bytes:
        """Generate image."""
        lines = content.split("\n")
        height = len(lines) * self.font_size
        img = Image.new(
            "RGB",
            (self.page_width, height or self.page_height),
            (255, 255, 255),
        )
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.font, self.font_size)
        y_text = 0
        for line in lines:
            draw.text((0, y_text), line, fill=(0, 0, 0), spacing=6, font=font)
            y_text += self.line_height

        buffer = BytesIO()
        img.save(buffer, format=provider.image_format)

        return buffer.getvalue()
