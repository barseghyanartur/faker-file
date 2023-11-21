import os
import tempfile
from abc import abstractmethod
from typing import Any, Dict, Optional, Union

from cloudpathlib import AnyPath

from ..base import DEFAULT_REL_PATH
from .base import BaseStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "CloudpathlibCloudStorage",
    "CloudpathlibFileSystemStorage",
)


DEFAULT_ROOT_PATH = "tmp"


class CloudpathlibCloudStorage(BaseStorage):
    """Base cloud storage."""

    bucket_name: str
    bucket: AnyPath
    credentials: Dict[str, str]
    schema: Optional[str] = None

    def __init__(
        self: "CloudpathlibCloudStorage",
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
        self.root_path = root_path or ""
        self.rel_path = rel_path or ""
        self.cache_dir = None
        credentials = credentials or {}

        if credentials:
            self.authenticate(**credentials)

        self.bucket = AnyPath(f"{self.schema}://{self.bucket_name}")
        # If bucket does not exist, create
        if not self.bucket.exists():
            self.bucket.mkdir(exist_ok=True)

        super().__init__(*args, **kwargs)

    @abstractmethod
    def authenticate(self, *args, **kwargs):
        raise NotImplementedError("Method authenticate is not implemented!")

    def generate_filename(
        self: "CloudpathlibCloudStorage",
        extension: str,
        prefix: Optional[str] = None,
        basename: Optional[str] = None,
    ) -> AnyPath:
        """Generate filename."""
        if not extension:
            raise Exception("Extension shall be given!")

        if basename:
            return (
                self.bucket
                / self.root_path
                / self.rel_path
                / f"{basename}.{extension}"
            )
        else:
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
        self: "CloudpathlibCloudStorage",
        filename: AnyPath,
        data: str,
        encoding: Optional[str] = None,
    ) -> int:
        """Write text."""
        # file = self.bucket / self.root_path / self.rel_path / filename
        file = filename
        return file.write_text(data, encoding)

    def write_bytes(
        self: "CloudpathlibCloudStorage",
        filename: AnyPath,
        data: bytes,
    ) -> int:
        """Write bytes."""
        # file = self.bucket / self.root_path / self.rel_path / filename
        file = filename
        return file.write_bytes(data)

    def exists(
        self: "CloudpathlibCloudStorage",
        filename: Union[AnyPath, str],
    ) -> bool:
        """Check if file exists."""
        if isinstance(filename, str):
            filename = self.bucket / self.root_path / filename
        return filename.exists()

    def relpath(self: "CloudpathlibCloudStorage", filename: AnyPath) -> str:
        """Return relative path."""
        return str(filename.relative_to(self.bucket / self.root_path))

    def abspath(self: "CloudpathlibCloudStorage", filename: AnyPath) -> str:
        """Return relative path."""
        return filename.as_uri()

    def unlink(
        self: "CloudpathlibCloudStorage",
        filename: Union[AnyPath, str],
    ) -> None:
        """Delete the file."""
        if isinstance(filename, str):
            filename = self.bucket / self.root_path / filename
        filename.unlink()


class CloudpathlibFileSystemStorage(CloudpathlibCloudStorage):
    """Pathy FileSystem Storage.

    Usage example:

    .. code-block:: python

        from faker_file.storages.cloudpathlib_cloud import (
            CloudpathlibFileSystemStorage
        )

        fs_storage = CloudpathlibFileSystemStorage(
            bucket_name="artur-testing-1"
        )
        file = fs_storage.generate_filename(prefix="zzz_", extension="docx")
        fs_storage.write_text(file, "Lorem ipsum")
        fs_storage.write_bytes(file, b"Lorem ipsum")
    """

    schema: str = "file"

    def authenticate(self: "CloudpathlibFileSystemStorage", **kwargs) -> None:
        """Authenticate. Does nothing."""
