Concepts
========
`faker-file` is designed to generate files with synthetic data. It can work
with a variety of file types, such as TXT, DOCX, PDF, PPTX, EML, and ZIP files.

It uses the `Faker` library to generate synthetic (fake) data. This data can
be used as the content of the generated files, allowing for files with
realistic, but synthetic, content.

Providers
---------
`faker-file` includes different file providers for each file type. They are
responsible for the creation of the files, each having a method to create a
specific file type:

- ``DocxFileProvider``
- ``PdfFileProvider``
- ``PptxFileProvider``
- ``TxtFileProvider``
- ``ZipFileProvider``
- ``EmlFileProvider``

Inner functions
---------------
`faker-file` includes a module named ``faker_file.providers.helpers.inner`` that
contains helper functions, referred to as "inner functions". These functions are
used to create files that are nested within other files (e.g., creating DOCX
files within a ZIP file).

List of inner functions:

- ``create_inner_docx_file``
- ``create_inner_zip_file``
- ``create_inner_eml_file``
- ``create_inner_epub_file``
- ``create_inner_txt_file``
- ``fuzzy_choice_create_inner_file``
- ``list_create_inner_file``

These inner functions are used to create a variety of files and structure them
in various ways, such as creating DOCX files in ZIP files, or creating nested
ZIP files. They also allow for the creation of files with dynamic content or
content based on templates, as well as control over the naming and directory
structure of the files.

File customization
------------------
``faker-file`` allows for various customization options for file generation.
Examples include static or dynamic content generation, character limits, line
wrapping, filename prefixing, and more.

Storage
-------
`faker-file` uses pluggable storages, which are responsible for managing how
and where files are stored in the (remote) file system.

DynamicTemplate
---------------
``DynamicTemplate`` is a wrapper used for creating DOCX and ODT files with
tables and images. This feature allows for full control over the content
creation process. It requires a list of tuples as input, where each tuple
contains a callable function and a dictionary of keyword arguments. The
callable function should accept arguments including a Faker generator or
instance, a document instance, a dictionary for data, a counter, and an
optional dictionary for additional arguments. This feature demonstrates
how to create a DOCX or ODT file with a table and an image.

GenericFileProvider
-------------------
``GenericFileProvider`` allows you to create files in any format from a
predefined template. This is particularly useful when you want to generate
a file in a format that is not directly supported by the library.
