Release history and notes
=========================
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
