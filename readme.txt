faker-file
**********

**Create files with fake data**. In many formats. With no efforts.

[image: PyPI Version][image][image: Supported Python
versions][image][image: Build Status][image][image: Documentation
Status][image][image: llms.txt - documentation for LLMs][image][image:
MIT][image][image: Coverage][image]


Prerequisites
=============

All of core dependencies of this package are *MIT* licensed. Most of
optional dependencies of this package are *MIT* licensed, while a few
are *BSD*-, *Apache 2*-, *GPL* or *HPND* licensed.

All licenses are mentioned below between the brackets.

* Core package requires Python 3.9, 3.10, 3.11 or 3.12.

* Faker (*MIT*) is the only required dependency.

* Django (*BSD*) integration with factory_boy (*MIT*) has been tested
  with "Django" starting from version 2.2 to 4.2 (although only
  maintained versions of Django are currently being tested against).

* "BMP", "GIF" and "TIFF" file support requires either just Pillow
  (*HPND*), or a combination of WeasyPrint (*BSD*), pdf2image (*MIT*),
  Pillow (*HPND*) and poppler (*GPLv2*).

* "DOCX" file support requires python-docx (*MIT*).

* "EPUB" file support requires xml2epub (*MIT*) and Jinja2 (*BSD*).

* "ICO", "JPEG", "PNG", "SVG" and "WEBP" files support requires either
  just Pillow (*HPND*), or a combination of imgkit (*MIT*) and
  wkhtmltopdf (*LGPLv3*).

* "MP3" file support requires gTTS (*MIT*) or edge-tts (*GPLv3*).

* "PDF" file support requires either Pillow (*HPND*), or a combination
  of pdfkit (*MIT*) and wkhtmltopdf (*LGPLv3*), or reportlab (*BSD*).

* "PPTX" file support requires python-pptx (*MIT*).

* "ODP" and "ODT" file support requires odfpy (*Apache 2*).

* "ODS" file support requires tablib (*MIT*) and odfpy (*Apache 2*).

* "XLSX" file support requires tablib (*MIT*) and openpyxl (*MIT*).

* "PathyFileSystemStorage" storage support requires pathy (*Apache
  2*).

* "AWSS3Storage" storage support requires pathy (*Apache 2*) and boto3
  (*Apache 2*).

* "AzureCloudStorage" storage support requires pathy (*Apache 2*) and
  azure-storage-blob (*MIT*).

* "GoogleCloudStorage" storage support requires pathy (*Apache 2*) and
  google-cloud-storage (*Apache 2*).

* "SFTPStorage" storage support requires paramiko (*LGLPv2.1*).

* "AugmentFileFromDirProvider" provider requires either a combination
  of textaugment (*MIT*) and nltk (*Apache 2*) or a combination of
  nlpaug (*MIT*), PyTorch (*BSD*), transformers (*Apache 2*), numpy
  (*BSD*), pandas (*BSD*), tika (*Apache 2*) and Apache Tika (*Apache
  2*).


Documentation
=============

* Documentation is available on Read the Docs.

* For bootstrapping check the Quick start.

* For various ready to use code examples see the Recipes.

* For tips on "PDF" creation see Creating PDF.

* For tips on "DOCX" creation see Creating DOCX.

* For tips on "ODT" creation see Creating ODT.

* For tips on images creation see Creating images.

* For CLI options see the CLI.

* Read the Methodology.

* For guidelines on contributing check the Contributor guidelines.


Online demos and related projects
=================================

Check the demo(s) and related projects below:

* REST API demo (based on faker-file-api REST API)

* UI frontend demo (based on faker-file-ui UI frontend)

* WASM frontend demo (based on faker-file-wasm WASM frontend)

* faker-file-qt GUI application (based on PyQT5).


Installation
============


Latest stable version from PyPI
-------------------------------

**WIth all dependencies**

   pip install faker-file'[all]'

**Only core**

   pip install faker-file

**With most common dependencies**

*Everything, except ML libraries which are required for data
augmentation only*

   pip install faker-file'[common]'

**With DOCX support**

   pip install faker-file'[docx]'

**With EPUB support**

   pip install faker-file'[epub]'

**With images support**

   pip install faker-file'[images]'

**With PDF support**

   pip install faker-file'[pdf]'

**With MP3 support**

   pip install faker-file'[mp3]'

**With XLSX support**

   pip install faker-file'[xlsx]'

**With ODS support**

   pip install faker-file'[ods]'

**With ODT support**

   pip install faker-file'[odt]'

**With data augmentation support**

   pip install faker-file'[data-augmentation]'

**With GoogleCloudStorage support**

   pip install faker-file'[gcs]'

**With AzureCloudStorage support**

   pip install faker-file'[azure]'

**With AWSS3Storage support**

   pip install faker-file'[s3]'


Or development version from GitHub
----------------------------------

   pip install https://github.com/barseghyanartur/faker-file/archive/main.tar.gz


Features
========


Supported file types
--------------------

* "BIN"

* "BMP"

* "CSV"

* "DOCX"

* "EML"

* "EPUB"

* "ICO"

* "GIF"

