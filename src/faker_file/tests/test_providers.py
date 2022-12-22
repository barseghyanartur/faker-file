import os.path
import tempfile
import unittest
from importlib import import_module, reload
from typing import Any, Callable, Dict, Optional, Union

import pytest
from faker import Faker
from parametrize import parametrize
from pathy import use_fs

from ..base import DEFAULT_REL_PATH
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
from ..providers.rtf_file import RtfFileProvider
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
    create_inner_rtf_file,
    create_inner_svg_file,
    create_inner_txt_file,
    create_inner_webp_file,
    create_inner_xlsx_file,
    create_inner_zip_file,
)
from ..storages.base import BaseStorage
from ..storages.cloud import PathyFileSystemStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("ProvidersTestCase",)


FileProvider = Union[
    CsvFileProvider,
    DocxFileProvider,
    IcoFileProvider,
    JpegFileProvider,
    PdfFileProvider,
    PngFileProvider,
    PptxFileProvider,
    RtfFileProvider,
    SvgFileProvider,
    TxtFileProvider,
    WebpFileProvider,
    XlsxFileProvider,
    ZipFileProvider,
]

_FAKER = Faker()
FS_STORAGE = FileSystemStorage()
PATHY_FS_STORAGE = PathyFileSystemStorage(bucket_name="tmp", rel_path="tmp")


