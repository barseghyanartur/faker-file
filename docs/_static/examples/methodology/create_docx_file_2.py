from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)

TEMPLATE = """
{{date}} {{city}}, {{country}}

Hello {{name}},

{{text}}

Address: {{address}}

Best regards,

{{name}}
{{address}}
{{phone_number}}
"""

docx_file = FAKER.docx_file(content=TEMPLATE)

print(docx_file)  # Sample value: 'tmp/tmpgdctmfbp.docx'
print(docx_file.data["content"])
# Sample value below:
#  2009-05-14 Pettyberg, Puerto Rico
#  Hello Lauren Williams,
#
#  Everyone bill I information. Put particularly note language support
#  green. Game free family probably case day vote.
#  Commercial especially game heart.
#
#  Address: 19017 Jennifer Drives
#  Jamesbury, MI 39121
#
#  Best regards,
#
#  Robin Jones
#  4650 Paul Extensions
#  Port Johnside, VI 78151
#  001-704-255-3093
