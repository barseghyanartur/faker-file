import os.path
import unittest
from typing import Any, Dict, Optional, Union

from faker import Faker
from parametrize import parametrize

from ..content_generators import RandomCharsContentGenerator
from ..providers.bin_file import BinFileProvider
from ..providers.csv_file import CsvFileProvider
from ..providers.docx_file import DocxFileProvider
from ..providers.ico_file import IcoFileProvider
from ..providers.jpeg_file import JpegFileProvider
from ..providers.pdf_file import PdfFileProvider
from ..providers.png_file import PngFileProvider
from ..providers.pptx_file import PptxFileProvider
from ..providers.svg_file import SvgFileProvider
from ..providers.txt_file import TxtFileProvider
from ..providers.webp_file import WebpFileProvider
from ..providers.xlsx_file import XlsxFileProvider
from ..providers.zip_file import (
    ZipFileProvider,
    create_inner_bin_file,
    create_inner_csv_file,
    create_inner_docx_file,
    create_inner_pdf_file,
    create_inner_pptx_file,
    create_inner_txt_file,
    create_inner_ico_file,
    create_inner_jpeg_file,
    create_inner_png_file,
    create_inner_svg_file,
    # create_inner_webp_file,
    create_inner_xlsx_file,
)

__all__ = ("ProvidersTestCase",)


FileProvider = Union[
    CsvFileProvider,
    DocxFileProvider,
    IcoFileProvider,
    JpegFileProvider,
    PdfFileProvider,
    PngFileProvider,
    PptxFileProvider,
    SvgFileProvider,
    TxtFileProvider,
    WebpFileProvider,
    XlsxFileProvider,
    ZipFileProvider,
]

_FAKER = Faker()

class ProvidersTestCase(unittest.TestCase):
    """Providers test case."""

    FAKER: Faker
    __parametrized_data = [
        # BIN
        (BinFileProvider, "bin_file", {}),
        # CSV
        (CsvFileProvider, "csv_file", {}),
        # DOCX
        (DocxFileProvider, "docx_file", {}),
        (
            DocxFileProvider,
            "docx_file",
            {
                "wrap_chars_after": 40,
                "content_generator": RandomCharsContentGenerator,
            },
        ),
        (
            DocxFileProvider,
            "docx_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
        ),
        # ICO
        (IcoFileProvider, "ico_file", {}),
        (
            IcoFileProvider,
            "ico_file",
            {
                "wrap_chars_after": 40,
                "content_generator": RandomCharsContentGenerator,
            },
        ),
        (
            IcoFileProvider,
            "ico_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
        ),
        # JPEG
        (JpegFileProvider, "jpeg_file", {}),
        (
            JpegFileProvider,
            "jpeg_file",
            {
                "wrap_chars_after": 40,
                "content_generator": RandomCharsContentGenerator,
            },
        ),
        (
            JpegFileProvider,
            "jpeg_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
        ),
        # PDF
        (PdfFileProvider, "pdf_file", {}),
        (
            PdfFileProvider,
            "pdf_file",
            {
                "wrap_chars_after": 40,
                "content_generator": RandomCharsContentGenerator,
            },
        ),
        (
            PdfFileProvider,
            "pdf_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
        ),
        # PNG
        (PngFileProvider, "png_file", {}),
        (
            PngFileProvider,
            "png_file",
            {
                "wrap_chars_after": 40,
                "content_generator": RandomCharsContentGenerator,
            },
        ),
        (
            PngFileProvider,
            "png_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
        ),
        # PPTX
        (PptxFileProvider, "pptx_file", {}),
        (
            PptxFileProvider,
            "pptx_file",
            {
                "wrap_chars_after": 40,
                "content_generator": RandomCharsContentGenerator,
            },
        ),
        (
            PptxFileProvider,
            "pptx_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
        ),
        # SVG
        (SvgFileProvider, "svg_file", {}),
        (
            SvgFileProvider,
            "svg_file",
            {
                "wrap_chars_after": 40,
                "content_generator": RandomCharsContentGenerator,
            },
        ),
        (
            SvgFileProvider,
            "svg_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
        ),
        # TXT
        (TxtFileProvider, "txt_file", {}),
        (
            TxtFileProvider,
            "txt_file",
            {
                "wrap_chars_after": 40,
                "content_generator": RandomCharsContentGenerator,
            },
        ),
        (
            TxtFileProvider,
            "txt_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
        ),
        # WEBP
        # (WebpFileProvider, "webp_file", {}),
        # XLSX
        (XlsxFileProvider, "xlsx_file", {}),
        # ZIP
        (ZipFileProvider, "zip_file", {}),
    ]

    @parametrize(
        "provider, method_name, kwargs",
        __parametrized_data,
    )
    def test_faker(
        self,
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
    ) -> None:
        """Test faker provider integration."""
        _faker = Faker()
        _faker.add_provider(provider)
        _method = getattr(_faker, method_name)
        _file = _method(**kwargs)
        self.assertTrue(os.path.exists(_file))

    @parametrize(
        "provider, method_name, kwargs",
        __parametrized_data,
    )
    def test_standalone_providers(
        self,
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
    ) -> None:
        """Test standalone providers."""
        _provider = provider(None)  # noqa
        _method = getattr(_provider, method_name)
        _file = _method(**kwargs)
        self.assertTrue(os.path.exists(_file))

    @parametrize(
        "create_inner_file_func, content",
        [
            (None, None),
            (create_inner_bin_file, "Lorem ipsum"),
            (create_inner_csv_file, "Lorem ipsum"),
            (create_inner_docx_file, "Lorem ipsum"),
            (create_inner_txt_file, "Lorem ipsum"),
            (create_inner_pdf_file, "Lorem ipsum"),
            (create_inner_pptx_file, "Lorem ipsum"),
            (create_inner_ico_file, "Lorem ipsum"),
            (create_inner_jpeg_file, "Lorem ipsum"),
            (create_inner_png_file, "Lorem ipsum"),
            (create_inner_svg_file, "Lorem ipsum"),
            # (create_inner_webp_file, "Lorem ipsum"),
            (create_inner_xlsx_file, None),
        ],
    )
    def test_standalone_zip_file(
        self,
        create_inner_file_func: Optional[callable] = None,
        content: Union[str, Dict] = None,
    ):
        """Test standalone ZIP file provider."""
        _options = {"content": content}
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(os.path.exists(_file))
