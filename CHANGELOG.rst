Release history and notes
=========================
.. Internal references

.. _Armenian genocide: https://en.wikipedia.org/wiki/Armenian_genocide
.. _Blockade of the Republic of Artsakh: https://en.wikipedia.org/wiki/Blockade_of_the_Republic_of_Artsakh_(2022%E2%80%93present)
.. _Pillow: https://pypi.org/project/pillow/
.. _WeasyPrint: https://pypi.org/project/weasyprint/
.. _imgkit: https://pypi.org/project/imgkit/
.. _pdf2image: https://pypi.org/project/pdf2image/
.. _pdfkit: https://pypi.org/project/pdfkit/
.. _reportlab: https://pypi.org/project/reportlab/
.. _wkhtmltopdf: https://wkhtmltopdf.org/

`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.17.9
------
2023-10-10

- Improvements and fixes in the documentation.
- Announcing feature plans to change default PDF and Image generators
  to `Pillow`_ based ones, instead of `wkhtmltopdf`_ in version 0.18.

0.17.8
------
2023-09-21

.. note::

    This release is dedicated to the victims of the war in Artsakh
    (Nagorno-Karabakh), a land now lost to its native inhabitants (Armenians).
    Following a grueling nine-month blockade, Azerbaijan initiated another
    military onslaught on September 19, 2023. The already weakened and
    outnumbered forces of Artsakh could no longer mount an effective
    resistance.

- Added support for ``DynamicTemplate`` to all non-graphic image providers.
  That means, that you can produce images with text, tables, various
  headings and other images. Correspondent snippets are implemented for all
  supported image generators; namely `reportlab`_, `WeasyPrint`_ and
  `Pillow`_.

0.17.7
------
2023-09-12

- Added ``GTTS_MP3_GENERATOR`` and ``EDGE_TTS_MP3_GENERATOR`` to
  the ``mp3_file`` provider import options.

0.17.6
------
2023-09-09

- Added ``add_paragraph``, ``add_picture``, ``add_heading_h1`` and other
  heading helpers to ``pil_snippets`` contrib module.

0.17.5
------
2023-08-22

.. note::

    This release might introduces minor backwards incompatible changes only
    if you have written own- or customized existing- image providers and used
    them in combination with `WeasyPrint`_-based image generator. A new
    property named ``image_format`` has been added to all image-based
    providers and the ``WeasyPrintImageGenerator`` is using that instead
    of formerly used ``extension`` property.

- Added ``PilImageGenerator`` (for text-to-image).
- Added ``PilPdfGenerator`` (for text-to-image).

0.17.4
------
2023-08-18

.. note::

    Release is dedicated to the victims and de-facto hostages of
    the `Blockade of the Republic of Artsakh`_. Have you ever heard
    of `Armenian genocide`_? It's happening again. For more than 8 months,
    Azerbaijan has launched an illegal blockade of the Republic of Artsakh,
    including critical civilian infrastructure such as gas, electricity and
    roads connecting Armenia and Artaskh. Shortages of essential goods –
    including electricity, fuel, and water reserves – are widespread and
    emergency reserves are being rationed. The blockade has resulted in
    significant medical and food shortages in Artsakh, leading to increased
    health complications, as reported by Artsakh Healthcare ministry.

     - Deaths due to cardiovascular diseases doubled in the first seven
       months of the year, with a particular surge in July-August.
     - Deaths from malignant tumors rose by 15.9% over the same period due
       to lack of medications and medical aid.
     - New cases of stroke and heart attacks increased by 26% and 9.7%
       respectively.
     - Newly diagnosed cases of malignant tumors rose by 24.3%.
     - Around 90% of monitored pregnant women developed anemia from poor
       nutrition and medication shortages.
     - While overall abortion numbers remained stable, medically indicated
       abortions quadrupled in July due to factors like stress and
       inadequate nutrition.
     - Reports of fainting surged by 91% in July-August.
     - Emergency calls for high blood pressure saw a 5.6-fold increase in
       July-August.

    The dire health outcomes are attributed to the blockade's impact,
    including medication shortages, stress, disrupted medical procedures,
    and restricted healthcare access. The Artsakh Health Ministry warns of
    further deterioration if the blockade continues, emphasizing the systemic
    challenges in healthcare delivery due to the blockade.

- Added ``AugmentRandomImageFromDirProvider``
  and ``AugmentImageFromPathProvider`` providers for basic image augmentation.
- Added ``storage`` to metadata for all providers for easy clean-up of files.
- Added ``unlink`` method to all storages for easy clean-up of files.
- Added ``FileRegistry`` to keep track of all files created and introduce
  functionality for cleaning up the files.
- Stop testing against Python 3.7.

0.17.3
------
2023-08-02

.. note::

    In memory of Sinead O'Connor.

- Allow to pass ``image`` argument (``bytes``) to the contrib ``add_picture``
  functions.
- Documentation improvements.

0.17.2
------
2023-07-25

- Added ``JSON`` file provider.

0.17.1
------
2023-07-21

- Added ``WeasyPrintImageGenerator`` image generator class based
  on `WeasyPrint`_ and `pdf2image`_ packages.
- Added ``BMP``, ``TIFF`` and ``GIF`` file providers (both text-to-image
  and graphic ones). Note, that above mentioned text-to-image providers
  are using ``WeasyPrintImageGenerator`` as a default image generator class,
  since ``ImagekitImageGenerator`` class isn't capable of supporting the
  above mentioned file formats.
- Added more helper functions for ``DynamicTemplate`` use for ODT, PDF and
  DOCX file providers to support h1, h2, h3, h4, h5 and h6 headings.

0.17
----
2023-07-12

.. note::

    Release is dedicated to the victims and de-facto hostages of
    the `Blockade of the Republic of Artsakh`_. Have you ever heard
    of `Armenian genocide`_? It's happening again and the world
    silently watches.

- Introducing graphic image providers. Prior to this release, images have
  been created using text-to-image solutions. Sometimes it's just handy to
  have a graphic image. Therefore, a number of graphic image file providers
  have been created (including inner functions support). The following graphic
  file providers have been added: ``GraphicIcoFileProvider``,
  ``GraphicJpegFileProvider``, ``GraphicPdfFileProvider``,
  ``GraphicPngFileProvider`` and ``GraphicWebpFileProvider`` to support
  creation of graphic ``ICO``, ``JPEG``, ``PDF``, ``PNG`` and ``WEBP`` files.
- The previously mentioned text-to-image rendering has been delegated to
  image generators. Default generator is still based on the `imgkit`_, but
  the change makes it possible to use custom generators.

0.16.4
------
2023-07-01

- Documentation improvements. Added a dedicated section for creating ODT files.
- Adding ``add_paragraph`` and ``add_page_break`` to ``ODT`` contrib module.

0.16.3
------
2023-06-30

- Documentation improvements. Added a dedicated section for creating PDF files.
  Added a dedicated section for creating DOCX files.
- Adding ``add_paragraph`` and ``add_page_break`` to ``DOCX`` contrib module.

0.16.2
------
2023-06-28

- Moving some of the snippets from tests to a ``contrib`` module to improve
  usability. The snippets are generic enough to be used in tests and if you
  don't like the way they work, you could always make a new one. New snippets
  to insert page breaks and paragraphs into PDF (using both `pdfkit`_
  and `reportlab`_ generators) have been added.

0.16.1
------
2023-06-23

- Better error handling in CLI.

0.16
----
2023-06-21

.. note::

    This release is dedicated to my beloved son - Tigran, who turned 11!

.. note::

    This release introduces minor backwards incompatible changes.

- Minor improvements in PDF generation. If you have been using
  ``DynamicTemplate`` to generate complex PDFs, you are likely affected
  by the change. Make sure to at least add an additional argument
  named ``generator`` to the functions passed to the ``DynamicTemplate``
  class. See the example below:

  Old:

    ``def add_pb(provider, story, data, counter, **kwargs):``

  New:

    ``def add_pb(provider, generator, story, data, counter, **kwargs):``

- Add code examples of how to generate a PDF with 100 pages with
  both ``PdfkitPdfGenerator`` and ``ReportlabPdfGenerator`` PDF generator
  classes.
- Add ``version`` CLI command.
- Add ``generate-completion`` and ``version`` commands to the CLI
  auto-completion.

0.15.5
------
2023-06-18

- Minor fixes and documentation improvements.

0.15.4
------
2023-06-15

- Improved ``SFTPStorage`` tests.
- Stop testing against Python 3.7.
- Stop testing against Django 4.0.

0.15.3
------
2023-06-14

- Add ``SFTPStorage`` and correspondent tests.

0.15.2
------
2023-06-08

- Add optional ``subject`` argument to the ``EmlFileProvider``. Update
  tests accordingly.
- Add data integrity tests.

0.15.1
------
2023-06-06

- Added ``FileFromPathProvider`` provider, which simply picks a file
  from path given. Add correspondent ``create_inner_file_from_path``
  inner function.

0.15
----
2023-06-05

- Added ``format_func`` argument to most of the providers. This allows to
  control which formatter function will be used as a default formatter.
  Previously it has been ``faker.provider.Python.pystr_format``, which has
  been changed to ``faker.provider.Python.parse``, since the latter is
  more convenient (as it does not transform characters
  like ``?``, ``!``, ``#`` into something else using ``bothify`` method).
  To revert this behaviour, make sure to pass a callable
  function ``faker_file.base.pystr_format_func`` in ``format_func`` argument
  to each correspondent provider or inner function.
- Added ``create_inner_random_file_from_dir`` inner function.
- Tested against Django 4.2.
- Stop testing against Django 2.2.

0.14.5
------
2023-05-11

- Minor fixes in ``xml_file`` provider.

0.14.4
------
2023-05-11

- Changed type of ``data_columns`` for ``xml_file`` provider from
  ``Sequence[Tuple[str, str]]`` to ``Dict[str, str]``.
- In the ``pdf_file`` provider, changed default value of ``pdf_generator_cls``
  from concrete ``PdfkitPdfGenerator`` value to its' string representation
  faker_file.providers.pdf_file.generators.pdfkit_generator.PdfkitPdfGenerator.
- In the ``mp3_file`` provider, changed default value of ``mp3_generator_cls``
  from concrete ``GttsMp3Generator`` value to its' string representation
  faker_file.providers.mp3_file.generators.gtts_generator.GttsMp3Generator.

0.14.3
------
2023-05-10

- Minor fixes in the ``GenericFileProvider``.

0.14.2
------
2023-05-09

- Add ``create_inner_generic_file`` inner function.
- Add ``generic_file`` support to CLI.

0.14.1
------
2023-05-08

- Add support for ``list_create_inner_file``-like functions to the ``EML``
  file provider. If you are using CLI and CLI-completion, make sure to
  re-generate the completion file.
- Add ``GenericFileProvider`` provider to support generic file types.

0.14
----
2023-05-07

.. note::

    This release introduces minor backwards incompatible changes.

- A new argument ``basename`` has been added to all providers, inner
  functions and storage classes. If you have customized things or created
  your own providers, make sure to make appropriate changes in your code.
  See the source code for more implementation examples. If you are using
  CLI and CLI-completion, make sure to re-generate the completion file.
- A new inner function ``list_create_inner_file`` has been added, using which
  it's possible to create just a list of given files (ignoring ``count`` value)
  using given arguments. The amount of files is determined by
  the ``func_list`` (each pair ``(Callable, kwargs)`` corresponds to a single
  file. Both ``ZipFileProvider`` and ``TarFileProvider`` have been altered to
  reflect these changes.
- Added to support for ``XML`` files through ``XmlFileProvider``.

0.13
----
2023-05-05

.. note::

    This release introduces minor backwards incompatible changes.

- Display full path to the created file in the CLI.
- Added ``DynamicTemplate`` support for ``PDF`` file. The ``generate``
  method of the ``BasePdfGenerator`` and classes derived from it,
  got two new arguments: ``data`` (``Dict[str, Any]``),
  and ``provider`` (``Union[Faker, Generator, Provider]``). If you have
  implemented custom generators for ``PDF`` (``pdf_file`` provider),
  make sure to reflect mentioned changes in your code.

0.12.6
------
2023-05-02

- Added ``DynamicTemplate`` support for ``DOCX`` and ``ODT`` files.

0.12.5
------
2023-04-24

.. note::

    In memory of the victims of the
    `Armenian Genocide <https://en.wikipedia.org/wiki/Armenian_genocide>`_.

