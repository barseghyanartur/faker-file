import logging
from typing import Any, Dict, Union

import pdfkit
from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider

from ....base import DynamicTemplate, StringList
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

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.pdf_file import PdfFileProvider
        from faker_file.providers.pdf_file.generators.pdfkit_generator import (
            PdfkitPdfGenerator
        )

        FAKER = Faker()
        FAKER.add_provider(PdfFileProvider)

        file = FAKER.pdf_file(pdf_generator_cls=PdfkitPdfGenerator)

    Using `DynamicTemplate`:

    .. code-block:: python

        from faker_file.base import DynamicTemplate
        from faker_file.contrib.pdf_file.pdfkit_snippets import (
            add_h1_heading,
            add_h2_heading,
            add_h3_heading,
            add_h4_heading,
            add_h5_heading,
            add_h6_heading,
            add_heading,
            add_page_break,
            add_paragraph,
            add_picture,
            add_table,
        )

        # Create a file with lots of elements
        file = FAKER.pdf_file(
            pdf_generator_cls=PdfkitPdfGenerator,
            content=DynamicTemplate(
                [
                    (add_h1_heading, {}),
                    (add_paragraph, {}),
                    (add_h2_heading, {}),
                    (add_h3_heading, {}),
                    (add_h4_heading, {}),
                    (add_h5_heading, {}),
                    (add_h6_heading, {}),
                    (add_paragraph, {}),
                    (add_picture, {}),
                    (add_page_break, {}),
                    (add_h6_heading, {}),
                    (add_table, {}),
                    (add_paragraph, {}),
                ]
            )
        )
    """

    encoding: str = DEFAULT_FILE_ENCODING

    def handle_kwargs(self: "PdfkitPdfGenerator", **kwargs) -> None:
        """Handle kwargs."""
        if "encoding" in kwargs:
            self.encoding = kwargs["encoding"]

    def generate(
        self: "PdfkitPdfGenerator",
        content: Union[str, DynamicTemplate],
        data: Dict[str, Any],
        provider: Union[Faker, Generator, Provider],
        **kwargs,
    ) -> bytes:
        """Generate PDF."""
        options = {"quiet": ""}
        if self.encoding is not None:
            options["encoding"] = self.encoding

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
            _content = f"<pre style='white-space: pre-wrap;'>{content}</pre>"

        return pdfkit.from_string(
            str(_content),
            options=options,
        )
