Testing files like a pro
========================
.. _Faker: https://faker.readthedocs.io/
.. _Lipsum: https://www.lipsum.com/
.. _factory_boy: https://factoryboy.readthedocs.io/
.. _Django: https://www.djangoproject.com/
.. _faker-file: https://faker-file.readthedocs.io/
.. _PyGrunn: https://pygrunn.org/

.. note::

    Talk from the `PyGrunn`_ conference in 2023.

Create files with fake data. In many formats. With no efforts.

Introduction
------------
Thank you for choosing this talk and for being here.

There might be many reasons why you're here. Perhaps you haven't done any
testing in Python that required files, so you're curious. Or maybe you have
done it many times, but never really liked what you did because it was too
verbose or intrusive.

Every time I had to deal with testing files, I had to invent things,
reinvent things, recall things from the past, and each time, before diving into
a rabbit hole of writing many lines of code or producing yet another
collection of files stored somewhere, I checked for available solutions that
could simplify things for me, make it easier, less intrusive, and less work.
I wanted to make it just fine and enjoyable to work with.

As of today, I have found a solution that works well for me, and that's what I
want to share with you.

Why/motivation
--------------

But why, you may ask?

Because test files are often not available when you need them. At least, not
at the right time for testing, because your customer or partner doesn't have
them. And even if they do have the right files, there are dozens of reasons
for never-ending delays, most of which are related to privacy regulations,
such as NDAs to be signed, anonymization, and so on.

And yet, there are deadlines. You have to come up with something, every time.
For every project you work on. For every file format you are expected
to support.

