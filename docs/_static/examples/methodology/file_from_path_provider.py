from faker import Faker
from faker_file.providers.file_from_path import FileFromPathProvider

FAKER = Faker()
FAKER.add_provider(FileFromPathProvider)

# Create a file to use
from faker_file.providers.docx_file import DocxFileProvider
FAKER.add_provider(DocxFileProvider)
file = FAKER.docx_file(basename="file")

# We assume that directory "/tmp/tmp/" exists and contains a file named
# "file.docx".
file = FAKER.file_from_path(
    path="/tmp/tmp/file.docx",
    prefix="zzz",
)
