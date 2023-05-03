from typing import Any, Dict, Union

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("BasePdfGenerator",)


class BasePdfGenerator:
    """Base PDF generator."""

    def __init__(
        self: "BasePdfGenerator",
        **kwargs,
    ) -> None:
        """Constructor.

        :param kwargs: Dictionary with parameters (for PDF generator
            specific tuning).
        """
        self.handle_kwargs(**kwargs)

    def handle_kwargs(self: "BasePdfGenerator", **kwargs):
        """Handle kwargs."""

    def generate(
        self: "BasePdfGenerator",
        content: str,
        data: Dict[str, Any],
        provider: Union[Faker, Generator, Provider],
    ) -> bytes:
        raise NotImplementedError("Method `generate` is not implemented.")
