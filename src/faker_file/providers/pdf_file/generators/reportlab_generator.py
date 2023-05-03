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

        from faker import Faker
        from faker_file.providers.pdf_file import PdfFileProvider
        from faker_file.providers.pdf_file.generators import reportlab_generator

        FAKER = Faker()

        file = PdfFileProvider(FAKER).pdf_file(
            pdf_generator_cls=reportlab_generator.ReportlabPdfGenerator
        )

    Using `DynamicContent`:
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
        """Generate PDF."""
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
                    self,
                    doc,
                    data,
                    counter,
                    **ct_modifier_kwargs,
                )
        else:
            paragraph = Paragraph(content, style_paragraph)
            story.append(paragraph)

        doc.build(story)

        return buffer.getvalue()
