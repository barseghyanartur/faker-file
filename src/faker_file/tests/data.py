from faker import Faker

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "DOCX_KWARGS",
    "GCS_CREDENTIALS_JSON",
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

GCS_CREDENTIALS_JSON = {
    "type": "service_account",
    "project_id": "test-12345",
    "private_key_id": "00000000000000000000000000",
    "private_key": "\n-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCfx5MW2anBbHKL\n4g1iazAtyxJGoHTfR03zGHr4mVsmfe2cV5vMZY4/oO3uszpbq342tdywfkAq5O8+\nFqbUUIEfAiobs5DVvZ9iL6uAkb/erLY2ObVFDr7hKBu0oRmc2EWYH6honxb/tNFI\nzLy3Sh7Bdor4/vH7PMalgcEorxt+RkFPJeo3cGyrJfO8jv0n2u0wakHKO5bPZshZ\nBAktnYDMVPnaV+kI/ezucxow91l3BXTdPuC3zVSlSuvqRssg8/jpDRgFv/hThuVm\nhUhU8ddS76QUQ0ekj6kBPp5iYvY6sJHwU9Bmf7qG3zAx4h56WBJV+SYDVoT+VydZ\nkqMc721LAgMBAAECggEAALPfxlDzH/U6VIa/W+ujjMzNnSvld60YZais5pAq4dkN\nHqV8yBuGONECjgzE6+3g7zXbhspdvXjzDskKUMXndQ7Z+o2bZgugbZq1QvdHhB/E\nT8OIzYkkEIw2Z8ckyRcv+/XfrermyGPi+IWV96rGxqXSNKG1lLV1HJM2gAqzfaZ1\nqL/TVxj9ZjI3FRGMSuxKeRC/RG6L4iHMq+tOIKSiST6UHSci6TbDDAWXpXMWzEeM\nmHEGCvNmp5yRHEPBF5n5Dl9hEfnhp8FpW20fuANjxIFlW9KMKtu9vkGgS1AdiT9f\nE1lgy41fBdwg2rdMHn3JhCN9H+J2MK7AtoWcD5TNGQKBgQDXszOluYO85hEbtJnN\nf5XtO/aoHtnjPixiI2wcxuGmLWaAYmtgy0KwWZlQldNXM7qH1BiEZ8wTFVOfqrqY\nlDuMYxgfTqPTaESS5wkirucMdZJJXuohLgDAaOaVbL0V+1YJbnq4AnLaHB0Y8sqX\nrnCawF1ke9F0032lbkQJn3qbJQKBgQC9obvTZO/53TrKz2/NWfBDJaTey7PaZ2fg\nJwvj63nUVVM91mQ262mjoqw/Wogp6GFr46XXcyQ/xk8g32EQ1a22p1MXIkdJTic3\n/m+VF//4+GaJD1MedqOxWMVWHZyYJxjekAM/tt3/epzcDFNdab6ZlRIyAh0Ro1mZ\nqJPmbCszrwKBgQCv1F2il2JDJswFaKgDcyCVHU9I5rU436KwcS2dG6Yvn0yyFQhx\nA+Ad/zvSDAAWUo2YUZWWwUICwFzFiBfJbvRH0TOFucYj/BgCJCE3S5n+dwzDkIKM\nf4KPVjO41MYiWBpfX9bbjutuzoINp0Tsdn9GNs8qrSAl+oyuwP7nVUBNnQKBgQCT\ne2fy/vvMnoyNE0vmr942ut5BELhuUiHtqTCMMKVtyHaXD1idhfWA+JFyLFzeCwdJ\nu6FNsRUuLHN6I4EAcM9L0VLEGTrL/mZuHAp4MFQ6NCa6zhpdBPRGh73iPeF+TFoB\nLov4T6bUfW3ljgiADC/ajp+6GP62qw6SfROaD+KBrQKBgHxz/IvyRE7zORNnhcld\n9y+Qr4GPLxV9oLeJlG0gjJaYC79gQk2gUjQfT2HEQlM76SeXr0qr/jOKSZeg4h7Q\nuZib/5m3YD5bI35qBexNHz/AZ1kQ9PiHjZmgS4PiCobuuHUXRPni0Vf0FKLCouQq\n0Bb9H46yp7+n+NCkjHB3IInM\n-----END PRIVATE KEY-----\n",  # noqa
    "client_email": "test-12345@appspot.gserviceaccount.com",
    "client_id": "2222222222222222222222222",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test-12345%40appspot.gserviceaccount.com",  # noqa
    "universe_domain": "googleapis.com",
}
