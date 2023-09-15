import io
import logging
from typing import Any, Dict, Union

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider
from pdf2image import convert_from_bytes
from PIL import Image
from weasyprint import HTML

from ...base import DynamicTemplate, StringList
from ...constants import DEFAULT_FILE_ENCODING
from ..base.image_generator import BaseImageGenerator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("WeasyPrintImageGenerator",)

LOGGER = logging.getLogger(__name__)


class WeasyPrintImageGenerator(BaseImageGenerator):
    """WeasyPrint and Pdf2Image ImageGenerator image generator.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.png_file import PngFileProvider
        from faker_file.providers.image.weasyprint_generator import (
            WeasyPrintImageGenerator
        )

        FAKER = Faker()
        FAKER.add_provider(PngFileProvider)

        file = FAKER.png_file(
            img_generator_cls=WeasyPrintImageGenerator
        )

    With dynamic content:

    .. code-block:: python

        from faker import Faker
        from faker_file.base import DynamicTemplate
        from faker_file.contrib.image.weasyprint_snippets import *
        from faker_file.providers.image.weasyprint_generator import (
            WeasyPrintImageGenerator
        )
        from faker_file.providers.png_file import PngFileProvider

        FAKER = Faker()
        FAKER.add_provider(PngFileProvider)

        file = FAKER.png_file(
            image_generator_cls=WeasyPrintImageGenerator,
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
            image_generator_cls=WeasyPrintImageGenerator,
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
            image_generator_cls=WeasyPrintImageGenerator,
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
            image_generator_cls=WeasyPrintImageGenerator,
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
            image_generator_cls=WeasyPrintImageGenerator,
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
    page_width: int = 794  # A4 size at 96 DPI
    page_height: int = 1123  # A4 size at 96 DPI
    wrapper_tag: str = "div"

    def __init__(self: "WeasyPrintImageGenerator", **kwargs):
        super().__init__(**kwargs)
        self.pages = []
        self.image_mode = "RGB"

    def handle_kwargs(self: "WeasyPrintImageGenerator", **kwargs) -> None:
        """Handle kwargs."""
        if "page_width" in kwargs:
            self.page_width = kwargs["page_width"]
        if "page_height" in kwargs:
            self.page_height = kwargs["page_height"]
        if "image_mode" in kwargs:
            self.image_mode = kwargs["image_mode"]
        if "wrapper_tag" in kwargs:
            self.wrapper_tag = kwargs["wrapper_tag"]

    def create_image_instance(
        self: "WeasyPrintImageGenerator",
        width: Union[int, None] = None,
        height: Union[int, None] = None,
    ) -> Image:
        return Image.new(
            self.image_mode,
            (width or self.page_width, height or self.page_height),
            # (width, height),
            (255, 255, 255),
        )

    def wrap(self: "WeasyPrintImageGenerator", content: str) -> str:
        return f"<{self.wrapper_tag}>" f"{content}" f"</{self.wrapper_tag}>"

    def generate(
        self: "WeasyPrintImageGenerator",
        content: str,
        data: Dict[str, Any],
        provider: Union[Faker, Generator, Provider],
        **kwargs,
    ) -> bytes:
        """Generate image."""
        if isinstance(content, DynamicTemplate):
            _content = StringList()
            for counter, (ct_modifier, ct_modifier_kwargs) in enumerate(
                content.content_modifiers
            ):
                ct_modifier(
                    provider,
                    self,
                    _content,
                    data,
                    counter,
                    **ct_modifier_kwargs,
                )
        else:
            # Convert the HTML to a PDF and store in memory
            pdf_bytes = HTML(
                string=f"<{self.wrapper_tag}>{content}</{self.wrapper_tag}>"
            ).write_pdf()

            # Convert the in-memory PDF to images
            self.pages = convert_from_bytes(pdf_bytes)

        # If the PDF has multiple pages, stitch them together
        if len(self.pages) > 1:
            # Get dimensions of combined image
            width, height = self.pages[0].size[0], sum(
                [img.size[1] for img in self.pages]
            )

            # Create a new image with white background
            result = self.create_image_instance(width, height)

            # Iterate over images and paste them onto the new image
            y_offset = 0
            for img in self.pages:
                result.paste(img, (0, y_offset))
                y_offset += img.size[1]
        else:
            # If there's only one page, use it directly
            result = self.pages[0]

        # Save the result to a BytesIO object
        output = io.BytesIO()
        result.save(output, format=provider.image_format)
        image_bytes = output.getvalue()  # Image, stored in memory

        return image_bytes