* "JPEG"

* "JSON"

* "MP3"

* "ODS"

* "ODT"

* "ODP"

* "PDF"

* "PNG"

* "RTF"

* "PPTX"

* "SVG"

* "TAR"

* "TIFF"

* "TXT"

* "WEBP"

* "XLSX"

* "XML"

* "ZIP"

For all image formats ("BMP", "ICO", "GIF", "JPEG", "PNG", "SVG",
"TIFF" and "WEBP") and "PDF", there are both graphic-only and mixed-
content file providers (that also have text-to-image capabilities).


Additional providers
--------------------

* "AugmentFileFromDirProvider": Make an augmented copy of randomly
  picked file from given directory. The following types are supported
  : "DOCX", "EML", "EPUB", "ODT",  "PDF", "RTF" and "TXT".

* "AugmentRandomImageFromDirProvider": Augment a random image file
  from given directory. The following types are supported : "BMP",
  "GIF", "JPEG", "PNG",  "TIFF" and "WEBP".

* "AugmentImageFromPathProvider": Augment an image file from given
  path. Supported file types are the same as for
  "AugmentRandomImageFromDirProvider" provider.

* "GenericFileProvider": Create files in any format from raw bytes or
  a predefined template.

* "RandomFileFromDirProvider": Pick a random file from given
  directory.

* "FileFromPathProvider": File from given path.


Supported file storages
-----------------------

* Native file system storage

* AWS S3 storage

* Azure Cloud Storage

* Google Cloud Storage

* SFTP storage


Usage examples
==============


With "Faker"
------------

**Recommended way**

   from faker import Faker
   # Import the file provider we want to use
   from faker_file.providers.txt_file import TxtFileProvider

   FAKER = Faker()  # Initialise Faker instance
   FAKER.add_provider(TxtFileProvider)  # Register the TXT file provider

   file = FAKER.txt_file()  # Generate a TXT file

   # Meta-data is stored inside a ``data`` attribute (``dict``).
   # The following line would produce something like /tmp/tmp/tmphzzb8mot.txt
   print(file.data["filename"])
   # The following line would produce a text generated by Faker, used as
   # the content of the generated file.
   print(file.data["content"])

Note:

  Note, that in this case "file" value is a "StringValue" instance,
  which inherits from "str" but contains meta-data such as absolute
  path to the generated file, and text used to generate the file,
  stored in "filename" and "content" keys of the "data" attribute
  respectively. See Meta-data for more information.

If you just need "bytes" back (instead of creating the file), provide
the "raw=True" argument (works with all provider classes and inner
functions):

   from faker import Faker
   from faker_file.providers.txt_file import TxtFileProvider

   FAKER = Faker()
   FAKER.add_provider(TxtFileProvider)

   raw = FAKER.txt_file(raw=True)

Note:

  Note, that in this case "file" value is a "BytesValue" instance,
  which inherits from "bytes" but contains meta-data such as absolute
  path to the generated file, and text used to generate the file,
  stored in "filename" and "content" keys of the "data" attribute
  respectively. See Meta-data for more information.

**But this works too**

   from faker import Faker
   from faker_file.providers.txt_file import TxtFileProvider

   FAKER = Faker()

   file = TxtFileProvider(FAKER).txt_file()

If you just need "bytes" back:

   from faker import Faker
   from faker_file.providers.txt_file import TxtFileProvider

   FAKER = Faker()

   raw = TxtFileProvider(FAKER).txt_file(raw=True)


With "factory_boy"
------------------

*Filename: upload/models.py*

   from django.db import models

   class Upload(models.Model):

       # ...
       file = models.FileField()

       class Meta:
           app_label = "upload"

*Filename: upload/factories.py*

Note, that when using "faker-file" with "Django" and native file
system storages, you need to pass your "MEDIA_ROOT" setting as
"root_path" value to the chosen file storage as show below.

   import factory
   from django.conf import settings
   from factory import Faker
   from factory.django import DjangoModelFactory
   from faker_file.providers.docx_file import DocxFileProvider
   from faker_file.storages.filesystem import FileSystemStorage

   from upload.models import Upload

   FS_STORAGE = FileSystemStorage(
       root_path=settings.MEDIA_ROOT,
       rel_path="tmp"
   )
   factory.Faker.add_provider(DocxFileProvider)

   class UploadFactory(DjangoModelFactory):

       # ...
       file = Faker("docx_file", storage=FS_STORAGE)

       class Meta:
           model = Upload


Meta-data
=========

The return value of any file provider file generator function is
either "StringValue" or "BytesValue", which inherit from "str" and
"bytes" respectively.

Both "StringValue" and "BytesValue" instances have a meta data
attribute named "data" (type "dict"). Various file providers use
"data" to store meta-data, such as "filename" (absolute path to the
generated file; valid for all file providers), or "content" (text used
when generating the file; valid for most file providers, except
"FileFromPathProvider", "RandomFileFromDirProvider", "TarFileProvider"
and "ZipFileProvider").

All file providers store an absolute path to the generated file in
"filename" key of the "data" attribute and instance of the storage
used in "storage" key. See the table below.

