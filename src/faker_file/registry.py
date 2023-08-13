import logging
from threading import Lock
from typing import Set

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
    """Stores list of tuples.

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

    def add(self, string_value: StringValue):
        with self._lock:
            self._registry.add(string_value)

    def remove(self, string_value: StringValue):
        with self._lock:
            # No error if the element doesn't exist
            self._registry.discard(string_value)

    def clean_up(self):
        with self._lock:
            while self._registry:
                file = self._registry.pop()
                try:
                    file.data["storage"].unlink(file.data["filename"])
                except Exception as e:
                    LOGGER.error(
                        f"Failed to unlink file {file.data['filename']}: {e}"
                    )


FILE_REGISTRY = FileRegistry()
