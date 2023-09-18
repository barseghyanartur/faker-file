Creating images
===============
.. External references

.. _imgkit: https://pypi.org/project/imgkit/
.. _Pillow: https://pillow.readthedocs.io/
.. _WeasyPrint: https://pypi.org/project/weasyprint/
.. _wkhtmltopdf: https://wkhtmltopdf.org/

Creating images could be a challenging task. One of the reasons for that might
be need in additional (system) dependencies. There are many image formats to
support. That makes it almost impossible and highly challenging to have
**just one right way** of creating image files.

That's why, creation of image files has been delegated to an abstraction layer
of image generators. If you don't like how image files are generated or format
you need isn't supported, you can create your own layer, using your favourite
library.

Currently, there are two types of image generators implemented:

- Graphic-only image generators
- Mixed-content image generators

The graphic-only image generators are only capable of producing random
graphics.

The mixed-content image generators can generate an image consisting of
both text and graphics. Moreover, text comes in variety of different
headings (such as h1, h2, h3, etc), paragraphs and tables.

And the image generators available to support

- ``PilPdfGenerator``, build on top of the `Pillow`_. It's the generator
  that will likely won't ask for any system dependencies that you don't
  yet have installed.
- ``ImgkitImageGenerator`` (default), built on top of the `imgkit`_
  and `wkhtmltopdf`_.
- ``WeasyPrintImageGenerator``, build on top of the famous `WeasyPrint`_.

Building images with text using `imgkit`_
-----------------------------------------
While `imgkit`_ generator is heavier and has `wkhtmltopdf`_ as a system
dependency, it produces better quality images and has no issues with fonts
or unicode characters.

See the following full functional snippet for generating PDF using `imgkit`_.

.. code-block:: python
    :name: test_building_images_using_imgkit

    # Imports
    from faker import Faker
    from faker_file.providers.png_file import PngFileProvider
    from faker_file.providers.image.imgkit_generator import (
        ImgkitImageGenerator,
    )

    FAKER = Faker() # Initialize Faker
    FAKER.add_provider(PngFileProvider)  # Register PngFileProvider

    # Generate PNG file using `imgkit`
    pdf_file = FAKER.png_file(image_generator_cls=ImgkitImageGenerator)

The generated PNG image will have 10,000 characters of text. The generated image
will be as wide as needed to fit those 10,000 characters, but newlines are
respected.

If you want image to be less wide, set value of ``wrap_chars_after`` to 80
characters (or any other number that fits your needs). See the example below:

.. code-block:: python

    # Generate PDF file, wrapping each line after 80 characters
    png_file = FAKER.png_file(
        image_generator_cls=ImgkitPdfGenerator, wrap_chars_after=80
    )

To have a longer text, increase the value of ``max_nb_chars`` accordingly.
See the example below:

.. code-block:: python

    # Generate PDF file of 20,000 characters
    png_file = FAKER.png_file(
        image_generator_cls=ImgkitPdfGenerator, max_nb_chars=20_000
    )

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables, manual text break and pretty much everything that
is supported by image format specification, although currently only images,
paragraphs and tables are supported out of the box. In order to customise the
blocks image file is built from, the ``DynamicTemplate``
class is used. See the example below for usage examples:

