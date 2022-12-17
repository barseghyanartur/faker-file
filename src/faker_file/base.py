from typing import Any, Callable, Dict, List, Optional, Union

from faker import Faker
from faker.providers.python import Provider

from .helpers import wrap_text

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "DEFAULT_REL_PATH",
    "FileMixin",
    "StringValue",
)


DEFAULT_REL_PATH = "tmp"


class StringValue(str):
    data: Dict[str, Any] = {}


class FileMixin:
    """File mixin."""

    numerify: Callable
    random_element: Callable
    formats: List[str]
    generator: Union[Provider, Faker]
    extension: str  # Desired file extension.

    def _generate_text_content(
        self,
        max_nb_chars: int,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
    ) -> str:
        """Generate text content.

        :param max_nb_chars: Max number of chars.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :return: String with random chars.
        """
        if self.generator is None:
            self.generator = Faker()

        # Specific
        if content is None:
            content = self.generator.text(max_nb_chars)
        else:
            content = self.generator.pystr_format(content)

        if wrap_chars_after:
            content = wrap_text(content, wrap_chars_after)

        return content
