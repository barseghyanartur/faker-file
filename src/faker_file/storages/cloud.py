import os
import tempfile
from pathlib import Path
from typing import Dict

from pathy import Pathy, get_fs_cache, use_fs, use_fs_cache

from ..base import DEFAULT_REL_PATH
from .base import BaseStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("CloudStorage",)


class CloudStorage(BaseStorage):
    """Cloud storage.

    Usage example:

        from faker_file.storages.cloud import CloudStorage

        storage = CloudStorage(
            schema="s3",
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = storage.generate_filename(prefix="zzz_", extension="docx")
        storage.write_text(file, "Lorem ipsum")
    """

    bucket_name: Pathy
    credentials: Dict[str, str]

    def __init__(self: "CloudStorage", *args, **kwargs):
        self.schema = kwargs.pop("schema", "file")
        self.bucket_name = kwargs.pop("bucket_name", None)
        self.rel_path = kwargs.pop("rel_path", DEFAULT_REL_PATH)
        self.cache_dir = None
        credentials = kwargs.pop("credentials", {})

        if not credentials:
            # Test/dev mode
            use_fs(Path(tempfile.gettempdir()))
            use_fs_cache()
            self.cache_dir = get_fs_cache()

            bucket = Pathy(f"{self.schema}://{self.bucket_name}")
            # If bucket does not exist, create
            if not bucket.exists():
                bucket.mkdir()

        callback = kwargs.pop("callback", None)

        super().__init__(*args, **kwargs)

        if callback and callable(callback):
            callback(self, credentials)

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
        file.write_text(data, encoding)

    def write_bytes(self: "CloudStorage", filename: Pathy, data: bytes) -> int:
        """Write bytes."""
        file = (
            Pathy(f"{self.schema}://{self.bucket_name}")
            / self.rel_path
            / filename
        )
        file.write_bytes(data)