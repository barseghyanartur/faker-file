import logging
from io import BytesIO
from typing import Any, Dict, Union

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate

from ....base import DynamicTemplate
from ....constants import DEFAULT_FONT_NAME, DEFAULT_FONT_PATH
from ...base.pdf_generator import BasePdfGenerator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("ReportlabPdfGenerator",)

LOGGER = logging.getLogger(__name__)


class ReportlabPdfGenerator(BasePdfGenerator):
    """Reportlab PDF generator.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.pdf_file import PdfFileProvider
        from faker_file.providers.pdf_file.generators import reportlab_generator

        FAKER = Faker()
        FAKER.add_provider(PdfFileProvider)

        file = FAKER.pdf_file(
            pdf_generator_cls=reportlab_generator.ReportlabPdfGenerator
        )

    Using `DynamicTemplate`:

    .. code-block:: python

        from io import BytesIO

        from faker import Faker
        from faker_file.base import DynamicTemplate
        from faker_file.providers.jpeg_file import JpegFileProvider
        from faker_file.providers.pdf_file import PdfFileProvider
        from faker_file.providers.pdf_file.generators import (
            reportlab_generator
        )
        from PIL import Image as PilImage
        from reportlab.lib.pagesizes import letter, landscape
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib import colors
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.platypus import (
            Image,
            Table,
            TableStyle,
            PageBreak,
            Paragraph,
        )

        FAKER = Faker()
        FAKER.add_provider(PdfFileProvider)

        # Add table function
        def pdf_add_table(
            provider, generator, story, data, counter, **kwargs
        ):
            rows = kwargs.get("rows", 3)
            cols = kwargs.get("cols", 4)

            # Define your table headers
            headers = [f"Header {i+1}" for i in range(cols)]

            # Generate the rest of the table data
            table_data = [
                [
                    provider.generator.word() for _ in range(cols)
                ] for _ in range(rows)
            ]

            # Add the headers to the table data
            table_data.insert(0, headers)

            # Create the table object
            table = Table(table_data)

            # Apply table styles
            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("FONTSIZE", (0, 0), (-1, 0), 14),
                        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                        ("GRID", (0, 0), (-1, -1), 1, colors.black),
                        ("BOX", (0, 0), (-1, -1), 1, colors.black),
                    ]
                )
            )

            # Add the table to the document and build it
            story.append(table)

        # Add picture function
        def pdf_add_picture(
            provider, generator, story, data, counter, **kwargs
        ):
            jpeg_file = JpegFileProvider(provider.generator).jpeg_file(
                raw=True
            )

            # Create a BytesIO object and load the image data
            with BytesIO(jpeg_file) as input_stream:
                pil_image = PilImage.open(input_stream)

                # Resize the image
                new_width = 400
                new_height = 400
                pil_image = pil_image.resize((new_width, new_height))

                # Create a BytesIO object outside the 'with' statement
                output_stream = BytesIO()
                pil_image.save(output_stream, format='JPEG')
                output_stream.seek(0)  # Move to the start of the stream

                # Now you can use output_stream as your image data
                img = Image(output_stream)
                img.width = new_width
                img.height = new_height
                story.append(img)

        # Add page break function
        def pdf_add_page_break(
            provider, generator, story, data, counter, **kwargs
        ):
            # Insert a page break
            story.append(PageBreak())

        # Add paragraph function
        def pdf_add_paragraph(
            provider, generator, story, data, counter, **kwargs
        ):
            # Insert a paragraph
            styles = getSampleStyleSheet()
            style_paragraph = styles["Normal"]
            style_paragraph.fontName = generator.font_name
            pdfmetrics.registerFont(
                TTFont(generator.font_name, generator.font_path)
            )
            content = provider.generator.text(max_nb_chars=5_000)
            paragraph = Paragraph(content, style_paragraph)
            story.append(paragraph)

        # Create a file with table, page-break, picture, page-break, paragraph
        file = FAKER.pdf_file(
            pdf_generator_cls=(
                reportlab_generator.ReportlabPdfGenerator
            ),
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
        file = FAKER.pdf_file(
            pdf_generator_cls=(
                reportlab_generator.ReportlabPdfGenerator
            ),
            content=DynamicTemplate(
                [
                    (pdf_add_paragraph, {}),
                    (pdf_add_page_break, {}),
                ] * 100
            )
        )
    """

    font_name: str = DEFAULT_FONT_NAME
    font_path: str = DEFAULT_FONT_PATH

    def handle_kwargs(self: "ReportlabPdfGenerator", **kwargs) -> None:
        """Handle kwargs."""
        if "font_name" in kwargs:
            self.font_name = kwargs["font_name"]
        if "font_path" in kwargs:
            self.font_path = kwargs["font_path"]

    def generate(
        self: "ReportlabPdfGenerator",
        content: Union[str, DynamicTemplate],
        data: Dict[str, Any],
        provider: Union[Faker, Generator, Provider],
        **kwargs,
    ) -> bytes:
        """Generate PDF.

        :param content:
        :param data:
        :param provider: `PdfFileProvider` instance.
        """
        styles = getSampleStyleSheet()
        style_paragraph = styles["Normal"]
        style_paragraph.fontName = self.font_name
        pdfmetrics.registerFont(TTFont(self.font_name, self.font_path))

        story = []
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            bottomMargin=0.4 * inch,
            topMargin=0.6 * inch,
            rightMargin=0.8 * inch,
            leftMargin=0.8 * inch,
        )
        if isinstance(content, DynamicTemplate):
            for counter, (ct_modifier, ct_modifier_kwargs) in enumerate(
                content.content_modifiers
            ):
                ct_modifier(
                    provider,
                    self,
                    story,
                    data,
                    counter,
                    **ct_modifier_kwargs,
                )
        else:
            paragraph = Paragraph(content, style_paragraph)
            story.append(paragraph)

        doc.build(story)

        return buffer.getvalue()
