from pathlib import Path
from typing import Union

import tika
from tika import parser

from ...base.text_extractor import BaseTextExtractor

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TikaTextExtractor",)


class TikaTextExtractor(BaseTextExtractor):
    """Text extractor based on `Apache Tika` and `tika-python`.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.augment_file_from_dir import (
            AugmentFileFromDirProvider,
        )
        from faker_file.providers.augment_file_from_dir.extractors import (
            tika_extractor,
        )

        FAKER = Faker()
        FAKER.add_provider(AugmentFileFromDirProvider)

        file = FAKER.augment_file_from_dir(
            text_extractor_cls=tika_extractor.TikaTextExtractor
        )
    """

    def handle_kwargs(self: "TikaTextExtractor", **kwargs) -> None:
        """Handle kwargs."""

    def extract(
        self: "TikaTextExtractor",
        source_file: Union[Path, str],
    ) -> str:
        """Extract text."""
        tika.initVM()
        parsed = parser.from_file(str(source_file))
        return parsed["content"]