- Expose ``mp3_generator_cls`` and ``pdf_generator_cls`` CLI options
  for ``mp3_file`` and ``pdf_file`` respectively.
- Add ``num_files`` CLI option for all providers.

0.12.4
------
2023-04-22

- Make it possible to load classes from strings for passing as arguments
  to ``mp3_file`` and ``pdf_file`` providers.

0.12.3
------
2023-04-21

- Fixes in CLI options.

0.12.2
------
2023-04-20

- Fixes in CLI options.

0.12.1
------
2023-04-19

- Added CLI options.

0.12
----
2023-02-24

*Note, that this release introduces breaking changes!*

- Make it easy to use a different PDF library with ``PdfFileProvider`` by
  adding ``pdf_generator_cls`` and ``pdf_generator_kwargs`` optional arguments
  to the ``pdf_file`` method. Added ``ReportlabPdfGenerator`` class based on
  the famous ``reportlab`` library. Default is still ``PdfkitPdfGenerator``.
  Since ``encoding`` was something specific for ``pdfkit`` library,
  it was moved from ``pdf_file`` method to ``PdfkitPdfGenerator``, to which it
  can be passed in ``pdf_generator_kwargs``. If you have passed the
  ``encoding`` argument explicitly, make sure to make correspondent changes.
  Note, that using the new ``ReportlabPdfGenerator`` class could speed-up PDF
  generation by about 40 times.

