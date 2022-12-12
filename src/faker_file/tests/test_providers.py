import os.path
import tempfile
import unittest
from importlib import import_module, reload
from typing import Any, Callable, Dict, Optional, Union

import pytest
from faker import Faker
from faker.providers import BaseProvider
from parametrize import parametrize

from ..base import DEFAULT_REL_PATH, FileMixin
from ..constants import DEFAULT_TEXT_CONTENT_TEMPLATE
from ..providers.bin_file import BinFileProvider
from ..providers.csv_file import CsvFileProvider
from ..providers.docx_file import DocxFileProvider
from ..providers.ico_file import IcoFileProvider
from ..providers.jpeg_file import JpegFileProvider
from ..providers.ods_file import OdsFileProvider
from ..providers.pdf_file import PdfFileProvider
from ..providers.png_file import PngFileProvider
from ..providers.pptx_file import PptxFileProvider
from ..providers.random_file_from_dir import RandomFileFromDirProvider
from ..providers.svg_file import SvgFileProvider
from ..providers.txt_file import TxtFileProvider
from ..providers.webp_file import WebpFileProvider
from ..providers.xlsx_file import XlsxFileProvider
from ..providers.zip_file import (
    ZipFileProvider,
    create_inner_bin_file,
    create_inner_csv_file,
    create_inner_docx_file,
    create_inner_ico_file,
    create_inner_jpeg_file,
    create_inner_ods_file,
    create_inner_pdf_file,
    create_inner_png_file,
    create_inner_pptx_file,
    create_inner_svg_file,
    create_inner_txt_file,
    create_inner_webp_file,
    create_inner_xlsx_file,
    create_inner_zip_file,
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
        (CsvFileProvider, "csv_file", {"content": "{{name}},{{date}}"}),
        # DOCX
        (DocxFileProvider, "docx_file", {}),
        (
            DocxFileProvider,
            "docx_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
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
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
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
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
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
        # ODS
        (OdsFileProvider, "ods_file", {}),
        # PDF
        (PdfFileProvider, "pdf_file", {}),
        (
            PdfFileProvider,
            "pdf_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
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
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
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
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
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
        # RandomFileFromDirProvider
        (
            RandomFileFromDirProvider,
            "random_file_from_dir",
            {
                "source_dir_path": os.path.join(
                    tempfile.gettempdir(), DEFAULT_REL_PATH
                )
            },
        ),
        # SVG
        (SvgFileProvider, "svg_file", {}),
        (
            SvgFileProvider,
            "svg_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
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
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
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
        self: "ProvidersTestCase",
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
        self: "ProvidersTestCase",
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
        "provider, method_name, kwargs",
        [
            (WebpFileProvider, "webp_file", {}),
        ],
    )
    @pytest.mark.xfail
    def test_standalone_providers_allow_failures(
        self: "ProvidersTestCase",
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
    ) -> None:
        """Test standalone providers, but allow failures."""
        _provider = provider(None)  # noqa
        _method = getattr(_provider, method_name)
        _file = _method(**kwargs)
        self.assertTrue(os.path.exists(_file))

    @parametrize(
        "create_inner_file_func, content",
        [
            (None, None),
            (create_inner_bin_file, b"Lorem ipsum"),
            (create_inner_csv_file, "Lorem ipsum"),
            (create_inner_docx_file, "Lorem ipsum"),
            (create_inner_txt_file, "Lorem ipsum"),
            (create_inner_pdf_file, "Lorem ipsum"),
            (create_inner_pptx_file, "Lorem ipsum"),
            (create_inner_ico_file, "Lorem ipsum"),
            (create_inner_jpeg_file, "Lorem ipsum"),
            (create_inner_ods_file, None),
            (create_inner_png_file, "Lorem ipsum"),
            (create_inner_svg_file, "Lorem ipsum"),
            # (create_inner_webp_file, "Lorem ipsum"),
            (create_inner_xlsx_file, None),
            (create_inner_zip_file, None),
        ],
    )
    def test_standalone_zip_file(
        self: "ProvidersTestCase",
        create_inner_file_func: Optional[callable] = None,
        content: Union[str, Dict] = None,
    ) -> None:
        """Test standalone ZIP file provider."""
        _options = {"content": content}
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(os.path.exists(_file))

    @parametrize(
        "create_inner_file_func, content",
        [
            (create_inner_webp_file, "Lorem ipsum"),
        ],
    )
    @pytest.mark.xfail
    def test_standalone_zip_file_allow_failures(
        self: "ProvidersTestCase",
        create_inner_file_func: Optional[callable] = None,
        content: Union[str, Dict] = None,
    ) -> None:
        """Test standalone ZIP file provider, but allow failures."""
        _options = {"content": content}
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(os.path.exists(_file))

    @parametrize(
        "module_path, module_name, create_inner_file_func",
        [
            # BIN
            (
                "faker_file.providers.bin_file",
                "BinFileProvider",
                create_inner_bin_file,
            ),
            # CSV
            (
                "faker_file.providers.csv_file",
                "CsvFileProvider",
                create_inner_csv_file,
            ),
            # DOCX
            (
                "faker_file.providers.docx_file",
                "DocxFileProvider",
                create_inner_docx_file,
            ),
            # ICO
            (
                "faker_file.providers.ico_file",
                "IcoFileProvider",
                create_inner_ico_file,
            ),
            # JPEG
            (
                "faker_file.providers.jpeg_file",
                "JpegFileProvider",
                create_inner_jpeg_file,
            ),
            # ODS
            (
                "faker_file.providers.ods_file",
                "OdsFileProvider",
                create_inner_ods_file,
            ),
            # PDF
            (
                "faker_file.providers.pdf_file",
                "PdfFileProvider",
                create_inner_pdf_file,
            ),
            # PNG
            (
                "faker_file.providers.png_file",
                "PngFileProvider",
                create_inner_png_file,
            ),
            # PPTX
            (
                "faker_file.providers.pptx_file",
                "PptxFileProvider",
                create_inner_pptx_file,
            ),
            # SVG
            (
                "faker_file.providers.svg_file",
                "SvgFileProvider",
                create_inner_svg_file,
            ),
            # TXT
            (
                "faker_file.providers.txt_file",
                "TxtFileProvider",
                create_inner_txt_file,
            ),
            # WEBP
            (
                "faker_file.providers.webp_file",
                "WebpFileProvider",
                create_inner_webp_file,
            ),
            # XLSX
            (
                "faker_file.providers.xlsx_file",
                "XlsxFileProvider",
                create_inner_xlsx_file,
            ),
        ],
    )
    def test_broken_imports(
        self,
        module_path: str,
        module_name: str,
        create_inner_file_func: Callable,
    ) -> None:
        """Test broken imports."""
        _module = import_module(module_path)
        del _module.__dict__[module_name]
        with self.assertRaises(ImportError):
            create_inner_file_func()
        reload(_module)

    def test_generate_filename_failure(self) -> None:
        """Test generate filename failure."""

        class _TestFileProvider(BaseProvider, FileMixin):
            extension: str = ""

        with self.assertRaises(Exception):
            _TestFileProvider(_FAKER)._generate_filename()
