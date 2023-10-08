Recipes
=======
When using with ``Faker``
-------------------------
When using with ``Faker``, there are two ways of using the providers.

Imports and initializations
~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Recommended way**

.. literalinclude:: _static/examples/recipes/imports_and_init_1.py
    :language: python

*See the full example*
:download:`here <_static/examples/recipes/imports_and_init_1.py>`

**But this works too**

.. literalinclude:: _static/examples/recipes/imports_and_init_2.py
    :language: python

*See the full example*
:download:`here <_static/examples/recipes/imports_and_init_2.py>`

Throughout documentation we will be mixing these approaches.

Create a TXT file with static content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Content of the file is ``Lorem ipsum``.

.. literalinclude:: _static/examples/recipes/txt_file_1.py
    :language: python
    :lines: 7-

*See the full example*
:download:`here <_static/examples/recipes/txt_file_1.py>`

Create a DOCX file with dynamically generated content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Content is generated dynamically.
- Content is limited to 1024 chars.
- Wrap lines after 80 chars.
- Prefix the filename with ``zzz``.

.. literalinclude:: _static/examples/recipes/docx_file_1.py
    :language: python
    :lines: 7-

*See the full example*
:download:`here <_static/examples/recipes/docx_file_1.py>`

Create a ZIP file consisting of TXT files with static content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 5 TXT files in the ZIP archive (default value is 5).
- Content of all files is ``Lorem ipsum``.

.. literalinclude:: _static/examples/recipes/zip_file_1.py
    :language: python
    :lines: 7-

*See the full example*
:download:`here <_static/examples/recipes/zip_file_1.py>`

Create a ZIP file consisting of 3 DOCX files with dynamically generated content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 3 DOCX files in the ZIP archive.
- Content is generated dynamically.
- Content is limited to 1024 chars.
- Prefix the filenames in archive with ``xxx_``.
- Prefix the filename of the archive itself with ``zzz``.
- Inside the ZIP, put all files in directory ``yyy``.

.. literalinclude:: _static/examples/recipes/zip_file_2.py
    :language: python
    :lines: 2, 7-

*See the full example*
:download:`here <_static/examples/recipes/zip_file_2.py>`

Create a ZIP file of 9 DOCX files with content generated from template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 9 DOCX files in the ZIP archive.
- Content is generated dynamically from given template.

.. literalinclude:: _static/examples/recipes/zip_file_3.py
    :language: python
    :lines: 2, 7-

*See the full example*
:download:`here <_static/examples/recipes/zip_file_3.py>`

Create a nested ZIP file
~~~~~~~~~~~~~~~~~~~~~~~~
Create a ZIP file which contains 5 ZIP files which contain 5 ZIP files which
contain 5 DOCX files.

- 5 ZIP files in the ZIP archive.
- Content is generated dynamically.
- Prefix the filenames in archive with ``nested_level_1_``.
- Prefix the filename of the archive itself with ``nested_level_0_``.
- Each of the ZIP files inside the ZIP file in their turn contains 5 other ZIP
  files, prefixed with ``nested_level_2_``, which in their turn contain 5
  DOCX files.

.. literalinclude:: _static/examples/recipes/zip_file_4.py
    :language: python
    :lines: 2-5, 10-

*See the full example*
:download:`here <_static/examples/recipes/zip_file_4.py>`

Create a ZIP file with variety of different file types within
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 50 files in the ZIP archive (limited to DOCX, EPUB and TXT types).
- Content is generated dynamically.
- Prefix the filename of the archive itself with ``zzz_archive_``.
- Inside the ZIP, put all files in directory ``zzz``.

.. literalinclude:: _static/examples/recipes/zip_file_5.py
    :language: python
    :lines: 2-7, 9-10, 14-

*See the full example*
:download:`here <_static/examples/recipes/zip_file_5.py>`

Another way to create a ZIP file with variety of different file types within
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 3 files in the ZIP archive (1 DOCX, and 2 XML types).
- Content is generated dynamically.
- Filename of the archive itself is ``alice-looking-through-the-glass.zip``.
- Files inside the archive have fixed name (passed with ``basename`` argument).

.. literalinclude:: _static/examples/recipes/zip_file_6.py
    :language: python
    :lines: 2-6, 11-

