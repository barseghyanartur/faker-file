from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)

# Create a file to test `random_file_from_dir` with
FAKER.docx_file(basename="file")

from faker_file.providers.file_from_path import FileFromPathProvider

FAKER.add_provider(FileFromPathProvider)

docx_file = FAKER.file_from_path(
    path="/tmp/tmp/file.docx",
    prefix="zzz",
)