Or maybe you do have a few test files, and you decide to test your
pipeline with the 100 you have (if you're lucky to have that much) and it
all works. Then you go live and discover that your system doesn't perform
well enough to handle thousands of them.

But what are files really? Are they not just pieces of texts and images,
sometimes tables, audios and videos, spreadsheets, presentations -
all mostly originated from text. We can generate text!

Nowadays, we have concepts such as Synthetic Data and libraries like `Faker`_
to support these concepts.

Intermezzo
----------

And if you have never heard of `Faker`_ or the term Synthetic Data, I'll make a
quick recap for you.

Synthetic data, or fake data, is computer-generated data that is similar to
real-world data. It's primary purpose is to increase the privacy and integrity
of systems.

As everything else in life, it has pros, cons and alternatives.

The pros
~~~~~~~~

- **Data privacy**: Because it's fake - there's no risk of exposing sensitive
  user data and no need to comply with data privacy regulations.
- **Scalability**: You can generate as much data as you need.
- **Controll**: You have full control over the data, so you can test specific
  rare edge cases.

The cons
~~~~~~~~

- **Realism**: Because it's fake it does not always accurately represent real
  data or contain the same patterns and anomalies. That could lead to less
  accurate testing.
- **Generation complexity**: Creating realistic data can be complex and
  time-consuming, depending on the domain and the complexity of the data
  structures.
- **Maintenance**: Keeping the data generation logic up-to-date with evolving
  application requirements does take time.

The alternatives
~~~~~~~~~~~~~~~~

- **Production data anonymization**: When you take a copy (or subset) of the
  real production data and anonymize it to remove or obfuscate sensitive
  information.
- **Manual test data creation**: When you manually create test data, usually
  done for smaller scale or more specific testing.
- **Data augmentation**: When you modify existing data to create new data.

All of the alternatives have their pros and cons too, but I'm not going to
cover any of that in this presentation.

`Faker`_ is a Python package for generating synthetic text data.
It's knows many patterns and locales. It can generate names, texts, addresses,
zip codes, ISBN numbers and a lot more.

I started to use `Faker`_ around 2016. It was such a relief! You could just
do things like this:

.. code-block:: python

    from faker import Faker
    FAKER = Faker()
    FAKER.first_name()
    FAKER.last_name()
    FAKER.address()
    FAKER.zip_code()
    FAKER.text()
    FAKER.isbn13()
    FAKER.email()
    FAKER.company_email()
    FAKER.company()
    FAKER.date_between(start_date="-30y", end_date="+30y")

Before `Faker`_ there was `Lorem Ipsum` (or `Lipsum`_), which was OK (or better
than nothing), but didn't make much sense.

Then `Faker`_ (and `Faker`-like libraries for creating fake data) emerged to
save us.

Then test cases became more complex. Primary data sources were often
files. We needed to test data/ETL pipelines. `Faker`_ still helped a lot, but
it was inconvenient to replicate your previous best approach for files and
reinvent the wheel for each new project.

That's why `faker-file`_ was created. I wrote it mainly for myself, but
you may find it useful too.

How does `faker-file`_ help to solve that problem?
--------------------------------------------------

In essence, `faker-file`_ is just a set of providers for the
famous `Faker`_ library.

- You can use it with `Faker`_ and `factory_boy`_ (for ORM integration).
- It works with `Django`_.
- It supports remote storages (AWS S3, Google Cloud Storage, Azure Cloud
  Storage).
- You are in control of the generated content. By default, for most basic
  cases, content it's generated using `Faker`_'s ``text`` method, but you
  could easily tweak that using the ``content`` argument.

You can use it to run a comprehensive integration test of your pipeline in your
favorite cloud.

Some of the most commonly-used file formats are supported:

- `BIN`
- `CSV`
- `DOCX`
- `EML`
- `EPUB`
- `ICO`
- `JPEG`
- `MP3`
- `ODP`
- `ODS`
- `ODT`
- `PDF`
- `PNG`
- `RTF`
- `PPTX`
- `SVG`
- `TXT`
- `WEBP`
- `XLSX`
- `XML`
- `ZIP`

**Installation**

.. code-block:: sh

    pip install faker-file[common]

Using it is as simple as follows.

Generate a `DOCX` file with fake content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Generate 1 `DOCX` file with fake content (generated by `Faker`_).

.. code-block:: python

    # Import the Faker class from faker package
    from faker import Faker

    # Import the file provider we want to use
    from faker_file.providers.docx_file import DocxFileProvider

    FAKER = Faker()  # Initialise Faker instance

    FAKER.add_provider(DocxFileProvider)  # Register the DOCX file provider

    file = FAKER.docx_file()  # Generate a DOCX file

    # Note, that `file` is this case is an instance of either `StringValue`
    # or `BytesValue` objects, which inherit from `str` and `bytes`
    # respectively, but add meta data. Meta data is stored inside the `data`
    # property (`Dict`). One of the common attributes of which (among all
    # file providers) is the `filename`, which holds an absolute path to the
    # generated file.
    print(file.data["filename"])

    # Another common attribute (although it's not available for all providers)
    # is `content`, which holds the text used to generate the file with.
    print(file.data["content"])

Provide content manually
~~~~~~~~~~~~~~~~~~~~~~~~
- Generate 1 `DOCX` file with developer defined content.

.. code-block:: python

    # The text we want have in our generated DOCX file
    TEXT = """
    "The Queen of Hearts, she made some tarts,
        All on a summer day:
    The Knave of Hearts, he stole those tarts,
        And took them quite away."
    """

    # Generate a DOCX file with the given text
    file = FAKER.docx_file(content=TEXT)

- Similarly, generate 1 `PNG` file.

.. code-block:: python

    from faker_file.providers.png_file import PngFileProvider

    FAKER.add_provider(PngFileProvider)

    file = FAKER.png_file()

- Similarly, generate 1 `PDF` file. Limit the line width to 80 characters.

.. code-block:: python

    from faker_file.providers.pdf_file import PdfFileProvider

    FAKER.add_provider(PdfFileProvider)

    file = FAKER.pdf_file(wrap_chars_after=80)

Provide templated content
~~~~~~~~~~~~~~~~~~~~~~~~~
You can generate documents from pre-defined templates.

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

    file = FAKER.pdf_file(content=TEMPLATE, wrap_chars_after=80)

Archive types
~~~~~~~~~~~~~
ZIP archive containing 5 TXT files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As you might have noticed, some archive types are also supported.
The created archive will contain 5 files in TXT format (defaults).

.. code-block:: python

    from faker_file.providers.zip_file import ZipFileProvider

    FAKER.add_provider(ZipFileProvider)

    file = FAKER.zip_file()

ZIP archive containing 3 DOCX files with text generated from a template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    from faker_file.providers.helpers.inner import create_inner_docx_file

    file = FAKER.zip_file(
        prefix="zzz",
        options={
            "count": 3,
            "create_inner_file_func": create_inner_docx_file,
            "create_inner_file_args": {
                "prefix": "xxx_",
                "content": TEMPLATE,
            },
            "directory": "yyy",
        }
    )

Nested ZIP archive
^^^^^^^^^^^^^^^^^^
And of course nested archives are supported too. Create a `ZIP` file which
contains 5 `ZIP` files which contain 5 `ZIP` files which contain 2 `DOCX`
files.

- 5 `ZIP` files in the `ZIP` archive.
- Content is generated dynamically.
- Prefix the filenames in archive with ``nested_level_1_``.
- Prefix the filename of the archive itself with ``nested_level_0_``.
- Each of the `ZIP` files inside the `ZIP` file in their turn contains 5 other
  `ZIP` files, prefixed with ``nested_level_2_``, which in their turn contain
  2 `DOCX` files.

.. code-block:: python

    from faker_file.providers.helpers.inner import create_inner_zip_file

    file = FAKER.zip_file(
        prefix="nested_level_0_",
        options={
            "create_inner_file_func": create_inner_zip_file,
            "create_inner_file_args": {
                "prefix": "nested_level_1_",
                "options": {
                    "create_inner_file_func": create_inner_zip_file,
                    "create_inner_file_args": {
                        "prefix": "nested_level_2_",
                        "options": {
                            "count": 2,
                            "create_inner_file_func": create_inner_docx_file,
                            "create_inner_file_args": {
                                "content": TEXT + "\n\n{{date}}",
                            }
                        }
                    },
                }
            },
        }
    )

It works similarly for `EML` files (using ``EmlFileProvider``).

.. code-block:: python

    from faker_file.providers.eml_file import EmlFileProvider
    from faker_file.providers.helpers.inner import create_inner_docx_file

    FAKER.add_provider(EmlFileProvider)

    file = FAKER.eml_file(
        prefix="zzz",
        content=TEMPLATE,
        options={
            "count": 3,
            "create_inner_file_func": create_inner_docx_file,
            "create_inner_file_args": {
                "prefix": "xxx_",
                "content": TEXT + "\n\n{{date}}",
            },
        }
    )

Create a ZIP file with variety of different file types within
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- 50 files in the ZIP archive (limited to DOCX, EPUB and TXT types).
- Content is generated dynamically.
- Prefix the filename of the archive itself with `zzz_archive_`.
- Inside the ZIP, put all files in directory zzz.

.. code-block:: python

  from faker import Faker
  from faker_file.providers.helpers.inner import (
      create_inner_docx_file,
      create_inner_epub_file,
      create_inner_txt_file,
      fuzzy_choice_create_inner_file,
  )
  from faker_file.providers.zip_file import ZipFileProvider
  from faker_file.storages.filesystem import FileSystemStorage

  FAKER = Faker()
  STORAGE = FileSystemStorage()

  kwargs = {"storage": STORAGE, "generator": FAKER}
  file = ZipFileProvider(FAKER).zip_file(
      prefix="zzz_archive_",
      options={
          "count": 50,
          "create_inner_file_func": fuzzy_choice_create_inner_file,
          "create_inner_file_args": {
              "func_choices": [
                  (create_inner_docx_file, kwargs),
                  (create_inner_epub_file, kwargs),
                  (create_inner_txt_file, kwargs),
              ],
          },
          "directory": "zzz",
      }
  )

Another way to create a ZIP file with variety of different file types within
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- 3 files in the ZIP archive (1 DOCX, and 2 XML types).
- Content is generated dynamically.
- Filename of the archive itself is `alice-looking-through-the-glass.zip`.
- Files inside the archive have fixed name (passed with basename argument).

.. code-block:: python

  from faker import Faker
  from faker_file.providers.helpers.inner import (
      create_inner_docx_file,
      create_inner_xml_file,
      list_create_inner_file,
  )
  from faker_file.providers.zip_file import ZipFileProvider
  from faker_file.storages.filesystem import FileSystemStorage

  FAKER = Faker()
  STORAGE = FileSystemStorage()

  kwargs = {"storage": STORAGE, "generator": FAKER}
  file = ZipFileProvider(FAKER).zip_file(
      basename="alice-looking-through-the-glass",
      options={
          "create_inner_file_func": list_create_inner_file,
          "create_inner_file_args": {
              "func_list": [
                  (create_inner_docx_file, {"basename": "doc"}),
                  (create_inner_xml_file, {"basename": "doc_metadata"}),
                  (create_inner_xml_file, {"basename": "doc_isbn"}),
              ],
          },
      }
  )

Using raw=True features in tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you pass ``raw=True`` argument to any provider or inner function, instead
of creating a file, you will get bytes back (or to be totally correct,
bytes-like object ``BytesValue``, which is basically bytes enriched with
meta-data). You could then use the bytes content of the file to build a test
payload as shown in the example test below:

.. code-block:: python

  import os
  from io import BytesIO

  from django.test import TestCase
  from django.urls import reverse
  from faker import Faker
  from faker_file.providers.docx_file import DocxFileProvider
  from rest_framework.status import HTTP_201_CREATED
  from upload.models import Upload

  FAKER = Faker()
  FAKER.add_provider(DocxFileProvider)

  class UploadTestCase(TestCase):
      """Upload test case."""

      def test_create_docx_upload(self) -> None:
          """Test create an Upload."""
          url = reverse("api:upload-list")

          raw = FAKER.docx_file(raw=True)
          test_file = BytesIO(raw)
          test_file.name = os.path.basename(raw.data["filename"])

          payload = {
              "name": FAKER.word(),
              "description": FAKER.paragraph(),
              "file": test_file,
          }

          response = self.client.post(url, payload, format="json")

          # Test if request is handled properly (HTTP 201)
          self.assertEqual(response.status_code, HTTP_201_CREATED)

          test_upload = Upload.objects.get(id=response.data["id"])

          # Test if the name is properly recorded
          self.assertEqual(str(test_upload.name), payload["name"])

          # Test if file name recorded properly
          self.assertEqual(str(test_upload.file.name), test_file.name)

Create a HTML file predefined template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you want to generate a file in a format that is not (yet) supported, you
can try to use ``GenericFileProvider``. In the following example, an HTML file
is generated from a template.

.. code-block:: python

  from faker import Faker
  from faker_file.providers.generic_file import GenericFileProvider

  file = GenericFileProvider(Faker()).generic_file(
      content="<html><body><p>{{text}}</p></body></html>",
      extension="html",
  )

Storages
~~~~~~~~

Example usage with `Django` (using local file system storage)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from django.conf import settings
    from faker_file.providers.txt_file import TxtFileProvider
    from faker_file.storages.filesystem import FileSystemStorage

    STORAGE = FileSystemStorage(
        root_path=settings.MEDIA_ROOT,
        rel_path="tmp",
    )

    FAKER.add_provider(TxtFileProvider)

    file = FAKER.txt_file(content=TEXT, storage=STORAGE)

Example usage with AWS S3 storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    from faker_file.storages.aws_s3 import AWSS3Storage

    S3_STORAGE = AWSS3Storage(
        bucket_name="test-bucket",
        root_path="tmp",  # Optional
        rel_path="sub-tmp",  # Optional
        # Credentials are optional too. If your AWS credentials are properly
        # set in the ~/.aws/credentials, you don't need to send them
        # explicitly.
        # credentials={
        #     "key_id": "YOUR KEY ID",
        #     "key_secret": "YOUR KEY SECRET"
        # },
    )

    file = FAKER.txt_file(storage=S3_STORAGE)

Augment existing files
~~~~~~~~~~~~~~~~~~~~~~
If you think `Faker`_ generated data doesn't make sense for you and you want
your files to look like a collection of 100 files you already have, you could
use augmentation features.

You will need additional requirements:

.. code-block:: sh

    pip install faker-file[ml]

Usage example:

.. code-block:: python

    from faker_file.providers.augment_file_from_dir import (
        AugmentFileFromDirProvider,
    )

    FAKER.add_provider(AugmentFileFromDirProvider)

    file = FAKER.augment_file_from_dir(
        source_dir_path="/home/me/Documents/faker_file_source/",
        wrap_chars_after=120,
    )

Generated file will resemble text of the original document, but
will not be the same.

CLI
~~~
Even if you're not using automated testing, but still want to quickly
generate a file with fake content, you could use faker-file:

.. code-block:: sh

  faker-file generate-completion
  source ~/faker_file_completion.sh

Generate an MP3 file:

.. code-block:: sh

  faker-file mp3_file --prefix=my_file_

Generate 10 DOCX files:

.. code-block:: sh

  faker-file docx_file --nb_files 10 --prefix=my_file_

Without `faker-file`_
---------------------
There are alternatives.

You could simply store a collection of test files somewhere. If you do so, make
sure you "know" your collection. It should be obvious of how to use it. In
other words - document it properly, alongside snippets to make most of it.

Then there comes a natural question - where to store? Should it be centrally
hosted or per repository?

An obvious drawback of centrally hosted approach is that modifications become
critical. A mistake may cause failure of your CI/CD pipeline. Also, you need to
take care of the setup (for both CI/CD and development).

On the other hand, if you do it per project/repository basis, or even using a
blue-print repository, you miss these direct contributions to the upstream.

BTW, consider storing your test files in GitLFS.

Besides, adding test files to the repository still feels a little bit strange
to me. There's always a case when you need to have a variation and therefore
you need to make another copy, sometimes a very long copy. And oh, refactoring
and cleaning up becomes almost unmanageable.

Additionally, you could always go for a mixed approach, when some of the
essentially needed files you still do store in the repository (and that can
be project specific), while you still make use of the synthetic data for the
cases when it's justified.

Recap/conclusion
----------------
- Most likely, combination of `Faker`_, `factory_boy`_ and `faker-file`_ will
  do just fine for your MVP and even way beyond that (you have all in one:
  synthetic data + dynamic fixtures + generation of files).
  This approach also saves you from thinking about where to store your test
  data, and overall, makes your code more manageable and simplifies the
  development process.
- If you need to test files in your project, think upfront about the details,
  such as amount of test files you will need, where to store them, how to store
  them, etc.
- If some of your test cases are too specific to replicate with `faker-file`_,
  consider using hybrid approach.
