import logging
import os
import tempfile
import threading
import time
import unittest
from typing import Any, Dict, Type, Union

from faker import Faker
from parametrize import parametrize

from ..providers.txt_file import TxtFileProvider
from ..storages.sftp_storage import SFTPStorage
from .sftp_server import SFTPServerManager

# from .sftp_server import start_server

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestSFTPStorageTestCase",)

SFTP_USER = os.environ.get("SFTP_USER", "foo")
SFTP_PASS = os.environ.get("SFTP_PASS", "pass")
SFTP_HOST = os.environ.get("SFTP_HOST", "0.0.0.0")
SFTP_PORT = int(os.environ.get("SFTP_PORT", 2222))
SFTP_ROOT_PATH = os.environ.get("SFTP_ROOT_PATH", "/upload")

LOGGER = logging.getLogger(__name__)

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)


class TestSFTPStorageTestCase(unittest.TestCase):
    """Test SFTP storage."""

    server_manager: SFTPServerManager
    server_thread: threading.Thread

    @classmethod
    def setUpClass(cls):
        os.makedirs(
            os.path.join(tempfile.gettempdir(), "upload", "sub"),
            exist_ok=True,
        )
        # Start the server in a separate thread
        cls.server_manager = SFTPServerManager()
        cls.server_thread = threading.Thread(target=cls.server_manager.start)
        # Daemonize the thread, so it exits when the main thread exits
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # Stop the server when tests are done
        cls.server_manager.stop()
        cls.server_thread.join()  # Wait for the server thread to finish

    # @classmethod
    # def setUpClass(cls):
    #     os.makedirs(
    #         os.path.join(tempfile.gettempdir(), "upload", "sub"),
    #         exist_ok=True,
    #     )
    #     # Start the server in a separate thread
    #     cls.server_thread = threading.Thread(target=start_server)
    #     # Daemonize the thread, so it exits when the main thread exits
    #     cls.server_thread.daemon = True
    #     cls.server_thread.start()
    #     time.sleep(2)

    @parametrize(
        "storage_cls, kwargs, prefix, basename, extension",
        [
            # SFTPStorage
            (
                SFTPStorage,
                {
                    "host": SFTP_HOST,
                    "port": SFTP_PORT,
                    "username": SFTP_USER,
                    "password": SFTP_PASS,
                    "root_path": SFTP_ROOT_PATH,
                },
                "zzz",
                None,
                "docx",
            ),
            (
                SFTPStorage,
                {
                    "host": SFTP_HOST,
                    "port": SFTP_PORT,
                    "username": SFTP_USER,
                    "password": SFTP_PASS,
                    "root_path": SFTP_ROOT_PATH,
                },
                None,
                "my_zzz_filename",
                "docx",
            ),
        ],
    )
    def test_storage(
        self: "TestSFTPStorageTestCase",
        storage_cls: Type[SFTPStorage],
        kwargs: Dict[str, Any],
        prefix: Union[str, None],
        basename: Union[str, None],
        extension: str,
    ) -> None:
        """Test storage."""
        storage = storage_cls(**kwargs)
        # Text file
        file_text = storage.generate_filename(
            basename=basename, prefix=prefix, extension=extension
        )
        # Write to the text file
        text_result = storage.write_text(file_text, "Lorem ipsum")
        # Check if file exists
        self.assertTrue(storage.exists(file_text))
        # Assert correct return value
        self.assertIsInstance(text_result, int)

        # Bytes
        file_bytes = storage.generate_filename(
            basename=basename, prefix=prefix, extension=extension
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
                SFTPStorage,
                {
                    "host": SFTP_HOST,
                    "port": SFTP_PORT,
                    "username": SFTP_USER,
                    "password": SFTP_PASS,
                    "root_path": SFTP_ROOT_PATH,
                },
                "zzz",
                "",
            ),
        ],
    )
    def test_storage_generate_filename_exceptions(
        self: "TestSFTPStorageTestCase",
        storage_cls: Type[SFTPStorage],
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

    def test_file_system_storage_abspath(
        self: "TestSFTPStorageTestCase",
    ) -> None:
        """Test `FileSystemStorage` `abspath`."""

        storage = SFTPStorage(
            host=SFTP_HOST,
            port=SFTP_PORT,
            username=SFTP_USER,
            password=SFTP_PASS,
            root_path=SFTP_ROOT_PATH,
        )
        filename = storage.generate_filename(prefix="", extension="tmp")
        self.assertTrue(storage.abspath(filename).startswith(SFTP_ROOT_PATH))

    def test_integration(self: "TestSFTPStorageTestCase") -> None:
        storage = SFTPStorage(
            host=SFTP_HOST,
            port=SFTP_PORT,
            username=SFTP_USER,
            password=SFTP_PASS,
            root_path=SFTP_ROOT_PATH,
        )
        file = FAKER.txt_file(storage=storage)
        self.assertTrue(storage.exists(file.data["filename"]))
        self.assertTrue(
            storage.abspath(file.data["filename"]).startswith(SFTP_ROOT_PATH)
        )

    def test_integration_sub_dir(self: "TestSFTPStorageTestCase") -> None:
        storage = SFTPStorage(
            host=SFTP_HOST,
            port=SFTP_PORT,
            username=SFTP_USER,
            password=SFTP_PASS,
            root_path=SFTP_ROOT_PATH,
            rel_path="sub",
        )
        file = FAKER.txt_file(storage=storage)
        self.assertTrue(storage.exists(file.data["filename"]))
        self.assertTrue(
            storage.abspath(file.data["filename"]).startswith(
                os.path.join(SFTP_ROOT_PATH, "sub")
            )
        )
