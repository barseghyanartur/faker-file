# Required imports
from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(DocxFileProvider)  # Register DocxFileProvider

# Generate DOCX file, wrapping each line after 80 characters
docx_file = FAKER.docx_file(wrap_chars_after=80)
