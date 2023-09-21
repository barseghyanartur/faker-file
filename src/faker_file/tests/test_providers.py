import logging
import os.path
import tempfile
import unittest
from copy import deepcopy
from functools import partial
from importlib import import_module, reload
from io import BytesIO
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

import pytest
from faker import Faker
from parametrize import parametrize
from pathy import use_fs
from PIL import Image, ImageDraw

from ..base import DEFAULT_REL_PATH, DynamicTemplate, pystr_format_func
from ..constants import (
    DEFAULT_FILE_ENCODING,
    DEFAULT_FONT_NAME,
    DEFAULT_FONT_PATH,
    DEFAULT_TEXT_CONTENT_TEMPLATE,
)
from ..contrib.docx_file import (
    add_h1_heading as docx_add_h1_heading,
    add_h2_heading as docx_add_h2_heading,
    add_h3_heading as docx_add_h3_heading,
    add_h4_heading as docx_add_h4_heading,
    add_h5_heading as docx_add_h5_heading,
    add_h6_heading as docx_add_h6_heading,
    add_page_break as docx_add_page_break,
    add_paragraph as docx_add_paragraph,
    add_picture as docx_add_picture,
    add_table as docx_add_table,
    add_title_heading as docx_add_title_heading,
)
from ..contrib.image.imgkit_snippets import (
    add_h1_heading as image_imgkit_add_h1_heading,
    add_h2_heading as image_imgkit_add_h2_heading,
    add_h3_heading as image_imgkit_add_h3_heading,
    add_h4_heading as image_imgkit_add_h4_heading,
    add_h5_heading as image_imgkit_add_h5_heading,
    add_h6_heading as image_imgkit_add_h6_heading,
    add_page_break as image_imgkit_add_page_break,
    add_paragraph as image_imgkit_add_paragraph,
    add_picture as image_imgkit_add_picture,
    add_table as image_imgkit_add_table,
)
from ..contrib.image.pil_snippets import (
    add_h1_heading as image_pil_add_h1_heading,
    add_h2_heading as image_pil_add_h2_heading,
    add_h3_heading as image_pil_add_h3_heading,
    add_h4_heading as image_pil_add_h4_heading,
    add_h5_heading as image_pil_add_h5_heading,
    add_h6_heading as image_pil_add_h6_heading,
    add_page_break as image_pil_add_page_break,
    add_paragraph as image_pil_add_paragraph,
    add_picture as image_pil_add_picture,
    add_table as image_pil_add_table,
)
from ..contrib.image.weasyprint_snippets import (
    add_h1_heading as image_weasyprint_add_h1_heading,
    add_h2_heading as image_weasyprint_add_h2_heading,
    add_h3_heading as image_weasyprint_add_h3_heading,
    add_h4_heading as image_weasyprint_add_h4_heading,
    add_h5_heading as image_weasyprint_add_h5_heading,
    add_h6_heading as image_weasyprint_add_h6_heading,
    add_heading as image_weasyprint_add_heading,
    add_page_break as image_weasyprint_add_page_break,
    add_paragraph as image_weasyprint_add_paragraph,
    add_picture as image_weasyprint_add_picture,
    add_table as image_weasyprint_add_table,
)
from ..contrib.odt_file import (
    add_h1_heading as odt_add_h1_heading,
    add_h2_heading as odt_add_h2_heading,
    add_h3_heading as odt_add_h3_heading,
    add_h4_heading as odt_add_h4_heading,
    add_h5_heading as odt_add_h5_heading,
    add_h6_heading as odt_add_h6_heading,
    add_page_break as odt_add_page_break,
    add_paragraph as odt_add_paragraph,
    add_picture as odt_add_picture,
    add_table as odt_add_table,
)
from ..contrib.pdf_file.pdfkit_snippets import (
    add_h1_heading as pdf_pdfkit_add_h1_heading,
    add_h2_heading as pdf_pdfkit_add_h2_heading,
    add_h3_heading as pdf_pdfkit_add_h3_heading,
    add_h4_heading as pdf_pdfkit_add_h4_heading,
    add_h5_heading as pdf_pdfkit_add_h5_heading,
    add_h6_heading as pdf_pdfkit_add_h6_heading,
    add_heading as pdf_pdfkit_add_heading,
    add_page_break as pdf_pdfkit_add_page_break,
    add_paragraph as pdf_pdfkit_add_paragraph,
    add_picture as pdf_pdfkit_add_picture,
    add_table as pdf_pdfkit_add_table,
)
from ..contrib.pdf_file.pil_snippets import (
    add_h1_heading as pdf_pil_add_h1_heading,
    add_h2_heading as pdf_pil_add_h2_heading,
    add_h3_heading as pdf_pil_add_h3_heading,
    add_h4_heading as pdf_pil_add_h4_heading,
    add_h5_heading as pdf_pil_add_h5_heading,
    add_h6_heading as pdf_pil_add_h6_heading,
    add_heading as pdf_pil_add_heading,
    add_page_break as pdf_pil_add_page_break,
    add_paragraph as pdf_pil_add_paragraph,
    add_picture as pdf_pil_add_picture,
    add_table as pdf_pil_add_table,
)
from ..contrib.pdf_file.reportlab_snippets import (
    add_h1_heading as pdf_reportlab_add_h1_heading,
    add_h2_heading as pdf_reportlab_add_h2_heading,
    add_h3_heading as pdf_reportlab_add_h3_heading,
    add_h4_heading as pdf_reportlab_add_h4_heading,
    add_h5_heading as pdf_reportlab_add_h5_heading,
    add_h6_heading as pdf_reportlab_add_h6_heading,
    add_heading as pdf_reportlab_add_heading,
    add_page_break as pdf_reportlab_add_page_break,
    add_paragraph as pdf_reportlab_add_paragraph,
    add_picture as pdf_reportlab_add_picture,
    add_table as pdf_reportlab_add_table,
)
from ..helpers import load_class_from_path
from ..providers.augment_image_from_path import AugmentImageFromPathProvider
from ..providers.augment_random_image_from_dir import (
    AugmentRandomImageFromDirProvider,
)
from ..providers.base.image_generator import BaseImageGenerator
from ..providers.base.mp3_generator import BaseMp3Generator
from ..providers.base.pdf_generator import BasePdfGenerator
from ..providers.bin_file import BinFileProvider
from ..providers.bmp_file import BmpFileProvider, GraphicBmpFileProvider
from ..providers.csv_file import CsvFileProvider
from ..providers.docx_file import DocxFileProvider
from ..providers.eml_file import EmlFileProvider
from ..providers.epub_file import EpubFileProvider
from ..providers.file_from_path import FileFromPathProvider
from ..providers.generic_file import GenericFileProvider
from ..providers.gif_file import GifFileProvider, GraphicGifFileProvider
from ..providers.helpers.inner import (
    create_inner_augment_image_from_path,
    create_inner_augment_random_image_from_dir,
    create_inner_bin_file,
    create_inner_csv_file,
    create_inner_docx_file,
    create_inner_eml_file,
    create_inner_epub_file,
    create_inner_file_from_path,
    create_inner_generic_file,
    create_inner_graphic_ico_file,
    create_inner_graphic_jpeg_file,
    create_inner_graphic_pdf_file,
    create_inner_graphic_png_file,
    create_inner_graphic_webp_file,
    create_inner_ico_file,
    create_inner_jpeg_file,
    create_inner_json_file,
    create_inner_mp3_file,
    create_inner_odp_file,
    create_inner_ods_file,
    create_inner_odt_file,
    create_inner_pdf_file,
    create_inner_png_file,
    create_inner_pptx_file,
    create_inner_random_file_from_dir,
    create_inner_rtf_file,
    create_inner_svg_file,
    create_inner_tar_file,
    create_inner_txt_file,
    create_inner_webp_file,
    create_inner_xlsx_file,
    create_inner_xml_file,
    create_inner_zip_file,
    fuzzy_choice_create_inner_file,
    list_create_inner_file,
)
from ..providers.ico_file import GraphicIcoFileProvider, IcoFileProvider
from ..providers.image.augment import color_jitter, equalize, random_crop
from ..providers.jpeg_file import GraphicJpegFileProvider, JpegFileProvider
from ..providers.json_file import JsonFileProvider
from ..providers.mixins.image_mixin import (
    IMAGEKIT_IMAGE_GENERATOR,
    PIL_IMAGE_GENERATOR,
    WEASYPRINT_IMAGE_GENERATOR,
)
from ..providers.mp3_file import (
    EDGE_TTS_MP3_GENERATOR,
    GTTS_MP3_GENERATOR,
    Mp3FileProvider,
)
from ..providers.mp3_file.generators.edge_tts_generator import (
    EdgeTtsMp3Generator,
)
from ..providers.mp3_file.generators.gtts_generator import GttsMp3Generator
from ..providers.odp_file import OdpFileProvider
from ..providers.ods_file import OdsFileProvider
from ..providers.odt_file import OdtFileProvider
from ..providers.pdf_file import (
    PDFKIT_PDF_GENERATOR,
    PIL_PDF_GENERATOR,
    REPORTLAB_PDF_GENERATOR,
    GraphicPdfFileProvider,
    PdfFileProvider,
)
from ..providers.pdf_file.generators.pdfkit_generator import PdfkitPdfGenerator
from ..providers.pdf_file.generators.reportlab_generator import (
    ReportlabPdfGenerator,
)
from ..providers.png_file import GraphicPngFileProvider, PngFileProvider
from ..providers.pptx_file import PptxFileProvider
from ..providers.random_file_from_dir import RandomFileFromDirProvider
from ..providers.rtf_file import RtfFileProvider
from ..providers.svg_file import SvgFileProvider
from ..providers.tar_file import TarFileProvider
from ..providers.tiff_file import GraphicTiffFileProvider, TiffFileProvider
from ..providers.txt_file import TxtFileProvider
from ..providers.webp_file import GraphicWebpFileProvider, WebpFileProvider
from ..providers.xlsx_file import XlsxFileProvider
from ..providers.xml_file import XmlFileProvider
from ..providers.zip_file import ZipFileProvider
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.cloud import PathyFileSystemStorage
from ..storages.filesystem import FileSystemStorage
from .data import (
    DOCX_KWARGS,
    XML_DOWNLOAD_KWARGS,
    XML_ISBN_KWARGS,
    XML_METADATA_KWARGS,
)
from .texts import TEXT_PDF

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("ProvidersTestCase",)


