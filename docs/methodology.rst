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
.. _xvfb: https://en.wikipedia.org/wiki/Xvfb

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
| BMP  | GraphicBmpFileProvider  | BmpFileProvider  | Pillow, WeasyPrint      |
+------+-------------------------+------------------+-------------------------+
| GIF  | GraphicGifFileProvider  | GifFileProvider  | Pillow, WeasyPrint      |
+------+-------------------------+------------------+-------------------------+
| ICO  | GraphicIcoFileProvider  | IcoFileProvider  | Pillow, Imagekit,       |
|      |                         |                  | WeasyPrint              |
+------+-------------------------+------------------+-------------------------+
| JPEG | GraphicJpegFileProvider | JpegFileProvider | Pillow, Imagekit,       |
|      |                         |                  | WeasyPrint              |
+------+-------------------------+------------------+-------------------------+
| PDF  | GraphicPdfFileProvider  | PdfFileProvider  | Pillow, Imagekit,       |
|      |                         |                  | WeasyPrint              |
+------+-------------------------+------------------+-------------------------+
| PNG  | GraphicPngFileProvider  | PngFileProvider  | Pillow, Imagekit,       |
|      |                         |                  | WeasyPrint              |
+------+-------------------------+------------------+-------------------------+
| SVG  | (not supported)         | SvgFileProvider  | Imagekit                |
+------+-------------------------+------------------+-------------------------+
| TIFF | GraphicTiffFileProvider | TiffFileProvider | Pillow, Imagekit*,      |
|      |                         |                  | WeasyPrint              |
+------+-------------------------+------------------+-------------------------+
| WEBP | GraphicWebpFileProvider | WebpFileProvider | Pillow, Imagekit*,      |
|      |                         |                  | WeasyPrint              |
+------+-------------------------+------------------+-------------------------+

.. note::

    Items marked with `*` may require `xvfb`_ to function properly.

At the moment, 2 of the 3 text-to-image providers require additional system
dependencies (such as `wkhtmltopdf`_ for `imgkit`_ and `poppler`_ for
`WeasyPrint`_, both of which are available for most popular operating systems,
including Windows, macOS and Linux).

A few formats, such as BMP, GIF and TIFF, which are not supported
by `imgkit`_ and underlying `wkhtmltopdf`_, rely on `WeasyPrint`_,
`pdf2image`_ and `poppler`_ through the ``WeasyPrintImageGenerator``.

The lightest alternative to `imgkit`_ and `WeasyPrint`_ generators is the
`Pillow`_ generator (``PilImageGenerator``), which is basic, but does not
require additional system dependencies to be installed (most of the
system dependencies for `Pillow`_ are likely already installed on
your system: ``libjpeg``, ``zlib``, ``libtiff``, ``libfreetype6`` and
``libwebp``).

Graphic image providers on the other hand rely on `Pillow`_ and underlying
system dependencies mentioned above.

Take a good look at the `prerequisites`_ to identify required dependencies.

TL;DR

For text-to-image file generation you could use `Pillow`_ based generators,
which are basic, but do not require additional system dependencies. For
advanced text-to-image file generation you could use either `imgkit`_ or
`WeasyPrint`_ based generators, which require `wkhtmltopdf`_ and `poppler`_
respectively.

For graphic file generation, the only option is to use graphic file providers,
which depend on `Pillow` (and underlying system dependencies) only.

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

.. literalinclude:: _static/examples/methodology/create_docx_file_1.py
    :language: python

*See the full example*
:download:`here <_static/examples/methodology/create_docx_file_1.py>`

Create a more structured DOCX file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Imagine, you need a letter sample. It contains

.. literalinclude:: _static/examples/methodology/create_docx_file_2.py
    :language: python
    :lines: 7-

*See the full example*
:download:`here <_static/examples/methodology/create_docx_file_2.py>`

Create even more structured DOCX file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Imagine, you need to generate a highly custom document with types of data,
such as images, tables, manual page breaks, paragraphs, etc.

.. literalinclude:: _static/examples/methodology/create_docx_file_3.py
    :language: python
    :lines: 2-8, 13-

*See the full example*
:download:`here <_static/examples/methodology/create_docx_file_3.py>`

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

.. literalinclude:: _static/examples/methodology/file_from_path_provider.py
    :language: python
    :lines: 3-4, 6, 11-

*See the full example*
:download:`here <_static/examples/methodology/file_from_path_provider.py>`

Now you don't have to copy-paste your file from one place to another.
It will be done for you in a convenient way.

RandomFileFromDirProvider
+++++++++++++++++++++++++
Create a file by copying it randomly from the given directory.

- Create an exact copy of the randomly picked file under a different name.
- Prefix of the destination file would be ``zzz``.
- ``source_dir_path`` is the absolute path to the directory to pick files from.

.. literalinclude:: _static/examples/methodology/rand_file_from_dir_provider.py
    :language: python
    :lines: 3-4, 6, 12-

*See the full example*
:download:`here <_static/examples/methodology/rand_file_from_dir_provider.py>`

Now you don't have to copy-paste your file from one place to another.
It will be done for you in a convenient way.

Clean up files
~~~~~~~~~~~~~~
``FileSystemStorage`` is the default storage and by default files are stored
inside a ``tmp`` directory within the system's temporary directory, which is
commonly cleaned up after system restart. However, there's a mechanism of
cleaning up files after the tests run. At any time, to clean up all files
created by that moment, call ``clean_up`` method of the ``FileRegistry``
class instance, as shown below:

.. literalinclude:: _static/examples/methodology/clean_up_files_1.py
    :language: python

*See the full example*
:download:`here <_static/examples/methodology/clean_up_files_1.py>`

Typically you would call the ``clean_up`` method in the ``tearDown``.

----

To remove a single file, use ``remove`` method of ``FileRegistry`` instance.

.. literalinclude:: _static/examples/methodology/clean_up_files_2.py
    :language: python
    :lines: 11-

*See the full example*
:download:`here <_static/examples/methodology/clean_up_files_2.py>`

----

If you only have a string representation of the ``StringValue``, try to search
for its' correspondent ``StringValue`` instance first using ``search`` method.

.. literalinclude:: _static/examples/methodology/clean_up_files_3.py
    :language: python
    :lines: 11-

*See the full example*
:download:`here <_static/examples/methodology/clean_up_files_3.py>`
