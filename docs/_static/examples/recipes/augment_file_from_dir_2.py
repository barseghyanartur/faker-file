from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.eml_file import EmlFileProvider
from faker_file.providers.odt_file import OdtFileProvider
from faker_file.providers.txt_file import TxtFileProvider

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)
FAKER.add_provider(TxtFileProvider)
FAKER.add_provider(EmlFileProvider)
FAKER.add_provider(OdtFileProvider)

# Create files to test `augment_file_from_dir` with
FAKER.docx_file()
FAKER.eml_file()
FAKER.odt_file()
FAKER.txt_file()

from faker_file.providers.augment_file_from_dir import (
    AugmentFileFromDirProvider,
)

FAKER.add_provider(AugmentFileFromDirProvider)

augmented_file = FAKER.augment_file_from_dir(
    source_dir_path="/tmp/tmp/",
    extensions={"docx", "odt"},  # Pick only DOCX or ODT
)
