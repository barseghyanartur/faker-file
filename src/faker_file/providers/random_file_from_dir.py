import os
from pathlib import Path
from random import choice
from typing import Optional, Union, overload

from faker.providers import BaseProvider

from ..base import BytesValue, FileMixin, StringValue
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("RandomFileFromDirProvider",)


class RandomFileFromDirProvider(BaseProvider, FileMixin):
    """Random file from given directory provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.random_file_from_dir import (
            RandomFileFromDirProvider,
        )

        FAKER = Faker()
        FAKER.add_provider(RandomFileFromDirProvider)

        file = FAKER.random_file_from_dir(
            source_dir_path="/tmp/tmp/",
        )

    Usage example with options:

    .. code-block:: python

        file = FAKER.random_file_from_dir(
            source_dir_path="/tmp/tmp/",
            prefix="zzz",
        )
    """

    extension: str = ""

    @overload
    def random_file_from_dir(
        self: "RandomFileFromDirProvider",
        source_dir_path: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def random_file_from_dir(
        self: "RandomFileFromDirProvider",
        source_dir_path: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def random_file_from_dir(
        self: "RandomFileFromDirProvider",
        source_dir_path: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Pick a random file from given directory.

        :param source_dir_path: Source files directory.
        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
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
            extension=source_file.suffix[1:],
            prefix=prefix,
            basename=basename,
        )
        data = {"filename": filename, "storage": storage}

        # Specific
        with open(source_file_path, "rb") as _file:
            if raw:
                raw_content = BytesValue(_file.read())
                raw_content.data = data
                return raw_content

            storage.write_bytes(filename, _file.read())

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
