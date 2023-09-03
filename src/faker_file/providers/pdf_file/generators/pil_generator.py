import logging
import textwrap
from io import BytesIO
from pathlib import Path
from typing import Any, Dict, Union

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider
from PIL import Image, ImageDraw, ImageFont

from ....base import DynamicTemplate
from ....constants import DEFAULT_FILE_ENCODING
from ...base.pdf_generator import BasePdfGenerator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("PilPdfGenerator",)

LOGGER = logging.getLogger(__name__)


def find_max_fit_for_multi_line_text(draw, lines, font, max_width):
    # Find the longest line
    longest_line = str(max(lines, key=len))
    return find_max_fit_for_single_line_text(
        draw, longest_line, font, max_width
    )


def find_max_fit_for_single_line_text(
    draw: ImageDraw,
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


class PilPdfGenerator(BasePdfGenerator):
    """Pillow PDF generator.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.pdf_file import PdfFileProvider
        from faker_file.providers.pdf_file.generators import pil_generator

        FAKER = Faker()
        FAKER.add_provider(PdfFileProvider)

        file = FAKER.pdf_file(
            pdf_generator_cls=pil_generator.PilPdfGenerator
        )

    With options:

    .. code-bloock:: python

        file = FAKER.pdf_file(
            pdf_generator_cls=PilPdfGenerator,
            pdf_generator_kwargs={
                "encoding": "utf8",
                "font_size": 14,
                "page_width": 800,
                "page_height": 1200,
                "line_height": 16,
                "spacing": 5,
            },
            wrap_chars_after=100,
        )
    """

    encoding: str = DEFAULT_FILE_ENCODING
    font: str = str(Path("Pillow") / "Tests" / "fonts" / "DejaVuSans.ttf")
    font_size: int = 12
    page_width: int = 794  # A4 size at 96 DPI
    page_height: int = 1123  # A4 size at 96 DPI
    line_height: int = 14
    spacing: int = 6  # Letter spacing

    def handle_kwargs(self: "PilPdfGenerator", **kwargs) -> None:
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

    def create_image_instance(self) -> Image:
        return Image.new(
            "RGB",
            (self.page_width, self.page_height),
            (255, 255, 255),
        )

    def generate(
        self: "PilPdfGenerator",
        content: Union[str, DynamicTemplate],
        data: Dict[str, Any],
        provider: Union[Faker, Generator, Provider],
        **kwargs,
    ) -> bytes:
        """Generate PDF."""
        pages = []
        if isinstance(content, DynamicTemplate):
            for counter, (ct_modifier, ct_modifier_kwargs) in enumerate(
                content.content_modifiers
            ):
                img = self.create_image_instance()
                draw = ImageDraw.Draw(img)
                # draw.image = img
                position = (0, 0)
                if "position" not in ct_modifier_kwargs:
                    ct_modifier_kwargs["position"] = position

                position = ct_modifier(
                    provider,
                    self,
                    draw,
                    data,
                    counter,
                    **ct_modifier_kwargs,
                )

                pages.append(img.copy())  # Add as a new page
        else:
            img = self.create_image_instance()
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(self.font, self.font_size)

            content_specs = kwargs.get("content_specs", {})
            line_max_num_chars = find_max_fit_for_multi_line_text(
                draw,
                content.split("\n"),
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
                text_width, text_height = draw.textsize(
                    line, font=font, spacing=6
                )
                # if counter % max_lines_per_page == 0:
                if y_text + text_height > self.page_height:
                    pages.append(img.copy())
                    img = self.create_image_instance()
                    draw = ImageDraw.Draw(img)
                    y_text = 0

                draw.text(
                    (0, y_text), line, fill=(0, 0, 0), spacing=6, font=font
                )
                y_text += text_height + self.line_height
                LOGGER.error(f"line: {line}")

            pages.append(img.copy())  # Add as a new page

        buffer = BytesIO()
        # Save as multi-page PDF
        pages[0].save(
            buffer, save_all=True, append_images=pages[1:], format="PDF"
        )

        return buffer.getvalue()