*See the full example*
:download:`here <_static/examples/recipes/zip_file_6.py>`

Note, that ``count`` argument (not shown in the example, but commonly
accepted by inner functions) will be simply ignored here.

Create an EML file consisting of TXT files with static content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 5 TXT files in the EML email (default value is 5).
- Content of all files is ``Lorem ipsum``.

.. literalinclude:: _static/examples/recipes/eml_file_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/eml_file_1.py>`

Create a EML file consisting of 3 DOCX files with dynamically generated content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 3 DOCX files in the EML email.
- Content is generated dynamically.
- Content is limited to 1024 chars.
- Prefix the filenames in email with ``xxx_``.
- Prefix the filename of the email itself with ``zzz``.

.. literalinclude:: _static/examples/recipes/eml_file_2.py
    :language: python
    :lines: 3, 7-

*See the full example*
:download:`here <_static/examples/recipes/eml_file_2.py>`

Create a nested EML file
~~~~~~~~~~~~~~~~~~~~~~~~
Create a EML file which contains 5 EML files which contain 5 EML files which
contain 5 DOCX files.

- 5 EML files in the EML file.
- Content is generated dynamically.
- Prefix the filenames in EML email with ``nested_level_1_``.
- Prefix the filename of the EML email itself with ``nested_level_0_``.
- Each of the EML files inside the EML file in their turn contains 5 other EML
  files, prefixed with ``nested_level_2_``, which in their turn contain 5
  DOCX files.

.. literalinclude:: _static/examples/recipes/eml_file_3.py
    :language: python
    :lines: 3-6, 10-

*See the full example*
:download:`here <_static/examples/recipes/eml_file_3.py>`

Create an EML file with variety of different file types within
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 10 files in the EML file (limited to DOCX, EPUB and TXT types).
- Content is generated dynamically.
- Prefix the filename of the EML itself with ``zzz``.

.. literalinclude:: _static/examples/recipes/eml_file_4.py
    :language: python
    :lines: 3-8, 17-

*See the full example*
:download:`here <_static/examples/recipes/eml_file_4.py>`

Create a PDF file with predefined template containing dynamic fixtures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Content template is predefined and contains dynamic fixtures.
- Wrap lines after 80 chars.

.. literalinclude:: _static/examples/recipes/pdf_file_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/pdf_file_1.py>`

Create a DOCX file with table and image using ``DynamicTemplate``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When pre-defined templating and dynamic fixtures are not enough and
full control is needed, you can use ``DynamicTemplate`` wrapper.
It takes a list of content modifiers
(tuples): ``(func: Callable, kwargs: dict)``. Each callable should accept
the following arguments:

- `provider`: Faker ``Generator`` instance or ``Faker`` instance.
- `document`: Document instance. Implementation specific.
- `data`: Dictionary. Used primarily for observability.
- `counter`: Integer. Index number of the content modifier.
- `**kwargs`: Dictionary. Useful to pass implementation-specific arguments.

The following example shows how to generate a DOCX file with paragraph, table
and image.

.. literalinclude:: _static/examples/recipes/docx_file_mixed_1.py
    :language: python
    :lines: 2-8, 13-

*See the full example*
:download:`here <_static/examples/recipes/docx_file_mixed_1.py>`

Create a ODT file with table and image using ``DynamicTemplate``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Similarly to previous section, the following example shows how to generate an
ODT file with table and image.

.. literalinclude:: _static/examples/recipes/odt_file_mixed_1.py
    :language: python
    :lines: 3-10, 12-

*See the full example*
:download:`here <_static/examples/recipes/odt_file_mixed_1.py>`

Create a PDF using `reportlab` generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. literalinclude:: _static/examples/recipes/pdf_file_reportlab_1.py
    :language: python
    :lines: 3-5, 9-

*See the full example*
:download:`here <_static/examples/recipes/pdf_file_reportlab_1.py>`

Create a PDF using `pdfkit` generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Note, that at the moment, ``pdfkit`` is the default generator. However,
you could set it explicitly as follows:

.. literalinclude:: _static/examples/recipes/pdf_file_pdfkit_1.py
    :language: python
    :lines: 3-5, 9-

*See the full example*
:download:`here <_static/examples/recipes/pdf_file_pdfkit_1.py>`

