import os
import tempfile

from ..base import DEFAULT_REL_PATH
from .base import BaseStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
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
    """

    def __init__(self: "FileSystemStorage", *args, **kwargs) -> None:
        self.root_path = kwargs.pop("root_path", tempfile.gettempdir())
        self.rel_path = kwargs.pop("rel_path", DEFAULT_REL_PATH)
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
        temp_file = tempfile.NamedTemporaryFile(
            prefix=prefix,
            dir=dir_path,
            suffix=f".{extension}",
        )
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

    def exists(self: "FileSystemStorage", filename: str) -> int:
        """Write bytes."""
        return os.path.exists(filename)
