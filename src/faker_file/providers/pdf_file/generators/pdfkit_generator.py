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

        from faker import Faker
        from faker_file.providers.pdf_file import PdfFileProvider
        from faker_file.providers.pdf_file.generators import pdfkit_generator

        FAKER = Faker()

        file = PdfFileProvider(FAKER).pdf_file(
            pdf_generator_cls=pdfkit_generator.PdfkitPdfGenerator
        )

    Using `DynamicTemplate`:

        import base64
        from faker import Faker
        from faker_file.base import DynamicTemplate
        from faker_file.providers.jpeg_file import JpegFileProvider
        from faker_file.providers.pdf_file import PdfFileProvider
        from faker_file.providers.pdf_file.generators import pdfkit_generator

        FAKER = Faker()

        def create_data_url(image_bytes, image_format):
            encoded_image = base64.b64encode(image_bytes).decode('utf-8')
            return f"data:image/{image_format};base64,{encoded_image}"

        # Add table function
        def pdf_add_table(
            provider, generator, document, data, counter, **kwargs
        ):
            rows = kwargs.get("rows", 3)
            cols = kwargs.get("cols", 4)

            # Begin the HTML table
            table_html = "<table>"

            for row_num in range(rows):
                table_html += "<tr>"

                for col_num in range(cols):
                    text = provider.generator.paragraph()
                    table_html += f"<td>{text}</td>"

                    data.setdefault("content_modifiers", {})
                    data["content_modifiers"].setdefault("add_table", {})
                    data["content_modifiers"]["add_table"].setdefault(
                        counter, []
                    )
                    data["content_modifiers"]["add_table"][counter].append(
                        text
                    )

                table_html += "</tr>"

            # End the HTML table
            table_html += "</table>"

            document += ("\r\n" + table_html)

        # Add picture function
        def pdf_add_picture(
            provider, generator, document, data, counter, **kwargs
        ):
            jpeg_file = JpegFileProvider(provider.generator).jpeg_file(
                raw=True
            )
            data_url = create_data_url(jpeg_file, "jpg")
            document += f"<img src='{data_url}' alt='Inline Image' />"
            data.setdefault("content_modifiers", {})
            data["content_modifiers"].setdefault("add_picture", {})
            data["content_modifiers"]["add_picture"].setdefault(counter, [])
            data["content_modifiers"]["add_picture"][counter].append(
                jpeg_file.data["content"]
            )
            data["content"] += ("\r\n" + jpeg_file.data["content"])

        # Add page break
        def pdf_add_page_break(
            provider, generator, document, data, counter, **kwargs
        ):
            page_break_html = "<div style='page-break-before: always;'></div>"
            document += "\r\n" + page_break_html

        # Add a paragraph
        def pdf_add_paragraph(
            provider, generator, document, data, counter, **kwargs
        ):
            content = provider.generator.text(max_nb_chars=5_000)
            paragraph_html = f"<div><p>{content}</p></div>"
            document += "\r\n" + paragraph_html

        # Create a file with table, page-break, picture, page-break, paragraph
        file = PdfFileProvider(Faker()).pdf_file(
            pdf_generator_cls=pdfkit_generator.PdfkitPdfGenerator,
            content=DynamicTemplate(
                [
                    (pdf_add_table, {}),
                    (pdf_add_page_break, {}),
                    (pdf_add_picture, {}),
                    (pdf_add_page_break, {}),
                    (pdf_add_paragraph, {}),
                ]
            )
        )

        # Create a file with text of 100 pages
        file = PdfFileProvider(Faker()).pdf_file(
            pdf_generator_cls=pdfkit_generator.PdfkitPdfGenerator,
            content=DynamicTemplate(
                [
                    (pdf_add_paragraph, {}),
                    (pdf_add_page_break, {}),
                ] * 100
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
