import os.path
import tempfile
import unittest
from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple, Type, Union

import tika
from faker import Faker
from parametrize import parametrize
from pathy import use_fs

from ..base import DEFAULT_REL_PATH
from ..providers.augment_file_from_dir import AugmentFileFromDirProvider
from ..providers.augment_file_from_dir.augmenters.nlpaug_augmenter import (
    DEFAULT_ACTION,
    DEFAULT_MODEL_PATH,
    ContextualWordEmbeddingsAugmenter,
)
from ..providers.base.text_augmenter import BaseTextAugmenter
from ..providers.base.text_extractor import BaseTextExtractor
from ..providers.docx_file import DocxFileProvider
from ..providers.eml_file import EmlFileProvider
from ..providers.epub_file import EpubFileProvider
from ..providers.pdf_file import PdfFileProvider
from ..providers.rtf_file import RtfFileProvider
from ..providers.txt_file import TxtFileProvider
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.cloud import PathyFileSystemStorage
from ..storages.filesystem import FileSystemStorage
from .texts import TEXT_DOCX, TEXT_EML, TEXT_EPUB, TEXT_PDF, TEXT_RTF, TEXT_TXT

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("AugmentFileFromDirProviderTestCase",)


FileProvider = Union[
    DocxFileProvider,
    EmlFileProvider,
    EpubFileProvider,
    PdfFileProvider,
    RtfFileProvider,
    TxtFileProvider,
]

_FAKER = Faker()
FS_STORAGE = FileSystemStorage()
PATHY_FS_STORAGE = PathyFileSystemStorage(bucket_name="tmp", rel_path="tmp")
SOURCE_DIR_PATH = os.path.join(tempfile.gettempdir(), DEFAULT_REL_PATH)


