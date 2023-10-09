from multiprocessing import Pool

from faker import Faker
from faker_file.providers.helpers.inner import (
    create_inner_docx_file,
    create_inner_epub_file,
    create_inner_pdf_file,
    create_inner_txt_file,
    fuzzy_choice_create_inner_file,
)
from faker_file.storages.filesystem import FileSystemStorage

FAKER = Faker()
STORAGE = FileSystemStorage()

# Document template
TEMPLATE = """
{{date}} {{city}}, {{country}}

Hello {{name}},

{{text}} {{text}} {{text}}

{{text}} {{text}} {{text}}

{{text}} {{text}} {{text}}

Address: {{address}}

Best regards,

{{name}}
{{address}}
{{phone_number}}
"""

kwargs = {"storage": STORAGE, "generator": FAKER, "content": TEMPLATE}

with Pool(processes=2) as pool:
    for _ in range(10):  # Number of times we want to run our function
        pool.apply_async(
            fuzzy_choice_create_inner_file,
            [
                [
                    (create_inner_docx_file, kwargs),
                    (create_inner_epub_file, kwargs),
                    (create_inner_pdf_file, kwargs),
                    (create_inner_txt_file, kwargs),
                ]
            ],
        )
    pool.close()
    pool.join()
