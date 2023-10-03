from faker import Faker
from faker_file.providers.pdf_file import GraphicPdfFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(GraphicPdfFileProvider)  # Register provider

file = FAKER.graphic_pdf_file(size=(800, 800))
