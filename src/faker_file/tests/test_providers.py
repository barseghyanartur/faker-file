import os.path
import unittest
from typing import Optional, Union

from faker import Faker
from faker.providers import BaseProvider
from parametrize import parametrize

from ..providers.docx_file import DocxFileProvider
from ..providers.pdf_file import PdfFileProvider
from ..providers.pptx_file import PptxFileProvider
from ..providers.txt_file import TxtFileProvider
from ..providers.zip_file import (
    ZipFileProvider,
    create_inner_docx_file,
    create_inner_pdf_file,
    create_inner_pptx_file,
    create_inner_txt_file,
)

__all__ = ("ProvidersTestCase",)


FileProvider = Union[
    DocxFileProvider,
    PdfFileProvider,
    PptxFileProvider,
    TxtFileProvider,
    ZipFileProvider,
]


class ProvidersTestCase(unittest.TestCase):
    """Providers test case."""

    FAKER: Faker

    @parametrize(
        "provider, method_name",
        [
            (DocxFileProvider, "docx_file"),
            (PdfFileProvider, "pdf_file"),
            (PptxFileProvider, "pptx_file"),
            (TxtFileProvider, "txt_file"),
            (ZipFileProvider, "zip_file"),
        ],
    )
    def test_faker(self, provider: FileProvider, method_name: str) -> None:
        """Test faker provider integration."""
        _faker = Faker()
        _faker.add_provider(provider)
        _method = getattr(_faker, method_name)
        _file = _method()
        self.assertTrue(os.path.exists(_file))

    @parametrize(
        "provider, method_name",
        [
            (DocxFileProvider, "docx_file"),
            (PdfFileProvider, "pdf_file"),
            (PptxFileProvider, "pptx_file"),
            (TxtFileProvider, "txt_file"),
            (ZipFileProvider, "zip_file"),
        ],
    )
    def test_standalone_providers(
        self,
        provider: FileProvider,
        method_name: str,
    ) -> None:
        """Test standalone providers."""
        _provider = provider(None)  # noqa
        _method = getattr(_provider, method_name)
        _file = _method()
        self.assertTrue(os.path.exists(_file))

    @parametrize(
        "create_inner_file_func",
        [
            (None,),
            (create_inner_docx_file,),
            (create_inner_txt_file,),
            (create_inner_pdf_file,),
            (create_inner_pptx_file,),
        ],
    )
    def test_standalone_zip_file(
        self,
        create_inner_file_func: Optional[callable] = None,
    ):
        """Test standalone ZIP file provider."""
        _options = {"content": "Lorem ipsum"}
        if create_inner_file_func is not None:
            _options["create_inner_file_func"] = create_inner_file_func
        _file = ZipFileProvider(None).zip_file(options=_options)

        self.assertTrue(os.path.exists(_file))
