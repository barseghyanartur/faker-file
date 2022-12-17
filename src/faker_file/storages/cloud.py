import os
import tempfile
from typing import Any, Dict, Optional, Union

from pathy import Pathy

from ..base import DEFAULT_REL_PATH
from .base import BaseStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "CloudStorage",
    "PathyFileSystemStorage",
)


DEFAULT_ROOT_PATH = "tmp"


class CloudStorage(BaseStorage):
    """Base cloud storage."""

    bucket_name: str
    bucket: Pathy
    credentials: Dict[str, str]
    schema: str = None

    def __init__(
        self: "CloudStorage",
        bucket_name: str,
        root_path: Optional[str] = DEFAULT_ROOT_PATH,
        rel_path: Optional[str] = DEFAULT_REL_PATH,
        credentials: Optional[Dict[str, Any]] = None,
        *args,
        **kwargs,
    ):
        if self.schema is None:
            raise Exception("The `schema` property should the set!")
        self.bucket_name = bucket_name
        self.root_path = root_path
        self.rel_path = rel_path
        self.cache_dir = None
        credentials = credentials or {}

        self.bucket = Pathy(f"{self.schema}://{self.bucket_name}")
        # If bucket does not exist, create
        if not self.bucket.exists():
            self.bucket.mkdir()

        super().__init__(*args, **kwargs)

        if credentials:
            self.authenticate(**credentials)

    def authenticate(self, **kwargs):
        raise NotImplementedError("Method authenticate is not implemented!")

    def generate_filename(
        self: "CloudStorage",
        prefix: str,
        extension: str,
    ) -> Pathy:
        """Generate filename."""
        if not extension:
            raise Exception("Extension shall be given!")
        with tempfile.NamedTemporaryFile(
            prefix=prefix,
            suffix=f".{extension}",
        ) as temp_file:
            return (
                self.bucket
                / self.root_path
                / self.rel_path
                / os.path.basename(temp_file.name)
            )

    def write_text(
        self: "CloudStorage",
        filename: Pathy,
        data: str,
        encoding: str = None,
    ) -> int:
        """Write text."""
        file = self.bucket / self.root_path / self.rel_path / filename
        return file.write_text(data, encoding)

    def write_bytes(self: "CloudStorage", filename: Pathy, data: bytes) -> int:
        """Write bytes."""
        file = self.bucket / self.root_path / self.rel_path / filename
        return file.write_bytes(data)

    def exists(self: "CloudStorage", filename: Union[Pathy, str]) -> bool:
        """Check if file exists."""
        if isinstance(filename, str):
            filename = self.bucket / self.root_path / filename
        return filename.exists()

    def relpath(self: "CloudStorage", filename: Pathy) -> str:
        """Return relative path."""
        return str(filename.relative_to(self.bucket / self.root_path))

    def abspath(self: "CloudStorage", filename: Pathy) -> str:
        """Return relative path."""
        return filename.as_uri()


class PathyFileSystemStorage(CloudStorage):
    """Pathy FileSystem Storage.

    Usage example:

        from faker_file.storages.cloud import PathyFileSystemStorage

        fs_storage = PathyFileSystemStorage(
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = fs_storage.generate_filename(prefix="zzz_", extension="docx")
        fs_storage.write_text(file, "Lorem ipsum")
        fs_storage.write_bytes(file, b"Lorem ipsum")
    """

    schema: str = "file"

    def authenticate(self: "PathyFileSystemStorage", **kwargs) -> None:
        """Authenticate. Does nothing."""
