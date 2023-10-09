# Required imports
from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(DocxFileProvider)  # Register DocxFileProvider

# Generate DOCX file of 20,000 characters
docx_file = FAKER.docx_file(max_nb_chars=20_000)
