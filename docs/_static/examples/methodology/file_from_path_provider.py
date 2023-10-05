from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.file_from_path import FileFromPathProvider

FAKER = Faker()
FAKER.add_provider(FileFromPathProvider)
FAKER.add_provider(DocxFileProvider)

# Create a file to use
docx_file = FAKER.docx_file(basename="file")

# We assume that directory "/tmp/tmp/" exists and contains a file named
# "file.docx".
docx_file_copy = FAKER.file_from_path(
    path="/tmp/tmp/file.docx",
    prefix="zzz",
)
