import io
import logging
from typing import Any, Dict, Union

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider
from pdf2image import convert_from_bytes
from PIL import Image
from weasyprint import HTML

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
    """

    encoding: str = DEFAULT_FILE_ENCODING

    def handle_kwargs(self: "WeasyPrintImageGenerator", **kwargs) -> None:
        """Handle kwargs."""

    def generate(
        self: "WeasyPrintImageGenerator",
        content: str,
        data: Dict[str, Any],
        provider: Union[Faker, Generator, Provider],
        **kwargs,
    ) -> bytes:
        """Generate image."""
        # Convert the HTML to a PDF and store in memory
        pdf_bytes = HTML(string=f"<pre>{content}</pre>").write_pdf()

        # Convert the in-memory PDF to images
        images = convert_from_bytes(pdf_bytes)

        # If the PDF has multiple pages, stitch them together
        if len(images) > 1:
            # Get dimensions of combined image
            width, height = images[0].size[0], sum(
                [img.size[1] for img in images]
            )

            # Create a new image with white background
            result = Image.new("RGB", (width, height), (255, 255, 255))

            # Iterate over images and paste them onto the new image
            y_offset = 0
            for img in images:
                result.paste(img, (0, y_offset))
                y_offset += img.size[1]
        else:
            # If there's only one page, use it directly
            result = images[0]

        # Save the result to a BytesIO object
        output = io.BytesIO()
        result.save(output, format=provider.extension)
        image_bytes = output.getvalue()  # Image, stored in memory

        return image_bytes
