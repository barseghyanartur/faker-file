from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)

docx_file = FAKER.docx_file(max_nb_chars=50)
print(docx_file)  # Sample value: 'tmp/tmpgdctmfbp.docx'
print(docx_file.data["content"])  # Sample value: 'Learn where receive social.'
print(docx_file.data["filename"])  # Sample value: '/tmp/tmp/tmpgdctmfbp.docx'
