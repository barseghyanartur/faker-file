# Imports and initialization
from faker import Faker
from faker_file.providers.augment_file_from_dir import (
    AugmentFileFromDirProvider,
)
from faker_file.providers.bin_file import BinFileProvider
from faker_file.providers.bmp_file import BmpFileProvider
from faker_file.providers.csv_file import CsvFileProvider
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.eml_file import EmlFileProvider
from faker_file.providers.epub_file import EpubFileProvider
from faker_file.providers.gif_file import GifFileProvider
from faker_file.providers.ico_file import (
    GraphicIcoFileProvider,
    IcoFileProvider,
)
from faker_file.providers.jpeg_file import (
    GraphicJpegFileProvider,
    JpegFileProvider,
)
from faker_file.providers.mp3_file import Mp3FileProvider
from faker_file.providers.odp_file import OdpFileProvider
from faker_file.providers.ods_file import OdsFileProvider
from faker_file.providers.odt_file import OdtFileProvider
from faker_file.providers.pdf_file import (
    GraphicPdfFileProvider,
    PdfFileProvider,
)
from faker_file.providers.png_file import (
    GraphicPngFileProvider,
    PngFileProvider,
)
from faker_file.providers.pptx_file import PptxFileProvider
from faker_file.providers.random_file_from_dir import RandomFileFromDirProvider
from faker_file.providers.rtf_file import RtfFileProvider
from faker_file.providers.svg_file import SvgFileProvider
from faker_file.providers.tar_file import TarFileProvider
from faker_file.providers.tiff_file import TiffFileProvider
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.providers.webp_file import (
    GraphicWebpFileProvider,
    WebpFileProvider,
)
from faker_file.providers.xlsx_file import XlsxFileProvider
from faker_file.providers.zip_file import ZipFileProvider

FAKER = Faker()
FAKER.add_provider(AugmentFileFromDirProvider)
FAKER.add_provider(BinFileProvider)
FAKER.add_provider(BmpFileProvider)
FAKER.add_provider(CsvFileProvider)
FAKER.add_provider(DocxFileProvider)
FAKER.add_provider(EmlFileProvider)
FAKER.add_provider(EpubFileProvider)
FAKER.add_provider(GifFileProvider)
FAKER.add_provider(GraphicIcoFileProvider)
FAKER.add_provider(GraphicJpegFileProvider)
FAKER.add_provider(GraphicPdfFileProvider)
FAKER.add_provider(GraphicPngFileProvider)
FAKER.add_provider(GraphicWebpFileProvider)
FAKER.add_provider(IcoFileProvider)
FAKER.add_provider(JpegFileProvider)
FAKER.add_provider(Mp3FileProvider)
FAKER.add_provider(OdpFileProvider)
FAKER.add_provider(OdsFileProvider)
FAKER.add_provider(OdtFileProvider)
FAKER.add_provider(PdfFileProvider)
FAKER.add_provider(PngFileProvider)
FAKER.add_provider(PptxFileProvider)
FAKER.add_provider(RandomFileFromDirProvider)
FAKER.add_provider(RtfFileProvider)
FAKER.add_provider(SvgFileProvider)
FAKER.add_provider(TarFileProvider)
FAKER.add_provider(TiffFileProvider)
FAKER.add_provider(TxtFileProvider)
FAKER.add_provider(WebpFileProvider)
FAKER.add_provider(XlsxFileProvider)
FAKER.add_provider(ZipFileProvider)

# Create files to test `augment_file_from_dir` with
FAKER.docx_file()
FAKER.eml_file()
FAKER.odt_file()
FAKER.txt_file()

# Usage examples
# augmented_file = FAKER.augment_file_from_dir(
#     source_dir_path="/tmp/tmp/",
# )
bin_file = FAKER.bin_file()
bmp_file = FAKER.bmp_file()
csv_file = FAKER.csv_file()
docx_file = FAKER.docx_file()
eml_file = FAKER.eml_file()
epub_file = FAKER.epub_file()
gif_file = FAKER.gif_file()
graphic_ico_file = FAKER.graphic_ico_file()
graphic_jpeg_file = FAKER.graphic_jpeg_file()
graphic_pdf_file = FAKER.graphic_pdf_file()
graphic_png_file = FAKER.graphic_png_file()
graphic_webp_file = FAKER.graphic_webp_file()
ico_file = FAKER.ico_file()
jpeg_file = FAKER.jpeg_file()
mp3_file = FAKER.mp3_file()
odp_file = FAKER.odp_file()
ods_file = FAKER.ods_file()
odt_file = FAKER.odt_file()
pdf_file = FAKER.pdf_file()
png_file = FAKER.png_file()
pptx_file = FAKER.pptx_file()
random_file = FAKER.random_file_from_dir(
    source_dir_path="/tmp/tmp/",
)
rtf_file = FAKER.rtf_file()
svg_file = FAKER.svg_file()
tar_file = FAKER.tar_file()
tiff_file = FAKER.tiff_file()
txt_file = FAKER.txt_file()
# webp_file = FAKER.webp_file()
xlsx_file = FAKER.xlsx_file()
zip_file = FAKER.zip_file()

# Usage examples bytes back
# augmented_raw = FAKER.augment_file_from_dir(
#     source_dir_path="/tmp/tmp/",
#     raw=True,
# )
bin_raw = FAKER.bin_file(raw=True)
bmp_raw = FAKER.bmp_file(raw=True)
csv_raw = FAKER.csv_file(raw=True)
docx_raw = FAKER.docx_file(raw=True)
eml_raw = FAKER.eml_file(raw=True)
epub_raw = FAKER.epub_file(raw=True)
gif_raw = FAKER.gif_file(raw=True)
ico_raw = FAKER.ico_file(raw=True)
jpeg_raw = FAKER.jpeg_file(raw=True)
mp3_raw = FAKER.mp3_file(raw=True)
odp_raw = FAKER.odp_file(raw=True)
ods_raw = FAKER.ods_file(raw=True)
odt_raw = FAKER.odt_file(raw=True)
pdf_raw = FAKER.pdf_file(raw=True)
png_raw = FAKER.png_file(raw=True)
pptx_raw = FAKER.pptx_file(raw=True)
random_raw = FAKER.random_file_from_dir(
    source_dir_path="/tmp/tmp/",
    raw=True,
)
rtf_raw = FAKER.rtf_file(raw=True)
svg_raw = FAKER.svg_file(raw=True)
tar_raw = FAKER.tar_file(raw=True)
tiff_raw = FAKER.tiff_file(raw=True)
txt_raw = FAKER.txt_file(raw=True)
# webp_raw = FAKER.webp_file(raw=True)
xlsx_raw = FAKER.xlsx_file(raw=True)
zip_raw = FAKER.zip_file(raw=True)
