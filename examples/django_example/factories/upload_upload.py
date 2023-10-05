from random import choice

from django.conf import settings
from django.core.files.storage import default_storage
from factory import Faker, LazyAttribute, Trait
from factory.django import DjangoModelFactory
from faker_file.providers.bin_file import BinFileProvider
from faker_file.providers.csv_file import CsvFileProvider
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.eml_file import EmlFileProvider
from faker_file.providers.epub_file import EpubFileProvider
from faker_file.providers.ico_file import IcoFileProvider
from faker_file.providers.jpeg_file import JpegFileProvider
from faker_file.providers.mp3_file import Mp3FileProvider
from faker_file.providers.odp_file import OdpFileProvider
from faker_file.providers.ods_file import OdsFileProvider
from faker_file.providers.odt_file import OdtFileProvider
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.png_file import PngFileProvider
from faker_file.providers.pptx_file import PptxFileProvider
from faker_file.providers.rtf_file import RtfFileProvider
from faker_file.providers.svg_file import SvgFileProvider
from faker_file.providers.tar_file import TarFileProvider
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.providers.webp_file import WebpFileProvider
from faker_file.providers.xlsx_file import XlsxFileProvider
from faker_file.providers.zip_file import ZipFileProvider
from faker_file.storages.aws_s3 import AWSS3Storage
from faker_file.storages.filesystem import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage

from upload.models import Upload

__all__ = ("UploadFactory",)

# Faker._DEFAULT_LOCALE = "hy_AM"
Faker.add_provider(BinFileProvider)
Faker.add_provider(CsvFileProvider)
Faker.add_provider(DocxFileProvider)
Faker.add_provider(EmlFileProvider)
Faker.add_provider(EpubFileProvider)
Faker.add_provider(IcoFileProvider)
Faker.add_provider(JpegFileProvider)
Faker.add_provider(Mp3FileProvider)
Faker.add_provider(OdpFileProvider)
Faker.add_provider(OdsFileProvider)
Faker.add_provider(OdtFileProvider)
Faker.add_provider(PdfFileProvider)
Faker.add_provider(PngFileProvider)
Faker.add_provider(PptxFileProvider)
Faker.add_provider(RtfFileProvider)
Faker.add_provider(SvgFileProvider)
Faker.add_provider(TarFileProvider)
Faker.add_provider(TxtFileProvider)
Faker.add_provider(WebpFileProvider)
Faker.add_provider(XlsxFileProvider)
Faker.add_provider(ZipFileProvider)

# Faker doesn't know anything about Django. That's why, if we want to support
# remote storages, we need to manually check which file storage backend is
# used. If `Boto3` storage backend (of the `django-storages` package) is used
# we use the correspondent `AWSS3Storage` class of the `faker-file`.
# Otherwise, fall back to native file system storage (`FileSystemStorage`) of
# the `faker-file`.
if isinstance(default_storage, S3Boto3Storage):
    STORAGE = AWSS3Storage(
        bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
        credentials={
            "key_id": settings.AWS_ACCESS_KEY_ID,
            "key_secret": settings.AWS_SECRET_ACCESS_KEY,
        },
        rel_path="tmp",
        check_bucket=False,
    )
else:
    STORAGE = FileSystemStorage(root_path=settings.MEDIA_ROOT, rel_path="tmp")


PROVIDER_CHOICES = [
    lambda: BinFileProvider(None).bin_file(storage=STORAGE),
    lambda: CsvFileProvider(None).csv_file(storage=STORAGE),
    lambda: DocxFileProvider(None).docx_file(storage=STORAGE),
    lambda: EmlFileProvider(None).eml_file(storage=STORAGE),
    lambda: EpubFileProvider(None).epub_file(storage=STORAGE),
    lambda: IcoFileProvider(None).ico_file(storage=STORAGE),
    lambda: JpegFileProvider(None).jpeg_file(storage=STORAGE),
    lambda: Mp3FileProvider(None).mp3_file(storage=STORAGE),
    lambda: OdpFileProvider(None).odp_file(storage=STORAGE),
    lambda: OdsFileProvider(None).ods_file(storage=STORAGE),
    lambda: OdtFileProvider(None).odt_file(storage=STORAGE),
    lambda: PdfFileProvider(None).pdf_file(storage=STORAGE),
    lambda: PngFileProvider(None).png_file(storage=STORAGE),
    lambda: PptxFileProvider(None).pptx_file(storage=STORAGE),
    lambda: RtfFileProvider(None).rtf_file(storage=STORAGE),
    lambda: SvgFileProvider(None).svg_file(storage=STORAGE),
    lambda: TarFileProvider(None).tar_file(storage=STORAGE),
    lambda: TxtFileProvider(None).txt_file(storage=STORAGE),
    lambda: XlsxFileProvider(None).xlsx_file(storage=STORAGE),
    lambda: ZipFileProvider(None).zip_file(storage=STORAGE),
]


def pick_random_provider(*args, **kwargs):
    return choice(PROVIDER_CHOICES)()


class AbstractUploadFactory(DjangoModelFactory):
    """Abstract Upload factory."""

    name = Faker("text", max_nb_chars=100)
    description = Faker("text", max_nb_chars=1000)

    class Meta:
        """Meta class."""

        model = Upload
        abstract = True


class UploadFactory(AbstractUploadFactory):
    """Upload factory."""

    class Params:
        bin_file = Trait(file=Faker("bin_file", storage=STORAGE))
        csv_file = Trait(file=Faker("csv_file", storage=STORAGE))
        docx_file = Trait(file=Faker("docx_file", storage=STORAGE))
        eml_file = Trait(file=Faker("eml_file", storage=STORAGE))
        epub_file = Trait(file=Faker("epub_file", storage=STORAGE))
        ico_file = Trait(file=Faker("ico_file", storage=STORAGE))
        jpeg_file = Trait(file=Faker("jpeg_file", storage=STORAGE))
        mp3_file = Trait(file=Faker("mp3_file", storage=STORAGE))
        odp_file = Trait(file=Faker("odp_file", storage=STORAGE))
        ods_file = Trait(file=Faker("ods_file", storage=STORAGE))
        odt_file = Trait(file=Faker("odt_file", storage=STORAGE))
        pdf_file = Trait(file=Faker("pdf_file", storage=STORAGE))
        png_file = Trait(file=Faker("png_file", storage=STORAGE))
        pptx_file = Trait(file=Faker("pptx_file", storage=STORAGE))
        rtf_file = Trait(file=Faker("rtf_file", storage=STORAGE))
        svg_file = Trait(file=Faker("svg_file", storage=STORAGE))
        tar_file = Trait(file=Faker("tar_file", storage=STORAGE))
        txt_file = Trait(file=Faker("txt_file", storage=STORAGE))
        webp_file = Trait(file=Faker("webp_file", storage=STORAGE))
        xlsx_file = Trait(file=Faker("xlsx_file", storage=STORAGE))
        zip_file = Trait(file=Faker("zip_file", storage=STORAGE))
        random_file = Trait(file=LazyAttribute(pick_random_provider))
