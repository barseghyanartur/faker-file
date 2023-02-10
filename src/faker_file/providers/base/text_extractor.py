from pathlib import Path
from typing import Union

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("BaseTextExtractor",)


class BaseTextExtractor:
    """Base text extractor."""

    path: str

    def __init__(
        self: "BaseTextExtractor",
        **kwargs,
    ) -> None:
        """Constructor.

        :param kwargs: Dictionary with parameters (for text extractor
            specific tuning).
        """
        self.handle_kwargs(**kwargs)

    def handle_kwargs(self: "BaseTextExtractor", **kwargs):
        """Handle kwargs."""

    def extract(
        self: "BaseTextExtractor",
        source_file: Union[Path, str],
    ) -> str:
        raise NotImplementedError("Method `extract` is not implemented.")
