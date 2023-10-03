from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)

docx_file = FAKER.docx_file(
    prefix="zzz",
    max_nb_chars=1_024,
    wrap_chars_after=80,
)
