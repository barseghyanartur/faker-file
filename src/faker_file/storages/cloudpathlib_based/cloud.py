from abc import abstractmethod
from typing import Any, Dict, Optional, Union

from cloudpathlib import CloudPath

from ...base import DEFAULT_REL_PATH
from ..base import BaseStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "CloudStorage",
    "LocalCloudFileSystemStorage",
)

DEFAULT_ROOT_PATH = "tmp"


class CloudStorage(BaseStorage):
    """Base cloud storage."""

    bucket_name: str
    bucket: CloudPath
    credentials: Dict[str, str]
    schema: Optional[str] = None

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
            raise Exception("The `schema` property should be set!")
        self.bucket_name = bucket_name
        self.root_path = root_path or ""
        self.rel_path = rel_path or ""
        self.cache_dir = None
        credentials = credentials or {}

        if credentials:
            self.authenticate(**credentials)

        self.bucket = CloudPath(f"{self.schema}://{self.bucket_name}")
        # If bucket does not exist, create it (if supported)
        if not self.bucket.exists():
            self.bucket.mkdir(exist_ok=True)

        super().__init__(*args, **kwargs)

    @abstractmethod
    def authenticate(self, *args, **kwargs):
        raise NotImplementedError("Method authenticate is not implemented!")

    def generate_filename(
        self: "CloudStorage",
        extension: str,
        prefix: Optional[str] = None,
        basename: Optional[str] = None,
    ) -> CloudPath:
        """Generate filename."""
        if not extension:
            raise Exception("Extension shall be given!")

        if not basename:
            basename = self.generate_basename(prefix)

        return (
            self.bucket /
            self.root_path /
            self.rel_path /
            f"{basename}.{extension}"
        )

    def write_text(
        self: "CloudStorage",
        filename: Union[CloudPath, str],
        data: str,
        encoding: Optional[str] = None,
    ) -> int:
        """Write text."""
        if not isinstance(filename, CloudPath):
            filename = self.bucket / self.root_path / self.rel_path / filename
        filename.write_text(data, encoding=encoding)
        return 0

    def write_bytes(
        self: "CloudStorage",
        filename: Union[CloudPath, str],
        data: bytes,
    ) -> int:
        """Write bytes."""
        if not isinstance(filename, CloudPath):
            filename = self.bucket / self.root_path / self.rel_path / filename
        filename.write_bytes(data)
        return 0

    def exists(self: "CloudStorage", filename: Union[CloudPath, str]) -> bool:
        """Check if file exists."""
        if not isinstance(filename, CloudPath):
            filename = self.bucket / self.root_path / filename
        return filename.exists()

    def relpath(self: "CloudStorage", filename: CloudPath) -> str:
        """Return relative path."""
        return str(filename.relative_to(self.bucket / self.root_path))

    def abspath(self: "CloudStorage", filename: CloudPath) -> str:
        """Return absolute path."""
        return str(filename)

    def unlink(self: "CloudStorage", filename: Union[CloudPath, str]) -> None:
        """Delete the file."""
        if not isinstance(filename, CloudPath):
            filename = self.bucket / self.root_path / filename
        filename.unlink()


class LocalCloudFileSystemStorage(CloudStorage):
    """Local Cloud FileSystem Storage.

    Usage example:

    .. code-block:: python

        from faker_file.storages.cloudpathlib_based.cloud import LocalCloudFileSystemStorage

        fs_storage = LocalCloudFileSystemStorage(bucket_name="artur-testing-1")
        file = fs_storage.generate_filename(prefix="zzz_", extension="docx")
        fs_storage.write_text(file, "Lorem ipsum")
        fs_storage.write_bytes(file, b"Lorem ipsum")
    """  # noqa

    schema: str = "file"

    def authenticate(self: "LocalCloudFileSystemStorage", **kwargs) -> None:
        """Authenticate. Does nothing for local filesystem."""
        pass
