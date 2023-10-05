from faker import Faker
from faker_file.providers.helpers.inner import (
    create_inner_docx_file,
    create_inner_xml_file,
    list_create_inner_file,
)
from faker_file.providers.zip_file import ZipFileProvider

FAKER = Faker()
FAKER.add_provider(ZipFileProvider)

zip_file = FAKER.zip_file(
    basename="alice-looking-through-the-glass",
    options={
        "create_inner_file_func": list_create_inner_file,
        "create_inner_file_args": {
            "func_list": [
                (create_inner_docx_file, {"basename": "doc"}),
                (create_inner_xml_file, {"basename": "doc_metadata"}),
                (create_inner_xml_file, {"basename": "doc_isbn"}),
            ],
        },
    },
)
