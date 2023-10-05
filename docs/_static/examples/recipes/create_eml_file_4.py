from faker import Faker
from faker_file.providers.eml_file import EmlFileProvider
from faker_file.providers.helpers.inner import (
    create_inner_docx_file,
    create_inner_epub_file,
    create_inner_txt_file,
    fuzzy_choice_create_inner_file,
)
from faker_file.storages.filesystem import FileSystemStorage

FAKER = Faker()
FAKER.add_provider(EmlFileProvider)

STORAGE = FileSystemStorage()

kwargs = {"storage": STORAGE, "generator": FAKER}

eml_file = FAKER.eml_file(
    prefix="zzz",
    options={
        "count": 10,
        "create_inner_file_func": fuzzy_choice_create_inner_file,
        "create_inner_file_args": {
            "func_choices": [
                (create_inner_docx_file, kwargs),
                (create_inner_epub_file, kwargs),
                (create_inner_txt_file, kwargs),
            ],
        },
    },
)
