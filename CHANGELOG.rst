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
