from typing import Union

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("BaseMp3Generator",)


class BaseMp3Generator:
    """Base MP3 generator."""

    content: str
    generator: Union[Faker, Generator, Provider]

    def __init__(
        self: "BaseMp3Generator",
        content: str,
        generator: Union[Faker, Generator, Provider],
        **kwargs,
    ) -> None:
        """Constructor.

        :param content: Text content to generate MP3 from.
        :param generator: `Faker` instance that could contain useful
            information, such as active locale.
        :param kwargs: Dictionary with parameters (for MP3 generator
            specific tuning).
        """
        self.content = content
        self.generator = generator
        self.handle_kwargs(**kwargs)

    def handle_kwargs(self: "BaseMp3Generator", **kwargs):
        """Handle kwargs."""

    def generate(self: "BaseMp3Generator", **kwargs) -> bytes:
        raise NotImplementedError("Method `generate` is not implemented.")
