import logging
import unittest
from copy import deepcopy
from typing import Any, Dict, List, Tuple, Type, Union

import pytest
from faker import Faker
from fuzzywuzzy import fuzz
from parametrize import parametrize
from tika import parser

from ..providers.docx_file import DocxFileProvider
from ..providers.eml_file import EmlFileProvider
from ..providers.epub_file import EpubFileProvider
from ..providers.odp_file import OdpFileProvider
from ..providers.ods_file import OdsFileProvider
from ..providers.odt_file import OdtFileProvider
from ..providers.pdf_file import PdfFileProvider
from ..providers.pdf_file.generators.pdfkit_generator import PdfkitPdfGenerator
from ..providers.pdf_file.generators.reportlab_generator import (
    ReportlabPdfGenerator,
)
from ..providers.pptx_file import PptxFileProvider
from ..providers.rtf_file import RtfFileProvider
from ..providers.txt_file import TxtFileProvider
from ..providers.xlsx_file import XlsxFileProvider
from ..providers.xml_file import XmlFileProvider
from ..registry import FILE_REGISTRY

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("DataIntegrityTestCase",)

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)
FAKER.add_provider(EmlFileProvider)
FAKER.add_provider(EpubFileProvider)
FAKER.add_provider(OdpFileProvider)
FAKER.add_provider(OdsFileProvider)
FAKER.add_provider(OdtFileProvider)
FAKER.add_provider(PdfFileProvider)
FAKER.add_provider(PptxFileProvider)
FAKER.add_provider(RtfFileProvider)
FAKER.add_provider(TxtFileProvider)
FAKER.add_provider(XlsxFileProvider)
FAKER.add_provider(XmlFileProvider)

FileProvider = Union[
    DocxFileProvider,
    EmlFileProvider,
    EpubFileProvider,
    OdpFileProvider,
    OdsFileProvider,
    OdtFileProvider,
    PdfFileProvider,
    PptxFileProvider,
    RtfFileProvider,
    TxtFileProvider,
    XlsxFileProvider,
    XmlFileProvider,
]

LOGGER = logging.getLogger(__name__)


class DataIntegrityTestCase(unittest.TestCase):
    """Data integrity tests.

    Methodology:

    - Generate file using given provider.
    - Extract text using Apache Tika.
    - Compare original text to the extracted text. If match is less
      than the specified margin, test fails.
    """

    # fake, provider, method_name, kwargs, similarity_margin
    __PARAMETRIZED_DATA: List[
        Tuple[
            Faker,
            Type[FileProvider],
            str,
            Dict[str, Any],
            int,
        ]
    ] = [
        # DOCX
        (FAKER, DocxFileProvider, "docx_file", {"max_nb_chars": 2_048}, 95),
        # EML
        (FAKER, EmlFileProvider, "eml_file", {"max_nb_chars": 2_048}, 95),
        # EPUB
        (FAKER, EpubFileProvider, "epub_file", {"max_nb_chars": 2_048}, 90),
        # ODP
        (FAKER, OdpFileProvider, "odp_file", {"max_nb_chars": 2_048}, 100),
        # ODS
        (FAKER, OdsFileProvider, "ods_file", {}, 75),
        # ODT
        (FAKER, OdtFileProvider, "odt_file", {"max_nb_chars": 2_048}, 100),
        # PDF
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "max_nb_chars": 2_048,
                "pdf_generator_cls": PdfkitPdfGenerator,
            },
            85,
        ),
        (
            FAKER,
            PdfFileProvider,
            "pdf_file",
            {
                "max_nb_chars": 2_048,
                "pdf_generator_cls": ReportlabPdfGenerator,
            },
            85,
        ),
        # PPTX
        (FAKER, PptxFileProvider, "pptx_file", {"max_nb_chars": 2_048}, 95),
        # RTF
        (FAKER, RtfFileProvider, "rtf_file", {"max_nb_chars": 2_048}, 100),
        # TXT
        (FAKER, TxtFileProvider, "txt_file", {"max_nb_chars": 2_048}, 100),
        # XLSX
        (FAKER, XlsxFileProvider, "xlsx_file", {}, 75),
        # XML
        (FAKER, XmlFileProvider, "xml_file", {}, 95),
    ]

    def tearDown(self) -> None:
        super().tearDown()
        FILE_REGISTRY.clean_up()

    @parametrize(
        "fake, provider, method_name, kwargs, similarity_margin",
        __PARAMETRIZED_DATA,
    )
    @pytest.mark.flaky(reruns=3)
    def test_file_content(
        self: "DataIntegrityTestCase",
        fake: Faker,
        provider: Type[FileProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        similarity_margin: int,
    ):
        _method = getattr(fake, method_name)
        _kwargs = deepcopy(kwargs)

        # Generate a file
        _file = _method(**_kwargs)

        # Extract the content from the generated file using Apache Tika
        parsed = parser.from_file(_file.data["filename"])
        extracted_content = parsed["content"]

        # Compare the original file content to the extracted content after
        # cleaning up both (remove double white-spaces).
        similarity = fuzz.ratio(
            " ".join(_file.data["content"].split()),
            " ".join(extracted_content.split()),
        )

        LOGGER.info(f"Provider: {method_name}, Similarity: {similarity}")
        if similarity < 100:
            LOGGER.warning(
                f"Original content: {_file.data['content']}\n"
                f"Extracted content: {extracted_content}"
            )

        # Assert that the similarity is at least the required margin %
        self.assertGreaterEqual(
            similarity,
            similarity_margin,
            f"Content of the generated {method_name} matches "
            f"the extracted content only for {similarity}% while "
            f"{similarity_margin}% is expected. \n"
            f"Original content: {_file.data['content']}\n"
            f"Extracted content: {extracted_content}",
        )
