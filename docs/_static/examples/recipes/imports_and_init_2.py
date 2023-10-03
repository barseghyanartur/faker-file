from faker import Faker
from faker_file.providers.bin_file import BinFileProvider
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.pptx_file import PptxFileProvider
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.providers.zip_file import ZipFileProvider

FAKER = Faker()

# Usage example
txt_file = TxtFileProvider(FAKER).txt_file(content="Lorem ipsum")
