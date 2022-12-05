import os
import string
from random import choice
from typing import Optional, Union

from faker import Faker
from faker.providers import BaseProvider

from .helpers import wrap_text

FAKER = Faker()

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "BaseContentGenerator",
    "FakeTextContentGenerator",
    "RandomCharsContentGenerator",
    "DEFAULT_CONTENT_GENERATOR",
)


class BaseContentGenerator:
    """Base content generator."""

    def __init__(self, provider: BaseProvider, *args, **kwargs):
        self.provider = provider
        super(BaseContentGenerator).__init__(*args, **kwargs)

    def generate_text(
        self,
        max_nb_chars: int,
        wrap_chars_after: Optional[int] = None,
    ) -> Union[str, bytes]:
        raise NotImplementedError


class RandomCharsContentGenerator(BaseContentGenerator):
    """Random chars content generator."""

    def generate_text(
        self,
        max_nb_chars: int,
        wrap_chars_after: Optional[int] = None,
    ) -> str:
        random_chars = "".join(
            choice(string.ascii_lowercase) for _ in range(max_nb_chars)
        )
        if wrap_chars_after:
            random_chars = wrap_text(random_chars, wrap_chars_after)
        return random_chars


class RandomBytesContentGenerator(BaseContentGenerator):
    """Random bytes content generator."""

    def generate_text(
        self,
        max_nb_chars: int,
        wrap_chars_after: Optional[int] = None,
    ) -> bytes:
        return os.urandom(max_nb_chars)


class FakeTextContentGenerator(BaseContentGenerator):
    """Fake text content generator."""

    def generate_text(
        self,
        max_nb_chars: int,
        wrap_chars_after: Optional[int] = None,
    ) -> str:
        fake_text = FAKER.text(max_nb_chars=max_nb_chars)
        if wrap_chars_after:
            fake_text = wrap_text(fake_text, wrap_chars_after)
        return fake_text


DEFAULT_CONTENT_GENERATOR = FakeTextContentGenerator
