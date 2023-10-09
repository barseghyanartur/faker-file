from faker import Faker
from faker_file.providers.pdf_file import GraphicPdfFileProvider

FAKER = Faker()
FAKER.add_provider(GraphicPdfFileProvider)

pdf_file = FAKER.graphic_pdf_file()
