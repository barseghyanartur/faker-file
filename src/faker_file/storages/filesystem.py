import os
import tempfile
from typing import Optional

from ..base import DEFAULT_REL_PATH
from .base import BaseStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("FileSystemStorage",)


class FileSystemStorage(BaseStorage):
    """File storage.

    Usage example:

        from faker_file.storages.filesystem import FileSystemStorage

        storage = FileSystemStorage()
        file = storage.generate_filename(prefix="zzz_", extension="docx")
        storage.write_text(file, "Lorem ipsum")
        storage.write_bytes(file, b"Lorem ipsum")

    Initialization with params:

        storage = FileSystemStorage()
    """

    def __init__(
        self: "FileSystemStorage",
        root_path: Optional[str] = tempfile.gettempdir(),
        rel_path: Optional[str] = DEFAULT_REL_PATH,
        *args,
        **kwargs,
    ) -> None:
        """
        :param root_path: Path of your files root directory (in case of Django
            it would be `settings.MEDIA_ROOT`).
        :param rel_path: Relative path (from root directory).
        """
        self.root_path = root_path
        self.rel_path = rel_path
        super().__init__(*args, **kwargs)

    def generate_filename(
        self: "FileSystemStorage",
        prefix: str,
        extension: str,
    ) -> str:
        """Generate filename."""
        dir_path = os.path.join(self.root_path, self.rel_path)
        os.makedirs(dir_path, exist_ok=True)
        if not extension:
            raise Exception("Extension shall be given!")
        with tempfile.NamedTemporaryFile(
            prefix=prefix,
            dir=dir_path,
            suffix=f".{extension}",
        ) as temp_file:
            return temp_file.name

    def write_text(
        self: "FileSystemStorage",
        filename: str,
        data: str,
        encoding: str = None,
    ) -> int:
        """Write text."""
        with open(filename, "w") as file:
            return file.write(data)

    def write_bytes(
        self: "FileSystemStorage",
        filename: str,
        data: bytes,
    ) -> int:
        """Write bytes."""
        with open(filename, "wb") as file:
            return file.write(data)

    def exists(self: "FileSystemStorage", filename: str) -> bool:
        """Write bytes."""
        if os.path.isabs(filename):
            return os.path.exists(filename)
        return os.path.exists(os.path.join(self.root_path, filename))

    def relpath(self: "FileSystemStorage", filename: str) -> str:
        """Return relative path."""
        return os.path.relpath(filename, self.root_path)

    def abspath(self: "FileSystemStorage", filename: str) -> str:
        """Return absolute path."""
        if os.path.isabs(filename):
            return os.path.abspath(filename)
        return os.path.abspath(os.path.join(self.root_path, filename))
