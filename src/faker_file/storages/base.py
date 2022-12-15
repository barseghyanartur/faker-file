import os
import tempfile
from typing import Any

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("BaseStorage",)


class BaseStorage:
    """Base storage."""

    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs

    def generate_filename(
        self: "BaseStorage", prefix: str, extension: str
    ) -> Any:
        """Generate filename."""
        raise NotImplementedError(
            "Method generate_filename is not implemented!"
        )

    def generate_temporary_local_filename(
        self: "BaseStorage", prefix: str, extension: str
    ) -> str:
        dir_path = os.path.join(tempfile.gettempdir(), self.rel_path)
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
        self: "BaseStorage", filename: Any, data: str, encoding: str = None
    ) -> int:
        """Write text."""
        raise NotImplementedError("Method write_text is not implemented!")

    def write_bytes(self: "BaseStorage", filename: Any, data: bytes) -> int:
        """Write bytes."""
        raise NotImplementedError("Method write_bytes is not implemented!")

    def exists(self: "BaseStorage", filename: Any) -> bool:
        """Check if file exists."""
        raise NotImplementedError("Method exists is not implemented!")

    def relpath(self: "BaseStorage", filename: Any) -> str:
        """Return relative path."""
        raise NotImplementedError("Method relpath is not implemented!")

    def abspath(self: "BaseStorage", filename: Any) -> str:
        """Return absolute path."""
        raise NotImplementedError("Method abspath is not implemented!")