FileProvider = Union[
    AugmentImageFromPathProvider,
    AugmentRandomImageFromDirProvider,
    BinFileProvider,
    BmpFileProvider,
    CsvFileProvider,
    DocxFileProvider,
    EmlFileProvider,
    EpubFileProvider,
    FileFromPathProvider,
    GenericFileProvider,
    GraphicBmpFileProvider,
    GraphicIcoFileProvider,
    GraphicGifFileProvider,
    GraphicJpegFileProvider,
    GraphicPdfFileProvider,
    GraphicPngFileProvider,
    GraphicTiffFileProvider,
    GraphicWebpFileProvider,
    GifFileProvider,
    IcoFileProvider,
    JpegFileProvider,
    JsonFileProvider,
    Mp3FileProvider,
    OdpFileProvider,
    OdsFileProvider,
    OdtFileProvider,
    PdfFileProvider,
    PngFileProvider,
    PptxFileProvider,
    RandomFileFromDirProvider,
    RtfFileProvider,
    SvgFileProvider,
    TarFileProvider,
    TiffFileProvider,
    TxtFileProvider,
    WebpFileProvider,
    XlsxFileProvider,
    XmlFileProvider,
    ZipFileProvider,
]

FAKER = Faker()
FAKER_HY = Faker(locale="hy_AM")
FS_STORAGE = FileSystemStorage()
PATHY_FS_STORAGE = PathyFileSystemStorage(bucket_name="tmp", rel_path="tmp")

SOURCE_FILE_FROM_PATH_FILENAME = FS_STORAGE.generate_filename(extension="txt")
SOURCE_BMP_FILE_FROM_PATH_FILENAME = FS_STORAGE.generate_filename(
    extension=GraphicBmpFileProvider.extension
)
SOURCE_GIF_FILE_FROM_PATH_FILENAME = FS_STORAGE.generate_filename(
    extension=GraphicGifFileProvider.extension
)
SOURCE_ICO_FILE_FROM_PATH_FILENAME = FS_STORAGE.generate_filename(
    extension=GraphicIcoFileProvider.extension
)
SOURCE_JPEG_FILE_FROM_PATH_FILENAME = FS_STORAGE.generate_filename(
    extension=GraphicJpegFileProvider.extension
)
SOURCE_PNG_FILE_FROM_PATH_FILENAME = FS_STORAGE.generate_filename(
    extension=GraphicPngFileProvider.extension
)
# SOURCE_SVG_FILE_FROM_PATH_FILENAME = FS_STORAGE.generate_filename(
#     extension=GraphicSvgFileProvider.extension
# )
SOURCE_TIFF_FILE_FROM_PATH_FILENAME = FS_STORAGE.generate_filename(
    extension=GraphicTiffFileProvider.extension
)
SOURCE_WEBP_FILE_FROM_PATH_FILENAME = FS_STORAGE.generate_filename(
    extension=GraphicWebpFileProvider.extension
)

pdf_pdfkit_add_non_existing_heading = partial(pdf_pdfkit_add_heading, level=0)
pdf_pil_add_non_existing_heading = partial(pdf_pil_add_heading, level=0)
pdf_reportlab_add_non_existing_heading = partial(
    pdf_reportlab_add_heading, level=0
)
image_weasyprint_add_non_existing_heading = partial(
    image_weasyprint_add_heading, level=0
)

logging.getLogger("fontTools").setLevel(logging.WARNING)


def generate_image_bytes(
    width: int = 100, height: int = 100, image_mode: str = "RGBA"
) -> bytes:
    """Generate an image.

    Usage example:

    .. code-block:: python

        image_bytes = generate_rgba_image_bytes()
    """
    # Create a new image with RGBA mode
    image_with_alpha = Image.new(
        image_mode,
        (width, height),
        (255, 255, 255, 255),
    )

    # Draw a red rectangle with partial transparency
    draw = ImageDraw.Draw(image_with_alpha)
    draw.rectangle(((20.0, 20.0), (80.0, 80.0)), fill=(255, 0, 0, 128))

    # Save to a BytesIO object
    stream = BytesIO()
    image_with_alpha.save(stream, "PNG")

    # Get the byte array of the image
    return stream.getvalue()


def create_test_files():
    """Create test files for `random_file_from_dir` and `file_from_path`.

    The following is important since some of the file providers
    such as RandomFileFromDirProvider or FileFromPathProvider,
    rely on physical presence of files.
    """
    source_file_from_path = Path(SOURCE_FILE_FROM_PATH_FILENAME)
    TxtFileProvider(FAKER).txt_file(
        basename=source_file_from_path.stem, max_nb_chars=100
    )

    # BMP
    source_bmp_file_from_path = Path(SOURCE_BMP_FILE_FROM_PATH_FILENAME)
    GraphicBmpFileProvider(FAKER).graphic_bmp_file(
        basename=source_bmp_file_from_path.stem
    )

    # GIF
    source_gif_file_from_path = Path(SOURCE_GIF_FILE_FROM_PATH_FILENAME)
    GraphicGifFileProvider(FAKER).graphic_gif_file(
        basename=source_gif_file_from_path.stem
    )

    # ICO
    source_ico_file_from_path = Path(SOURCE_ICO_FILE_FROM_PATH_FILENAME)
    GraphicIcoFileProvider(FAKER).graphic_ico_file(
        basename=source_ico_file_from_path.stem
    )

    # JPG
    source_jpeg_file_from_path = Path(SOURCE_JPEG_FILE_FROM_PATH_FILENAME)
    GraphicJpegFileProvider(FAKER).graphic_jpeg_file(
        basename=source_jpeg_file_from_path.stem
    )

    # PNG
    source_png_file_from_path = Path(SOURCE_PNG_FILE_FROM_PATH_FILENAME)
    GraphicPngFileProvider(FAKER).graphic_png_file(
        basename=source_png_file_from_path.stem
    )

    # # SVG
    # source_svg_file_from_path = Path(SOURCE_SVG_FILE_FROM_PATH_FILENAME)
    # GraphicSvgFileProvider(FAKER).graphic_svg_file(
    #     basename=source_svg_file_from_path.stem
    # )

    # TIF
    source_tiff_file_from_path = Path(SOURCE_TIFF_FILE_FROM_PATH_FILENAME)
    GraphicTiffFileProvider(FAKER).graphic_tiff_file(
        basename=source_tiff_file_from_path.stem
    )

    # WEBP
    source_webp_file_from_path = Path(SOURCE_WEBP_FILE_FROM_PATH_FILENAME)
    GraphicWebpFileProvider(FAKER).graphic_webp_file(
        basename=source_webp_file_from_path.stem
    )


