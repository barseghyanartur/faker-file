import tempfile
import unittest
from pathlib import Path
from typing import Any, Dict, Type

from faker import Faker
from parametrize import parametrize
from pathy import use_fs, use_fs_cache

from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage
from ..storages.cloud import (
    CloudStorage,
    authenticate_azure_callback,
    authenticate_gcs_callback,
    authenticate_s3_callback,
)

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestStoragesTestCase",)

FAKER = Faker()

GCS_CREDENTIALS = tempfile.NamedTemporaryFile(suffix="json").name
with open(GCS_CREDENTIALS, "w") as file:
    file.write(
        """{"token_uri": "http://example", "client_email": "a@b.c"}"""
    )


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
            # CloudStorage
            (
                CloudStorage,
                {
                    "schema": "s3",
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                },
                "zzz",
                "docx",
            ),
            (
                CloudStorage,
                {
                    "schema": "s3",
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                    "credentials": {
                        "key_id": "key",
                        "key_secret": "key_secret",
                    },
                    "callback": authenticate_s3_callback,
                },
                "zzz",
                "docx",
            ),
            (
                CloudStorage,
                {
                    "schema": "gs",
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                    # "credentials": {
                    #     "json_file_path": GCS_CREDENTIALS,
                    # },
                    # "callback": authenticate_gcs_callback,
                },
                "zzz",
                "docx",
            ),
            (
                CloudStorage,
                {
                    "schema": "azure",
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                    "credentials": {"connection_string": "abcd1234"},
                    "callback": authenticate_azure_callback,
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
            # CloudStorage
            (
                CloudStorage,
                {
                    "schema": "s3",
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                },
                "zzz",
                "",
            ),
        ],
    )
    def test_storage_exceptions(
        self,
        storage_cls: Type[BaseStorage],
        kwargs: Dict[str, Any],
        prefix: str,
        extension: str,
    ):
        """Test storage exceptions."""
        storage = storage_cls(**kwargs)

        with self.assertRaises(Exception):
            # Generate filename
            storage.generate_filename(prefix=prefix, extension=extension)
