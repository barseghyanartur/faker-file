from faker import Faker
from faker_file.providers.helpers.inner import create_inner_docx_file
from faker_file.providers.zip_file import ZipFileProvider

FAKER = Faker()
FAKER.add_provider(ZipFileProvider)

TEMPLATE = "Hey {{name}},\n{{text}},\nBest regards\n{{name}}"

zip_file = FAKER.zip_file(
    options={
        "count": 9,
        "create_inner_file_func": create_inner_docx_file,
        "create_inner_file_args": {
            "content": TEMPLATE,
        },
    }
)
