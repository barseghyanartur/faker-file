import tempfile
import unittest
from pathlib import Path
from typing import Any, Dict, Type

from faker import Faker
from parametrize import parametrize
from pathy import use_fs, use_fs_cache

from ..storages.aws_s3 import AWSS3Storage
from ..storages.azure_cloud_storage import AzureCloudStorage
from ..storages.base import BaseStorage
from ..storages.cloud import CloudStorage, PathyFileSystemStorage
from ..storages.filesystem import FileSystemStorage
from ..storages.google_cloud_storage import GoogleCloudStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestStoragesTestCase",)

FAKER = Faker()


class TestStoragesTestCase(unittest.TestCase):
    """Test storages."""

    @parametrize(
        "storage_cls, kwargs, prefix, extension",
        [
            # FileSystemStorage
            (
                FileSystemStorage,
                {},
                "zzz",
                "docx",
            ),
            # PathyFileSystemStorage
            (
                PathyFileSystemStorage,
                {
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                },
                "zzz",
                "docx",
            ),
            # AWS S3
            (
                AWSS3Storage,
                {
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                    "credentials": {
                        "key_id": "key",
                        "key_secret": "key_secret",
                    },
                },
                "zzz",
                "docx",
            ),
            # Google Cloud Storage
            (
                GoogleCloudStorage,
                {
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                    # "credentials": {
                    #     "json_file_path": GCS_CREDENTIALS,
                    # },
                },
                "zzz",
                "docx",
            ),
            # Azure Cloud Storage
            (
                AzureCloudStorage,
                {
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                    "credentials": {"connection_string": "abcd1234"},
                },
                "zzz",
                "docx",
            ),
        ],
    )
    def test_storage(
        self,
        storage_cls: Type[BaseStorage],
        kwargs: Dict[str, Any],
        prefix: str,
        extension: str,
    ):
        """Test storage."""
        # Just for testing purposes
        if issubclass(storage_cls, CloudStorage):
            use_fs(Path(tempfile.gettempdir()))
            use_fs_cache()

        storage = storage_cls(**kwargs)
        # Text file
        file_text = storage.generate_filename(
            prefix=prefix, extension=extension
        )
        # Write to the text file
        text_result = storage.write_text(file_text, "Lorem ipsum")
        # Check if file exists
        self.assertTrue(storage.exists(file_text))
        # Assert correct return value
        self.assertIsInstance(text_result, int)

        # Bytes
        file_bytes = storage.generate_filename(
            prefix=prefix, extension=extension
        )
        # Write to bytes file
        bytes_result = storage.write_bytes(file_bytes, b"Lorem ipsum")
        # Check if file exists
        self.assertTrue(storage.exists(file_bytes))
        # Assert correct return value
        self.assertIsInstance(bytes_result, int)

    @parametrize(
        "storage_cls, kwargs, prefix, extension",
        [
            # FileSystemStorage
            (
                FileSystemStorage,
                {},
                "zzz",
                "",
            ),
            # PathyFileSystemStorage
            (
                PathyFileSystemStorage,
                {
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                },
                "zzz",
                "",
            ),
        ],
    )
    def test_storage_generate_filename_exceptions(
        self,
        storage_cls: Type[BaseStorage],
        kwargs: Dict[str, Any],
        prefix: str,
        extension: str,
    ):
        """Test storage `generate_filename` exceptions."""
        storage = storage_cls(**kwargs)

        with self.assertRaises(Exception):
            # Generate filename
            storage.generate_filename(prefix=prefix, extension=extension)

    @parametrize(
        "storage_cls, kwargs",
        [
            # CloudStorage
            (CloudStorage, {"bucket_name": "testing"}),
        ],
    )
    def test_storage_initialization_exceptions(
        self,
        storage_cls: Type[BaseStorage],
        kwargs: Dict[str, Any],
    ):
        """Test storage initialization exceptions."""
        with self.assertRaises(Exception):
            # Initialize the storage
            storage_cls(**kwargs)

    @parametrize(
        "method_name, method_kwargs",
        [
            ("generate_filename", {"prefix": "zzz", "extension": "txt"}),
            ("write_text", {"filename": "test.txt", "data": "Test"}),
            ("write_bytes", {"filename": "test.txt", "data": b"Test"}),
            ("exists", {"filename": "test.txt"}),
            ("relpath", {"filename": "test.txt"}),
            ("abspath", {"filename": "test.txt"}),
        ],
    )
    def test_base_storage_exceptions(self, method_name, method_kwargs):
        """Test Base storage exceptions."""
        base_storage = BaseStorage()
        method = getattr(base_storage, method_name)
        with self.assertRaises(NotImplementedError):
            method(**method_kwargs)

    @parametrize(
        "method_name, method_kwargs",
        [
            ("authenticate", {}),
        ],
    )
    def test_cloud_storage_exceptions(self, method_name, method_kwargs):
        """Test Base storage exceptions."""

        class TestCloudStorage(CloudStorage):
            schema: str = "file"

        test_storage = TestCloudStorage(bucket_name="testing")
        method = getattr(test_storage, method_name)
        with self.assertRaises(NotImplementedError):
            method(**method_kwargs)