class ProvidersTestCase(unittest.TestCase):
    """Providers test case."""

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        use_fs(tempfile.gettempdir())

    FAKER: Faker
    __parametrized_data = [
        # BIN
        (BinFileProvider, "bin_file", {}, None),
        (BinFileProvider, "bin_file", {}, False),
        (BinFileProvider, "bin_file", {}, PATHY_FS_STORAGE),
        # CSV
        (CsvFileProvider, "csv_file", {}, None),
        (CsvFileProvider, "csv_file", {}, False),
        (CsvFileProvider, "csv_file", {}, PATHY_FS_STORAGE),
        (CsvFileProvider, "csv_file", {"content": "{{name}},{{date}}"}, None),
        # DOCX
        (DocxFileProvider, "docx_file", {}, None),
        (DocxFileProvider, "docx_file", {}, False),
        (DocxFileProvider, "docx_file", {}, PATHY_FS_STORAGE),
        (
            DocxFileProvider,
            "docx_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            DocxFileProvider,
            "docx_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
            None,
        ),
        # ICO
        (IcoFileProvider, "ico_file", {}, None),
        (IcoFileProvider, "ico_file", {}, False),
        (IcoFileProvider, "ico_file", {}, PATHY_FS_STORAGE),
        (
            IcoFileProvider,
            "ico_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            IcoFileProvider,
            "ico_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
            None,
        ),
        # JPEG
        (JpegFileProvider, "jpeg_file", {}, None),
        (JpegFileProvider, "jpeg_file", {}, False),
        (JpegFileProvider, "jpeg_file", {}, PATHY_FS_STORAGE),
        (
            JpegFileProvider,
            "jpeg_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            JpegFileProvider,
            "jpeg_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
            None,
        ),
        # ODS
        (OdsFileProvider, "ods_file", {}, None),
        (OdsFileProvider, "ods_file", {}, False),
        (OdsFileProvider, "ods_file", {}, PATHY_FS_STORAGE),
        # PDF
        (PdfFileProvider, "pdf_file", {}, None),
        (PdfFileProvider, "pdf_file", {}, False),
        (PdfFileProvider, "pdf_file", {}, PATHY_FS_STORAGE),
        (
            PdfFileProvider,
            "pdf_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            PdfFileProvider,
            "pdf_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
            None,
        ),
        # PNG
        (PngFileProvider, "png_file", {}, None),
        (PngFileProvider, "png_file", {}, False),
        (PngFileProvider, "png_file", {}, PATHY_FS_STORAGE),
        (
            PngFileProvider,
            "png_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            PngFileProvider,
            "png_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
            None,
        ),
        # PPTX
        (PptxFileProvider, "pptx_file", {}, None),
        (PptxFileProvider, "pptx_file", {}, False),
        (PptxFileProvider, "pptx_file", {}, PATHY_FS_STORAGE),
        (
            PptxFileProvider,
            "pptx_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            PptxFileProvider,
            "pptx_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
            None,
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
            None,
        ),
        (
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
            RandomFileFromDirProvider,
            "random_file_from_dir",
            {
                "source_dir_path": os.path.join(
                    tempfile.gettempdir(), DEFAULT_REL_PATH
                )
            },
            PATHY_FS_STORAGE,
        ),
        # RTF
        (RtfFileProvider, "rtf_file", {}, None),
        (RtfFileProvider, "rtf_file", {}, False),
        (RtfFileProvider, "rtf_file", {}, PATHY_FS_STORAGE),
        (
            RtfFileProvider,
            "rtf_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            RtfFileProvider,
            "rtf_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
            None,
        ),
        # SVG
        (SvgFileProvider, "svg_file", {}, None),
        (SvgFileProvider, "svg_file", {}, False),
        (SvgFileProvider, "svg_file", {}, PATHY_FS_STORAGE),
        (
            SvgFileProvider,
            "svg_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            SvgFileProvider,
            "svg_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
            None,
        ),
        # TXT
        (TxtFileProvider, "txt_file", {}, None),
        (TxtFileProvider, "txt_file", {}, False),
        (TxtFileProvider, "txt_file", {}, PATHY_FS_STORAGE),
        (
            TxtFileProvider,
            "txt_file",
            {
                "wrap_chars_after": 40,
                "content": DEFAULT_TEXT_CONTENT_TEMPLATE,
            },
            None,
        ),
        (
            TxtFileProvider,
            "txt_file",
            {
                "wrap_chars_after": 40,
                "content": _FAKER.text(),
            },
            None,
        ),
        # WEBP
        # (WebpFileProvider, "webp_file", {}, None),
        # (WebpFileProvider, "webp_file", {}, PATHY_FS_STORAGE),
        # XLSX
        (XlsxFileProvider, "xlsx_file", {}, None),
        (XlsxFileProvider, "xlsx_file", {}, False),
        (XlsxFileProvider, "xlsx_file", {}, PATHY_FS_STORAGE),
        # ZIP
        (ZipFileProvider, "zip_file", {}, None),
        (ZipFileProvider, "zip_file", {}, False),
        (ZipFileProvider, "zip_file", {}, PATHY_FS_STORAGE),
    ]

    @parametrize(
        "provider, method_name, kwargs, storage",
        __parametrized_data,
    )
    def test_faker(
        self: "ProvidersTestCase",
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
        storage: BaseStorage = None,
    ) -> None:
        """Test faker provider integration."""
        if storage is False:
            storage = FS_STORAGE
        _faker = Faker()
        _faker.add_provider(provider)
        _method = getattr(_faker, method_name)
        kwargs["storage"] = storage
        _file = _method(**kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "provider, method_name, kwargs, storage",
        __parametrized_data,
    )
    def test_standalone_providers(
        self: "ProvidersTestCase",
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
        storage: BaseStorage = None,
    ) -> None:
        """Test standalone providers."""
        if storage is False:
            storage = FS_STORAGE
        _provider = provider(None)  # noqa
        _method = getattr(_provider, method_name)
        kwargs["storage"] = storage
        _file = _method(**kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "provider, method_name, kwargs, storage",
        [
            (WebpFileProvider, "webp_file", {}, None),
            (WebpFileProvider, "webp_file", {}, PATHY_FS_STORAGE),
        ],
    )
    @pytest.mark.xfail
    def test_standalone_providers_allow_failures(
        self: "ProvidersTestCase",
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
        storage: BaseStorage = None,
    ) -> None:
        """Test standalone providers, but allow failures."""
        if storage is None:
            storage = FS_STORAGE
        _provider = provider(None)  # noqa
        _method = getattr(_provider, method_name)
        kwargs["storage"] = storage
        _file = _method(**kwargs)
        self.assertTrue(storage.exists(_file))

    @parametrize(
        "create_inner_file_func, content",
        [
            (None, None),
            (create_inner_bin_file, b"Lorem ipsum"),
            (create_inner_csv_file, "Lorem ipsum"),
            (create_inner_docx_file, "Lorem ipsum"),
            (create_inner_ico_file, "Lorem ipsum"),
            (create_inner_jpeg_file, "Lorem ipsum"),
            (create_inner_ods_file, None),
            (create_inner_pdf_file, "Lorem ipsum"),
            (create_inner_png_file, "Lorem ipsum"),
            (create_inner_pptx_file, "Lorem ipsum"),
            (create_inner_rtf_file, "Lorem ipsum"),
            (create_inner_svg_file, "Lorem ipsum"),
            (create_inner_txt_file, "Lorem ipsum"),
            # (create_inner_webp_file, "Lorem ipsum"),
            (create_inner_xlsx_file, None),
            (create_inner_zip_file, None),
        ],
    )
    def test_standalone_zip_file(
        self: "ProvidersTestCase",
        create_inner_file_func: Optional[Callable] = None,
        content: Union[str, Dict] = None,
    ) -> None:
        """Test standalone ZIP file provider."""
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
    def test_standalone_zip_file_allow_failures(
        self: "ProvidersTestCase",
        create_inner_file_func: Optional[Callable] = None,
        content: Union[str, Dict] = None,
    ) -> None:
        """Test standalone ZIP file provider, but allow failures."""
        _options = {"content": content}
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

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
            # RTF
            (
                "faker_file.providers.rtf_file",
                "RtfFileProvider",
                create_inner_rtf_file,
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