Create a graphic PDF file using `Pillow`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Graphic PDF file does not contain text. Don't use it when you need text based
content. However, sometimes you just need a valid file in PDF format, without
caring much about the content. That's where a GraphicPdfFileProvider comes to
rescue:

.. literalinclude:: _static/examples/recipes/pdf_file_pillow_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/pdf_file_pillow_1.py>`

The generated file will contain a random graphic (consisting of lines and
shapes of different colours). One of the most useful arguments supported is
``size``.

.. literalinclude:: _static/examples/recipes/pdf_file_pillow_2.py
    :language: python
    :lines: 7-

*See the full example*
:download:`here <_static/examples/recipes/pdf_file_pillow_2.py>`

Graphic providers
~~~~~~~~~~~~~~~~~
Graphic file providers does not contain text. Don't use it when you need text
based content. However, sometimes you just need a valid image file with
graphics of a certain size. That's where graphic file providers help.

Supported files formats are: `BMP`, `GIF`, `ICO`, `JPEG`, `PDF`, `PNG`, `SVG`
`TIFF` and `WEBP`.

Create an ICO file
^^^^^^^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/graphic_ico_file_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/graphic_ico_file_1.py>`

Create a JPEG file
^^^^^^^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/graphic_jpeg_file_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/graphic_jpeg_file_1.py>`

Create a PNG file
^^^^^^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/graphic_png_file_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/graphic_png_file_1.py>`

Create a WEBP file
^^^^^^^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/graphic_webp_file_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/graphic_webp_file_1.py>`

Create a MP3 file
~~~~~~~~~~~~~~~~~
.. literalinclude:: _static/examples/recipes/mp3_file_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/mp3_file_1.py>`

Create a MP3 file by explicitly specifying MP3 generator class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Google Text-to-Speech
^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/mp3_file_gtts_1.py
    :language: python
    :lines: 3-5, 9-

*See the full example*
:download:`here <_static/examples/recipes/mp3_file_gtts_1.py>`

----

You can tune arguments too:

.. literalinclude:: _static/examples/recipes/mp3_file_gtts_2.py
    :language: python
    :lines: 10-

*See the full example*
:download:`here <_static/examples/recipes/mp3_file_gtts_2.py>`

Refer to https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang
for list of accepted values for ``lang`` argument.

Refer to https://gtts.readthedocs.io/en/latest/module.html#localized-accents
for list of accepted values for ``tld`` argument.

Microsoft Edge Text-to-Speech
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/mp3_file_edge_tts_1.py
    :language: python
    :lines: 3-5, 9-

*See the full example*
:download:`here <_static/examples/recipes/mp3_file_edge_tts_1.py>`

----

You can tune arguments too:

.. literalinclude:: _static/examples/recipes/mp3_file_edge_tts_2.py
    :language: python
    :lines: 10-

*See the full example*
:download:`here <_static/examples/recipes/mp3_file_edge_tts_2.py>`

Run ``edge-tts -l`` from terminal for list of available voices.

Create a MP3 file with custom MP3 generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Default MP3 generator class is ``GttsMp3Generator`` which uses Google
Text-to-Speech services to generate an MP3 file from given or
randomly generated text. It does not require additional services to
run and the only dependency here is the ``gtts`` package. You can
however implement your own custom MP3 generator class and pass it to
te ``mp3_file`` method in ``mp3_generator_cls`` argument instead of the
default ``GttsMp3Generator``. Read about quotas of Google Text-to-Speech
services `here <https://cloud.google.com/text-to-speech/quotas>`_.

Usage with custom MP3 generator class.

.. literalinclude:: _static/examples/recipes/mp3_file_custom_1.py
    :language: python
    :lines: 2, 4, 9-

*See the full example*
:download:`here <_static/examples/recipes/mp3_file_custom_1.py>`

See exact implementation of
`marytts_mp3_generator <https://github.com/barseghyanartur/faker-file/tree/main/examples/customizations/marytts_mp3_generator>`_
in the examples.

Pick a random file from a directory given
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Create an exact copy of the randomly picked file under a different name.
- Prefix of the destination file would be ``zzz``.
- ``source_dir_path`` is the absolute path to the directory to pick files from.

.. literalinclude:: _static/examples/recipes/random_file_from_dir_1.py
    :language: python
    :lines: 2, 4, 7, 12-

