from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.file_from_path import FileFromPathProvider

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)
FAKER.add_provider(FileFromPathProvider)

# Create a file to test `file_from_path` with.
FAKER.docx_file(basename="file")

# We assume that the file "/tmp/tmp/file.docx" exists.
docx_file = FAKER.file_from_path(
    path="/tmp/tmp/file.docx",
    prefix="zzz",
)
