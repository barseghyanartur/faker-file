from faker import Faker

FAKER = Faker()

from faker_file.providers.pdf_file import GraphicPdfFileProvider

FAKER.add_provider(GraphicPdfFileProvider)

pdf_file = FAKER.graphic_pdf_file(size=(800, 800))
