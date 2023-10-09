# Required imports
from faker import Faker
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.pdf_file.generators.reportlab_generator import (
    ReportlabPdfGenerator,
)

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(PdfFileProvider)  # Register provider

# Generate PDF file using `reportlab`
pdf_file = FAKER.pdf_file(pdf_generator_cls=ReportlabPdfGenerator)
