Creating ODT
============

See the following full functional snippet for generating ODT.

.. code-block:: python
    :name: test_creating_odt

    # Imports
    from faker import Faker
    from faker_file.providers.odt_file import OdtFileProvider

    FAKER = Faker() # Initialize Faker
    FAKER.add_provider(OdtFileProvider)  # Register OdtFileProvider

    # Generate ODT file
    odt_file = FAKER.odt_file()

The generated ODT will have 10,000 characters of text, which is about 5 pages.

If you want ODT with more pages, you could either:

- Increase the value of ``max_nb_chars`` accordingly.
- Set value of ``wrap_chars_after`` to 80 characters to force longer pages.
- Insert manual page breaks and other content.

See the example below for ``max_nb_chars`` tweak:

.. code-block:: python

    # Generate ODT file of 20,000 characters
    odt_file = FAKER.odt_file(max_nb_chars=20_000)

See the example below for ``wrap_chars_after`` tweak:

.. code-block:: python

    # Generate ODT file, wrapping each line after 80 characters
    odt_file = FAKER.odt_file(wrap_chars_after=80)

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables, manual text break and pretty much everything that
is supported by ODT format specification, although currently only images,
paragraphs, tables and manual text breaks are supported out of the box. In
order to customise the blocks ODT file is built from, the ``DynamicTemplate``
class is used. See the example below for usage examples:

.. code-block:: python

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
            ] * 100  # Will repeat your config 100 times
        )
    )
