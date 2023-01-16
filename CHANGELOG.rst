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
