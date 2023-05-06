from faker import Faker

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "DOCX_KWARGS",
    "XML_DOWNLOAD_KWARGS",
    "XML_DOWNLOAD_TEMPLATE",
    "XML_ISBN_KWARGS",
    "XML_ISBN_TEMPLATE",
    "XML_METADATA_KWARGS",
    "XML_METADATA_TEMPLATE",
)

FAKER = Faker()
BOOK_ID = FAKER.pystr()

XML_METADATA_TEMPLATE = """
<book>
  <title>{{sentence}}</title>
  <description>{{paragraph}}</description>
  <date>{{date}}</date>
</book>
"""

XML_ISBN_TEMPLATE = """
<submission>
  <publisher id="{{pyint}}"/>
  <isbn10>{{isbn10}}</isbn10>
  <isbn13>{{isbn13}}</isbn13>
</submission>
"""

XML_DOWNLOAD_TEMPLATE = f"""
<download>
  <filegroup>
    <archive-file name="{BOOK_ID}.zip" />
    <metadata-file name="{BOOK_ID}_metadata.xml" />
    <file name="{BOOK_ID}.pdf" />
    <isbn-file name="{BOOK_ID}_isbn.xml" />
  </filegroup>
</download>
"""

XML_METADATA_KWARGS = {
    "content": XML_METADATA_TEMPLATE,
    "basename": f"{BOOK_ID}_metadata",
}
XML_DOWNLOAD_KWARGS = {
    "content": XML_DOWNLOAD_TEMPLATE,
    "basename": f"{BOOK_ID}_download",
}
XML_ISBN_KWARGS = {
    "content": XML_ISBN_TEMPLATE,
    "basename": f"{BOOK_ID}_isbn",
}
DOCX_KWARGS = {"basename": BOOK_ID}
