import logging
from threading import Lock
from typing import Optional, Set, Union

from .base import StringValue

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "FILE_REGISTRY",
    "FileRegistry",
)


LOGGER = logging.getLogger(__name__)


class FileRegistry:
    """Stores list `StringValue` instances.

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.txt_file import TxtFileProvider

        FAKER = Faker()
        FAKER.add_provider(TxtFileProvider)

        txt_file_1 = FAKER.txt_file()
        txt_file_2 = FAKER.txt_file()
        ...
        txt_file_n = FAKER.txt_file()

        # The FileRegistry._registry would then contain this:
        {
            txt_file_1,
            txt_file_2,
            ...,
            txt_file_n,
        }
    """

    def __init__(self):
        self._registry: Set[StringValue] = set()
        self._lock = Lock()

    def add(self, string_value: StringValue) -> None:
        with self._lock:
            self._registry.add(string_value)

    def remove(self, string_value: Union[StringValue, str]) -> bool:
        if not isinstance(string_value, StringValue):
            string_value = self.search(string_value)

        if not string_value:
            return False

        with self._lock:
            # No error if the element doesn't exist
            self._registry.discard(string_value)
            try:
                string_value.data["storage"].unlink(
                    string_value.data["filename"]
                )
                return True
            except Exception as e:
                LOGGER.error(
                    f"Failed to unlink file "
                    f"{string_value.data['filename']}: {e}"
                )
            return False

    def search(self, value: str) -> Optional[StringValue]:
        with self._lock:
            for string_value in self._registry:
                if string_value == value:
                    return string_value
        return None

    def clean_up(self) -> None:
        with self._lock:
            while self._registry:
                file = self._registry.pop()
                try:
                    file.data["storage"].unlink(file.data["filename"])
                except Exception as err:
                    LOGGER.error(
                        f"Failed to unlink file {file.data['filename']}: {err}"
                    )


FILE_REGISTRY = FileRegistry()