class ProvidersTestCase(unittest.TestCase):
    """Providers test case."""

    # fake, provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # BIN
        (FAKER, BinFileProvider, "bin_file", {}, None),
        (FAKER, BinFileProvider, "bin_file", {}, False),
        (FAKER, BinFileProvider, "bin_file", {}, PATHY_FS_STORAGE),
        # BMP
        (FAKER, BmpFileProvider, "bmp_file", {}, None),
        (
            FAKER,
            BmpFileProvider,
            "bmp_file",
            {"image_generator_cls": PIL_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            BmpFileProvider,
            "bmp_file",
            {"image_generator_cls": WEASYPRINT_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            BmpFileProvider,
            "bmp_file",
            {"image_generator_cls": IMAGEKIT_IMAGE_GENERATOR},
            None,
        ),
        (FAKER, BmpFileProvider, "bmp_file", {}, False),
        (FAKER, BmpFileProvider, "bmp_file", {}, PATHY_FS_STORAGE),
        (FAKER, GraphicBmpFileProvider, "graphic_bmp_file", {}, None),
        # CSV
        (FAKER, CsvFileProvider, "csv_file", {}, None),
        (FAKER_HY, CsvFileProvider, "csv_file", {}, None),
        (FAKER, CsvFileProvider, "csv_file", {}, False),
        (FAKER, CsvFileProvider, "csv_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            CsvFileProvider,
            "csv_file",
            {"content": "{{name}},{{date}}"},
            None,
        ),
        (
            FAKER,
            CsvFileProvider,
            "csv_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # DOCX
        (FAKER, DocxFileProvider, "docx_file", {}, None),
        (FAKER_HY, DocxFileProvider, "docx_file", {}, None),
        (FAKER, DocxFileProvider, "docx_file", {}, False),
        (FAKER, DocxFileProvider, "docx_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            DocxFileProvider,
            "docx_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            DocxFileProvider,
            "docx_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        (
            FAKER,
            DocxFileProvider,
            "docx_file",
            {
                "content": DynamicTemplate(
                    [
                        (docx_add_title_heading, {}),
                        (docx_add_h1_heading, {}),
                        (docx_add_h2_heading, {}),
                        (docx_add_h3_heading, {}),
                        (docx_add_h4_heading, {}),
                        (docx_add_h5_heading, {}),
                        (docx_add_h6_heading, {}),
                        (docx_add_picture, {}),
                        (docx_add_paragraph, {}),
                        (docx_add_page_break, {}),
                        (docx_add_h6_heading, {}),
                        (docx_add_table, {}),
                    ]
                ),
            },
            None,
        ),
        (
            FAKER,
            DocxFileProvider,
            "docx_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # EML
        (FAKER, EmlFileProvider, "eml_file", {}, None),
        (FAKER_HY, EmlFileProvider, "eml_file", {}, None),
        (
            FAKER,
            EmlFileProvider,
            "eml_file",
            {
                "options": {
                    "count": 5,
                    "create_inner_file_func": create_inner_docx_file,
                    "create_inner_file_args": {
                        "prefix": "zzz_file_",
                        "max_nb_chars": 1_024,
                        "content": "{{date}}\r\n{{text}}\r\n{{name}}",
                    },
                }
            },
            None,
        ),
        (FAKER, EmlFileProvider, "eml_file", {}, False),
        (FAKER, EmlFileProvider, "eml_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            EmlFileProvider,
            "eml_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            EmlFileProvider,
            "eml_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        (
            FAKER,
            EmlFileProvider,
            "eml_file",
            {
                "basename": "alice-looking-through-the-glass",
                "options": {
                    "create_inner_file_func": list_create_inner_file,
                    "create_inner_file_args": {
                        "func_list": [
                            (create_inner_xml_file, XML_METADATA_KWARGS),
                            (create_inner_xml_file, XML_ISBN_KWARGS),
                            (create_inner_docx_file, DOCX_KWARGS),
                        ]
                    },
                },
            },
            None,
        ),
        (
            FAKER,
            EmlFileProvider,
            "eml_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # EPUB
        (FAKER, EpubFileProvider, "epub_file", {}, None),
        (FAKER_HY, EpubFileProvider, "epub_file", {}, None),
        (FAKER, EpubFileProvider, "epub_file", {}, False),
        (FAKER, EpubFileProvider, "epub_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            EpubFileProvider,
            "epub_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            EpubFileProvider,
            "epub_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        (
            FAKER,
            EpubFileProvider,
            "epub_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # Generic
        (
            FAKER,
            GenericFileProvider,
            "generic_file",
            {
                "content": "<html><body><p>{{text}}</p></body></html>",
                "extension": "html",
            },
            None,
        ),
        (
            FAKER_HY,
            GenericFileProvider,
            "generic_file",
            {
                "content": "<html><body><p>{{text}}</p></body></html>",
                "extension": "html",
            },
            None,
        ),
        (
            FAKER,
            GenericFileProvider,
            "generic_file",
            {
                "content": "<html><body><p>{{text}}</p></body></html>",
                "extension": "html",
            },
            False,
        ),
        (
            FAKER,
            GenericFileProvider,
            "generic_file",
            {
                "content": "<html><body><p>{{text}}</p></body></html>",
                "extension": "html",
            },
            PATHY_FS_STORAGE,
        ),
        (
            FAKER,
            GenericFileProvider,
            "generic_file",
            {
                "content": "<html><body><p>{{text}}</p></body></html>",
                "extension": "html",
                "basename": "index",
            },
            None,
        ),
        (
            FAKER,
            GenericFileProvider,
            "generic_file",
            {
                "content": b"<html><body><p>Hello world</p></body></html>",
                "extension": "html",
                "prefix": "index_",
            },
            None,
        ),
        (
            FAKER,
            GenericFileProvider,
            "generic_file",
            {
                "content": b"<html><body><p>{{text}}</p></body></html>",
                "extension": "html",
                "format_func": pystr_format_func,
            },
            None,
        ),
        # GIF
        (FAKER, GifFileProvider, "gif_file", {}, None),
        (FAKER_HY, GifFileProvider, "gif_file", {}, None),
        (
            FAKER,
            GifFileProvider,
            "gif_file",
            {"image_generator_cls": PIL_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            GifFileProvider,
            "gif_file",
            {"image_generator_cls": WEASYPRINT_IMAGE_GENERATOR},
            None,
        ),
        # Since GIF format is not supported by imgkit and wkhtmltopdf,
        # the `ImgkitImageGenerator` does not support it either.
        # (
        #     FAKER,
        #     GifFileProvider,
        #     "gif_file",
        #     {"image_generator_cls": IMAGEKIT_IMAGE_GENERATOR},
        #     None,
        # ),
        (FAKER, GifFileProvider, "gif_file", {}, False),
        (FAKER, GifFileProvider, "gif_file", {}, PATHY_FS_STORAGE),
        (FAKER, GraphicGifFileProvider, "graphic_gif_file", {}, None),
        # ICO
        (FAKER, IcoFileProvider, "ico_file", {}, None),
        (FAKER_HY, IcoFileProvider, "ico_file", {}, None),
        (
            FAKER,
            IcoFileProvider,
            "ico_file",
            {"image_generator_cls": PIL_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            IcoFileProvider,
            "ico_file",
            {"image_generator_cls": WEASYPRINT_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            IcoFileProvider,
            "ico_file",
            {"image_generator_cls": IMAGEKIT_IMAGE_GENERATOR},
            None,
        ),
        (FAKER, IcoFileProvider, "ico_file", {}, False),
        (FAKER, IcoFileProvider, "ico_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            IcoFileProvider,
            "ico_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            IcoFileProvider,
            "ico_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        (
            FAKER,
            IcoFileProvider,
            "ico_file",
            {"format_func": pystr_format_func},
            None,
        ),
        (
            FAKER,
            GraphicIcoFileProvider,
            "graphic_ico_file",
            {"size": (100, 100)},
            None,
        ),
        # JPEG
        (FAKER, JpegFileProvider, "jpeg_file", {}, None),
        (FAKER_HY, JpegFileProvider, "jpeg_file", {}, None),
        (FAKER, JpegFileProvider, "jpeg_file", {}, False),
        (FAKER, JpegFileProvider, "jpeg_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            JpegFileProvider,
            "jpeg_file",
            {"image_generator_cls": None},
            None,
        ),
        (
            FAKER,
            JpegFileProvider,
            "jpeg_file",
            {"image_generator_cls": PIL_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            JpegFileProvider,
            "jpeg_file",
            {
                "image_generator_cls": PIL_IMAGE_GENERATOR,
                "image_generator_kwargs": {
                    "encoding": "utf8",
                    "font_size": 14,
                    "page_width": 800,
                    "page_height": 1200,
                    "line_height": 16,
                    "spacing": 5,
                },
            },
            None,
        ),
        (
            FAKER,
            JpegFileProvider,
            "jpeg_file",
            {"image_generator_cls": WEASYPRINT_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            JpegFileProvider,
            "jpeg_file",
            {"image_generator_cls": IMAGEKIT_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            JpegFileProvider,
            "jpeg_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            JpegFileProvider,
            "jpeg_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        (
            FAKER,
            GraphicJpegFileProvider,
            "graphic_jpeg_file",
            {"size": (100, 100)},
            None,
        ),
        # JSON
        (FAKER, JsonFileProvider, "json_file", {}, None),
        (FAKER_HY, JsonFileProvider, "json_file", {}, None),
        (FAKER, JsonFileProvider, "json_file", {}, False),
        (FAKER, JsonFileProvider, "json_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            JsonFileProvider,
            "json_file",
            {"content": "{name: {{name}}, date: {{date}}}"},
            None,
        ),
        (
            FAKER,
            JsonFileProvider,
            "json_file",
            {"data_columns": {"name": "{{name}}", "date": "{{date}}"}},
            None,
        ),
        (
            FAKER,
            JsonFileProvider,
            "json_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # ODP
        (FAKER, OdpFileProvider, "odp_file", {}, None),
        (FAKER_HY, OdpFileProvider, "odp_file", {}, None),
        (FAKER, OdpFileProvider, "odp_file", {}, False),
        (FAKER, OdpFileProvider, "odp_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            OdpFileProvider,
            "odp_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            OdpFileProvider,
            "odp_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # ODS
        (FAKER, OdsFileProvider, "ods_file", {}, None),
        (FAKER_HY, OdsFileProvider, "ods_file", {}, None),
        (FAKER, OdsFileProvider, "ods_file", {}, False),
        (FAKER, OdsFileProvider, "ods_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            OdsFileProvider,
            "ods_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # ODT
        (FAKER, OdtFileProvider, "odt_file", {}, None),
        (FAKER_HY, OdtFileProvider, "odt_file", {}, None),
        (FAKER, OdtFileProvider, "odt_file", {}, False),
        (FAKER, OdtFileProvider, "odt_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            OdtFileProvider,
            "odt_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            OdtFileProvider,
            "odt_file",
            {
                "content": DynamicTemplate(
                    [
                        (odt_add_h1_heading, {}),
                        (odt_add_h2_heading, {}),
                        (odt_add_h3_heading, {}),
                        (odt_add_h4_heading, {}),
                        (odt_add_h5_heading, {}),
                        (odt_add_h6_heading, {}),
                        (odt_add_picture, {}),
                        (odt_add_paragraph, {}),
                        (odt_add_page_break, {}),
                        (odt_add_h6_heading, {}),
                        (odt_add_table, {}),
                    ]
                ),
            },
            None,
        ),
        (
            FAKER,
            OdtFileProvider,
            "odt_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # PDF
        (FAKER, PdfFileProvider, "pdf_file", {}, None),
        (FAKER_HY, PdfFileProvider, "pdf_file", {}, None),
        (FAKER, PdfFileProvider, "pdf_file", {}, False),
        (FAKER, PdfFileProvider, "pdf_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": ReportlabPdfGenerator,
                "pdf_generator_kwargs": {},
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": ReportlabPdfGenerator,
                "pdf_generator_kwargs": {
                    "font_name": DEFAULT_FONT_NAME,
                    "font_path": DEFAULT_FONT_PATH,
                },
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": None,
                # "pdf_generator_kwargs": {},
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": PdfkitPdfGenerator,
                "pdf_generator_kwargs": {"encoding": DEFAULT_FILE_ENCODING},
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": PDFKIT_PDF_GENERATOR,
                "pdf_generator_kwargs": {"encoding": DEFAULT_FILE_ENCODING},
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": (
                    "faker_file.providers.pdf_file.generators"
                    ".pdfkit_generator.PdfkitPdfGenerator"
                ),
                "pdf_generator_kwargs": {"encoding": DEFAULT_FILE_ENCODING},
                "content": DynamicTemplate(
                    [
                        (pdf_pdfkit_add_h1_heading, {}),
                        (pdf_pdfkit_add_h2_heading, {}),
                        (pdf_pdfkit_add_h3_heading, {}),
                        (pdf_pdfkit_add_h4_heading, {}),
                        (pdf_pdfkit_add_h5_heading, {}),
                        (pdf_pdfkit_add_h6_heading, {}),
                        (pdf_pdfkit_add_picture, {}),
                        (pdf_pdfkit_add_paragraph, {"content": TEXT_PDF}),
                        (pdf_pdfkit_add_page_break, {}),
                        (pdf_pdfkit_add_h6_heading, {}),
                        (pdf_pdfkit_add_table, {}),
                        (pdf_pdfkit_add_non_existing_heading, {}),
                    ]
                ),
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": PIL_PDF_GENERATOR,
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": PIL_PDF_GENERATOR,
                "pdf_generator_kwargs": {
                    "encoding": "utf8",
                    "font_size": 14,
                    "page_width": 800,
                    "page_height": 1200,
                    "line_height": 16,
                    "spacing": 5,
                },
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": PIL_PDF_GENERATOR,
                "pdf_generator_kwargs": {
                    "encoding": "utf8",
                    "font_size": 14,
                    "page_width": 800,
                    "page_height": 1200,
                    "line_height": 16,
                    "spacing": 5,
                },
                "content": DynamicTemplate(
                    [
                        (pdf_pil_add_h1_heading, {}),
                        (
                            pdf_pil_add_picture,
                            {"image_width": 801, "image_height": 1201},
                        ),
                        (pdf_pil_add_paragraph, {"max_nb_chars": 5_000}),
                        (pdf_pil_add_h2_heading, {}),
                        (pdf_pil_add_h3_heading, {}),
                        (pdf_pil_add_h4_heading, {}),
                        (pdf_pil_add_h5_heading, {}),
                        (pdf_pil_add_h6_heading, {}),
                        (pdf_pil_add_picture, {}),
                        (
                            pdf_pil_add_paragraph,
                            {"content": TEXT_PDF, "margin": (1, 1, 1, 1)},
                        ),
                        (pdf_pil_add_page_break, {}),
                        (pdf_pil_add_h6_heading, {}),
                        (
                            pdf_pil_add_picture,
                            {
                                "image_bytes": generate_image_bytes(
                                    image_mode="RGBA"
                                )
                            },
                        ),
                        (pdf_pil_add_table, {}),
                        (pdf_pil_add_non_existing_heading, {}),
                    ]
                ),
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": PIL_PDF_GENERATOR,
                "pdf_generator_kwargs": {
                    "encoding": "utf8",
                    "font_size": 14,
                    "page_width": 800,
                    "page_height": 1200,
                    "line_height": 16,
                    "spacing": 5,
                    "image_mode": "RGBA",
                },
                "content": DynamicTemplate(
                    [
                        (pdf_pil_add_h1_heading, {}),
                        (
                            pdf_pil_add_picture,
                            {
                                "image_bytes": generate_image_bytes(
                                    image_mode="RGB"
                                )
                            },
                        ),
                    ]
                ),
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "pdf_generator_cls": REPORTLAB_PDF_GENERATOR,
                "pdf_generator_kwargs": {},
                "content": DynamicTemplate(
                    [
                        (pdf_reportlab_add_h1_heading, {}),
                        (pdf_reportlab_add_h2_heading, {}),
                        (pdf_reportlab_add_h3_heading, {}),
                        (pdf_reportlab_add_h4_heading, {}),
                        (pdf_reportlab_add_h5_heading, {}),
                        (pdf_reportlab_add_h6_heading, {}),
                        (pdf_reportlab_add_picture, {}),
                        (pdf_reportlab_add_paragraph, {"content": TEXT_PDF}),
                        (pdf_reportlab_add_page_break, {}),
                        (pdf_reportlab_add_h6_heading, {}),
                        (pdf_reportlab_add_table, {}),
                        (pdf_reportlab_add_non_existing_heading, {}),
                    ]
                ),
            },
            None,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {"format_func": pystr_format_func},
            None,
        ),
        (
            FAKER,
            GraphicPdfFileProvider,
            "graphic_pdf_file",
            {"size": (100, 100)},
            None,
        ),
        # PNG
        (FAKER, PngFileProvider, "png_file", {}, None),
        (FAKER_HY, PngFileProvider, "png_file", {}, None),
        (
            FAKER,
            PngFileProvider,
            "png_file",
            {"image_generator_cls": PIL_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            PngFileProvider,
            "png_file",
            {"image_generator_cls": WEASYPRINT_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            PngFileProvider,
            "png_file",
            {"image_generator_cls": IMAGEKIT_IMAGE_GENERATOR},
            None,
        ),
        (FAKER, PngFileProvider, "png_file", {}, False),
        (FAKER, PngFileProvider, "png_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            PngFileProvider,
            "png_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            PngFileProvider,
            "png_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        (
            FAKER,
            GraphicPngFileProvider,
            "graphic_png_file",
            {"size": (100, 100), "image_generator_cls": None},
            None,
        ),
        (
            FAKER,
            PngFileProvider,
            "png_file",
            {
                "image_generator_cls": IMAGEKIT_IMAGE_GENERATOR,
                "content": DynamicTemplate(
                    [
                        (image_imgkit_add_h1_heading, {}),  # Add h1
                        (image_imgkit_add_h2_heading, {}),  # Add h2
                        (image_imgkit_add_h3_heading, {}),  # Add h3
                        (image_imgkit_add_h4_heading, {}),  # Add h4
                        (image_imgkit_add_h5_heading, {}),  # Add h5
                        (image_imgkit_add_h6_heading, {}),  # Add h6
                        (image_imgkit_add_paragraph, {}),  # Add paragraph
                        (image_imgkit_add_picture, {}),  # Add picture
                        (image_imgkit_add_table, {}),  # Add table
                        (image_imgkit_add_page_break, {}),  # Add page break
                    ]
                ),
            },
            None,
        ),
        (
            FAKER,
            PngFileProvider,
            "png_file",
            {
                "image_generator_cls": PIL_IMAGE_GENERATOR,
                "image_generator_kwargs": {
                    "image_mode": "RGB",
                },
                "content": DynamicTemplate(
                    [
                        (image_pil_add_h1_heading, {}),  # Add h1
                        (image_pil_add_h2_heading, {}),  # Add h2
                        (image_pil_add_h3_heading, {}),  # Add h3
                        (image_pil_add_h4_heading, {}),  # Add h4
                        (image_pil_add_h5_heading, {}),  # Add h5
                        (image_pil_add_h6_heading, {}),  # Add h6
                        (image_pil_add_paragraph, {}),  # Add paragraph
                        (image_pil_add_picture, {}),  # Add picture
                        (image_pil_add_table, {}),  # Add table
                        (image_pil_add_page_break, {}),  # Add page break
                    ]
                ),
            },
            None,
        ),
        # Testing one page
        (
            FAKER,
            PngFileProvider,
            "png_file",
            {
                "image_generator_cls": WEASYPRINT_IMAGE_GENERATOR,
                "content": DynamicTemplate(
                    [
                        (image_weasyprint_add_h1_heading, {}),  # Add h1
                    ]
                ),
            },
            None,
        ),
        (
            FAKER,
            PngFileProvider,
            "png_file",
            {
                "image_generator_cls": WEASYPRINT_IMAGE_GENERATOR,
                "image_generator_kwargs": {
                    "page_width": 800,
                    "page_height": 1200,
                    "image_mode": "RGB",
                    "wrapper_tag": "div",
                },
                "content": DynamicTemplate(
                    [
                        (image_weasyprint_add_h1_heading, {}),  # Add h1
                        (image_weasyprint_add_h2_heading, {}),  # Add h2
                        (image_weasyprint_add_h3_heading, {}),  # Add h3
                        (image_weasyprint_add_h4_heading, {}),  # Add h4
                        (image_weasyprint_add_h5_heading, {}),  # Add h5
                        (image_weasyprint_add_h6_heading, {}),  # Add h6
                        (image_weasyprint_add_non_existing_heading, {}),
                        (image_weasyprint_add_paragraph, {}),  # Add paragraph
                        (
                            image_weasyprint_add_paragraph,
                            {"max_nb_chars": 1_000},
                        ),  # Add paragraph
                        (image_weasyprint_add_picture, {}),  # Add picture
                        (image_weasyprint_add_table, {}),  # Add table
                        (image_weasyprint_add_page_break, {}),  # Add page break
                    ]
                ),
            },
            None,
        ),
        # PPTX
        (FAKER, PptxFileProvider, "pptx_file", {}, None),
        (FAKER_HY, PptxFileProvider, "pptx_file", {}, None),
        (FAKER, PptxFileProvider, "pptx_file", {}, False),
        (FAKER, PptxFileProvider, "pptx_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            PptxFileProvider,
            "pptx_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            PptxFileProvider,
            "pptx_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        (
            FAKER,
            PptxFileProvider,
            "pptx_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # RTF
        (FAKER, RtfFileProvider, "rtf_file", {}, None),
        (FAKER_HY, RtfFileProvider, "rtf_file", {}, None),
        (FAKER, RtfFileProvider, "rtf_file", {}, False),
        (FAKER, RtfFileProvider, "rtf_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            RtfFileProvider,
            "rtf_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            RtfFileProvider,
            "rtf_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        (
            FAKER,
            RtfFileProvider,
            "rtf_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # SVG
        (FAKER, SvgFileProvider, "svg_file", {}, None),
        # Since SVG is not yet supported by Pillow, it's skipped.
        # (
        #     FAKER,
        #     SvgFileProvider,
        #     "svg_file",
        #     {"image_generator_cls": PIL_IMAGE_GENERATOR},
        #     None,
        # ),
        # Since SVG is not yet supported by WeasyPrint, it's skipped.
        # (
        #     FAKER,
        #     SvgFileProvider,
        #     "svg_file",
        #     {"image_generator_cls": WEASYPRINT_IMAGE_GENERATOR},
        #     None,
        # ),
        (
            FAKER,
            SvgFileProvider,
            "svg_file",
            {"image_generator_cls": IMAGEKIT_IMAGE_GENERATOR},
            None,
        ),
        (FAKER_HY, SvgFileProvider, "svg_file", {}, None),
        (FAKER, SvgFileProvider, "svg_file", {}, False),
        (FAKER, SvgFileProvider, "svg_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            SvgFileProvider,
            "svg_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            SvgFileProvider,
            "svg_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        # TIFF
        (FAKER, TiffFileProvider, "tiff_file", {}, None),
        (FAKER_HY, TiffFileProvider, "tiff_file", {}, None),
        (
            FAKER,
            TiffFileProvider,
            "tiff_file",
            {"image_generator_cls": PIL_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            TiffFileProvider,
            "tiff_file",
            {"image_generator_cls": WEASYPRINT_IMAGE_GENERATOR},
            None,
        ),
        (FAKER, TiffFileProvider, "tiff_file", {}, False),
        (FAKER, TiffFileProvider, "tiff_file", {}, PATHY_FS_STORAGE),
        (FAKER, GraphicTiffFileProvider, "graphic_tiff_file", {}, None),
        # TAR
        (FAKER, TarFileProvider, "tar_file", {}, None),
        (FAKER, TarFileProvider, "tar_file", {}, False),
        (FAKER, TarFileProvider, "tar_file", {}, PATHY_FS_STORAGE),
        (FAKER, TarFileProvider, "tar_file", {"compression": "gz"}, None),
        (FAKER, TarFileProvider, "tar_file", {"compression": "bz2"}, None),
        (FAKER, TarFileProvider, "tar_file", {"compression": "xz"}, None),
        (
            FAKER,
            TarFileProvider,
            "tar_file",
            {
                "basename": "alice-looking-through-the-glass",
                "options": {
                    "create_inner_file_func": list_create_inner_file,
                    "create_inner_file_args": {
                        "func_list": [
                            (create_inner_xml_file, XML_METADATA_KWARGS),
                            (create_inner_xml_file, XML_ISBN_KWARGS),
                            (create_inner_docx_file, DOCX_KWARGS),
                        ]
                    },
                },
            },
            None,
        ),
        # TXT
        (FAKER, TxtFileProvider, "txt_file", {}, None),
        (FAKER_HY, TxtFileProvider, "txt_file", {}, None),
        (FAKER, TxtFileProvider, "txt_file", {}, False),
        (FAKER, TxtFileProvider, "txt_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            TxtFileProvider,
            "txt_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            FAKER,
            TxtFileProvider,
            "txt_file",
            {
                "wrap_chars_after": 40,
                "content": FAKER.text(),
            },
            None,
        ),
        (
            FAKER,
            TxtFileProvider,
            "txt_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # Defined in allow_failures
        # WEBP
        # (FAKER, WebpFileProvider, "webp_file", {}, None),
        # (FAKER, WebpFileProvider, "webp_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            GraphicWebpFileProvider,
            "graphic_webp_file",
            {"size": (100, 100)},
            None,
        ),
        # XLSX
        (FAKER, XlsxFileProvider, "xlsx_file", {}, None),
        (FAKER_HY, XlsxFileProvider, "xlsx_file", {}, None),
        (FAKER, XlsxFileProvider, "xlsx_file", {}, False),
        (FAKER, XlsxFileProvider, "xlsx_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            XlsxFileProvider,
            "xlsx_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # XML
        (FAKER, XmlFileProvider, "xml_file", {}, None),
        (FAKER_HY, XmlFileProvider, "xml_file", {}, None),
        (FAKER, XmlFileProvider, "xml_file", {}, False),
        (FAKER, XmlFileProvider, "xml_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            XmlFileProvider,
            "xml_file",
            {"format_func": pystr_format_func},
            None,
        ),
        # ZIP
        (FAKER, ZipFileProvider, "zip_file", {}, None),
        (FAKER, ZipFileProvider, "zip_file", {}, False),
        (FAKER, ZipFileProvider, "zip_file", {}, PATHY_FS_STORAGE),
        (FAKER, ZipFileProvider, "zip_file", XML_DOWNLOAD_KWARGS, None),
        (
            FAKER,
            ZipFileProvider,
            "zip_file",
            {
                "basename": "alice-looking-through-the-glass",
                "options": {
                    "create_inner_file_func": list_create_inner_file,
                    "create_inner_file_args": {
                        "func_list": [
                            (create_inner_xml_file, XML_METADATA_KWARGS),
                            (create_inner_xml_file, XML_ISBN_KWARGS),
                            (create_inner_docx_file, DOCX_KWARGS),
                        ]
                    },
                },
            },
            None,
        ),
    ]

    # provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA_RETRY_FAILURES: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # MP3
        (FAKER, Mp3FileProvider, "mp3_file", {}, None),
        (FAKER, Mp3FileProvider, "mp3_file", {}, False),
        (FAKER, Mp3FileProvider, "mp3_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            Mp3FileProvider,
            "mp3_file",
            {
                "mp3_generator_cls": EdgeTtsMp3Generator,
                "mp3_generator_kwargs": {
                    "voice": "en-GB-LibbyNeural",
                },
            },
            None,
        ),
        (
            FAKER,
            Mp3FileProvider,
            "mp3_file",
            {
                "mp3_generator_cls": GttsMp3Generator,
                "mp3_generator_kwargs": {
                    "lang": "en",
                    "tld": "co.uk",
                },
            },
            None,
        ),
        (
            FAKER,
            Mp3FileProvider,
            "mp3_file",
            {
                "mp3_generator_cls": EDGE_TTS_MP3_GENERATOR,
                "mp3_generator_kwargs": {
                    "voice": "en-GB-LibbyNeural",
                },
            },
            None,
        ),
        (
            FAKER,
            Mp3FileProvider,
            "mp3_file",
            {
                "mp3_generator_cls": GTTS_MP3_GENERATOR,
                "mp3_generator_kwargs": {
                    "lang": "en",
                    "tld": "co.uk",
                },
            },
            None,
        ),
    ]

    # fake, provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA_ALLOW_FAILURES: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # TIFF
        (
            FAKER,
            TiffFileProvider,
            "tiff_file",
            {"image_generator_cls": IMAGEKIT_IMAGE_GENERATOR},
            None,
        ),
        # WEBP
        (FAKER, WebpFileProvider, "webp_file", {}, None),
        (FAKER, WebpFileProvider, "webp_file", {}, PATHY_FS_STORAGE),
        (
            FAKER,
            WebpFileProvider,
            "webp_file",
            {"image_generator_cls": PIL_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            WebpFileProvider,
            "webp_file",
            {"image_generator_cls": WEASYPRINT_IMAGE_GENERATOR},
            None,
        ),
        (
            FAKER,
            WebpFileProvider,
            "webp_file",
            {"image_generator_cls": IMAGEKIT_IMAGE_GENERATOR},
            None,
        ),
    ]

    # create_inner_file_func, options, create_inner_file_args
    __PARAMETRIZED_DATA_ARCHIVES: List[
        Tuple[
            Optional[Callable],
            Optional[Dict[str, Any]],
            Optional[Dict[str, Any]],
        ]
    ] = [
        (None, {}, None),
        # BIN
        (create_inner_bin_file, {"content": b"Lorem ipsum"}, {}),
        # CSV
        (create_inner_csv_file, {"content": "Lorem ipsum"}, {}),
        # DOCX
        (create_inner_docx_file, {"content": "Lorem ipsum"}, {}),
        # EML
        (create_inner_eml_file, {"content": None}, {}),
        # EPUB
        (create_inner_epub_file, {"content": "Lorem ipsum"}, {}),
        # Generic
        (
            create_inner_generic_file,
            {},
            {
                "content": "<html><body><p>{{text}}</p></body></html>",
                "extension": "html",
            },
        ),
        # ICO
        (create_inner_ico_file, {"content": "Lorem ipsum"}, {}),
        (create_inner_graphic_ico_file, {"size": (100, 100)}, {}),
        # JPEG
        (create_inner_jpeg_file, {"content": "Lorem ipsum"}, {}),
        (create_inner_graphic_jpeg_file, {"size": (100, 100)}, {}),
        # JSON
        (create_inner_json_file, {"content": None}, {}),
        # MP3
        (create_inner_mp3_file, {"content": "Lorem ipsum"}, {}),
        # ODP
        (create_inner_odp_file, {"content": "Lorem ipsum"}, {}),
        # ODS
        (create_inner_ods_file, {"content": None}, {}),
        # ODT
        (create_inner_odt_file, {"content": "Lorem ipsum"}, {}),
        # PDF
        (create_inner_pdf_file, {"content": "Lorem ipsum"}, {}),
        (create_inner_graphic_pdf_file, {"size": (100, 100)}, {}),
        # PNG
        (create_inner_png_file, {"content": "Lorem ipsum"}, {}),
        (create_inner_graphic_png_file, {"size": (100, 100)}, {}),
        # PPTX
        (create_inner_pptx_file, {"content": "Lorem ipsum"}, {}),
        # RTF
        (create_inner_rtf_file, {"content": "Lorem ipsum"}, {}),
        # SVG
        (create_inner_svg_file, {"content": "Lorem ipsum"}, {}),
        # TAR
        (create_inner_tar_file, {"content": None}, {}),
        # TXT
        (create_inner_txt_file, {"content": "Lorem ipsum"}, {}),
        # WEBP
        # (create_inner_webp_file, {"content": "Lorem ipsum"}, {}),
        (create_inner_graphic_webp_file, {"size": (100, 100)}, {}),
        # XLSX
        (create_inner_xlsx_file, {"content": None}, {}),
        # XML
        (create_inner_xml_file, {"content": None}, {}),
        # ZIP
        (create_inner_zip_file, {"content": None}, {}),
        # fuzzy_choice_create_inner_file
        (
            fuzzy_choice_create_inner_file,
            {"content": None},
            {
                "func_choices": [
                    (
                        create_inner_docx_file,
                        {"storage": FS_STORAGE, "generator": FAKER},
                    ),
                    (
                        create_inner_epub_file,
                        {"storage": FS_STORAGE, "generator": FAKER},
                    ),
                    (
                        create_inner_txt_file,
                        {"storage": FS_STORAGE, "generator": FAKER},
                    ),
                ]
            },
        ),
    ]

    __RAW_PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # BIN
        (FAKER, BinFileProvider, "bin_file", {}, None),
        # CSV
        (FAKER, CsvFileProvider, "csv_file", {}, None),
        (FAKER_HY, CsvFileProvider, "csv_file", {}, None),
        # DOCX
        (FAKER, DocxFileProvider, "docx_file", {}, None),
        (FAKER_HY, DocxFileProvider, "docx_file", {}, None),
        # EML
        (FAKER, EmlFileProvider, "eml_file", {}, None),
        (FAKER_HY, EmlFileProvider, "eml_file", {}, None),
        # EPUB
        (FAKER, EpubFileProvider, "epub_file", {}, None),
        (FAKER_HY, EpubFileProvider, "epub_file", {}, None),
        # Generic
        (
            FAKER,
            GenericFileProvider,
            "generic_file",
            {
                "content": "<html><body><p>{{text}}</p></body></html>",
                "extension": "html",
            },
            None,
        ),
        (
            FAKER_HY,
            GenericFileProvider,
            "generic_file",
            {
                "content": "<html><body><p>{{text}}</p></body></html>",
                "extension": "html",
            },
            None,
        ),
        (
            FAKER,
            GenericFileProvider,
            "generic_file",
            {
                "content": "<html><body><p>{{text}}</p></body></html>",
                "extension": "html",
            },
            None,
        ),
        (
            FAKER,
            GenericFileProvider,
            "generic_file",
            {
                "content": b"<html><body><p>Hello, World</p></body></html>",
                "extension": "html",
            },
            None,
        ),
        # ICO
        (FAKER, IcoFileProvider, "ico_file", {}, None),
        (FAKER_HY, IcoFileProvider, "ico_file", {}, None),
        (
            FAKER,
            GraphicIcoFileProvider,
            "graphic_ico_file",
            {"size": (100, 100)},
            None,
        ),
        # JPEG
        (FAKER, JpegFileProvider, "jpeg_file", {}, None),
        (FAKER_HY, JpegFileProvider, "jpeg_file", {}, None),
        (
            FAKER,
            GraphicJpegFileProvider,
            "graphic_jpeg_file",
            {"size": (100, 100)},
            None,
        ),
        # JSON
        (FAKER, JsonFileProvider, "json_file", {}, None),
        (FAKER_HY, JsonFileProvider, "json_file", {}, None),
        # ODP
        (FAKER, OdpFileProvider, "odp_file", {}, None),
        (FAKER_HY, OdpFileProvider, "odp_file", {}, None),
        # ODS
        (FAKER, OdsFileProvider, "ods_file", {}, None),
        (FAKER_HY, OdsFileProvider, "ods_file", {}, None),
        # ODT
        (FAKER, OdtFileProvider, "odt_file", {}, None),
        (FAKER_HY, OdtFileProvider, "odt_file", {}, None),
        # PDF
        (FAKER, PdfFileProvider, "pdf_file", {}, None),
        (FAKER_HY, PdfFileProvider, "pdf_file", {}, None),
        (
            FAKER,
            GraphicPdfFileProvider,
            "graphic_pdf_file",
            {"size": (100, 100)},
            None,
        ),
        # PNG
        (FAKER, PngFileProvider, "png_file", {}, None),
        (FAKER_HY, PngFileProvider, "png_file", {}, None),
        (
            FAKER,
            GraphicPngFileProvider,
            "graphic_png_file",
            {"size": (100, 100)},
            None,
        ),
        # PPTX
        (FAKER, PptxFileProvider, "pptx_file", {}, None),
        (FAKER_HY, PptxFileProvider, "pptx_file", {}, None),
        # RTF
        (FAKER, RtfFileProvider, "rtf_file", {}, None),
        (FAKER_HY, RtfFileProvider, "rtf_file", {}, None),
        # SVG
        (FAKER, SvgFileProvider, "svg_file", {}, None),
        (FAKER_HY, SvgFileProvider, "svg_file", {}, None),
        # TAR
        (FAKER, TarFileProvider, "tar_file", {}, None),
        # TXT
        (FAKER, TxtFileProvider, "txt_file", {}, None),
        (FAKER_HY, TxtFileProvider, "txt_file", {}, None),
        # WEBP
        # (FAKER, WebpFileProvider, "webp_file", {}, None),
        (
            FAKER,
            GraphicWebpFileProvider,
            "graphic_webp_file",
            {"size": (100, 100)},
            None,
        ),
        # XLSX
        (FAKER, XlsxFileProvider, "xlsx_file", {}, None),
        (FAKER_HY, XlsxFileProvider, "xlsx_file", {}, None),
        # XML
        (FAKER, XmlFileProvider, "xml_file", {}, None),
        (FAKER_HY, XmlFileProvider, "xml_file", {}, None),
        # ZIP
        (FAKER, ZipFileProvider, "zip_file", {}, None),
    ]

    # provider, method_name, kwargs, storage
    __RAW_PARAMETRIZED_DATA_RETRY_FAILURES: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # MP3
        (FAKER, Mp3FileProvider, "mp3_file", {}, None),
    ]

    # fake, provider, method_name, kwargs, storage
    __RAW_PARAMETRIZED_DATA_ALLOW_FAILURES: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        (FAKER, WebpFileProvider, "webp_file", {}, None),
    ]

    def setUp(self: "ProvidersTestCase"):
        super().setUp()
        use_fs(tempfile.gettempdir())

        # The following is important since some of the file providers
        # such as RandomFileFromDirProvider or FileFromPathProvider,
        # rely on physical presence of files.
        create_test_files()

    def tearDown(self) -> None:
        super().tearDown()
        FILE_REGISTRY.clean_up()

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA,
    )
    def test_faker(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test faker provider integration."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        _kwargs["storage"] = storage
        _file = _method(**_kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA_RETRY_FAILURES,
    )
    @pytest.mark.flaky(reruns=5)
    def test_faker_retry_failures(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test faker provider integration, retry on failures."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        _kwargs["storage"] = storage
        _file = _method(**_kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA,
    )
    def test_standalone_providers(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test standalone providers."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        _provider = provider(fake)  # noqa
        _method = getattr(_provider, method_name)
        _kwargs["storage"] = storage
        _file = _method(**_kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA_RETRY_FAILURES,
    )
    @pytest.mark.flaky(reruns=5)
    def test_standalone_providers_retry_failures(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test standalone providers."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        _provider = provider(fake)  # noqa
        _method = getattr(_provider, method_name)
        _kwargs["storage"] = storage
        _file = _method(**_kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA_ALLOW_FAILURES,
    )
    @pytest.mark.xfail
    def test_standalone_providers_allow_failures(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test standalone providers, but allow failures."""
        _kwargs = deepcopy(kwargs)
        if storage is None:
            storage = FS_STORAGE
        _provider = provider(fake)  # noqa
        _method = getattr(_provider, method_name)
        _kwargs["storage"] = storage
        _file = _method(**_kwargs)
        self.assertTrue(storage.exists(_file))

    @parametrize(
        "create_inner_file_func, options, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_zip_file(
        self: "ProvidersTestCase",
        create_inner_file_func: Optional[Callable] = None,
        options: Optional[Dict[str, Any]] = None,
        create_inner_file_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Test standalone ZIP file provider."""
        _options = {}
        _options.update(options)
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

    @parametrize(
        "create_inner_file_func, options, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_tar_file(
        self: "ProvidersTestCase",
        create_inner_file_func: Optional[Callable] = None,
        options: Optional[Dict[str, Any]] = None,
        create_inner_file_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Test standalone TAR file provider."""
        _options = {}
        _options.update(options)
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = TarFileProvider(None).tar_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

    @parametrize(
        "create_inner_file_func, content",
        [
            (create_inner_webp_file, "Lorem ipsum"),
        ],
    )
    @pytest.mark.xfail
    def test_standalone_zip_file_allow_failures(
        self: "ProvidersTestCase",
        create_inner_file_func: Optional[Callable] = None,
        content: Optional[Union[str, Dict]] = None,
    ) -> None:
        """Test standalone ZIP file provider, but allow failures."""
        _options = {"content": content}
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

    @parametrize(
        "create_inner_file_func, content",
        [
            (create_inner_webp_file, "Lorem ipsum"),
        ],
    )
    @pytest.mark.xfail
    def test_standalone_tar_file_allow_failures(
        self: "ProvidersTestCase",
        create_inner_file_func: Optional[Callable] = None,
        content: Optional[Union[str, Dict]] = None,
    ) -> None:
        """Test standalone TAR file provider, but allow failures."""
        _options = {"content": content}
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        _file = TarFileProvider(None).tar_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

    @parametrize(
        "module_path, "
        "module_name, "
        "create_inner_file_func, "
        "create_inner_file_args",
        [
            # AugmentImageFromPath
            (
                "faker_file.providers.augment_image_from_path",
                "AugmentImageFromPathProvider",
                create_inner_augment_image_from_path,
                {
                    "path": SOURCE_FILE_FROM_PATH_FILENAME,
                },
            ),
            # AugmentRandomImageFromDir
            (
                "faker_file.providers.augment_random_image_from_dir",
                "AugmentRandomImageFromDirProvider",
                create_inner_augment_random_image_from_dir,
                {
                    "source_dir_path": os.path.join(
                        SOURCE_FILE_FROM_PATH_FILENAME
                    )
                },
            ),
            # BIN
            (
                "faker_file.providers.bin_file",
                "BinFileProvider",
                create_inner_bin_file,
                {},
            ),
            # CSV
            (
                "faker_file.providers.csv_file",
                "CsvFileProvider",
                create_inner_csv_file,
                {},
            ),
            # DOCX
            (
                "faker_file.providers.docx_file",
                "DocxFileProvider",
                create_inner_docx_file,
                {},
            ),
            # EML
            (
                "faker_file.providers.eml_file",
                "EmlFileProvider",
                create_inner_eml_file,
                {},
            ),
            # EPUB
            (
                "faker_file.providers.epub_file",
                "EpubFileProvider",
                create_inner_epub_file,
                {},
            ),
            # FileFromPathProvider
            (
                "faker_file.providers.file_from_path",
                "FileFromPathProvider",
                create_inner_file_from_path,
                {
                    "path": SOURCE_FILE_FROM_PATH_FILENAME,
                },
            ),
            # Generic
            (
                "faker_file.providers.generic_file",
                "GenericFileProvider",
                create_inner_generic_file,
                {
                    "content": "<html><body><p>{{text}}</p></body></html>",
                    "extension": "html",
                },
            ),
            # ICO
            (
                "faker_file.providers.ico_file",
                "IcoFileProvider",
                create_inner_ico_file,
                {},
            ),
            (
                "faker_file.providers.ico_file",
                "GraphicIcoFileProvider",
                create_inner_graphic_ico_file,
                {},
            ),
            # JPEG
            (
                "faker_file.providers.jpeg_file",
                "JpegFileProvider",
                create_inner_jpeg_file,
                {},
            ),
            (
                "faker_file.providers.jpeg_file",
                "GraphicJpegFileProvider",
                create_inner_graphic_jpeg_file,
                {},
            ),
            # JSON
            (
                "faker_file.providers.json_file",
                "JsonFileProvider",
                create_inner_json_file,
                {},
            ),
            # MP3
            (
                "faker_file.providers.mp3_file",
                "Mp3FileProvider",
                create_inner_mp3_file,
                {},
            ),
            # ODP
            (
                "faker_file.providers.odp_file",
                "OdpFileProvider",
                create_inner_odp_file,
                {},
            ),
            # ODS
            (
                "faker_file.providers.ods_file",
                "OdsFileProvider",
                create_inner_ods_file,
                {},
            ),
            # ODT
            (
                "faker_file.providers.odt_file",
                "OdtFileProvider",
                create_inner_odt_file,
                {},
            ),
            # PDF
            (
                "faker_file.providers.pdf_file",
                "PdfFileProvider",
                create_inner_pdf_file,
                {},
            ),
            (
                "faker_file.providers.pdf_file",
                "GraphicPdfFileProvider",
                create_inner_graphic_pdf_file,
                {},
            ),
            # PNG
            (
                "faker_file.providers.png_file",
                "PngFileProvider",
                create_inner_png_file,
                {},
            ),
            (
                "faker_file.providers.png_file",
                "GraphicPngFileProvider",
                create_inner_graphic_png_file,
                {},
            ),
            # PPTX
            (
                "faker_file.providers.pptx_file",
                "PptxFileProvider",
                create_inner_pptx_file,
                {},
            ),
            # RandomFileFromDirProvider
            (
                "faker_file.providers.random_file_from_dir",
                "RandomFileFromDirProvider",
                create_inner_random_file_from_dir,
                {
                    "source_dir_path": os.path.join(
                        tempfile.gettempdir(), DEFAULT_REL_PATH
                    )
                },
            ),
            # RTF
            (
                "faker_file.providers.rtf_file",
                "RtfFileProvider",
                create_inner_rtf_file,
                {},
            ),
            # SVG
            (
                "faker_file.providers.svg_file",
                "SvgFileProvider",
                create_inner_svg_file,
                {},
            ),
            # TAR
            (
                "faker_file.providers.tar_file",
                "TarFileProvider",
                create_inner_tar_file,
                {},
            ),
            # TXT
            (
                "faker_file.providers.txt_file",
                "TxtFileProvider",
                create_inner_txt_file,
                {},
            ),
            # WEBP
            (
                "faker_file.providers.webp_file",
                "WebpFileProvider",
                create_inner_webp_file,
                {},
            ),
            (
                "faker_file.providers.webp_file",
                "GraphicWebpFileProvider",
                create_inner_graphic_webp_file,
                {},
            ),
            # XLSX
            (
                "faker_file.providers.xlsx_file",
                "XlsxFileProvider",
                create_inner_xlsx_file,
                {},
            ),
            # XML
            (
                "faker_file.providers.xml_file",
                "XmlFileProvider",
                create_inner_xml_file,
                {},
            ),
            # ZIP
            (
                "faker_file.providers.zip_file",
                "ZipFileProvider",
                create_inner_zip_file,
                {},
            ),
        ],
    )
    def test_broken_imports(
        self: "ProvidersTestCase",
        module_path: str,
        module_name: str,
        create_inner_file_func: Callable,
        create_inner_file_args: Dict[str, Any],
    ) -> None:
        """Test broken imports."""
        _module = import_module(module_path)
        del _module.__dict__[module_name]
        with self.assertRaises(ImportError):
            create_inner_file_func(**create_inner_file_args)
        reload(_module)

    def test_mp3_file_generate_not_implemented_exception(
        self: "ProvidersTestCase",
    ):
        """Generating mp3_file with BaseMp3Generator should fail."""
        with self.assertRaises(NotImplementedError):
            Mp3FileProvider(FAKER).mp3_file(mp3_generator_cls=BaseMp3Generator)

        class MyMp3Generator(BaseMp3Generator):
            """Test MP3 generator."""

        with self.assertRaises(NotImplementedError):
            Mp3FileProvider(FAKER).mp3_file(mp3_generator_cls=MyMp3Generator)

    def test_pdf_file_generate_not_implemented_exception(
        self: "ProvidersTestCase",
    ):
        """Generating pdf_file with BasePdfGenerator should fail."""
        with self.assertRaises(NotImplementedError):
            PdfFileProvider(FAKER).pdf_file(pdf_generator_cls=BasePdfGenerator)

        class MyPdfGenerator(BasePdfGenerator):
            """Test PDF generator."""

        with self.assertRaises(NotImplementedError):
            PdfFileProvider(FAKER).pdf_file(pdf_generator_cls=MyPdfGenerator)

    def test_image_file_generate_not_implemented_exception(
        self: "ProvidersTestCase",
    ):
        """Generating image_file with BaseImageGenerator should fail."""
        with self.assertRaises(NotImplementedError):
            PngFileProvider(FAKER).png_file(
                image_generator_cls=BaseImageGenerator
            )

        class MyImageGenerator(BaseImageGenerator):
            """Test image generator."""

        with self.assertRaises(NotImplementedError):
            PngFileProvider(FAKER).png_file(
                image_generator_cls=MyImageGenerator
            )

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __RAW_PARAMETRIZED_DATA,
    )
    def test_raw_standalone_providers(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test standalone providers with raw=True."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        _provider = provider(fake)  # noqa
        _method = getattr(_provider, method_name)
        _kwargs["storage"] = storage
        _kwargs["raw"] = True
        _bytes = _method(**_kwargs)
        self.assertIsInstance(_bytes, bytes)
        self.assertGreater(len(_bytes), 0)

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __RAW_PARAMETRIZED_DATA_RETRY_FAILURES,
    )
    @pytest.mark.flaky(reruns=5)
    def test_raw_standalone_providers_retry_failures(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test standalone providers."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        _provider = provider(fake)  # noqa
        _method = getattr(_provider, method_name)
        _kwargs["storage"] = storage
        _kwargs["raw"] = True
        _bytes = _method(**_kwargs)
        self.assertIsInstance(_bytes, bytes)
        self.assertGreater(len(_bytes), 0)

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __RAW_PARAMETRIZED_DATA_ALLOW_FAILURES,
    )
    @pytest.mark.xfail
    def test_raw_standalone_providers_allow_failures(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test standalone providers, but allow failures."""
        _kwargs = deepcopy(kwargs)
        if storage is None:
            storage = FS_STORAGE
        _provider = provider(fake)  # noqa
        _method = getattr(_provider, method_name)
        _kwargs["storage"] = storage
        _kwargs["raw"] = True
        _bytes = _method(**_kwargs)
        self.assertIsInstance(_bytes, bytes)
        self.assertGreater(len(_bytes), 0)

    def test_load_class_from_path_class_not_found(self) -> None:
        """Test load_class_from_path class not found."""
        with self.assertRaises(ImportError):
            load_class_from_path(
                "faker_file.providers.mp3_file.generators"
                ".gtts_generator.ClassDoesNotExist"
            )

    def test_load_class_from_path_no_class_type(self) -> None:
        """Test load_class_from_path imported is not class."""
        with self.assertRaises(ImportError):
            load_class_from_path(
                "faker_file.providers.mp3_file.generators"
                ".gtts_generator.DEFAULT_LANG"
            )

    def test_load_class_from_non_existing_path(self) -> None:
        """Test load_class_from_path invalid path."""
        with self.assertRaises(ImportError):
            load_class_from_path("faker_file.providers.does_not_exist.MyClass")


class RandomFileFromDirProviderTestCase(unittest.TestCase):
    """RandomFileFromDirProvider test case."""

    # fake, provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # RandomFileFromDirProvider
        (
            FAKER,
            RandomFileFromDirProvider,
            "random_file_from_dir",
            {
                "source_dir_path": os.path.join(
                    tempfile.gettempdir(), DEFAULT_REL_PATH
                )
            },
            None,
        ),
        (
            FAKER,
            RandomFileFromDirProvider,
            "random_file_from_dir",
            {
                "source_dir_path": os.path.join(
                    tempfile.gettempdir(), DEFAULT_REL_PATH
                )
            },
            False,
        ),
        (
            FAKER,
            RandomFileFromDirProvider,
            "random_file_from_dir",
            {
                "source_dir_path": os.path.join(
                    tempfile.gettempdir(), DEFAULT_REL_PATH
                )
            },
            PATHY_FS_STORAGE,
        ),
    ]

    # create_inner_file_func, options, create_inner_file_args
    __PARAMETRIZED_DATA_ARCHIVES: List[
        Tuple[
            Optional[Callable],
            Optional[Dict[str, Any]],
            Optional[Dict[str, Any]],
        ]
    ] = [
        # RandomFileFromDir
        (
            create_inner_random_file_from_dir,
            {"content": None},
            {
                "source_dir_path": os.path.join(
                    tempfile.gettempdir(), DEFAULT_REL_PATH
                )
            },
        ),
    ]

    __RAW_PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # RandomFileFromDirProvider
        (
            FAKER,
            RandomFileFromDirProvider,
            "random_file_from_dir",
            {
                "source_dir_path": os.path.join(
                    tempfile.gettempdir(), DEFAULT_REL_PATH
                )
            },
            None,
        ),
    ]

    def setUp(self: "RandomFileFromDirProviderTestCase"):
        super().setUp()
        use_fs(tempfile.gettempdir())

        # The following is important since some of the file providers
        # such as RandomFileFromDirProvider or FileFromPathProvider,
        # rely on physical presence of files.
        create_test_files()

    def tearDown(self) -> None:
        super().tearDown()
        FILE_REGISTRY.clean_up()

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA,
    )
    def test_faker(
        self: "RandomFileFromDirProviderTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test faker provider integration."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        _kwargs["storage"] = storage
        _file = _method(**_kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __RAW_PARAMETRIZED_DATA,
    )
    def test_faker_raw(
        self: "RandomFileFromDirProviderTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test faker provider integration raw."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        _kwargs["storage"] = storage
        _kwargs["raw"] = True
        _bytes = _method(**_kwargs)
        self.assertIsInstance(_bytes, bytes)
        self.assertGreater(len(_bytes), 0)

    @parametrize(
        "create_inner_file_func, options, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_zip_file(
        self: "RandomFileFromDirProviderTestCase",
        create_inner_file_func: Optional[Callable] = None,
        options: Optional[Dict[str, Any]] = None,
        create_inner_file_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Test standalone ZIP file provider."""
        _options = {}
        _options.update(options)
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

    @parametrize(
        "create_inner_file_func, options, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_tar_file(
        self: "RandomFileFromDirProviderTestCase",
        create_inner_file_func: Optional[Callable] = None,
        options: Optional[Dict[str, Any]] = None,
        create_inner_file_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Test standalone TAR file provider."""
        _options = {}
        _options.update(options)
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = TarFileProvider(None).tar_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))


class FileFromPathProviderTestCase(unittest.TestCase):
    """FileFromPathProvider test case."""

    # fake, provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # FileFromPathProvider
        (
            FAKER,
            FileFromPathProvider,
            "file_from_path",
            {
                "path": SOURCE_FILE_FROM_PATH_FILENAME,
            },
            None,
        ),
        (
            FAKER,
            FileFromPathProvider,
            "file_from_path",
            {
                "path": SOURCE_FILE_FROM_PATH_FILENAME,
            },
            False,
        ),
        (
            FAKER,
            FileFromPathProvider,
            "file_from_path",
            {
                "path": SOURCE_FILE_FROM_PATH_FILENAME,
            },
            PATHY_FS_STORAGE,
        ),
    ]

    # create_inner_file_func, options, create_inner_file_args
    __PARAMETRIZED_DATA_ARCHIVES: List[
        Tuple[
            Optional[Callable],
            Optional[Dict[str, Any]],
            Optional[Dict[str, Any]],
        ]
    ] = [
        # FileFromPath
        (
            create_inner_file_from_path,
            {"content": None},
            {
                "path": SOURCE_FILE_FROM_PATH_FILENAME,
            },
        ),
    ]

    __RAW_PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # FileFromPathProvider
        (
            FAKER,
            FileFromPathProvider,
            "file_from_path",
            {
                "path": SOURCE_FILE_FROM_PATH_FILENAME,
            },
            None,
        ),
    ]

    def setUp(self: "FileFromPathProviderTestCase"):
        super().setUp()
        use_fs(tempfile.gettempdir())

        # The following is important since some of the file providers
        # such as RandomFileFromDirProvider or FileFromPathProvider,
        # rely on physical presence of files.
        create_test_files()

    def tearDown(self) -> None:
        super().tearDown()
        FILE_REGISTRY.clean_up()

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA,
    )
    def test_faker(
        self: "FileFromPathProviderTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test faker provider integration."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        _kwargs["storage"] = storage
        _file = _method(**_kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __RAW_PARAMETRIZED_DATA,
    )
    def test_faker_raw(
        self: "FileFromPathProviderTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test faker provider integration raw."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        _kwargs["storage"] = storage
        _kwargs["raw"] = True
        _bytes = _method(**_kwargs)
        self.assertIsInstance(_bytes, bytes)
        self.assertGreater(len(_bytes), 0)

    @parametrize(
        "create_inner_file_func, options, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_zip_file(
        self: "FileFromPathProviderTestCase",
        create_inner_file_func: Optional[Callable] = None,
        options: Optional[Dict[str, Any]] = None,
        create_inner_file_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Test standalone ZIP file provider."""
        _options = {}
        _options.update(options)
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

    @parametrize(
        "create_inner_file_func, options, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_tar_file(
        self: "FileFromPathProviderTestCase",
        create_inner_file_func: Optional[Callable] = None,
        options: Optional[Dict[str, Any]] = None,
        create_inner_file_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Test standalone TAR file provider."""
        _options = {}
        _options.update(options)
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = TarFileProvider(None).tar_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))


class AugmentImageFromPathProviderTestCase(unittest.TestCase):
    """AugmentImageFromPathProvider test case."""

    # fake, provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # AugmentImageFromPathProvider
        # BMP
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_BMP_FILE_FROM_PATH_FILENAME,
            },
            None,
        ),
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_BMP_FILE_FROM_PATH_FILENAME,
                "augmentations": [
                    (color_jitter, {}),
                    (equalize, {}),
                    (random_crop, {}),
                ],
            },
            None,
        ),
        # GIF
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_GIF_FILE_FROM_PATH_FILENAME,
            },
            None,
        ),
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_GIF_FILE_FROM_PATH_FILENAME,
                "augmentations": [
                    (color_jitter, {}),
                    (equalize, {}),
                    (random_crop, {}),
                ],
            },
            None,
        ),
        # ICO
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_ICO_FILE_FROM_PATH_FILENAME,
            },
            None,
        ),
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_ICO_FILE_FROM_PATH_FILENAME,
                "augmentations": [
                    (color_jitter, {}),
                    (equalize, {}),
                    (random_crop, {}),
                ],
            },
            None,
        ),
        # JPEG
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
            },
            None,
        ),
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
            },
            False,
        ),
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
            },
            PATHY_FS_STORAGE,
        ),
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
                "augmentations": [
                    (color_jitter, {}),
                    (equalize, {}),
                    (random_crop, {}),
                ],
            },
            None,
        ),
        # PNG
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_PNG_FILE_FROM_PATH_FILENAME,
            },
            None,
        ),
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_PNG_FILE_FROM_PATH_FILENAME,
                "augmentations": [
                    (color_jitter, {}),
                    (equalize, {}),
                    (random_crop, {}),
                ],
            },
            None,
        ),
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_PNG_FILE_FROM_PATH_FILENAME,
                "augmentations": [
                    (equalize, {}),
                    (color_jitter, {}),
                    (random_crop, {}),
                ],
                "pop_func": list.pop,
            },
            None,
        ),
        # # SVG
        # (
        #     FAKER,
        #     AugmentImageFromPathProvider,
        #     "augment_image_from_path",
        #     {
        #         "path": SOURCE_SVG_FILE_FROM_PATH_FILENAME,
        #     },
        #     None,
        # ),
        # TIFF
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_TIFF_FILE_FROM_PATH_FILENAME,
            },
            None,
        ),
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_TIFF_FILE_FROM_PATH_FILENAME,
                "augmentations": [
                    (color_jitter, {}),
                    (equalize, {}),
                    (random_crop, {}),
                ],
            },
            None,
        ),
        # WEBP
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_WEBP_FILE_FROM_PATH_FILENAME,
            },
            None,
        ),
        (
            FAKER,
            AugmentImageFromPathProvider,
            "augment_image_from_path",
            {
                "path": SOURCE_WEBP_FILE_FROM_PATH_FILENAME,
                "augmentations": [
                    (color_jitter, {}),
                    (equalize, {}),
                    (random_crop, {}),
                ],
            },
            None,
        ),
    ]

    # create_inner_file_func, options, create_inner_file_args
    __PARAMETRIZED_DATA_ARCHIVES: List[
        Tuple[
            Optional[Callable],
            Optional[Dict[str, Any]],
            Optional[Dict[str, Any]],
        ]
    ] = [
        # AugmentImageFromPath
        (
            create_inner_augment_image_from_path,
            {},
            {
                "path": SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
            },
        ),
    ]

    __RAW_PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = deepcopy(__PARAMETRIZED_DATA)

    def setUp(self: "AugmentImageFromPathProviderTestCase"):
        super().setUp()
        use_fs(tempfile.gettempdir())

        # The following is important since some of the file providers
        # such as RandomFileFromDirProvider or FileFromPathProvider,
        # rely on physical presence of files.
        create_test_files()

    def tearDown(self) -> None:
        super().tearDown()
        FILE_REGISTRY.clean_up()

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA,
    )
    def test_faker(
        self: "AugmentImageFromPathProviderTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test faker provider integration."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        _kwargs["storage"] = storage
        _file = _method(**_kwargs)
        self.assertTrue(_file.data["storage"].exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __RAW_PARAMETRIZED_DATA,
    )
    def test_faker_raw(
        self: "AugmentImageFromPathProviderTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test faker provider integration raw."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        _kwargs["storage"] = storage
        _kwargs["raw"] = True
        _bytes = _method(**_kwargs)
        self.assertIsInstance(_bytes, bytes)
        self.assertGreater(len(_bytes), 0)

    @parametrize(
        "create_inner_file_func, options, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_zip_file(
        self: "AugmentImageFromPathProviderTestCase",
        create_inner_file_func: Optional[Callable] = None,
        options: Optional[Dict[str, Any]] = None,
        create_inner_file_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Test standalone ZIP file provider."""
        _options = {}
        _options.update(options)
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

    @parametrize(
        "create_inner_file_func, options, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_tar_file(
        self: "AugmentImageFromPathProviderTestCase",
        create_inner_file_func: Optional[Callable] = None,
        options: Optional[Dict[str, Any]] = None,
        create_inner_file_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Test standalone TAR file provider."""
        _options = {}
        _options.update(options)
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = TarFileProvider(None).tar_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))


class AugmentRandomImageFromDirProviderTestCase(unittest.TestCase):
    """AugmentRandomImageFromDirProvider test case."""

    # fake, provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # AugmentRandomImageFromDirProvider
        (
            FAKER,
            AugmentRandomImageFromDirProvider,
            "augment_random_image_from_dir",
            {
                "source_dir_path": os.path.dirname(
                    SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
                ),
            },
            None,
        ),
        (
            FAKER,
            AugmentRandomImageFromDirProvider,
            "augment_random_image_from_dir",
            {
                "source_dir_path": os.path.dirname(
                    SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
                ),
            },
            False,
        ),
        (
            FAKER,
            AugmentRandomImageFromDirProvider,
            "augment_random_image_from_dir",
            {
                "source_dir_path": os.path.dirname(
                    SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
                ),
            },
            PATHY_FS_STORAGE,
        ),
        (
            FAKER,
            AugmentRandomImageFromDirProvider,
            "augment_random_image_from_dir",
            {
                "source_dir_path": os.path.dirname(
                    SOURCE_PNG_FILE_FROM_PATH_FILENAME,
                ),
            },
            None,
        ),
        (
            FAKER,
            AugmentRandomImageFromDirProvider,
            "augment_random_image_from_dir",
            {
                "source_dir_path": os.path.dirname(
                    SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
                ),
                "augmentations": [
                    (color_jitter, {}),
                    (equalize, {}),
                    (random_crop, {}),
                ],
            },
            None,
        ),
        (
            FAKER,
            AugmentRandomImageFromDirProvider,
            "augment_random_image_from_dir",
            {
                "source_dir_path": os.path.dirname(
                    SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
                ),
                "augmentations": [],
            },
            None,
        ),
    ]

    # create_inner_file_func, options, create_inner_file_args
    __PARAMETRIZED_DATA_ARCHIVES: List[
        Tuple[
            Optional[Callable],
            Optional[Dict[str, Any]],
            Optional[Dict[str, Any]],
        ]
    ] = [
        # AugmentRandomImageFromDir
        (
            create_inner_augment_random_image_from_dir,
            {},
            {
                "source_dir_path": os.path.dirname(
                    SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
                ),
            },
        ),
    ]

    __RAW_PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = deepcopy(__PARAMETRIZED_DATA)

    def setUp(self: "AugmentRandomImageFromDirProviderTestCase") -> None:
        super().setUp()
        use_fs(tempfile.gettempdir())

        # The following is important since some of the file providers
        # such as RandomFileFromDirProvider or FileFromPathProvider,
        # rely on physical presence of files.
        create_test_files()

    def tearDown(self) -> None:
        super().tearDown()
        FILE_REGISTRY.clean_up()

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA,
    )
    def test_faker(
        self: "AugmentRandomImageFromDirProviderTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test faker provider integration."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        _kwargs["storage"] = storage
        _file = _method(**_kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA,
    )
    def test_faker_raw(
        self: "AugmentRandomImageFromDirProviderTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test faker provider integration raw."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        _kwargs["storage"] = storage
        _kwargs["raw"] = True
        _bytes = _method(**_kwargs)
        self.assertIsInstance(_bytes, bytes)
        self.assertGreater(len(_bytes), 0)

    @parametrize(
        "create_inner_file_func, options, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_zip_file(
        self: "AugmentRandomImageFromDirProviderTestCase",
        create_inner_file_func: Optional[Callable] = None,
        options: Optional[Dict[str, Any]] = None,
        create_inner_file_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Test standalone ZIP file provider."""
        _options = {}
        _options.update(options)
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

    @parametrize(
        "create_inner_file_func, options, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_tar_file(
        self: "AugmentRandomImageFromDirProviderTestCase",
        create_inner_file_func: Optional[Callable] = None,
        options: Optional[Dict[str, Any]] = None,
        create_inner_file_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Test standalone TAR file provider."""
        _options = {}
        _options.update(options)
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = TarFileProvider(None).tar_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

    def test_augment_random_image_from_dir_bad_augment_func_exception(
        self: "AugmentRandomImageFromDirProviderTestCase",
    ):
        """Call `augment_random_image_from_dir` with wrong augment function."""
        file = AugmentRandomImageFromDirProvider(
            FAKER
        ).augment_random_image_from_dir(
            **{
                "source_dir_path": os.path.dirname(
                    SOURCE_JPEG_FILE_FROM_PATH_FILENAME,
                ),
                "augmentations": [(lambda: True, {})] * 2,
            }
        )
        self.assertTrue(file.data["storage"].exists(file))
