Methodology
===========
.. Internal references

.. _faker-file: https://github.com/barseghyanartur/faker-file/
.. _prerequisites: https://faker-file.readthedocs.io/en/latest/?badge=latest#prerequisites

.. External references

.. _Pillow: https://pillow.readthedocs.io/
.. _WeasyPrint: https://pypi.org/project/weasyprint/
.. _imgkit: https://pypi.org/project/imgkit/
.. _pdf2image: https://pypi.org/project/pdf2image/
.. _pip-tools: https://pip-tools.readthedocs.io
.. _poppler: https://poppler.freedesktop.org/
.. _wkhtmltopdf: https://wkhtmltopdf.org/

But why
-------
Let's start with some hypothetical questions.

"But why generate testing files dynamically", - you may ask?

And the answer would be, - "for a number of reasons":

Because you do need files and managing test files is a pain nobody wants to
have. You create testing files for one use case, then you need to support
another, but you need to modify the original files or make modifications
there. You either duplicate or make changes, then at some point, after a
number of iterations, your test files collection grows so big, you can't
easily find out how some of the test files different one from another or
your test fail, you spend some time to investigate and find out that there
has been a slight modification of one of the files, which made your pipeline
to fail. You fix the error and decide to document your collection (a good
thing anyway). But then your collection grows even more. The burden of
managing both test files, the documentation of the test files and the
test code becomes unbearable.

Now imagine doing it not for one, but for a number of projects. You want
to be smart and make a collection of files, document it properly and think
you've done a good job, but then you start to realise that you do need to
deviate or add new files to the collection to support new use cases. You
want to be safe and decide to version control it. Your collection grows,
you start ot accept PRs from other devs and go down the rabbit whole of
owning another critical repository. Your documentation grows and so does
the repository size (mostly binary content). Storing such a huge amount of
files becomes a burden. It slows down everyone.

Not even talking about, that you might not be allowed to store some of the
you're using for testing centrally, because you would then need to run
obfuscation, anonymization to legally address concerns of privacy regulations.

When test files are generated dynamically
-----------------------------------------
When test files are generated dynamically, you are relieved from most of the
concerns mentioned above. There are a couple of drawbacks here too, such as
tests execution time (because generating of the test files on the fly does
require some computation resources and therefore - your CI execution time will
grow).

Best practices
--------------
In some very specific use-cases, mimicking original files might be too
difficult and you might want to still consider including some of the very
specific and hard-to-recreate files in the project repository, but on much
lower scale. Use `faker-file`_ for simple use cases and only use custom
files when things get too complicated otherwise. The so-called hybrid
approach.

Identify what kind of files do you need
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`faker-file`_ supports a large variety of file types, but content of files
can be generally broken down by 2 categories:

- Text based: Useful when testing OCR or text processing pipelines. ATM, most
  of the `faker-file`_ providers generate text-based content.
- Non-text based: Typically images and non-human readable formats such as BIN.
  Useful when you need to test validity of the uploaded file, but don't care
  much about what's inside.

Image providers:

+------+-------------------------+------------------+-------------------------+
| File | Graphic                 | Text             | Generator               |
| type |                         |                  |                         |
+======+=========================+==================+=========================+
| BMP  | GraphicBmpFileProvider  | BmpFileProvider  | WeasyPrint              |
+------+-------------------------+------------------+-------------------------+
| GIF  | GraphicGifFileProvider  | GifFileProvider  | WeasyPrint              |
+------+-------------------------+------------------+-------------------------+
| ICO  | GraphicIcoFileProvider  | IcoFileProvider  | Imagekit, WeasyPrint    |
+------+-------------------------+------------------+-------------------------+
| JPEG | GraphicJpegFileProvider | JpegFileProvider | Imagekit, WeasyPrint    |
+------+-------------------------+------------------+-------------------------+
| PDF  | GraphicPdfFileProvider  | PdfFileProvider  | Imagekit, WeasyPrint    |
+------+-------------------------+------------------+-------------------------+
| PNG  | GraphicPngFileProvider  | PngFileProvider  | Imagekit, WeasyPrint    |
+------+-------------------------+------------------+-------------------------+
| SVG  | (not supported)         | SvgFileProvider  | Imagekit, WeasyPrint    |
+------+-------------------------+------------------+-------------------------+
| TIFF | GraphicTiffFileProvider | TiffFileProvider | WeasyPrint              |
+------+-------------------------+------------------+-------------------------+
| WEBP | GraphicWebpFileProvider | WebpFileProvider | Imagekit, WeasyPrint    |
+------+-------------------------+------------------+-------------------------+

