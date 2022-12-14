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

    def generate_filename(self, prefix: str, extension: str) -> Any:
        """Generate filename."""
        raise NotImplementedError(
            "Method generate_filename is not implemented!"
        )

    def write_text(self, filename: Any, data: str, encoding: str = None) -> int:
        """Write text."""
        raise NotImplementedError("Method write_text is not implemented!")

    def write_bytes(self, filename: Any, data: bytes) -> int:
        """Write bytes."""
        raise NotImplementedError("Method write_bytes is not implemented!")

    def exists(self, filename: Any) -> bool:
        """Check if file exists."""
        raise NotImplementedError("Method exists is not implemented!")