*See the full example*
:download:`here <_static/examples/recipes/random_file_from_dir_1.py>`

File from path given
~~~~~~~~~~~~~~~~~~~~
- Create an exact copy of a file under a different name.
- Prefix of the destination file would be ``zzz``.
- ``path`` is the absolute path to the file to copy.

.. literalinclude:: _static/examples/recipes/file_from_path_1.py
    :language: python
    :lines: 3-4, 7, 11-

*See the full example*
:download:`here <_static/examples/recipes/file_from_path_1.py>`

Generate a file of a certain size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The only two file types for which it is easy to foresee the file size are BIN
and TXT. Note, that size of BIN files is always exact, while for TXT it is
approximate.

BIN
^^^
.. literalinclude:: _static/examples/recipes/file_of_size_bin_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/file_of_size_bin_1.py>`

TXT
^^^
.. literalinclude:: _static/examples/recipes/file_of_size_txt_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/file_of_size_txt_1.py>`

Generate a files using multiprocessing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generate 10 DOCX files
^^^^^^^^^^^^^^^^^^^^^^
- Use template.
- Generate 10 DOCX files.

.. literalinclude:: _static/examples/recipes/files_multiprocessing_1.py
    :language: python
    :lines: 1, 4-6, 8-

*See the full example*
:download:`here <_static/examples/recipes/files_multiprocessing_1.py>`

Randomize the file format
^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/files_multiprocessing_2.py
    :language: python
    :lines: 4-10, 36-

*See the full example*
:download:`here <_static/examples/recipes/files_multiprocessing_2.py>`

Generating files from existing documents using NLP augmentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
See the following example:

.. literalinclude:: _static/examples/recipes/augment_file_from_dir_1.py
    :language: python
    :lines: 2-4, 9, 15, 22-

*See the full example*
:download:`here <_static/examples/recipes/augment_file_from_dir_1.py>`

Generated file will resemble text of the original document, but
will not be the same. This is useful when you don't want to
test on text generated by ``Faker``, but rather something that
makes more sense for your use case, still want to ensure
uniqueness of the documents.

The following file types are supported:

- ``DOCX``
- ``EML``
- ``EPUB``
- ``ODT``
- ``PDF``
- ``RTF``
- ``TXT``

----

By default, all supported files are eligible for random selection. You could
however narrow that list by providing ``extensions`` argument:

.. literalinclude:: _static/examples/recipes/augment_file_from_dir_2.py
    :language: python
    :lines: 23-

*See the full example*
:download:`here <_static/examples/recipes/augment_file_from_dir_2.py>`

----

By default ``bert-base-multilingual-cased`` model is used, which is
pretrained on the top 104 languages with the largest Wikipedia using a
masked language modeling (MLM) objective. If you want to use a different
model, specify the proper identifier in the ``model_path`` argument.
Some well working options for ``model_path`` are:

- ``bert-base-multilingual-cased``
- ``bert-base-multilingual-uncased``
- ``bert-base-cased``
- ``bert-base-uncased``
- ``bert-base-german-cased``
- ``GroNLP/bert-base-dutch-cased``

.. literalinclude:: _static/examples/recipes/augment_file_from_dir_3.py
    :language: python
    :lines: 5-7, 25-

*See the full example*
:download:`here <_static/examples/recipes/augment_file_from_dir_3.py>`

Refer to ``nlpaug``
`docs <https://nlpaug.readthedocs.io/en/latest/example/example.html>`__
and check `Textual augmenters` examples.

Using `raw=True` features in tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you pass ``raw=True`` argument to any provider or inner function,
instead of creating a file, you will get ``bytes`` back (or to be
totally correct, ``bytes``-like object ``BytesValue``, which is basically
bytes enriched with meta-data). You could then use the ``bytes`` content
of the file to build a test payload as shown in the example test below:

.. literalinclude:: _static/examples/recipes/raw_1.py
    :language: python
    :lines: 16-

*See the full example*
:download:`here <_static/examples/recipes/raw_1.py>`

Create a HTML file from predefined template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you want to generate a file in a format that is not (yet) supported,
you can try to use ``GenericFileProvider``. In the following example,
an HTML file is generated from a template.