At the moment, most of the text-to-image providers rely on the `imgkit`_
Python package and `wkhtmltopdf`_ system dependency (available for most
popular operating systems, including Windows, macOS and Linux).

However, a few formats, such as BMP, GIF and TIFF, which are not supported
by `imgkit`_ and underlying `wkhtmltopdf`_, rely on `WeasyPrint`_,
`pdf2image`_ and `poppler`_ through an alternative
``WeasyPrintImageGenerator``.

Graphic image providers on the other hand rely on Pillow and underlying
system dependencies such as ``libjpeg``, ``zlib``, ``libtiff``,
``libfreetype6`` and ``libwebp``.

Take a good look at the `prerequisites`_ to identify required dependencies.

Installation
~~~~~~~~~~~~
When using `faker-file`_ for automated tests in a large project with a lot of
dependencies, the recommended way to install it is to carefully pick the
dependencies required and further use requirements management package,
like `pip-tools`_, to compile them into hashed set of packages working well
together.

For instance, if we only need DOCX and PDF support, your ``requirements.in``
file could look as follows:

.. code-block:: text

    faker
    faker-file
    python-docx
    reportlab

If you only plan to use `faker-file`_ as a CLI application, just install all
common dependencies as follows:

.. code-block:: sh

    pipx install "faker-file[common]"

Creating files
~~~~~~~~~~~~~~
A couple of use-cases when `faker-file`_ can help you out:

Create a simple DOCX file
^^^^^^^^^^^^^^^^^^^^^^^^^
Let's imagine we need to generate a DOCX file with text 50 chars long (just
for observability).

.. code-block:: python
    :name: test_crate_a_simple_docx_file

    from faker import Faker
    from faker_file.providers.docx_file import DocxFileProvider

    FAKER = Faker()
    FAKER.add_provider(DocxFileProvider)

    file = FAKER.docx_file(max_nb_chars=50)
    print(file)  # Sample value: 'tmp/tmpgdctmfbp.docx'
    print(file.data["content"])  # Sample value: 'Learn where receive social.'
    print(file.data["filename"])  # Sample value: '/tmp/tmp/tmpgdctmfbp.docx'

Create a more structured DOCX file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Imagine, you need a letter sample. It contains

.. code-block:: python

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

    file = FAKER.docx_file(content=TEMPLATE)

    print(file)  # Sample value: 'tmp/tmpgdctmfbp.docx'
    print(file.data["content"])
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

Create even more structured DOCX file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Imagine, you need to generate a highly custom document with types of data,
such as images, tables, manual page breaks, paragraphs, etc.

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
    file = FAKER.docx_file(
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

.. note::

    All callables do accept arguments. You could provide ``content=TEMPLATE``
    argument to the ``add_paragraph`` function and instead of just random text,
    you would get a more structured paragraph (from one of previous examples).

For when you think `faker-file`_ isn't enough
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As previously mentioned, sometimes when test documents are too complex it
might be hard to replicate them and you want to store just a few very specific
documents in the project repository.

`faker-file`_ comes up with a couple of providers that might still help you
in that case.

Both `FileFromPathProvider`_ and `RandomFileFromDirProvider`_ are created to
support the hybrid approach.

FileFromPathProvider
++++++++++++++++++++
Create a file by copying it from the given path.

- Create an exact copy of a file under a different name.
- Prefix of the destination file would be ``zzz``.
- ``path`` is the absolute path to the file to copy.

.. code-block:: python

    from faker import Faker
    from faker_file.providers.file_from_path import FileFromPathProvider

    FAKER = Faker()
    FAKER.add_provider(FileFromPathProvider)

    file = FAKER.file_from_path(
        path="/path/to/file.docx",
        prefix="zzz",
    )

Now you don't have to copy-paste your file from one place to another.
It will be done for you in a convenient way.

RandomFileFromDirProvider
+++++++++++++++++++++++++
Create a file by copying it randomly from the given directory.

- Create an exact copy of the randomly picked file under a different name.
- Prefix of the destination file would be ``zzz``.
- ``source_dir_path`` is the absolute path to the directory to pick files from.

.. code-block:: python
    :name: test_random_file_from_dir_provider

    from faker import Faker
    from faker_file.providers.random_file_from_dir import (
        RandomFileFromDirProvider,
    )

    FAKER = Faker()
    FAKER.add_provider(RandomFileFromDirProvider)

    file = FAKER.random_file_from_dir(
        source_dir_path="/tmp/tmp/",
        prefix="zzz",
    )

Now you don't have to copy-paste your file from one place to another.
It will be done for you in a convenient way.
