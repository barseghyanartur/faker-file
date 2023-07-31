from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
    get_type_hints,
)

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider

from .helpers import wrap_text

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "BytesValue",
    "DEFAULT_FORMAT_FUNC",
    "DEFAULT_REL_PATH",
    "DynamicTemplate",
    "FileMixin",
    "StringList",
    "StringValue",
    "parse_format_func",
    "pystr_format_func",
    "returns_list",
)


DEFAULT_REL_PATH = "tmp"


class StringValue(str):
    data: Dict[str, Any] = {}


class BytesValue(bytes):
    data: Dict[str, Any] = {}


def parse_format_func(
    generator: Union[Faker, Generator, Provider], content: str
) -> str:
    return generator.parse(content)


def pystr_format_func(
    generator: Union[Faker, Generator, Provider], content: str
) -> str:
    return generator.pystr_format(content)


DEFAULT_FORMAT_FUNC = parse_format_func


class FileMixin:
    """File mixin."""

    numerify: Callable
    random_element: Callable
    formats: List[str]
    generator: Union[Faker, Generator, Provider]
    extension: str  # Desired file extension.

    def _generate_text_content(
        self,
        max_nb_chars: int,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
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
            content = format_func(self.generator, content)

        if wrap_chars_after:
            content = wrap_text(content, wrap_chars_after)

        return content


class DynamicTemplate:
    """Dynamic template."""

    def __init__(
        self, content_modifiers: List[Tuple[Callable, Dict[str, Any]]]
    ):
        self.content_modifiers = content_modifiers


class StringList:
    """String list.

    Usage example:

    .. code-block:: python
        :name: test_rst_string_list

        my_string = StringList(separator="\r\n")
        my_string += "grape"
        my_string += "peaches"
        print(my_string)
    """

    def __init__(
        self: "StringList",
        strings: Optional[List[str]] = None,
        separator: str = " ",
    ) -> None:
        self.strings = strings if strings is not None else []
        self.separator = separator

    def __repr__(self: "StringList") -> str:
        return self.__str__()

    def __str__(self: "StringList") -> str:
        return self.separator.join(self.strings)

    def __iadd__(self: "StringList", value: str) -> "StringList":
        self.add_string(value)
        return self

    def add_string(self: "StringList", value: str) -> None:
        self.strings.append(value)

    def remove_string(self: "StringList", value: str) -> None:
        if value in self.strings:
            self.strings.remove(value)


def returns_list(func: Callable) -> bool:
    """Checks if callable returns a list of Union[BytesValue, StringValue].

    Returns True if it's a List. Returns False otherwise.
    """
    try:
        return_type = get_type_hints(func).get("return", None)
    except Exception:
        return False

    if not return_type:
        return False

    return_origin = getattr(return_type, "__origin__", None)
    if return_origin is list or return_origin is List:
        # If it's a list, check the type of its elements
        element_type = getattr(return_type, "__args__", [None])[0]
        element_origin = getattr(element_type, "__origin__", None)
        if element_origin is Union:
            if set(getattr(element_type, "__args__", [])) == {
                BytesValue,
                StringValue,
            }:
                return True

    return False
