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

0.5
---
2022-12-10

*Note, that this release introduces breaking changes!*

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
