import random
import string
from typing import Any, Optional

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2025 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("BaseStorage",)


class BaseStorage:
    """Base storage."""

    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs

    def generate_basename(
        self: "BaseStorage",
        prefix: str = "tmp",
        length: int = 8,
    ) -> str:
        """Generate a random alphanumeric sequence."""
        if not prefix:
            prefix = "tmp"
        # Use lowercase letters, digits and underscore
        characters = string.ascii_lowercase + string.digits + "_"
        return prefix + "".join(random.choices(characters, k=length))

    def generate_filename(
        self: "BaseStorage",
        extension: str,
        prefix: Optional[str] = None,
        basename: Optional[str] = None,
    ) -> Any:
        """Generate filename."""
        raise NotImplementedError(
            "Method generate_filename is not implemented!"
        )

    def write_text(
        self: "BaseStorage",
        filename: Any,
        data: str,
        encoding: Optional[str] = None,
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

    def unlink(self: "BaseStorage", filename: Any) -> None:
        """Delete the file."""
        raise NotImplementedError("Method unlink is not implemented!")
