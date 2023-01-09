import os
from pathlib import Path
from random import choice
from typing import Optional

from faker.providers import BaseProvider

from ..base import FileMixin, StringValue
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("RandomFileFromDirProvider",)


class RandomFileFromDirProvider(BaseProvider, FileMixin):
    """Random file from given directory provider.

    Usage example:

        from faker_file.providers.random_file_from_dir import (
            RandomFileFromDirProvider,
        )

        file = RandomFileFromDirProvider(None).random_file_from_dir(
            source_dir_path="/tmp/tmp/",
        )

    Usage example with options:

        from faker_file.providers.random_file_from_dir import (
            RandomFileFromDirProvider,
        )

        file = RandomFileFromDirProvider(None).random_file_from_dir(
            source_dir_path="/tmp/tmp/",
            prefix="zzz",
        )
    """

    extension: str = ""

    def random_file_from_dir(
        self: "RandomFileFromDirProvider",
        source_dir_path: str,
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Pick a random file from given directory.

        :param source_dir_path: Source files directory.
        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.

        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        # Specific
        source_file_choices = [
            os.path.join(source_dir_path, _f)
            for _f in os.listdir(source_dir_path)
            if os.path.isfile(os.path.join(source_dir_path, _f))
        ]
        source_file_path = choice(source_file_choices)
        source_file = Path(source_file_path)

        # Generic
        filename = storage.generate_filename(
            prefix=prefix,
            extension=source_file.suffix[1:],
        )

        # Specific
        with open(source_file_path, "rb") as _file:
            storage.write_bytes(filename, _file.read())

        # Generic
        file_name = StringValue(storage.relpath(filename))
        return file_name