.. code-block:: python

    # Additional imports
    from faker_file.base import DynamicTemplate
    from faker_file.contrib.image.imgkit_snippets import (
        add_paragraph,
        add_picture,
        add_table,
    )

    # Create an image file with a paragraph, a picture and a table. The ``DynamicTemplate`` simply
    # accepts a list of callables (such as ``add_paragraph``,
    # ``add_page_break``) and dictionary to be later on fed to the callables
    # as keyword arguments for customising the default values.
    png_file = FAKER.png_file(
        image_generator_cls=ImgkitPdfGenerator,
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
    png_file = FAKER.png_file(
        image_generator_cls=ImgkitPdfGenerator,
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

Building images with text using `WeasyPrint`_
---------------------------------------------
While `WeasyPrint`_ generator isn't better or faster than the `imgkit`_, it
supports formats that `imgkit`_ doesn't (and vice-versa) and therefore is a
good alternative to.

See the following full functional snippet for generating PDF using `WeasyPrint`_.

.. code-block:: python
    :name: test_building_images_using_weasyprint

    # Imports
    from faker import Faker
    from faker_file.providers.png_file import PngFileProvider
    from faker_file.providers.image.weasyprint_generator import (
        WeasyPrintImageGenerator,
    )

    FAKER = Faker() # Initialize Faker
    FAKER.add_provider(PngFileProvider)  # Register provider

    # Generate image file using `WeasyPrint`
    png_file = FAKER.png_file(image_generator_cls=WeasyPrintImageGenerator)

All examples shown for `imgkit`_ apply for `WeasyPrint`_ generator, however
when building images files from blocks (paragraphs, images and tables), the
imports shall be adjusted:

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables and pretty much everything else that you could
think of, although currently only images, paragraphs and tables are supported.
In order to customise the blocks image file is built from, the
``DynamicTemplate`` class is used. See the example below for usage examples:

.. code-block:: python

    # Additional imports
    from faker_file.base import DynamicTemplate
    from faker_file.contrib.image.weasyprint_snippets import (
        add_paragraph,
        add_picture,
        add_table,
    )

    # Create an image file with paragraph, picture and table.
    # The ``DynamicTemplate`` simply accepts a list of callables (such
    # as ``add_paragraph``, ``add_picture``) and dictionary to be later on
    # fed to the callables as keyword arguments for customising the default
    # values.
    png_file = FAKER.png_file(
        image_generator_cls=WeasyPrintImageGenerator,
        content=DynamicTemplate(
            [
                (add_paragraph, {}),  # Add paragraph
                (add_picture, {}),  # Add picture
                (add_table, {}),  # Add table
            ]
        )
    )

    # You could make the list as long as you like or simply multiply for
    # easier repetition as follows:
    png_file = FAKER.png_file(
        image_generator_cls=WeasyPrintImageGenerator,
        content=DynamicTemplate(
            [
                (add_paragraph, {}),  # Add paragraph
                (add_picture, {}),  # Add picture
                (add_table, {}),  # Add table
            ] * 100
        )
    )

Building PDFs with text using `Pillow`_
---------------------------------------
Usage example:

.. code-block:: python
    :name: test_building_images_using_pillow

    from faker import Faker
    from faker_file.providers.png_file import PngFileProvider
    from faker_file.providers.image.pil_generator import PilImageGenerator

    FAKER = Faker()
    FAKER.add_provider(PngFileProvider)

    png_file = FAKER.png_file(image_generator_cls=PilImageGenerator)

With options:

.. code-block:: python

    png_file = FAKER.png_file(
        image_generator_cls=PilImageGenerator,
        image_generator_kwargs={
            "encoding": "utf8",
            "font_size": 14,
            "page_width": 800,
            "page_height": 1200,
            "line_height": 16,
            "spacing": 5,
        },
        wrap_chars_after=100,
    )

All examples shown for `imgkit`_ and `WeasyPrint`_ apply to `Pillow`_ generator,
however when building image files from blocks (paragraphs, images and tables
breaks), the imports shall be adjusted:

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables and pretty much everything that you could think of,
although currently only images, paragraphs and tables are supported. In order
to customise the blocks image file is built from, the ``DynamicTemplate``
class is used. See the example below for usage examples:

.. code-block:: python

    # Additional imports
    from faker_file.base import DynamicTemplate
    from faker_file.contrib.png_file.pil_snippets import (
        add_paragraph,
        add_picture,
        add_table,
    )

    # Create an image file with paragraph, picture and table.
    # The ``DynamicTemplate`` simply accepts a list of callables (such as
    # ``add_paragraph``, ``add_picture``) and dictionary to be later on fed
    # to the callables as keyword arguments for customising the default
    # values.
    png_file = FAKER.png_file(
        image_generator_cls=PilImageGenerator,
        content=DynamicTemplate(
            [
                (add_paragraph, {}),  # Add paragraph
                (add_picture, {}),  # Add picture
                (add_table, {}),  # Add table
            ]
        )
    )

    # You could make the list as long as you like or simply multiply for
    # easier repetition as follows:
    png_file = FAKER.png_file(
        image_generator_cls=PilImageGenerator,
        content=DynamicTemplate(
            [
                (add_paragraph, {}),  # Add paragraph
                (add_picture, {}),  # Add picture
                (add_table, {}),  # Add table
            ] * 100
        )
    )

Creating images with graphics-only using `Pillow`_
--------------------------------------------------
There are so called ``graphic`` image file providers available. Produced image
files would not contain text, so don't use it when you need text based content.
However, sometimes you just need a valid image file, without caring much about
the content. That's where graphic image providers comes to rescue:

.. code-block:: python
    :name: test_building_images_with_graphics_using_pillow

    from faker import Faker
    from faker_file.providers.png_file import GraphicPngFileProvider

    FAKER = Faker() # Initialize Faker
    FAKER.add_provider(GraphicPngFileProvider)  # Register provider

    png_file = FAKER.graphic_png_file()

The generated file will contain a random graphic (consisting of lines and
shapes of different colours). One of the most useful arguments supported is
``size``.

.. code-block:: python

    png_file = FAKER.graphic_png_file(
        size=(800, 800),
    )
