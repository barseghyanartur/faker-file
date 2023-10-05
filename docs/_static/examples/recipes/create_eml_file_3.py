from faker import Faker
from faker_file.providers.eml_file import EmlFileProvider

FAKER = Faker()
FAKER.add_provider(EmlFileProvider)

# Additional imports
from faker_file.providers.helpers.inner import (
    create_inner_docx_file,
    create_inner_eml_file,
)

eml_file = FAKER.eml_file(
    prefix="nested_level_0_",
    options={
        "create_inner_file_func": create_inner_eml_file,
        "create_inner_file_args": {
            "prefix": "nested_level_1_",
            "options": {
                "create_inner_file_func": create_inner_eml_file,
                "create_inner_file_args": {
                    "prefix": "nested_level_2_",
                    "options": {
                        "create_inner_file_func": create_inner_docx_file,
                    },
                },
            },
        },
    },
)
