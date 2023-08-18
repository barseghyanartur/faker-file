from pathlib import Path
from typing import Optional, Union, overload

from faker.providers import BaseProvider

from ..base import BytesValue, FileMixin, StringValue
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("FileFromPathProvider",)


class FileFromPathProvider(BaseProvider, FileMixin):
    """File from given path provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.file_from_path import (
            FileFromPathProvide
        )

        FAKER = Faker()
        FAKER.add_provider(FileFromPathProvider)

        file = FAKER.file_from_path(
            path="/path/to/file.pdf"
        )

    Usage example with options:

    .. code-block:: python

        file = FAKER.file_from_path(
            path="/path/to/file.pdf",
            prefix="zzz",
        )
    """

    extension: str = ""

    @overload
    def file_from_path(
        self: "FileFromPathProvider",
        path: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def file_from_path(
        self: "FileFromPathProvider",
        path: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def file_from_path(
        self: "FileFromPathProvider",
        path: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """File from given path.

        :param path: Path to source file.
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
        source_file = Path(path)

        # Generic
        filename = storage.generate_filename(
            extension=source_file.suffix[1:],
            prefix=prefix,
            basename=basename,
        )
        data = {"filename": filename, "storage": storage}

        # Specific
        with open(path, "rb") as _file:
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
