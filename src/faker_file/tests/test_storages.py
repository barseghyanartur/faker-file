import json
import tempfile
import unittest
from pathlib import Path
from typing import Any, Dict, Type, Union

from faker import Faker
from parametrize import parametrize
from pathy import use_fs, use_fs_cache

from ..providers.json_file import JsonFileProvider
from ..registry import FILE_REGISTRY
from ..storages.aws_s3 import AWSS3Storage
from ..storages.azure_cloud_storage import AzureCloudStorage
from ..storages.base import BaseStorage
from ..storages.cloud import CloudStorage, PathyFileSystemStorage
from ..storages.filesystem import FileSystemStorage
from ..storages.google_cloud_storage import GoogleCloudStorage
from .data import GCS_CREDENTIALS_JSON

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestStoragesTestCase",)

FAKER = Faker()
FAKER.add_provider(JsonFileProvider)
FS_STORAGE = FileSystemStorage()
GCS_CREDENTIALS_JSON_FILENAME = FS_STORAGE.generate_filename(
    basename="gc_credentials", extension="json"
)


class TestStoragesTestCase(unittest.TestCase):
    """Test storages."""

    def setUp(self) -> None:
        super().setUp()

        gcs_credentials_json_filename = Path(GCS_CREDENTIALS_JSON_FILENAME)
        FAKER.json_file(
            basename=gcs_credentials_json_filename.stem,
            content=json.dumps(GCS_CREDENTIALS_JSON),
        )

    def tearDown(self) -> None:
        super().tearDown()
        FILE_REGISTRY.clean_up()  # Clean up files

    @parametrize(
        "storage_cls, kwargs, prefix, basename, extension",
        [
            # FileSystemStorage
            (
                FileSystemStorage,
                {},
                "zzz",
                None,
                "docx",
            ),
            (
                FileSystemStorage,
                {},
                None,
                "my_zzz_filename",
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
                None,
                "docx",
            ),
            (
                PathyFileSystemStorage,
                {
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                },
                None,
                "my_zzz_filename",
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
                None,
                "docx",
            ),
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
                None,
                "my_zzz_filename",
                "docx",
            ),
            # Google Cloud Storage
            (
                GoogleCloudStorage,
                {
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                    "credentials": {
                        "json_file_path": GCS_CREDENTIALS_JSON_FILENAME,
                    },
                },
                "zzz",
                None,
                "docx",
            ),
            (
                GoogleCloudStorage,
                {
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                    "credentials": {
                        "json_file_path": GCS_CREDENTIALS_JSON_FILENAME,
                    },
                },
                None,
                "my_zzz_filename",
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
                None,
                "docx",
            ),
            (
                AzureCloudStorage,
                {
                    "bucket_name": "testing",
                    "rel_path": "tmp",
                    "credentials": {"connection_string": "abcd1234"},
                },
                None,
                "my_zzz_filename",
                "docx",
            ),
        ],
    )
    def test_storage(
        self: "TestStoragesTestCase",
        storage_cls: Type[BaseStorage],
        kwargs: Dict[str, Any],
        prefix: Union[str, None],
        basename: Union[str, None],
        extension: str,
    ) -> None:
        """Test storage."""
        # Just for testing purposes
        if issubclass(storage_cls, CloudStorage):
            use_fs(Path(tempfile.gettempdir()))
            use_fs_cache()

        storage = storage_cls(**kwargs)
        # Text file
        filename_text = storage.generate_filename(
            basename=basename, prefix=prefix, extension=extension
        )
        # Write to the text file
        text_result = storage.write_text(filename_text, "Lorem ipsum")
        # Check if file exists
        self.assertTrue(storage.exists(filename_text))
        # Assert correct return value
        self.assertIsInstance(text_result, int)
        # Clean up
        storage.unlink(filename_text)

        # Bytes
        filename_bytes = storage.generate_filename(
            basename=basename, prefix=prefix, extension=extension
        )
        # Write to bytes file
        bytes_result = storage.write_bytes(filename_bytes, b"Lorem ipsum")
        # Check if file exists
        self.assertTrue(storage.exists(filename_bytes))
        # Assert correct return value
        self.assertIsInstance(bytes_result, int)

        # Clean up
        storage.unlink(filename_bytes)

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
        self: "TestStoragesTestCase",
        storage_cls: Type[BaseStorage],
        kwargs: Dict[str, Any],
        prefix: str,
        extension: str,
    ) -> None:
        """Test storage `generate_filename` exceptions."""
        storage = storage_cls(**kwargs)

        with self.assertRaises(Exception):
            # Generate filename
            storage.generate_filename(prefix=prefix, extension=extension)

        with self.assertRaises(Exception):
            # Generate filename
            storage.generate_filename(basename=prefix, extension=extension)

    @parametrize(
        "storage_cls, kwargs",
        [
            # CloudStorage
            (CloudStorage, {"bucket_name": "testing"}),
        ],
    )
    def test_storage_initialization_exceptions(
        self: "TestStoragesTestCase",
        storage_cls: Type[BaseStorage],
        kwargs: Dict[str, Any],
    ) -> None:
        """Test storage initialization exceptions."""
        with self.assertRaises(Exception):
            # Initialize the storage
            storage_cls(**kwargs)

    @parametrize(
        "method_name, method_kwargs",
        [
            ("generate_filename", {"prefix": "zzz", "extension": "txt"}),
            (
                "generate_filename",
                {"basename": "my_zzz_file", "extension": "txt"},
            ),
            ("write_text", {"filename": "test.txt", "data": "Test"}),
            ("write_bytes", {"filename": "test.txt", "data": b"Test"}),
            ("exists", {"filename": "test.txt"}),
            ("relpath", {"filename": "test.txt"}),
            ("abspath", {"filename": "test.txt"}),
            ("unlink", {"filename": "test.txt"}),
        ],
    )
    def test_base_storage_exceptions(
        self: "TestStoragesTestCase",
        method_name: str,
        method_kwargs: Dict[str, Any],
    ) -> None:
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
    def test_cloud_storage_exceptions(
        self: "TestStoragesTestCase",
        method_name: str,
        method_kwargs: Dict[str, Any],
    ) -> None:
        """Test Base storage exceptions."""

        class TestCloudStorage(CloudStorage):
            schema: str = "file"

        test_storage = TestCloudStorage(bucket_name="testing")  # type: ignore
        method = getattr(test_storage, method_name)
        with self.assertRaises(NotImplementedError):
            method(**method_kwargs)

    def test_file_system_storage_abspath(self: "TestStoragesTestCase") -> None:
        """Test `FileSystemStorage` `abspath`."""
        storage = FileSystemStorage(
            root_path=tempfile.gettempdir(),
            rel_path="rel_tmp",
        )
        filename = storage.generate_filename(prefix="", extension="tmp")
        self.assertTrue(storage.abspath(filename).startswith("/tmp/rel_tmp/"))

    def test_pathy_file_system_storage_abspath(
        self: "TestStoragesTestCase",
    ) -> None:
        """Test `PathyFileSystemStorage` `abspath`."""
        storage = PathyFileSystemStorage(
            bucket_name="faker-file-tmp",
            root_path="root_tmp",
            rel_path="rel_tmp",
        )
        filename = storage.generate_filename(prefix="", extension="tmp")
        self.assertTrue(
            storage.abspath(filename).startswith(
                "file://faker-file-tmp/root_tmp/rel_tmp/"
            )
        )

    def test_pathy_file_system_storage_unlink(
        self: "TestStoragesTestCase",
    ) -> None:
        """Test `PathyFileSystemStorage` `unlink`."""
        storage = PathyFileSystemStorage(
            bucket_name="faker-file-tmp",
            root_path="root_tmp",
            rel_path="rel_tmp",
        )
        with self.subTest("Test unlink by Pathy"):
            filename_1 = storage.generate_filename(prefix="", extension="tmp")
            storage.write_text(filename=filename_1, data=FAKER.text())
            self.assertTrue(storage.exists(filename_1))
            storage.unlink(filename_1)
            self.assertFalse(storage.exists(filename_1))

        with self.subTest("Test unlink by str"):
            filename_2 = storage.generate_filename(prefix="", extension="tmp")
            storage.write_text(filename=filename_2, data=FAKER.text())
            self.assertTrue(storage.exists(filename_2))
            storage.unlink(str(filename_2))
            self.assertFalse(storage.exists(filename_2))
