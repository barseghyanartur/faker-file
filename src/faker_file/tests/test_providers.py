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
from ..providers.eml_file import EmlFileProvider
from ..providers.epub_file import EpubFileProvider
from ..providers.helpers.inner import (
    create_inner_bin_file,
    create_inner_csv_file,
    create_inner_docx_file,
    create_inner_eml_file,
    create_inner_epub_file,
    create_inner_ico_file,
    create_inner_jpeg_file,
    create_inner_mp3_file,
    create_inner_odp_file,
    create_inner_ods_file,
    create_inner_odt_file,
    create_inner_pdf_file,
    create_inner_png_file,
    create_inner_pptx_file,
    create_inner_rtf_file,
    create_inner_svg_file,
    create_inner_tar_file,
    create_inner_txt_file,
    create_inner_webp_file,
    create_inner_xlsx_file,
    create_inner_zip_file,
    fuzzy_choice_create_inner_file,
)
from ..providers.ico_file import IcoFileProvider
from ..providers.jpeg_file import JpegFileProvider
from ..providers.mp3_file import Mp3FileProvider
from ..providers.mp3_file.generators.base import BaseMp3Generator
from ..providers.mp3_file.generators.edge_tts_generator import (
    EdgeTtsMp3Generator,
)
from ..providers.mp3_file.generators.gtts_generator import GttsMp3Generator
from ..providers.odp_file import OdpFileProvider
from ..providers.ods_file import OdsFileProvider
from ..providers.odt_file import OdtFileProvider
from ..providers.pdf_file import PdfFileProvider
from ..providers.png_file import PngFileProvider
from ..providers.pptx_file import PptxFileProvider
from ..providers.random_file_from_dir import RandomFileFromDirProvider
from ..providers.rtf_file import RtfFileProvider
from ..providers.svg_file import SvgFileProvider
from ..providers.tar_file import TarFileProvider
from ..providers.txt_file import TxtFileProvider
from ..providers.webp_file import WebpFileProvider
from ..providers.xlsx_file import XlsxFileProvider
from ..providers.zip_file import ZipFileProvider
from ..storages.base import BaseStorage
from ..storages.cloud import PathyFileSystemStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("ProvidersTestCase",)


FileProvider = Union[
    BinFileProvider,
    CsvFileProvider,
    DocxFileProvider,
    EmlFileProvider,
    EpubFileProvider,
    IcoFileProvider,
    JpegFileProvider,
    Mp3FileProvider,
    OdpFileProvider,
    OdsFileProvider,
    OdtFileProvider,
    PdfFileProvider,
    PngFileProvider,
    PptxFileProvider,
    RtfFileProvider,
    SvgFileProvider,
    TarFileProvider,
    TxtFileProvider,
    WebpFileProvider,
    XlsxFileProvider,
    ZipFileProvider,
]

FAKER = Faker()
FAKER_HY = Faker(locale="hy_AM")
FS_STORAGE = FileSystemStorage()
PATHY_FS_STORAGE = PathyFileSystemStorage(bucket_name="tmp", rel_path="tmp")


