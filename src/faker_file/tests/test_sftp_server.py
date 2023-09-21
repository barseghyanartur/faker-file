import asyncio
import logging
import os
import socket
import threading
import time
from typing import Callable
from unittest import IsolatedAsyncioTestCase

import asyncssh
from faker import Faker

from ..providers.txt_file import TxtFileProvider
from ..registry import FILE_REGISTRY
from .sftp_server import SFTPServerManager, start_server, start_server_async
from .utils import AutoFreePortInt

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "TestSFTPServerWithManager",
    "TestSFTPServerWithStartServer",
    "TestSFTPServerWithStartServerAsync",
)

SFTP_USER = os.environ.get("SFTP_USER", "foo")
SFTP_PASS = os.environ.get("SFTP_PASS", "pass")
SFTP_HOST = os.environ.get("SFTP_HOST", "127.0.0.1")
SFTP_PORT = int(os.environ.get("SFTP_PORT", AutoFreePortInt(host=SFTP_HOST)))
SFTP_ROOT_PATH = os.environ.get("SFTP_ROOT_PATH", "/upload")

LOGGER = logging.getLogger(__name__)

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)


class __TestSFTPServerMixin:
    """Test SFTP server mix-in."""

    assertIsInstance: Callable
    assertRaises: Callable
    assertEqual: Callable
    assertTrue: Callable
    assertFalse: Callable
    sftp_host: str
    sftp_port: int
    sftp_user: str
    sftp_pass: str

    @staticmethod
    def is_port_in_use(host: str, port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex((host, port)) == 0

    @classmethod
    def free_port(cls: "__TestSFTPServerMixin") -> None:
        # Check if the port is in use and wait until it is free
        while cls.is_port_in_use(cls.sftp_host, cls.sftp_port):
            LOGGER.info(
                f"Port {cls.sftp_port} in use on host {cls.sftp_host}, "
                f"waiting..."
            )
            time.sleep(1)

    async def test_successful_connection(self: "__TestSFTPServerMixin") -> None:
        async with asyncssh.connect(
            self.sftp_host,
            port=self.sftp_port,
            username=self.sftp_user,
            password=self.sftp_pass,
            known_hosts=None,
        ) as conn:
            async with conn.start_sftp_client() as sftp:
                self.assertIsInstance(sftp, asyncssh.SFTPClient)

    async def test_failed_connection(self: "__TestSFTPServerMixin") -> None:
        with self.assertRaises(asyncssh.PermissionDenied):
            async with asyncssh.connect(
                self.sftp_host,
                port=self.sftp_port,
                username=self.sftp_user,
                password="wrong_password",
                known_hosts=None,
            ):
                pass

    async def test_file_upload(self: "__TestSFTPServerMixin") -> None:
        async with asyncssh.connect(
            self.sftp_host,
            port=self.sftp_port,
            username=self.sftp_user,
            password=self.sftp_pass,
            known_hosts=None,
        ) as conn:
            async with conn.start_sftp_client() as sftp:
                test_file = FAKER.txt_file()
                await sftp.put(
                    test_file.data["filename"], "/testfile_upload.txt"
                )

                # Read back the file and check its contents
                async with sftp.open(
                    "/testfile_upload.txt", "r"
                ) as uploaded_file:
                    uploaded_contents = await uploaded_file.read()

                self.assertEqual(test_file.data["content"], uploaded_contents)
                FILE_REGISTRY.clean_up()

    async def test_file_delete(self: "__TestSFTPServerMixin") -> None:
        async with asyncssh.connect(
            self.sftp_host,
            port=self.sftp_port,
            username=self.sftp_user,
            password=self.sftp_pass,
            known_hosts=None,
        ) as conn:
            async with conn.start_sftp_client() as sftp:
                test_file = FAKER.txt_file()
                await sftp.put(
                    test_file.data["filename"], "/testfile_delete.txt"
                )

                # Ensure the file exists
                self.assertTrue(await sftp.exists("/testfile_delete.txt"))

                # Delete the file and ensure it's gone
                await sftp.remove("/testfile_delete.txt")
                self.assertFalse(await sftp.exists("/testfile_delete.txt"))
                FILE_REGISTRY.clean_up()


class TestSFTPServerWithStartServerAsync(
    IsolatedAsyncioTestCase,
    __TestSFTPServerMixin,
):
    sftp_host: str = SFTP_HOST
    sftp_port: int = int(AutoFreePortInt(host=SFTP_HOST))
    sftp_user: str = SFTP_USER
    sftp_pass: str = SFTP_PASS

    @classmethod
    def setUpClass(cls):
        # Free port
        cls.free_port()

        # This function will be run in a new thread
        def run_loop_in_thread(_loop):
            asyncio.set_event_loop(_loop)
            _loop.run_forever()

        # Get the current event loop, create if it doesn't exist
        loop = asyncio.new_event_loop()

        # Schedule the coroutine to be executed
        loop.create_task(
            start_server_async(host=cls.sftp_host, port=cls.sftp_port)
        )

        # Start a new thread running the loop
        server_thread = threading.Thread(
            target=run_loop_in_thread, args=(loop,)
        )
        server_thread.daemon = True
        server_thread.start()

        # Allow some time for the server to start
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # Since the server thread is a daemon, it will be stopped when the
        # main thread exits.
        pass


class TestSFTPServerWithStartServer(
    IsolatedAsyncioTestCase,
    __TestSFTPServerMixin,
):
    sftp_host = SFTP_HOST
    sftp_port = int(AutoFreePortInt(host=SFTP_HOST))
    sftp_user = SFTP_USER
    sftp_pass = SFTP_PASS

    @classmethod
    def setUpClass(cls):
        # Free port
        cls.free_port()

        # Note: start_server is not async, and it creates its own thread
        start_server(host=cls.sftp_host, port=cls.sftp_port)

        # Give server some time to start
        loop = asyncio.new_event_loop()
        loop.run_until_complete(asyncio.sleep(2))

    @classmethod
    def tearDownClass(cls):
        # Since the server is running in a daemonized thread,
        # it will be terminated when the main process finishes.
        # No explicit tear down is required for the server in this test case.
        pass


class TestSFTPServerWithManager(
    IsolatedAsyncioTestCase,
    __TestSFTPServerMixin,
):
    manager: SFTPServerManager
    manager_thread: threading.Thread
    sftp_host = SFTP_HOST
    sftp_port = int(AutoFreePortInt(host=SFTP_HOST))
    sftp_user = SFTP_USER
    sftp_pass = SFTP_PASS

    @classmethod
    def setUpClass(cls):
        # Create and set an event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # Free port
        cls.free_port()

        cls.manager = SFTPServerManager(host=cls.sftp_host, port=cls.sftp_port)
        # Starting the manager in a separate thread since it uses
        # `run_until_complete`.
        cls.manager_thread = threading.Thread(target=cls.manager.start)
        cls.manager_thread.daemon = True
        cls.manager_thread.start()

        # Allow some time for the server to start and check if it's ready
        max_retries = 100
        retries = 0
        while retries < max_retries:
            try:
                # Try to establish a connection to the server
                with socket.create_connection(
                    (cls.sftp_host, cls.sftp_port), timeout=5
                ):
                    LOGGER.info(f"Server started on port {cls.sftp_port}")
                    break
            except (ConnectionRefusedError, socket.timeout):
                LOGGER.info("Waiting for server to start...")
                retries += 1
                time.sleep(1)
        else:
            raise RuntimeError("Server did not start")

    @classmethod
    def tearDownClass(cls):
        # Stop the server
        cls.manager.stop()
        cls.manager_thread.join()
