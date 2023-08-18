import logging
import os
import tempfile
from typing import Optional

import paramiko

from .base import BaseStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("SFTPStorage",)

LOGGER = logging.getLogger(__name__)


class SFTPStorage(BaseStorage):
    """SFTP storage.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.txt_file import TxtFileProvider
        from faker_file.storages.sftp_storage import SFTPStorage

        FAKER = Faker()
        FAKER.add_provider(TxtFileProvider)

        # SFTP storage class
        STORAGE = SFTPStorage(
            host="0.0.0.0",
            username="foo",
            password="pass",
        )

        # Generate TXT file in the default directory
        txt_file = FAKER.txt_file(storage=STORAGE)

        # Another SFTP storage class, but inside a `/upload/another` directory
        STORAGE_SUB_DIR = SFTPStorage(
            host="0.0.0.0",
            username="foo",
            password="pass",
            root_path="/upload/another",
        )

        # Generate TXT file inside `/upload/another` directory
        txt_file = FAKER.txt_file(storage=STORAGE_SUB_DIR)
    """

    sftp: Optional[paramiko.SFTPClient] = None
    transport: Optional[paramiko.Transport] = None

    def __init__(
        self: "SFTPStorage",
        host: str,
        port: int = 22,
        username: str = "",
        password: Optional[str] = None,
        key: Optional[paramiko.PKey] = None,
        root_path: str = "",
        rel_path: str = "",
        *args,
        **kwargs,
    ) -> None:
        """
        :param host: The hostname of the SFTP server.
        :param port: The port of the SFTP server.
        :param username: The username to authenticate as.
        :param password: The password to use when connecting.
        :param key: The private key to use when connecting.
        :param root_path: Path of your files root directory.
        :param rel_path: Relative path (from root directory).
        """
        self.root_path = root_path
        self.rel_path = rel_path

        self.transport = paramiko.Transport((host, port))

        # Authentication
        try:
            if key:
                self.transport.connect(username=username, pkey=key)
            else:
                self.transport.connect(username=username, password=password)
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        except Exception as e:
            LOGGER.exception(f"Failed to connect to SFTP server: {e}")
            raise
        super().__init__(*args, **kwargs)

    def _build_path(self: "SFTPStorage", filename: str) -> str:
        """Build the full path for a file."""
        return os.path.join(self.root_path, self.rel_path, filename)

    def generate_filename(
        self: "SFTPStorage",
        extension: str,
        prefix: Optional[str] = None,
        basename: Optional[str] = None,
    ) -> str:
        """Generate filename."""
        if not extension:
            LOGGER.error("File extension is required")
            raise ValueError("Extension shall be given!")

        if basename:
            return self._build_path(f"{basename}.{extension}")
        else:
            with tempfile.NamedTemporaryFile(
                prefix=prefix,
                suffix=f".{extension}",
            ) as temp_file:
                return self._build_path(os.path.basename(temp_file.name))

    def write_text(
        self: "SFTPStorage",
        filename: str,
        data: str,
        encoding: Optional[str] = "utf-8",
    ) -> int:
        """Write text."""
        try:
            # Encode the text data into bytes before writing
            encoded_data = data.encode(encoding)
            with self.sftp.open(self._build_path(filename), "wb") as file:
                file.write(encoded_data)
                return 0
        except Exception as err:
            LOGGER.exception(f"Failed to write text to {filename}: {err}")
            return -1

    def write_bytes(self: "SFTPStorage", filename: str, data: bytes) -> int:
        """Write bytes."""
        try:
            with self.sftp.open(self._build_path(filename), "wb") as file:
                file.write(data)
                return 0
        except Exception as err:
            LOGGER.exception(f"Failed to write bytes to {filename}: {err}")
            return -1

    def exists(self: "SFTPStorage", filename: str) -> bool:
        """Check if file exists."""
        try:
            self.sftp.stat(self._build_path(filename))
            return True
        except IOError:
            return False

    def relpath(self: "SFTPStorage", filename: str) -> str:
        """Return relative path."""
        return os.path.relpath(self._build_path(filename), self.root_path)

    def abspath(self: "SFTPStorage", filename: str) -> str:
        """Return absolute path."""
        return self._build_path(filename)

    def unlink(self: "SFTPStorage", filename: str) -> None:
        """Remove a file."""
        try:
            self.sftp.remove(self._build_path(filename))
        except Exception as err:
            LOGGER.exception(f"Failed to remove {filename}: {err}")

    def close(self: "SFTPStorage"):
        """Explicitly close the connection."""
        if self.sftp:
            self.sftp.close()
        if self.transport:
            self.transport.close()

    def __del__(self: "SFTPStorage"):
        """Destructor to ensure connection is closed."""
        self.close()
