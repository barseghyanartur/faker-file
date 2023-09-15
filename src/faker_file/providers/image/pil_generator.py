import logging
import textwrap
from io import BytesIO
from pathlib import Path
from typing import Any, Dict, List, Type, Union

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider
from PIL import Image, ImageDraw, ImageFont

from ...base import DynamicTemplate
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

    With dynamic content:

    .. code-block:: python

        from faker import Faker
        from faker_file.base import DynamicTemplate
        from faker_file.contrib.image.pil_snippets import *
        from faker_file.providers.image.pil_generator import PilImageGenerator
        from faker_file.providers.png_file import PngFileProvider

        FAKER = Faker()
        FAKER.add_provider(PngFileProvider)

        file = FAKER.png_file(
            image_generator_cls=PilImageGenerator,
            content=DynamicTemplate(
                [
                    (add_h1_heading, {}),
                    (add_paragraph, {"max_nb_chars": 500}),
                    (add_paragraph, {"max_nb_chars": 500}),
                    (add_paragraph, {"max_nb_chars": 500}),
                    (add_paragraph, {"max_nb_chars": 500}),
                ]
            )
        )

        file = FAKER.png_file(
            image_generator_cls=PilImageGenerator,
            content=DynamicTemplate(
                [
                    (add_h1_heading, {}),
                    (add_paragraph, {}),
                    (add_picture, {}),
                    (add_paragraph, {}),
                    (add_picture, {}),
                    (add_paragraph, {}),
                    (add_picture, {}),
                    (add_paragraph, {}),
                ]
            )
        )

        file = FAKER.png_file(
            image_generator_cls=PilImageGenerator,
            content=DynamicTemplate(
                [
                    (add_h1_heading, {}),
                    (add_picture, {}),
                    (add_paragraph, {"max_nb_chars": 500}),
                    (add_picture, {}),
                    (add_paragraph, {"max_nb_chars": 500}),
                    (add_picture, {}),
                    (add_paragraph, {"max_nb_chars": 500}),
                    (add_picture, {}),
                    (add_paragraph, {"max_nb_chars": 500}),
                ]
            )
        )

        file = FAKER.png_file(
            image_generator_cls=PilImageGenerator,
            content=DynamicTemplate(
                [
                    (add_h1_heading, {}),
                    (add_picture, {}),
                    (add_paragraph, {"max_nb_chars": 500}),
                    (add_table, {"rows": 5, "cols": 4}),
                ]
            )
        )

        file = FAKER.png_file(
            image_generator_cls=PilImageGenerator,
            content=DynamicTemplate(
                [
                    (add_h1_heading, {"margin": (2, 2)}),
                    (add_picture, {"margin": (2, 2)}),
                    (add_paragraph, {"max_nb_chars": 500, "margin": (2, 2)}),
                    (add_picture, {"margin": (2, 2)}),
                    (add_paragraph, {"max_nb_chars": 500, "margin": (2, 2)}),
                    (add_picture, {"margin": (2, 2)}),
                    (add_paragraph, {"max_nb_chars": 500, "margin": (2, 2)}),
                    (add_picture, {"margin": (2, 2)}),
                    (add_paragraph, {"max_nb_chars": 500, "margin": (2, 2)}),
                ]
            )
        )
    """

    encoding: str = DEFAULT_FILE_ENCODING
    font: str = str(Path("Pillow") / "Tests" / "fonts" / "DejaVuSans.ttf")
    font_size: int = 12
    page_width: int = 794  # A4 size at 96 DPI
    page_height: int = 1123  # A4 size at 96 DPI
    line_height: int = 14
    spacing: int = 6

    def __init__(self: "PilImageGenerator", **kwargs) -> None:
        super().__init__(**kwargs)
        self.pages = []
        self.img = None
        self.draw = None
        self.image_mode = "RGB"

    @classmethod
    def find_max_fit_for_multi_line_text(
        cls: Type["PilImageGenerator"],
        draw: ImageDraw,
        lines: List[str],
        font: ImageFont,
        max_width: int,
    ):
        # Find the longest line
        longest_line = str(max(lines, key=len))
        return cls.find_max_fit_for_single_line_text(
            draw, longest_line, font, max_width
        )

    @classmethod
    def find_max_fit_for_single_line_text(
        cls: Type["PilImageGenerator"],
        draw: "ImageDraw",
        text: str,
        font: ImageFont,
        max_width: int,
    ) -> int:
        low, high = 0, len(text)
        while low < high:
            mid = (high + low) // 2
            text_width, _ = draw.textsize(text[:mid], font=font)

            if text_width > max_width:
                high = mid
            else:
                low = mid + 1

        return low - 1

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
        if "image_mode" in kwargs:
            self.image_mode = kwargs["image_mode"]

    def create_image_instance(self, height: Union[int, None] = None) -> Image:
        return Image.new(
            self.image_mode,
            (self.page_width, height or self.page_height),
            (255, 255, 255),
        )

    def start_new_page(self):
        self.img = self.create_image_instance()
        self.draw = ImageDraw.Draw(self.img)

    def save_and_start_new_page(self):
        self.pages.append(self.img.copy())
        self.start_new_page()

    def combine_images_vertically(self):
        # Calculate total width and height
        total_width = max(image.width for image in self.pages)
        total_height = sum(image.height for image in self.pages)

        # Create a new, white canvas to paste images onto
        new_image = Image.new("RGB", (total_width, total_height), "white")

        # Paste each image
        y_offset = 0
        for image in self.pages:
            new_image.paste(image, (0, y_offset))
            y_offset += image.height

        return new_image

    def generate(
        self: "PilImageGenerator",
        content: str,
        data: Dict[str, Any],
        provider: Union[Faker, Generator, Provider],
        **kwargs,
    ) -> bytes:
        """Generate image."""
        position = (0, 0)
        if isinstance(content, DynamicTemplate):
            self.start_new_page()
            for counter, (ct_modifier, ct_modifier_kwargs) in enumerate(
                content.content_modifiers
            ):
                ct_modifier_kwargs["position"] = position
                # LOGGER.debug(f"ct_modifier_kwargs: {ct_modifier_kwargs}")
                add_page, position = ct_modifier(
                    provider,
                    self,
                    data,
                    counter,
                    **ct_modifier_kwargs,
                )

            self.pages.append(self.img.copy())  # Add as a new page
        else:
            self.img = self.create_image_instance()
            self.draw = ImageDraw.Draw(self.img)
            font = ImageFont.truetype(self.font, self.font_size)

            # The `content_specs` is a dictionary that holds two keys:
            # `max_nb_chars` and `wrap_chars_after`. Those are the same values
            # passed to the `PdfFileProvider`.
            content_specs = kwargs.get("content_specs", {})
            lines = content.split("\n")
            line_max_num_chars = self.find_max_fit_for_multi_line_text(
                self.draw,
                lines,
                font,
                self.page_width,
            )
            wrap_chars_after = content_specs.get("wrap_chars_after")
            if (
                not wrap_chars_after
                or wrap_chars_after
                and (wrap_chars_after > line_max_num_chars)
            ):
                lines = textwrap.wrap(content, line_max_num_chars)

            y_text = 0
            for counter, line in enumerate(lines):
                text_width, text_height = self.draw.textsize(
                    line, font=font, spacing=self.spacing
                )
                if y_text + text_height > self.page_height:
                    self.save_and_start_new_page()
                    y_text = 0

                self.draw.text(
                    (0, y_text),
                    line,
                    fill=(0, 0, 0),
                    spacing=self.spacing,
                    font=font,
                )
                y_text += text_height + self.line_height

            self.pages.append(self.img.copy())  # Add as a new page

        buffer = BytesIO()
        # Combine images together vertically
        combined_image = self.combine_images_vertically()
        combined_image.save(
            buffer,
            resolution=100.0,
            quality=95,
            format=provider.image_format,
        )

        return buffer.getvalue()
