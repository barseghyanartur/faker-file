from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)

file = FAKER.docx_file(max_nb_chars=50)
print(file)  # Sample value: 'tmp/tmpgdctmfbp.docx'
print(file.data["content"])  # Sample value: 'Learn where receive social.'
print(file.data["filename"])  # Sample value: '/tmp/tmp/tmpgdctmfbp.docx'