+-------------+-------------------------------------------------------------------+
| Key name    | File provider                                                     |
|=============|===================================================================|
| filename    | all                                                               |
+-------------+-------------------------------------------------------------------+
| storage     | all                                                               |
+-------------+-------------------------------------------------------------------+
| content     | all except FileFromPathProvider, RandomFileFromDirProvider,       |
|             | TarFileProvider, ZipFileProvider and all graphic file providers   |
|             | such as GraphicBmpFileProvider, GraphicGifFileProvider,           |
|             | GraphicIcoFileProvider, GraphicJpegFileProvider,                  |
|             | GraphicPdfFileProvider, GraphicPngFileProvider,                   |
|             | GraphicTiffFileProvider and GraphicWebpFileProvider               |
+-------------+-------------------------------------------------------------------+
| inner       | only EmlFileProvider, TarFileProvider and ZipFileProvider         |
+-------------+-------------------------------------------------------------------+


File storages
=============

All file operations are delegated to a separate abstraction layer of
storages.

The following storages are implemented:

* "FileSystemStorage": Does not have additional requirements.

* "PathyFileSystemStorage": Requires pathy.

* "AzureCloudStorage": Requires pathy and *Azure* related
  dependencies.

* "GoogleCloudStorage": Requires pathy and *Google Cloud* related
  dependencies.

* "AWSS3Storage": Requires pathy and *AWS S3* related dependencies.

* "SFTPStorage": Requires paramiko and related dependencies.


Usage example with storages
---------------------------


*FileSystemStorage* example
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Native file system storage. Does not have dependencies.

* "root_path": Path to the root directory. Given the example of
  Django, this would be the path to the "MEDIA_ROOT" directory. It's
  important to know, that "root_path" will not be embedded into the
  string representation of the file. Only "rel_path" will.

* "rel_path": Relative path from the root directory. Given the example
  of Django, this would be the rest of the path to the file.

   import tempfile
   from faker import Faker
   from faker_file.providers.txt_file import TxtFileProvider
   from faker_file.storages.filesystem import FileSystemStorage

   FS_STORAGE = FileSystemStorage(
       root_path=tempfile.gettempdir(),  # Use settings.MEDIA_ROOT for Django
       rel_path="tmp",
   )

   FAKER = Faker()

   file = TxtFileProvider(FAKER).txt_file(storage=FS_STORAGE)

   FS_STORAGE.exists(file)


*PathyFileSystemStorage* example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Native file system storage. Requires "pathy".

   import tempfile
   from pathy import use_fs
   from faker import Faker
   from faker_file.providers.txt_file import TxtFileProvider
   from faker_file.storages.cloud import PathyFileSystemStorage

   use_fs(tempfile.gettempdir())
   PATHY_FS_STORAGE = PathyFileSystemStorage(
       bucket_name="bucket_name",
       root_path="tmp",
       rel_path="sub-tmp",
   )

   FAKER = Faker()

   file = TxtFileProvider(FAKER).txt_file(storage=PATHY_FS_STORAGE)

   PATHY_FS_STORAGE.exists(file)


*AWSS3Storage* example
~~~~~~~~~~~~~~~~~~~~~~

AWS S3 storage. Requires "pathy" and "boto3".

   from faker import Faker
   from faker_file.providers.txt_file import TxtFileProvider
   from faker_file.storages.aws_s3 import AWSS3Storage

   S3_STORAGE = AWSS3Storage(
       bucket_name="bucket_name",
       root_path="tmp",  # Optional
       rel_path="sub-tmp",  # Optional
       # Credentials are optional too. If your AWS credentials are properly
       # set in the ~/.aws/credentials, you don't need to send them
       # explicitly.
       credentials={
           "key_id": "YOUR KEY ID",
           "key_secret": "YOUR KEY SECRET"
       },
   )

   FAKER = Faker()

   file = TxtFileProvider(FAKER).txt_file(storage=S3_STORAGE)

   assert S3_STORAGE.exists(file)


Testing
=======

Simply type:

   pytest -vrx

Or use tox:

   tox

Or use tox to check specific env:

   tox -e py310-django41


Writing documentation
=====================

Keep the following hierarchy.

   =====
   title
   =====

   header
   ======

   sub-header
   ----------

   sub-sub-header
   ~~~~~~~~~~~~~~

   sub-sub-sub-header
   ^^^^^^^^^^^^^^^^^^

   sub-sub-sub-sub-header
   ++++++++++++++++++++++

   sub-sub-sub-sub-sub-header
   **************************


License
=======

MIT


Support
=======

For security issues contact me at the e-mail given in the Author
section.

For overall issues, go to GitHub.


Author
======

Artur Barseghyan <artur.barseghyan@gmail.com>


Citation
========

Please, use the following entry when citing faker-file in your
research:

   @software{faker-file,
     author = {Artur Barseghyan},
     title = {faker-file: Create files with fake data. In many formats. With no efforts.},
     year = {2022-2025},
     publisher = {GitHub},
     journal = {GitHub repository},
     howpublished = {https://github.com/barseghyanartur/faker-file},
   }
