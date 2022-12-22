from random import choice

from factory import Faker, LazyAttribute, Sequence
from factory.alchemy import SQLAlchemyModelFactory
from faker_file_admin import db
from faker_file_admin.models import Upload

from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.ods_file import OdsFileProvider
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.pptx_file import PptxFileProvider
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.providers.zip_file import ZipFileProvider
from faker_file.storages.filesystem import FileSystemStorage

__all__ = (
    "DocxUploadFactory",
    "OdsUploadFactory",
    "PdfUploadFactory",
    "PptxUploadFactory",
    "TxtUploadFactory",
    "UploadFactory",
    "ZipUploadFactory",
)

# Faker._DEFAULT_LOCALE = "hy_AM"
Faker.add_provider(DocxFileProvider)
Faker.add_provider(OdsFileProvider)
Faker.add_provider(PdfFileProvider)
Faker.add_provider(PptxFileProvider)
Faker.add_provider(TxtFileProvider)
Faker.add_provider(ZipFileProvider)


STORAGE = FileSystemStorage(root_path="", rel_path="tmp")


class AbstractUploadFactory(SQLAlchemyModelFactory):
    """Base Upload factory.

    Usage example:

        import sqlalchemy_factories as factories
        from faker_file_admin import app, db

        with app.app_context():
            document = factories.DocxUploadFactory()
            db.session.commit()
    """

    id = Sequence(lambda n: n)
    name = Faker("text", max_nb_chars=100)
    description = Faker("text", max_nb_chars=1000)

    class Meta:
        """Meta class."""

        model = Upload
        sqlalchemy_session = db.session  # the SQLAlchemy session object
        abstract = True


class DocxUploadFactory(AbstractUploadFactory):
    """DOCX Upload factory."""

    file = Faker("docx_file", storage=STORAGE)


class OdsUploadFactory(AbstractUploadFactory):
    """ODS Upload factory."""

    file = Faker("ods_file", storage=STORAGE)


class PptxUploadFactory(AbstractUploadFactory):
    """PPTX Upload factory."""

    file = Faker("pptx_file", storage=STORAGE)


class PdfUploadFactory(AbstractUploadFactory):
    """PDF Upload factory."""

    file = Faker("pdf_file", storage=STORAGE)


class TxtUploadFactory(AbstractUploadFactory):
    """TXT Upload factory."""

    file = Faker("txt_file", storage=STORAGE)


class ZipUploadFactory(AbstractUploadFactory):
    """ZIP Upload factory."""

    file = Faker("zip_file", storage=STORAGE)


PROVIDER_CHOICES = [
    lambda: DocxFileProvider(None).docx_file(storage=STORAGE),
    lambda: PdfFileProvider(None).pdf_file(storage=STORAGE),
    lambda: PptxFileProvider(None).pptx_file(storage=STORAGE),
    lambda: TxtFileProvider(None).txt_file(storage=STORAGE),
    lambda: ZipFileProvider(None).zip_file(storage=STORAGE),
]


def pick_random_provider(*args, **kwargs):
    return choice(PROVIDER_CHOICES)()


class UploadFactory(AbstractUploadFactory):
    """Upload factory that randomly picks a file provider."""

    file = LazyAttribute(pick_random_provider)
