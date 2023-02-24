import logging

import pdfkit

from ....constants import DEFAULT_FILE_ENCODING
from ...base.pdf_generator import BasePdfGenerator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("PdfkitPdfGenerator",)

LOGGER = logging.getLogger(__name__)


class PdfkitPdfGenerator(BasePdfGenerator):
    """Pdfkit PDF generator.

    Usage example:

        from faker import Faker
        from faker_file.providers.pdf_file import PdfFileProvider
        from faker_file.providers.pdf_file.generators import pdfkit_generator

        FAKER = Faker()

        file = PdfFileProvider(FAKER).pdf_file(
            pdf_generator_cls=pdfkit_generator.PdfkitPdfGenerator
        )
    """

    encoding: str = DEFAULT_FILE_ENCODING

    def handle_kwargs(self: "PdfkitPdfGenerator", **kwargs) -> None:
        """Handle kwargs."""
        if "encoding" in kwargs:
            self.encoding = kwargs["encoding"]

    def generate(self: "PdfkitPdfGenerator", content: str, **kwargs) -> bytes:
        """Generate PDF."""
        options = {"quiet": ""}
        if self.encoding is not None:
            options["encoding"] = self.encoding

        return pdfkit.from_string(
            f"<pre style='white-space: pre-wrap;'>{content}</pre>",
            options=options,
        )