0.11.5
------
2023-02-20

- Fixes in typing of ``CsvFileProvider``. ``Tuple[str, str]``
  becomes ``Tuple[str, ...]``.

0.11.4
------
2023-02-16

.. note::

    Release dedicated to my dear valentine - Anahit.

- Added ``filename`` to ``data`` property of values returned by
  ``Mp3FileProvider`` provider (``StringValue``, ``BytesValue``).

0.11.3
------
2023-02-10

- Moved several interface classes from one location to another. If you haven't
  implemented custom generators, this won't affect you. If you did, make sure
  to update your imports:

    - ``BaseTextAugmenter`` has been moved from
      ``faker_file.providers.augment_file_from_dir.augmenters.base`` to
      ``faker_file.providers.base.text_augmenter``.
    - ``BaseTextExtractor`` has been moved from
      ``faker_file.providers.augment_file_from_dir.extractors.base`` to
      ``faker_file.providers.base.text_extractor``.
    - ``BaseMp3Generator`` has been moved from
      ``faker_file.providers.mp3_file.generators.base`` to
      ``faker_file.providers.base.mp3_generator``.

0.11.2
------
2023-02-07

- Add ``filename`` to ``data`` property of values returned by providers
  (``StringValue``, ``BytesValue``).

0.11.1
------
2023-01-31

