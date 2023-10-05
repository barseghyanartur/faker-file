from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.random_file_from_dir import RandomFileFromDirProvider

FAKER = Faker()
FAKER.add_provider(RandomFileFromDirProvider)
FAKER.add_provider(DocxFileProvider)

# Create files to use
for __i in range(10):
    FAKER.docx_file(basename="file")

# We assume that directory "/tmp/tmp/" exists and contains files with".docx"
# extension.
docx_file_copy = FAKER.random_file_from_dir(
    source_dir_path="/tmp/tmp/",
    prefix="zzz",
)
