from faker import Faker
from faker_file.providers.pdf_file import PdfFileProvider

FAKER = Faker()
FAKER.add_provider(PdfFileProvider)

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

pdf_file = FAKER.pdf_file(content=TEMPLATE, wrap_chars_after=80)
