from faker import Faker
from faker_file.providers.helpers.inner import (
    create_inner_docx_file,
    create_inner_epub_file,
    create_inner_txt_file,
    fuzzy_choice_create_inner_file,
)
from faker_file.providers.zip_file import ZipFileProvider
from faker_file.storages.filesystem import FileSystemStorage

FAKER = Faker()
FAKER.add_provider(ZipFileProvider)

STORAGE = FileSystemStorage()

kwargs = {"storage": STORAGE, "generator": FAKER}

zip_file = FAKER.zip_file(
    prefix="zzz_archive_",
    options={
        "count": 50,
        "create_inner_file_func": fuzzy_choice_create_inner_file,
        "create_inner_file_args": {
            "func_choices": [
                (create_inner_docx_file, kwargs),
                (create_inner_epub_file, kwargs),
                (create_inner_txt_file, kwargs),
            ],
        },
        "directory": "zzz",
    },
)
