import logging
import os
import socket
import tempfile
import threading
import time
import unittest
from functools import partial
from typing import Any, Dict, Type, Union

from faker import Faker
from parametrize import parametrize

from ..providers.txt_file import TxtFileProvider
from ..registry import FILE_REGISTRY
from ..storages.sftp_storage import SFTPStorage
from .sftp_server import SFTPServerManager, start_server
from .utils import AutoFreePortInt

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestSFTPStorageTestCase",)

SFTP_USER = os.environ.get("SFTP_USER", "foo")
SFTP_PASS = os.environ.get("SFTP_PASS", "pass")
SFTP_HOST = os.environ.get("SFTP_HOST", "127.0.0.1")
SFTP_PORT = int(os.environ.get("SFTP_PORT", AutoFreePortInt(host=SFTP_HOST)))
SFTP_ROOT_PATH = os.environ.get("SFTP_ROOT_PATH", "/upload")

LOGGER = logging.getLogger(__name__)

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)


class TestSFTPStorageTestCase(unittest.TestCase):
    """Test SFTP storage."""

    server_manager: SFTPServerManager
    server_thread: threading.Thread
    sftp_host: str = SFTP_HOST
    sftp_port: int = int(AutoFreePortInt(host=SFTP_HOST))
    sftp_user: str = SFTP_USER
    sftp_pass: str = SFTP_PASS
    sftp_root_path: str = SFTP_ROOT_PATH

    @staticmethod
    def is_port_in_use(host: str, port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex((host, port)) == 0

    @classmethod
    def free_port(cls: "TestSFTPStorageTestCase") -> None:
        # Check if the port is in use and wait until it is free
        while cls.is_port_in_use(cls.sftp_host, cls.sftp_port):
            LOGGER.info(
                f"Port {cls.sftp_port} in use on host {cls.sftp_host}, "
                f"waiting..."
            )
            time.sleep(1)

    def tearDown(self) -> None:
        super().tearDown()
        # FILE_REGISTRY.clean_up()

    @classmethod
    def setUpClass(cls):
        # Free port
        cls.free_port()

        os.makedirs(
            os.path.join(tempfile.gettempdir(), "upload", "sub"),
            exist_ok=True,
        )

        # Create a partial function with custom arguments
        start_server_partial = partial(
            start_server, host=cls.sftp_host, port=cls.sftp_port
        )

        # Start the server in a separate thread
        cls.server_thread = threading.Thread(target=start_server_partial)
        # Daemonize the thread, so it exits when the main thread exits
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(2)

    @parametrize(
        "storage_cls, kwargs, prefix, basename, extension",
        [
            # SFTPStorage
            (
                SFTPStorage,
                {
                    "host": sftp_host,
                    "port": sftp_port,
                    "username": sftp_user,
                    "password": sftp_pass,
                    "root_path": sftp_root_path,
                },
                "zzz",
                None,
                "docx",
            ),
            (
                SFTPStorage,
                {
                    "host": sftp_host,
                    "port": sftp_port,
                    "username": sftp_user,
                    "password": sftp_pass,
                    "root_path": sftp_root_path,
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

        # Clean up
        storage.unlink(file_text)
        storage.unlink(file_bytes)

    @parametrize(
        "storage_cls, kwargs, prefix, extension",
        [
            # FileSystemStorage
            (
                SFTPStorage,
                {
                    "host": sftp_host,
                    "port": sftp_port,
                    "username": sftp_user,
                    "password": sftp_pass,
                    "root_path": sftp_root_path,
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
            host=self.sftp_host,
            port=self.sftp_port,
            username=self.sftp_user,
            password=self.sftp_pass,
            root_path=self.sftp_root_path,
        )
        filename = storage.generate_filename(prefix="", extension="tmp")
        self.assertTrue(
            storage.abspath(filename).startswith(self.sftp_root_path)
        )

    def test_integration(self: "TestSFTPStorageTestCase") -> None:
        storage = SFTPStorage(
            host=self.sftp_host,
            port=self.sftp_port,
            username=self.sftp_user,
            password=self.sftp_pass,
            root_path=self.sftp_root_path,
        )
        file = FAKER.txt_file(storage=storage)
        self.assertTrue(storage.exists(file.data["filename"]))
        self.assertTrue(
            storage.abspath(file.data["filename"]).startswith(
                self.sftp_root_path
            )
        )

        FILE_REGISTRY.clean_up()  # Clean up storage files

    def test_integration_sub_dir(self: "TestSFTPStorageTestCase") -> None:
        storage = SFTPStorage(
            host=self.sftp_host,
            port=self.sftp_port,
            username=self.sftp_user,
            password=self.sftp_pass,
            root_path=self.sftp_root_path,
            rel_path="sub",
        )
        file = FAKER.txt_file(storage=storage)
        self.assertTrue(storage.exists(file.data["filename"]))
        self.assertTrue(
            storage.abspath(file.data["filename"]).startswith(
                os.path.join(self.sftp_root_path, "sub")
            )
        )

        FILE_REGISTRY.clean_up()  # Clean up storage files

    @parametrize(
        "kwargs",
        [
            # Wrong username, key
            (
                {
                    "host": sftp_host,
                    "port": sftp_port,
                    "username": "wrong",
                    "key": "wrong",
                },
            ),
            # Wrong username, password
            (
                {
                    "host": sftp_host,
                    "port": sftp_port,
                    "username": "wrong",
                    "password": "wrong",
                },
            ),
        ],
    )
    def test_storage_initialization_exceptions(
        self: "TestSFTPStorageTestCase",
        kwargs: Dict[str, Any],
    ) -> None:
        with self.assertRaises(Exception):
            # Initialize the storage
            SFTPStorage(**kwargs)

    def test_storage_write_text_exceptions(self) -> None:
        storage = SFTPStorage(
            host=self.sftp_host,
            port=self.sftp_port,
            username=self.sftp_user,
            password=self.sftp_pass,
            root_path=self.sftp_root_path,
        )
        val = storage.write_text(
            filename=FAKER.file_name(),
            data=1,  # type: ignore
        )
        self.assertEqual(val, -1)

    def test_storage_write_bytes_exceptions(self) -> None:
        storage = SFTPStorage(
            host=self.sftp_host,
            port=self.sftp_port,
            username=self.sftp_user,
            password=self.sftp_pass,
            root_path=self.sftp_root_path,
        )
        val = storage.write_bytes(
            filename=FAKER.file_name(),
            data=1,  # type: ignore
        )
        self.assertEqual(val, -1)

    def test_storage_exists_exceptions(self) -> None:
        storage = SFTPStorage(
            host=self.sftp_host,
            port=self.sftp_port,
            username=self.sftp_user,
            password=self.sftp_pass,
            root_path=self.sftp_root_path,
        )
        val = storage.exists(
            filename=FAKER.file_name(),
        )
        self.assertFalse(val)