- Documentation improvements.
- MyPy fixes.

0.11
----
2023-01-25

- Allow returning binary contents of the file by providing the ``raw=True``
  argument (``False`` by default, works with all provider classes and inner
  functions). If you  have subclassed or overriden provider classes or
  written custom inner functions, make sure to reflect the changes in your
  code.

0.10.12
-------
2023-01-21

- Add ``TarFileProvider`` and ``create_inner_tar_file`` function.
- Add ``OdpFileProvider`` and ``create_inner_odp_file`` function.

0.10.11
-------
2023-01-20

- Improve ``EPUB`` document layout.
- Improve ``PDF`` document layout.
- Minor documentation improvements.

0.10.10
-------
2023-01-19

- Allow passing ``model_name`` and ``action`` arguments to
  the ``ContextualWordEmbeddingsAugmenter``.
- Replace ``bert-base-cased`` with ``bert-base-multilingual-cased`` as a
  default model for ``ContextualWordEmbeddingsAugmenter``.
- Improve ``PPTX`` document layout.
- Minor fixes in documentation.

0.10.9
------
2023-01-18

- Add an installation directive ``[common]`` to install everything except
  ML libraries.
- Added testing of UTF8 content.

0.10.8
------
2023-01-16

- Switch to PyPI releases of ``gtts``.
- Stop testing against Django 3.0 and 3.1.
- Documentation improvements.
- Tests improvements.

0.10.7
------
2023-01-13

- Add ``OdtFileProvider`` and ``create_inner_odt_file`` function.
- Documentation improvements.
- Async related deprecation fixes in ``EdgeTtsMp3Generator``.
- Optimize example factories.

0.10.6
------
2023-01-11

- Add ``AugmentFileFromDirProvider`` provider for making augmented copies of
  randomly picked files from given directory.
- Documentation improvements.
- Fixes in setup.

0.10.5
------
2023-01-09

- Add ``fuzzy_choice_create_inner_file`` inner function for easy
  diversion of files within archives (``ZIP``, ``EML``).
- Documentation improvements.
- Add ``MaryTTS`` example (another MP3 generator for ``Mp3FileProvider``).

0.10.4
------
2023-01-08

- Add missing ``mp3_generator_kwargs`` argument to
  the ``create_inner_mp3_file`` function.
- Clean-up.

