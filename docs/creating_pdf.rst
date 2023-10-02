Creating PDF
============
.. External references

.. _pdfkit: https://pypi.org/project/pdfkit/
.. _Pillow: https://pillow.readthedocs.io/
.. _reportlab: https://pypi.org/project/reportlab/
.. _wkhtmltopdf: https://wkhtmltopdf.org/

PDF is certainly one of the most complicated formats out there. And
certainly one of the formats most of the developers will be having trouble
with, as there are many versions and dialects. That makes it almost impossible
and highly challenging to have **just one right way** of creating PDF files.
That's why, creation of PDF files has been delegated to an abstraction layer
of PDF generators. If you don't like how PDF files are generated, you can
create your own layer, using your favourite library.

Currently, there are three PDF generators implemented:

- ``PdfkitPdfGenerator`` (default), built on top of the `pdfkit`_
  and `wkhtmltopdf`_.
- ``ReportlabPdfGenerator``, build on top of the famous `reportlab`_.
- ``PilPdfGenerator``, build on top of the `Pillow`_. Produced PDFs would
  contain images only (even texts are stored as images), unlike `pdfkit`_ or
  `reportlab`_ based solutions, where PDFs would simply contain selectable
  text. However, it's the generator that will likely won't ask for any
  system dependencies that you don't yet have installed.

Building PDF with text using `pdfkit`_
--------------------------------------
While `pdfkit`_ generator is heavier and has `wkhtmltopdf`_ as a system
dependency, it produces better quality PDFs and has no issues with fonts
or unicode characters.

See the following full functional snippet for generating PDF using `pdfkit`_.

.. literalinclude:: _static/examples/creating_pdf/pdfkit_1.py
    :language: python

*See the full example*
:download:`here <_static/examples/creating_pdf/pdfkit_1.py>`.

The generated PDF will have 10,000 characters of text, which is about 2 pages.

If you want PDF with more pages, you could either:

- Increase the value of ``max_nb_chars`` accordingly.
- Set value of ``wrap_chars_after`` to 80 characters to force longer pages.
- Insert manual page breaks and other content.

----

See the example below for ``max_nb_chars`` tweak:

.. literalinclude:: _static/examples/creating_pdf/pdfkit_2.py
    :language: python
    :lines: 11-

*See the full example*
:download:`here <_static/examples/creating_pdf/pdfkit_2.py>`.

----

See the example below for ``wrap_chars_after`` tweak:

.. literalinclude:: _static/examples/creating_pdf/pdfkit_3.py
    :language: python
    :lines: 11-

*See the full example*
:download:`here <_static/examples/creating_pdf/pdfkit_3.py>`.

----

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables, manual text break and pretty much everything that
is supported by PDF format specification, although currently only images,
paragraphs, tables and manual text breaks are supported out of the box. In
order to customise the blocks PDF file is built from, the ``DynamicTemplate``
class is used. See the example below for usage examples:

.. literalinclude:: _static/examples/creating_pdf/pdfkit_4.py
    :language: python
    :lines: 11-

*See the full example*
:download:`here <_static/examples/creating_pdf/pdfkit_4.py>`.

Building PDFs with text using `reportlab`_
------------------------------------------
While `reportlab`_ generator is much lighter than the `pdfkit`_ and does not
have system dependencies, but might produce PDF files with questionable
encoding when generating unicode text.

See the following full functional snippet for generating PDF using `reportlab`_.

.. literalinclude:: _static/examples/creating_pdf/reportlab_1.py
    :language: python

*See the full example*
:download:`here <_static/examples/creating_pdf/reportlab_1.py>`.

----

All examples shown for `pdfkit`_ apply for `reportlab`_ generator, however
when building PDF files from blocks (paragraphs, images, tables and page
breaks), the imports shall be adjusted:

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables, manual text break and pretty much everything that
is supported by PDF format specification, although currently only images,
paragraphs, tables and manual text breaks are supported. In order to customise
the blocks PDF file is built from, the ``DynamicTemplate`` class is used.
See the example below for usage examples:

.. literalinclude:: _static/examples/creating_pdf/reportlab_2.py
    :language: python
    :lines: 11-

*See the full example*
:download:`here <_static/examples/creating_pdf/reportlab_2.py>`.

Building PDFs with text using `Pillow`_
---------------------------------------
Usage example:

.. literalinclude:: _static/examples/creating_pdf/pillow_1.py
    :language: python

*See the full example*
:download:`here <_static/examples/creating_pdf/pillow_1.py>`.

----

With options:

.. literalinclude:: _static/examples/creating_pdf/pillow_2.py
    :language: python
    :lines: 10-

*See the full example*
:download:`here <_static/examples/creating_pdf/pillow_2.py>`.

----

All examples shown for `pdfkit`_ and `reportlab`_ apply to `Pillow`_ generator,
however when building PDF files from blocks (paragraphs, images, tables and page
breaks), the imports shall be adjusted:

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables, manual text break and pretty much everything that
is supported by PDF format specification, although currently only images,
paragraphs, tables and manual text breaks are supported. In order to customise
the blocks PDF file is built from, the ``DynamicTemplate`` class is used.
See the example below for usage examples:

.. code-block:: python

    # Additional imports
    from faker_file.base import DynamicTemplate
    from faker_file.contrib.pdf_file.pil_snippets import (
        add_page_break,
        add_paragraph,
        add_picture,
        add_table,
    )

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
        )
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
            ] * 100
        )
    )

Creating PDFs with graphics using `Pillow`_
-------------------------------------------
There's a so called `graphic` PDF file provider available. Produced PDF files
would not contain text, so don't use it when you need text based content.
However, sometimes you just need a valid file in PDF format, without
caring much about the content. That's where a GraphicPdfFileProvider comes to
rescue:

.. code-block:: python
    :name: test_building_pdfs_with_graphics_using_pillow

    from faker import Faker
    from faker_file.providers.pdf_file import GraphicPdfFileProvider

    FAKER = Faker() # Initialize Faker
    FAKER.add_provider(GraphicPdfFileProvider)  # Register provider

    file = FAKER.graphic_pdf_file()

The generated file will contain a random graphic (consisting of lines and
shapes of different colours). One of the most useful arguments supported is
``size``.

.. code-block:: python

    file = FAKER.graphic_pdf_file(
        size=(800, 800),
    )
