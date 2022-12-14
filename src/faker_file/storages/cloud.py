import os
import tempfile
from typing import Dict

from pathy import Pathy

from ..base import DEFAULT_REL_PATH
from .base import BaseStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("CloudStorage",)


class CloudStorage(BaseStorage):
    """Base cloud storage.

    Usage example:

        from faker_file.storages.cloud import CloudStorage

        storage = CloudStorage(
            schema="s3",
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = storage.generate_filename(prefix="zzz_", extension="docx")
        storage.write_text(file, "Lorem ipsum")
        storage.write_bytes(file, b"Lorem ipsum")
    """

    bucket_name: Pathy
    credentials: Dict[str, str]
    schema: str = None

    def __init__(self: "CloudStorage", *args, **kwargs):
        if not self.schema:
            self.schema = kwargs.pop("schema", "file")
        self.bucket_name = kwargs.pop("bucket_name", None)
        self.rel_path = kwargs.pop("rel_path", DEFAULT_REL_PATH)
        self.cache_dir = None
        credentials = kwargs.pop("credentials", {})

        bucket = Pathy(f"{self.schema}://{self.bucket_name}")
        # If bucket does not exist, create
        if not bucket.exists():
            bucket.mkdir()

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
        temp_file = tempfile.NamedTemporaryFile(
            prefix=prefix,
            suffix=f".{extension}",
        )
        return (
            Pathy(f"{self.schema}://{self.bucket_name}")
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
        file = (
            Pathy(f"{self.schema}://{self.bucket_name}")
            / self.rel_path
            / filename
        )
        return file.write_text(data, encoding)

    def write_bytes(self: "CloudStorage", filename: Pathy, data: bytes) -> int:
        """Write bytes."""
        file = (
            Pathy(f"{self.schema}://{self.bucket_name}")
            / self.rel_path
            / filename
        )
        return file.write_bytes(data)

    def exists(self: "CloudStorage", filename: Pathy) -> int:
        """Check if file exists."""
        return filename.exists()
