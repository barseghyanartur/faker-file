import os
from pathlib import Path
from random import choice
from typing import Any, Dict, Iterable, Optional, Type

from faker.providers import BaseProvider

from ...base import FileMixin, StringValue
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage
from ..helpers.inner import (
    create_inner_docx_file,
    create_inner_eml_file,
    create_inner_epub_file,
    create_inner_odt_file,
    create_inner_pdf_file,
    create_inner_rtf_file,
    create_inner_txt_file,
)
from .augmenters.base import BaseTextAugmenter
from .augmenters.nlpaug_augmenter import ContextualWordEmbeddingsAugmenter
from .extractors.base import BaseTextExtractor
from .extractors.tika_extractor import TikaTextExtractor

# Full list:
# create_inner_bin_file: N/A
# create_inner_csv_file: Not supported
# create_inner_docx_file: Supported
# create_inner_eml_file: Supported
# create_inner_epub_file: Supported
# create_inner_ico_file: Not supported
# create_inner_jpeg_file: Not supported
# create_inner_mp3_file: Not supported
# create_inner_ods_file: Not supported
# create_inner_odt_file: Supported
# create_inner_pdf_file: Supported
# create_inner_png_file: Not supported
# create_inner_pptx_file: Not supported
# create_inner_rtf_file: Supported
# create_inner_svg_file: Not supported
# create_inner_txt_file: Supported
# create_inner_webp_file: Not supported
# create_inner_xlsx_file: Not supported
# create_inner_zip_file: Not supported


__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("AugmentFileFromDirProvider",)

FILE_TYPE_TO_INNER_FUNC_MAPPING = {
    "docx": create_inner_docx_file,
    "eml": create_inner_eml_file,
    "epub": create_inner_epub_file,
    "odt": create_inner_odt_file,
    "pdf": create_inner_pdf_file,
    "rtf": create_inner_rtf_file,
    "txt": create_inner_txt_file,
}

EXTENSIONS = set(FILE_TYPE_TO_INNER_FUNC_MAPPING.keys())


class AugmentFileFromDirProvider(BaseProvider, FileMixin):
    """Augment file from given directory provider.

    Usage example:

        from faker_file.providers.augment_file_from_dir import (
            AugmentFileFromDirProvider,
        )

        file = AugmentFileFromDirProvider(None).augment_file_from_dir(
            source_dir_path="/tmp/tmp/",
        )

    Usage example with options:

        from faker_file.providers.augment_file_from_dir import (
            AugmentFileFromDirProvider,
        )

        file = AugmentFileFromDirProvider(None).augment_file_from_dir(
            source_dir_path="/tmp/tmp/",
            prefix="zzz",
            extensions={"docx", "pdf"}
        )
    """

    extension: str = ""

    def augment_file_from_dir(
        self: "AugmentFileFromDirProvider",
        source_dir_path: str,
        extensions: Iterable[str] = None,
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        wrap_chars_after: Optional[int] = None,
        text_extractor_cls: Type[BaseTextExtractor] = TikaTextExtractor,
        text_extractor_kwargs: Optional[Dict[str, Any]] = None,
        text_augmenter_cls: Type[
            BaseTextAugmenter
        ] = ContextualWordEmbeddingsAugmenter,
        text_augmenter_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> StringValue:
        """Augment a random file from given directory.

        :param source_dir_path: Source files directory.
        :param extensions: Allowed extensions.
        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param text_extractor_cls: Text extractor class.
        :param text_extractor_kwargs: Text extractor kwargs.
        :param text_augmenter_cls: Text augmenter class.
        :param text_augmenter_kwargs: Text augmenter kwargs.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        if extensions is None:
            extensions = EXTENSIONS

        # Specific
        source_file_choices = [
            os.path.join(source_dir_path, _f)
            for _f in os.listdir(source_dir_path)
            if (
                os.path.isfile(os.path.join(source_dir_path, _f))
                and os.path.splitext(_f)[1][1:] in extensions
            )
        ]
        source_file_path = choice(source_file_choices)
        source_file = Path(source_file_path)

        if text_extractor_cls is None:
            text_extractor_cls = TikaTextExtractor

        if not text_extractor_kwargs:
            text_extractor_kwargs = {}

        text_extractor = text_extractor_cls(**text_extractor_kwargs)
        extracted_content = text_extractor.extract(source_file)
        file_type = source_file.suffix[1:]

        if text_augmenter_cls is None:
            text_augmenter_cls = ContextualWordEmbeddingsAugmenter

        if not text_augmenter_kwargs:
            text_augmenter_kwargs = {}

        text_augmenter = text_augmenter_cls(**text_augmenter_kwargs)
        content = text_augmenter.augment(extracted_content)

        return FILE_TYPE_TO_INNER_FUNC_MAPPING[file_type](
            storage=storage,
            prefix=prefix,
            content=content,
            wrap_chars_after=wrap_chars_after,
        )
