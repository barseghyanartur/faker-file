import logging
import unittest
from copy import deepcopy
from typing import Any, Dict, List, Tuple, Type, Union

from faker import Faker
from fuzzywuzzy import fuzz
from parametrize import parametrize
from tika import parser

from ..providers.docx_file import DocxFileProvider
from ..providers.eml_file import EmlFileProvider
from ..providers.odt_file import OdtFileProvider
from ..providers.pdf_file import PdfFileProvider
from ..providers.pdf_file.generators.reportlab_generator import (
    ReportlabPdfGenerator,
)
from ..providers.rtf_file import RtfFileProvider
from ..providers.txt_file import TxtFileProvider

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("DataIntegrityTestCase",)

FAKER = Faker()
FAKER.add_provider(DocxFileProvider)
FAKER.add_provider(EmlFileProvider)
FAKER.add_provider(OdtFileProvider)
FAKER.add_provider(PdfFileProvider)
FAKER.add_provider(RtfFileProvider)
FAKER.add_provider(TxtFileProvider)

FileProvider = Union[
    DocxFileProvider,
    EmlFileProvider,
    OdtFileProvider,
    PdfFileProvider,
    RtfFileProvider,
    TxtFileProvider,
]

LOGGER = logging.getLogger(__name__)


class DataIntegrityTestCase(unittest.TestCase):
    # fake, provider, method_name, kwargs
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
        (FAKER, DocxFileProvider, "docx_file", {"max_nb_chars": 2_048}, 90),
        # EML
        (FAKER, EmlFileProvider, "eml_file", {"max_nb_chars": 2_048}, 90),
        # ODT
        (FAKER, OdtFileProvider, "odt_file", {"max_nb_chars": 2_048}, 100),
        # PDF
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
        # RTF
        (FAKER, RtfFileProvider, "rtf_file", {"max_nb_chars": 2_048}, 100),
        # TXT
        (FAKER, TxtFileProvider, "txt_file", {"max_nb_chars": 2_048}, 100),
    ]

    @parametrize(
        "fake, provider, method_name, kwargs, similarity_margin",
        __PARAMETRIZED_DATA,
    )
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

        # Compare the original file content to the extracted content
        similarity = fuzz.ratio(_file.data["content"], extracted_content)

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
