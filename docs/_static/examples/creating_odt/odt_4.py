# Required imports
from faker import Faker
from faker_file.providers.odt_file import OdtFileProvider

FAKER = Faker()  # Initialize Faker
FAKER.add_provider(OdtFileProvider)  # Register OdtFileProvider

# Additional imports
from faker_file.base import DynamicTemplate
from faker_file.contrib.odt_file import (
    add_page_break,
    add_paragraph,
    add_picture,
    add_table,
)

# Create a ODT file with paragraph, picture, table and manual page breaks
# in between the mentioned elements. The ``DynamicTemplate`` simply
# accepts a list of callables (such as ``add_paragraph``,
# ``add_page_break``) and dictionary to be later on fed to the callables
# as keyword arguments for customising the default values.
odt_file = FAKER.odt_file(
    content=DynamicTemplate(
        [
            (add_paragraph, {}),  # Add paragraph
            (add_page_break, {}),  # Add page break
            (add_picture, {}),  # Add picture
            (add_page_break, {}),  # Add page break
            (add_table, {}),  # Add table
            (add_page_break, {}),  # Add page break
        ]
    )
)

# You could make the list as long as you like or simply multiply for
# easier repetition as follows:
odt_file = FAKER.odt_file(
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
    )
)
