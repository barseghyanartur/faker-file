from faker import Faker
from faker_file.providers.augment_file_from_dir import (
    AugmentFileFromDirProvider,
)
from faker_file.providers.augment_file_from_dir.augmenters import (
    textaugment_augmenter,
)
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.eml_file import EmlFileProvider
from faker_file.providers.odt_file import OdtFileProvider
from faker_file.providers.txt_file import TxtFileProvider

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)
FAKER.add_provider(TxtFileProvider)
FAKER.add_provider(EmlFileProvider)
FAKER.add_provider(OdtFileProvider)
FAKER.add_provider(AugmentFileFromDirProvider)

# Create files to test `augment_file_from_dir` with
FAKER.docx_file()
FAKER.eml_file()
FAKER.odt_file()
FAKER.txt_file()

# We assume that directory "/tmp/tmp/" exists and contains
# files of `DOCX`, `EML`, `EPUB`, `ODT`, `PDF`, `RTF` or `TXT`
# formats. Valid values for `action` are: "random_deletion",
# "random_insertion", "random_swap" and "synonym_replacement" (default).
augmented_file = FAKER.augment_file_from_dir(
    source_dir_path="/tmp/tmp/",
    text_augmenter_cls=textaugment_augmenter.EDATextaugmentAugmenter,
    text_augmenter_kwargs={
        "action": "synonym_replacement",
    },
)
