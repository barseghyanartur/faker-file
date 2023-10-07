from faker import Faker
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.pdf_file.generators.pil_generator import (
    PilPdfGenerator,
)

FAKER = Faker()
FAKER.add_provider(PdfFileProvider)

pdf_file = FAKER.pdf_file(
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
