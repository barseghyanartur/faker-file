from faker import Faker
from faker_file.providers.eml_file import EmlFileProvider

FAKER = Faker()
FAKER.add_provider(EmlFileProvider)

# Additional imports
from faker_file.providers.helpers.inner import create_inner_docx_file

eml_file = FAKER.eml_file(
    prefix="zzz",
    options={
        "count": 3,
        "create_inner_file_func": create_inner_docx_file,
        "create_inner_file_args": {
            "prefix": "xxx_",
            "max_nb_chars": 1_024,
        },
    }
)