class ProvidersTestCase(unittest.TestCase):
    """Providers test case."""

    # fake, provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA = [
        # BIN
        (FAKER, BinFileProvider, "bin_file", {}, None),
        (FAKER, BinFileProvider, "bin_file", {}, False),
        (FAKER, BinFileProvider, "bin_file", {}, PATHY_FS_STORAGE),
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
        # ICO
        (FAKER, IcoFileProvider, "ico_file", {}, None),
        (FAKER_HY, IcoFileProvider, "ico_file", {}, None),
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
        # JPEG
        (FAKER, JpegFileProvider, "jpeg_file", {}, None),
        (FAKER_HY, JpegFileProvider, "jpeg_file", {}, None),
        (FAKER, JpegFileProvider, "jpeg_file", {}, False),
        (FAKER, JpegFileProvider, "jpeg_file", {}, PATHY_FS_STORAGE),
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
        # ODS
        (FAKER, OdsFileProvider, "ods_file", {}, None),
        (FAKER_HY, OdsFileProvider, "ods_file", {}, None),
        (FAKER, OdsFileProvider, "ods_file", {}, False),
        (FAKER, OdsFileProvider, "ods_file", {}, PATHY_FS_STORAGE),
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
        # PNG
        (FAKER, PngFileProvider, "png_file", {}, None),
        (FAKER_HY, PngFileProvider, "png_file", {}, None),
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
        # SVG
        (FAKER, SvgFileProvider, "svg_file", {}, None),
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
        # TAR
        (FAKER, TarFileProvider, "tar_file", {}, None),
        (FAKER, TarFileProvider, "tar_file", {}, False),
        (FAKER, TarFileProvider, "tar_file", {}, PATHY_FS_STORAGE),
        (FAKER, TarFileProvider, "tar_file", {"compression": "gz"}, None),
        (FAKER, TarFileProvider, "tar_file", {"compression": "bz2"}, None),
        (FAKER, TarFileProvider, "tar_file", {"compression": "xz"}, None),
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
        # WEBP
        # (FAKER, WebpFileProvider, "webp_file", {}, None),
        # (FAKER, WebpFileProvider, "webp_file", {}, PATHY_FS_STORAGE),
        # XLSX
        (FAKER, XlsxFileProvider, "xlsx_file", {}, None),
        (FAKER_HY, XlsxFileProvider, "xlsx_file", {}, None),
        (FAKER, XlsxFileProvider, "xlsx_file", {}, False),
        (FAKER, XlsxFileProvider, "xlsx_file", {}, PATHY_FS_STORAGE),
        # ZIP
        (FAKER, ZipFileProvider, "zip_file", {}, None),
        (FAKER, ZipFileProvider, "zip_file", {}, False),
        (FAKER, ZipFileProvider, "zip_file", {}, PATHY_FS_STORAGE),
    ]

    # provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA_RETRY_FAILURES = [
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
    ]

    # fake, provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA_ALLOW_FAILURES = [
        (FAKER, WebpFileProvider, "webp_file", {}, None),
        (FAKER, WebpFileProvider, "webp_file", {}, PATHY_FS_STORAGE),
    ]

    # create_inner_file_func, content, create_inner_file_args
    __PARAMETRIZED_DATA_ARCHIVES = [
        (None, None, None),
        (create_inner_bin_file, b"Lorem ipsum", {}),
        (create_inner_csv_file, "Lorem ipsum", {}),
        (create_inner_docx_file, "Lorem ipsum", {}),
        (create_inner_eml_file, None, {}),
        (create_inner_epub_file, "Lorem ipsum", {}),
        (create_inner_ico_file, "Lorem ipsum", {}),
        (create_inner_jpeg_file, "Lorem ipsum", {}),
        (create_inner_mp3_file, "Lorem ipsum", {}),
        (create_inner_odp_file, "Lorem ipsum", {}),
        (create_inner_ods_file, None, {}),
        (create_inner_odt_file, "Lorem ipsum", {}),
        (create_inner_pdf_file, "Lorem ipsum", {}),
        (create_inner_png_file, "Lorem ipsum", {}),
        (create_inner_pptx_file, "Lorem ipsum", {}),
        (create_inner_rtf_file, "Lorem ipsum", {}),
        (create_inner_svg_file, "Lorem ipsum", {}),
        (create_inner_tar_file, None, {}),
        (create_inner_txt_file, "Lorem ipsum", {}),
        # (create_inner_webp_file, "Lorem ipsum", {}),
        (create_inner_xlsx_file, None, {}),
        (create_inner_zip_file, None, {}),
        (
            fuzzy_choice_create_inner_file,
            None,
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

    def setUp(self: "ProvidersTestCase"):
        super().setUp()
        use_fs(tempfile.gettempdir())

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA,
    )
    def test_faker(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
        storage: BaseStorage = None,
    ) -> None:
        """Test faker provider integration."""
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        kwargs["storage"] = storage
        _file = _method(**kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA_RETRY_FAILURES,
    )
    @pytest.mark.flaky(reruns=5)
    def test_faker_retry_failures(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
        storage: BaseStorage = None,
    ) -> None:
        """Test faker provider integration, retry on failures."""
        if storage is False:
            storage = FS_STORAGE
        fake.add_provider(provider)
        _method = getattr(fake, method_name)
        kwargs["storage"] = storage
        _file = _method(**kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA,
    )
    def test_standalone_providers(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
        storage: BaseStorage = None,
    ) -> None:
        """Test standalone providers."""
        if storage is False:
            storage = FS_STORAGE
        _provider = provider(fake)  # noqa
        _method = getattr(_provider, method_name)
        kwargs["storage"] = storage
        _file = _method(**kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA_RETRY_FAILURES,
    )
    @pytest.mark.flaky(reruns=5)
    def test_standalone_providers_retry_failures(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
        storage: BaseStorage = None,
    ) -> None:
        """Test standalone providers."""
        if storage is False:
            storage = FS_STORAGE
        _provider = provider(fake)  # noqa
        _method = getattr(_provider, method_name)
        kwargs["storage"] = storage
        _file = _method(**kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    @parametrize(
        "fake, provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA_ALLOW_FAILURES,
    )
    @pytest.mark.xfail
    def test_standalone_providers_allow_failures(
        self: "ProvidersTestCase",
        fake: Faker,
        provider: FileProvider,
        method_name: str,
        kwargs: Dict[str, Any],
        storage: BaseStorage = None,
    ) -> None:
        """Test standalone providers, but allow failures."""
        if storage is None:
            storage = FS_STORAGE
        _provider = provider(fake)  # noqa
        _method = getattr(_provider, method_name)
        kwargs["storage"] = storage
        _file = _method(**kwargs)
        self.assertTrue(storage.exists(_file))

    @parametrize(
        "create_inner_file_func, content, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_zip_file(
        self: "ProvidersTestCase",
        create_inner_file_func: Optional[Callable] = None,
        content: Union[str, Dict] = None,
        create_inner_file_args: Dict[str, Any] = None,
    ) -> None:
        """Test standalone ZIP file provider."""
        _options = {"content": content}
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        if create_inner_file_args is not None:
            _options["create_inner_file_args"] = create_inner_file_args
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(FS_STORAGE.exists(_file))

    @parametrize(
        "create_inner_file_func, content, create_inner_file_args",
        __PARAMETRIZED_DATA_ARCHIVES,
    )
    def test_standalone_tar_file(
        self: "ProvidersTestCase",
        create_inner_file_func: Optional[Callable] = None,
        content: Union[str, Dict] = None,
        create_inner_file_args: Dict[str, Any] = None,
    ) -> None:
        """Test standalone TAR file provider."""
        _options = {"content": content}
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
        content: Union[str, Dict] = None,
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
        content: Union[str, Dict] = None,
    ) -> None:
        """Test standalone TAR file provider, but allow failures."""
        _options = {"content": content}
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        _file = TarFileProvider(None).tar_file(options=_options)

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
            # EML
            (
                "faker_file.providers.eml_file",
                "EmlFileProvider",
                create_inner_eml_file,
            ),
            # EPUB
            (
                "faker_file.providers.epub_file",
                "EpubFileProvider",
                create_inner_epub_file,
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
            # MP3
            (
                "faker_file.providers.mp3_file",
                "Mp3FileProvider",
                create_inner_mp3_file,
            ),
            # ODP
            (
                "faker_file.providers.odp_file",
                "OdpFileProvider",
                create_inner_odp_file,
            ),
            # ODS
            (
                "faker_file.providers.ods_file",
                "OdsFileProvider",
                create_inner_ods_file,
            ),
            # ODT
            (
                "faker_file.providers.odt_file",
                "OdtFileProvider",
                create_inner_odt_file,
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
            # TAR
            (
                "faker_file.providers.tar_file",
                "TarFileProvider",
                create_inner_tar_file,
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
            # ZIP
            (
                "faker_file.providers.zip_file",
                "ZipFileProvider",
                create_inner_zip_file,
            ),
        ],
    )
    def test_broken_imports(
        self: "ProvidersTestCase",
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

    def test_mp3_file_generate_not_implemented_exception(
        self: "ProvidersTestCase",
    ):
        with self.assertRaises(NotImplementedError):
            Mp3FileProvider(FAKER).mp3_file(mp3_generator_cls=BaseMp3Generator)

        class MyMp3Generator(BaseMp3Generator):
            """Test MP3 generator."""

        with self.assertRaises(NotImplementedError):
            Mp3FileProvider(FAKER).mp3_file(mp3_generator_cls=MyMp3Generator)
