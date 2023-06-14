import asyncio
import os
import threading
import time
from typing import Callable
from unittest import IsolatedAsyncioTestCase

import asyncssh
from faker import Faker

from faker_file.providers.txt_file import TxtFileProvider

from .sftp_server import start_server, start_server_async

# from .sftp_server import SFTPServerManager

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    # "TestSFTPServerWithManager",
    "TestSFTPServerWithStartServer",
    "TestSFTPServerWithStartServerAsync",
)

SFTP_USER = os.environ.get("SFTP_USER", "foo")
SFTP_PASS = os.environ.get("SFTP_PASS", "pass")
SFTP_HOST = os.environ.get("SFTP_HOST", "0.0.0.0")
SFTP_PORT = int(os.environ.get("SFTP_PORT", 2222))
SFTP_ROOT_PATH = os.environ.get("SFTP_ROOT_PATH", "/upload")

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)


class __TestSFTPServerMixin:
    assertIsInstance: Callable
    assertRaises: Callable
    assertEqual: Callable
    assertTrue: Callable
    assertFalse: Callable
    sftp_host: str
    sftp_port: int
    sftp_user: str
    sftp_pass: str

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


class TestSFTPServerWithStartServerAsync(
    IsolatedAsyncioTestCase,
    __TestSFTPServerMixin,
):
    sftp_host = SFTP_HOST
    sftp_port = 2223
    sftp_user = SFTP_USER
    sftp_pass = SFTP_PASS

    @classmethod
    def setUpClass(cls):
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
    sftp_port = 2224
    sftp_user = SFTP_USER
    sftp_pass = SFTP_PASS

    @classmethod
    def setUpClass(cls):
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


# class TestSFTPServerWithManager(
#     IsolatedAsyncioTestCase,
#     __TestSFTPServerMixin,
# ):
#     manager: SFTPServerManager
#     manager_thread: threading.Thread
#     sftp_host = SFTP_HOST
#     sftp_port = SFTP_PORT
#     sftp_user = SFTP_USER
#     sftp_pass = SFTP_PASS
#
#     async def asyncSetUpClass(self):
#         self.manager = SFTPServerManager()
#         # Starting the manager in a separate thread since it uses
#         # `run_until_complete`
#         self.manager_thread = threading.Thread(target=self.manager.start)
#         self.manager_thread.daemon = True
#         self.manager_thread.start()
#         time.sleep(2)  # Allow some time for the server to start
#
#     async def asyncTearDown(self):
#         # Stop the server
#         self.manager.stop()
#         self.manager_thread.join()


# class TestSFTPServerWithManager(
#     IsolatedAsyncioTestCase,
#     __TestSFTPServerMixin,
#     ):
#
#     manager: SFTPServerManager
#     manager_thread: threading.Thread
#     sftp_host = SFTP_HOST
#     sftp_port = SFTP_PORT
#     sftp_user = SFTP_USER
#     sftp_pass = SFTP_PASS
#
#     @classmethod
#     def setUpClass(cls):
#         cls.manager = SFTPServerManager()
#         # Starting the manager in a separate thread since it uses
#         # `run_until_complete`
#         cls.manager_thread = threading.Thread(target=cls.manager.start)
#         cls.manager_thread.daemon = True
#         cls.manager_thread.start()
#
#         # Allow some time for the server to start
#         time.sleep(2)
#
#     @classmethod
#     def tearDownClass(cls):
#         # Stop the server
#         cls.manager.stop()
#         cls.manager_thread.join()
