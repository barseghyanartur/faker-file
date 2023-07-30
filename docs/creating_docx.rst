Creating DOCX
=============

See the following full functional snippet for generating DOCX.

.. code-block:: python
    :name: test_creating_docx

    # Imports
    from faker import Faker
    from faker_file.providers.docx_file import DocxFileProvider

    FAKER = Faker() # Initialize Faker
    FAKER.add_provider(DocxFileProvider)  # Register DocxFileProvider

    # Generate DOCX file
    docx_file = FAKER.docx_file()

The generated DOCX will have 10,000 characters of text, which is about 5 pages.

If you want DOCX with more pages, you could either:

- Increase the value of ``max_nb_chars`` accordingly.
- Set value of ``wrap_chars_after`` to 80 characters to force longer pages.
- Insert manual page breaks and other content.

See the example below for ``max_nb_chars`` tweak:

.. code-block:: python

    # Generate DOCX file of 20,000 characters
    docx_file = FAKER.docx_file(max_nb_chars=20_000)

See the example below for ``wrap_chars_after`` tweak:

.. code-block:: python

    # Generate DOCX file, wrapping each line after 80 characters
    docx_file = FAKER.docx_file(wrap_chars_after=80)

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables, manual text break and pretty much everything that
is supported by DOCX format specification, although currently only images,
paragraphs, tables and manual text breaks are supported out of the box. In
order to customise the blocks DOCX file is built from, the ``DynamicTemplate``
class is used. See the example below for usage examples:

.. code-block:: python

    # Additional imports
    from faker_file.base import DynamicTemplate
    from faker_file.contrib.docx_file import (
        add_page_break,
        add_paragraph,
        add_picture,
        add_table,
    )

    # Create a DOCX file with paragraph, picture, table and manual page breaks
    # in between the mentioned elements. The ``DynamicTemplate`` simply
    # accepts a list of callables (such as ``add_paragraph``,
    # ``add_page_break``) and dictionary to be later on fed to the callables
    # as keyword arguments for customising the default values.
    docx_file = FAKER.docx_file(
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
    docx_file = FAKER.docx_file(
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