0.10.3
------
2023-01-07

Improvements of the ``Mp3FileProvider`` module:

- Pass active generator to the ``Mp3FileProvider`` in the ``generator``
  argument if ``BaseMp3Generator`` (and all implementations).
- Introduce ``handle_kwargs`` method in the ``BaseMp3Generator`` to handle
  arbitrary provider specific tuning.
- Add ``EdgeTtsMp3Generator`` MP3 generator.
- Add ``mp3_generator_kwargs`` argument to the ``Mp3FileProvider.mp3_file``
  method.

0.10.2
------
2023-01-06

- Add ``Mp3FileProvider``.
- Add ``create_inner_mp3_file`` inner function.

0.10.1
------
2023-01-05

- Fixes in ``ZipFileProvider``.

0.10
----
2023-01-04

*Note, that this release introduces breaking changes!*

- Move all ``create_inner_*_file`` functions from
  ``faker_file.providers.zip_file`` to
  ``faker_file.providers.helpers.inner`` module. Adjust your imports
  accordingly.
- Add ``EmlFileProvider``.
- Add ``create_inner_eml_file`` inner function.

0.9.3
-----
2023-01-03

- Add ``EpubFileProvider`` provider.

0.9.2
-----
2022-12-23

- Add ``RrfFileProvider``.
- Added ``SQLAlchemy`` factory example.

0.9.1
-----
2022-12-19

- Fixes in cloud storage.
- Documentation fixes.

0.9
---
2022-12-17

- Add optional ``encoding`` argument to ``CsvFileProvider`` and
  ``PdfFileProvider`` providers.
- Add ``root_path`` argument to cloud storages.
- Moved all image related code (``IcoFileProvider``, ``JpegFileProvider``,
  ``PngFileProvider``, ``SvgFileProvider``, ``WebpFileProvider``) to
  ``ImageMixin``. Moved all tabular data related code (``OdsFileProvider``,
  ``XlsxFileProvider``) to ``TabularDataMixin``.
- Documentation improvements.

0.8
---
2022-12-16

*Note, that this release introduces breaking changes!*

- All file system based operations are moved to a separate abstraction layer
  of file storages. The following storages have been implemented:
  ``FileSystemStorage``, ``PathyFileSystemStorage``, ``AWSS3Storage``,
  ``GoogleCloudStorage`` and ``AzureStorage``. The ``root_path``
  and ``rel_path`` params of the providers are deprecated in favour of
  storages. See the docs more usage examples.

0.7
---
2022-12-12

- Added ``RandomFileFromDirProvider`` which picks a random file from
  directory given.
- Improved docs.

0.6
---
2022-12-11

- Pass optional ``generator`` argument to inner functions of
  the ``ZipFileProvider``.
- Added ``create_inner_zip_file`` inner function which allows to create
  nested ZIPs.
- Reached test coverage of 100%.

0.5
---
2022-12-10

*Note, that this release introduces breaking changes!*

- Added `ODS` file support.
- Switched to ``tablib`` for easy, non-variant support of various
  formats (`XLSX`, `ODS`).
- Silence ``imgkit`` logging output.
- `ZipFileProvider` allows to pass arbitrary arguments to inner functions.
  Put all your inner function arguments into a dictionary and pass it
  in `create_inner_file_args` key inside `options` argument. See the
  example below.

    .. code-block:: python

        zip_file = ZipFileProvider(None).file(
            prefix="zzz_archive_",
            options={
                "count": 5,
                "create_inner_file_func": create_inner_docx_file,
                "create_inner_file_args": {
                    "prefix": "zzz_file_",
                    "max_nb_chars": 1_024,
                    "content": "{{date}}\r\n{{text}}\r\n{{name}}",
                },
                "directory": "zzz",
            }
        )

0.4
---
2022-12-09

*Note, that this release introduces breaking changes!*

- Remove the concept of content generators (and the
  correspondent ``content_generator`` arguments in implemented providers).
  Instead, allow usage of dynamic fixtures in the provided ``content``
  argument.
- Remove temporary files when creating ZIP archives.
- Various improvements and fixes in docs.

0.3
---
2022-12-08

- Add support for `BIN`, `CSV` and `XLSX` files.
- Better visual representation of generated images and PDFs.

0.2
---
2022-12-07

- Added support for `ICO`, `JPEG`, `PNG`, `SVG` and `WEBP` files.
- Documentation improvements.

0.1
---
2022-12-06

- Initial beta release.
