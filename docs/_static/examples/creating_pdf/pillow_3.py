from faker import Faker
from faker_file.base import DynamicTemplate
from faker_file.contrib.pdf_file.pil_snippets import (
    add_page_break,
    add_paragraph,
    add_picture,
    add_table,
)
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.pdf_file.generators.pil_generator import (
    PilPdfGenerator,
)

FAKER = Faker()
FAKER.add_provider(PdfFileProvider)

# Create a PDF file with paragraph, picture, table and manual page breaks
# in between the mentioned elements. The ``DynamicTemplate`` simply
# accepts a list of callables (such as ``add_paragraph``,
# ``add_page_break``) and dictionary to be later on fed to the callables
# as keyword arguments for customising the default values.
pdf_file = FAKER.pdf_file(
    pdf_generator_cls=PilPdfGenerator,
    content=DynamicTemplate(
        [
            (add_paragraph, {}),  # Add paragraph
            (add_page_break, {}),  # Add page break
            (add_picture, {}),  # Add picture
            (add_page_break, {}),  # Add page break
            (add_table, {}),  # Add table
            (add_page_break, {}),  # Add page break
        ]
    ),
)

# You could make the list as long as you like or simply multiply for
# easier repetition as follows:
pdf_file = FAKER.pdf_file(
    pdf_generator_cls=PilPdfGenerator,
    content=DynamicTemplate(
        [
            (add_paragraph, {}),  # Add paragraph
            (add_page_break, {}),  # Add page break
            (add_picture, {}),  # Add picture
            (add_page_break, {}),  # Add page break
            (add_table, {}),  # Add table
            (add_page_break, {}),  # Add page break
        ]
        * 5  # Will repeat your config 5 times
    ),
)