class AugmentFileFromDirProviderTestCase(unittest.TestCase):
    """AugmentFileFromDirProvider test case."""

    FAKER: Faker
    # provider, method_name, kwargs, storage
    __PARAMETRIZED_DATA: List[
        Tuple[
            Type[AugmentFileFromDirProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # AugmentFileFromDirProvider
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {
                "source_dir_path": SOURCE_DIR_PATH,
                "text_augmenter_cls": ContextualWordEmbeddingsAugmenter,
                "text_augmenter_kwargs": {
                    "model_path": DEFAULT_MODEL_PATH,
                    "action": DEFAULT_ACTION,
                },
            },
            None,
        ),
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {
                "source_dir_path": SOURCE_DIR_PATH,
            },
            None,
        ),
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {
                "source_dir_path": SOURCE_DIR_PATH,
            },
            False,
        ),
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {
                "source_dir_path": SOURCE_DIR_PATH,
            },
            PATHY_FS_STORAGE,
        ),
        # Testing Nones
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {
                "source_dir_path": SOURCE_DIR_PATH,
                "text_extractor_cls": None,
                "text_augmenter_cls": None,
            },
            PATHY_FS_STORAGE,
        ),
        # DOCX
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {"source_dir_path": SOURCE_DIR_PATH, "extensions": ["docx"]},
            None,
        ),
        # EML
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {"source_dir_path": SOURCE_DIR_PATH, "extensions": ["eml"]},
            None,
        ),
        # EPUB
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {"source_dir_path": SOURCE_DIR_PATH, "extensions": ["epub"]},
            None,
        ),
        # PDF
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {"source_dir_path": SOURCE_DIR_PATH, "extensions": ["pdf"]},
            None,
        ),
        # RTF
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {"source_dir_path": SOURCE_DIR_PATH, "extensions": ["rtf"]},
            None,
        ),
        # TXT
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {"source_dir_path": SOURCE_DIR_PATH, "extensions": ["txt"]},
            None,
        ),
    ]

    # provider, method_name, kwargs, storage
    __RAW_PARAMETRIZED_DATA: List[
        Tuple[
            Type[AugmentFileFromDirProvider],
            str,
            Dict[str, Any],
            Optional[Union[bool, PathyFileSystemStorage]],
        ]
    ] = [
        # AugmentFileFromDirProvider
        (
            AugmentFileFromDirProvider,
            "augment_file_from_dir",
            {
                "source_dir_path": SOURCE_DIR_PATH,
            },
            None,
        ),
    ]

    def setUp(self: "AugmentFileFromDirProviderTestCase"):
        super().setUp()
        tika.initVM()
        use_fs(tempfile.gettempdir())

    @classmethod
    def setUpClass(cls: Type["AugmentFileFromDirProviderTestCase"]) -> None:
        super().setUpClass()
        DocxFileProvider(_FAKER).docx_file(
            prefix="source_",
            content=TEXT_DOCX,
            storage=FS_STORAGE,
        )
        EmlFileProvider(_FAKER).eml_file(
            prefix="source_",
            content=TEXT_EML,
            storage=FS_STORAGE,
        )
        EpubFileProvider(_FAKER).epub_file(
            prefix="source_",
            content=TEXT_EPUB,
            storage=FS_STORAGE,
        )
        PdfFileProvider(_FAKER).pdf_file(
            prefix="source_",
            content=TEXT_PDF,
            storage=FS_STORAGE,
        )
        RtfFileProvider(_FAKER).rtf_file(
            prefix="source_",
            content=TEXT_RTF,
            storage=FS_STORAGE,
        )
        TxtFileProvider(_FAKER).txt_file(
            prefix="source_",
            content=TEXT_TXT,
            storage=FS_STORAGE,
        )

    @classmethod
    def tearDownClass(cls: Type["AugmentFileFromDirProviderTestCase"]) -> None:
        super().tearDownClass()
        FILE_REGISTRY.clean_up()

    @parametrize(
        "provider, method_name, kwargs, storage",
        __PARAMETRIZED_DATA,
    )
    def test_standalone(
        self: "AugmentFileFromDirProviderTestCase",
        provider: Type[AugmentFileFromDirProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test standalone."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        _provider = provider(None)  # noqa
        _method = getattr(_provider, method_name)
        _kwargs["storage"] = storage
        _file = _method(**_kwargs)
        self.assertTrue((storage or FS_STORAGE).exists(_file))

    def test_augment_file_from_dir_extract_not_implemented_exception(
        self: "AugmentFileFromDirProviderTestCase",
    ):
        with self.assertRaises(NotImplementedError):
            AugmentFileFromDirProvider(_FAKER).augment_file_from_dir(
                source_dir_path=SOURCE_DIR_PATH,
                text_extractor_cls=BaseTextExtractor,
            )

        class MyTextExtractor(BaseTextExtractor):
            """Test text extractor."""

        with self.assertRaises(NotImplementedError):
            AugmentFileFromDirProvider(_FAKER).augment_file_from_dir(
                source_dir_path=SOURCE_DIR_PATH,
                text_extractor_cls=MyTextExtractor,
            )

    def test_augment_file_from_dir_augment_not_implemented_exception(
        self: "AugmentFileFromDirProviderTestCase",
    ):
        with self.assertRaises(NotImplementedError):
            AugmentFileFromDirProvider(_FAKER).augment_file_from_dir(
                source_dir_path=SOURCE_DIR_PATH,
                text_augmenter_cls=BaseTextAugmenter,
            )

        class MyTextAugmenter(BaseTextAugmenter):
            """Test text augmenter."""

        with self.assertRaises(NotImplementedError):
            AugmentFileFromDirProvider(_FAKER).augment_file_from_dir(
                source_dir_path=SOURCE_DIR_PATH,
                text_augmenter_cls=MyTextAugmenter,
            )

    @parametrize(
        "provider, method_name, kwargs, storage",
        __RAW_PARAMETRIZED_DATA,
    )
    def test_raw_standalone(
        self: "AugmentFileFromDirProviderTestCase",
        provider: Type[AugmentFileFromDirProvider],
        method_name: str,
        kwargs: Dict[str, Any],
        storage: Optional[BaseStorage] = None,
    ) -> None:
        """Test standalone."""
        _kwargs = deepcopy(kwargs)
        if storage is False:
            storage = FS_STORAGE
        _provider = provider(None)  # noqa
        _method = getattr(_provider, method_name)
        _kwargs["storage"] = storage
        _kwargs["raw"] = True
        _bytes = _method(**_kwargs)
        self.assertIsInstance(_bytes, bytes)
        self.assertGreater(len(_bytes), 0)