.. literalinclude:: _static/examples/recipes/generic_file_1.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/recipes/generic_file_1.py>`

Working with storages
~~~~~~~~~~~~~~~~~~~~~
AWS S3 storage
^^^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/aws_s3_storage_1.py
    :language: python
    :lines: 3, 7-

*See the full example*
:download:`here <_static/examples/recipes/aws_s3_storage_1.py>`

----

Depending on the ORM or framework you're using, you might want to tweak the
``root_path`` and ``rel_path`` values. Especially if you store files in
directories (like ``your-bucket-name/path/to/the/file.ext``).

For instance, if you use ``Django`` and ``django-storages``, and want to
store the files inside ``/user/uploads`` directory the following would be
correct:

.. literalinclude:: _static/examples/recipes/aws_s3_storage_2.py
    :language: python
    :lines: 8-12

*See the full example*
:download:`here <_static/examples/recipes/aws_s3_storage_2.py>`

Google Cloud Storage
^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/google_cloud_storage_1.py
    :language: python
    :lines: 3, 7-

*See the full example*
:download:`here <_static/examples/recipes/google_cloud_storage_1.py>`

----

Similarly to ``AWSS3Storage``, if you use ``Django`` and ``django-storages``,
and want to store the files inside ``/user/uploads`` directory the following
would be correct:

.. literalinclude:: _static/examples/recipes/google_cloud_storage_2.py
    :language: python
    :lines: 8-12

*See the full example*
:download:`here <_static/examples/recipes/google_cloud_storage_2.py>`

SFTP storage
^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/sftp_storage_1.py
    :language: python
    :lines: 3, 7-

*See the full example*
:download:`here <_static/examples/recipes/sftp_storage_1.py>`

When using with ``Django`` (and ``factory_boy``)
------------------------------------------------
When used with Django (to generate fake data with ``factory_boy`` factories),
the ``root_path`` argument of the correspondent file storage shall be provided.
Otherwise (although no errors will be triggered) the generated files will
reside outside the ``MEDIA_ROOT`` directory (by default in ``/tmp/`` on
Linux) and further operations with those files through Django will cause
``SuspiciousOperation`` exception.

----

Basic example
~~~~~~~~~~~~~

Imaginary ``Django`` model
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: _static/examples/recipes/factory_boy_models_1.py
    :language: python
    :lines: 4-11

*See the full example*
:download:`here <_static/examples/recipes/factory_boy_models_1.py>`

Correspondent ``factory_boy`` factory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: _static/examples/recipes/factory_boy_factory_1.py
    :language: python
    :lines: 1-87

And then somewhere in your code:

.. literalinclude:: _static/examples/recipes/factory_boy_factory_1.py
    :language: python
    :lines: 91-

*See the full example*
:download:`here <_static/examples/recipes/factory_boy_factory_1.py>`

----

Randomize provider choice
~~~~~~~~~~~~~~~~~~~~~~~~~
.. literalinclude:: _static/examples/recipes/factory_boy_factory_2.py
    :language: python
    :lines: 1, 4, 6, 27, 30-49, 55-95

And then somewhere in your code:

.. literalinclude:: _static/examples/recipes/factory_boy_factory_2.py
    :language: python
    :lines: 98-

*See the full example*
:download:`here <_static/examples/recipes/factory_boy_factory_2.py>`

Use a different locale
~~~~~~~~~~~~~~~~~~~~~~
.. literalinclude:: _static/examples/recipes/factory_boy_factory_3.py
    :language: python
    :lines: 23-24

*See the full example*
:download:`here <_static/examples/recipes/factory_boy_factory_3.py>`

Other Django usage examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Faker example with AWS S3 storage**

.. literalinclude:: _static/examples/recipes/aws_s3_storage_3.py
    :language: python
    :lines: 2, 4-

*See the full example*
:download:`here <_static/examples/recipes/aws_s3_storage_3.py>`

----

**factory-boy example with AWS S3 storage**

.. literalinclude:: _static/examples/recipes/aws_s3_storage_4.py
    :language: python
    :lines: 2, 4-6, 9-

*See the full example*
:download:`here <_static/examples/recipes/aws_s3_storage_4.py>`

----

**Flexible storage selection**

.. literalinclude:: _static/examples/recipes/flexible_storage_1.py
    :language: python
    :lines: 2-

*See the full example*
:download:`here <_static/examples/recipes/flexible_storage_1.py>`
