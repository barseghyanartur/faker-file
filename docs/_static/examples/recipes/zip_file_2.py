from faker import Faker
from faker_file.providers.helpers.inner import create_inner_docx_file
from faker_file.providers.zip_file import ZipFileProvider

FAKER = Faker()
FAKER.add_provider(ZipFileProvider)

zip_file = FAKER.zip_file(
    prefix="zzz",
    options={
        "count": 3,
        "create_inner_file_func": create_inner_docx_file,
        "create_inner_file_args": {
            "prefix": "xxx_",
            "max_nb_chars": 1_024,
        },
        "directory": "yyy",
    },
)
