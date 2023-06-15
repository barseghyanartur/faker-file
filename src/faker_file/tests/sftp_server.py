import asyncio
import logging
import os
import tempfile
import threading
from asyncio import Semaphore
from typing import Type

import asyncssh

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "SFTPServer",
    "SFTPServerManager",
    "SSHServer",
    "start_server",
    "start_server_async",
)

DIR_PATH = os.environ.get("DIR_PATH", tempfile.gettempdir())
SFTP_USER = os.environ.get("SFTP_USER", "foo")
SFTP_PASS = os.environ.get("SFTP_PASS", "pass")
SFTP_HOST = os.environ.get("SFTP_HOST", "0.0.0.0")
SFTP_PORT = int(os.environ.get("SFTP_PORT", 2222))
NUM_CONCURRENT_CONNECTIONS = int(
    os.environ.get("NUM_CONCURRENT_CONNECTIONS", 50)
)
LOGGER = logging.getLogger(__name__)


class SFTPServer(asyncssh.SFTPServer):
    def __init__(self: "SFTPServer", conn: asyncssh.SSHServerChannel) -> None:
        root = DIR_PATH
        super().__init__(conn, chroot=root)


class SSHServer(asyncssh.SSHServer):
    def __init__(self: "SSHServer", connection_semaphore: Semaphore) -> None:
        self._connection_semaphore = connection_semaphore

    def password_auth_supported(self: "SSHServer") -> bool:
        return True

    def validate_password(
        self: "SSHServer", username: str, password: str
    ) -> bool:
        user_passwords = {SFTP_USER: SFTP_PASS}
        return user_passwords.get(username) == password

    def session_requested(self: "SSHServer") -> bool:
        return True

    def sftp_requested(self: "SSHServer") -> Type[SFTPServer]:
        return SFTPServer

    async def begin_auth(self: "SSHServer", username: str) -> bool:
        await self._connection_semaphore.acquire()
        return True

    def auth_completed(self: "SSHServer") -> None:
        self._connection_semaphore.release()


async def start_server_async(
    host: str = SFTP_HOST, port: int = SFTP_PORT
) -> None:
    # Generate an SSH keypair or use an existing one
    server_key = asyncssh.generate_private_key("ssh-rsa")

    # Create a connection semaphore with the desired maximum number of
    # connections.
    connection_semaphore = Semaphore(50)

    LOGGER.info(f"Starting SFTP server at {host}:{port}")
    print(f"start_server_async: Starting SFTP server at {host}:{port}")

    server = await asyncssh.listen(
        host,
        port,
        server_host_keys=[server_key],
        server_factory=lambda: SSHServer(connection_semaphore),
        sftp_factory=SFTPServer,
    )

    async with server:
        try:
            await server.wait_closed()
        except asyncio.CancelledError:
            pass


def start_server(host: str = SFTP_HOST, port: int = SFTP_PORT) -> None:
    print(f"start_server: Starting SFTP server at {host}:{port}")

    # This function will be run in a new thread
    def run_loop_in_thread(_loop):
        asyncio.set_event_loop(_loop)
        _loop.run_forever()

    # Get the current event loop, create if it doesn't exist
    loop = asyncio.new_event_loop()

    # Schedule the coroutine to be executed
    loop.create_task(start_server_async(host=host, port=port))

    # Start a new thread running the loop
    server_thread = threading.Thread(target=run_loop_in_thread, args=(loop,))
    server_thread.daemon = True
    server_thread.start()


class SFTPServerManager:
    def __init__(self, host: str = SFTP_HOST, port: int = SFTP_PORT) -> None:
        self.loop = asyncio.get_event_loop()
        self.stop_event = asyncio.Event()
        self.host = host
        self.port = port

    async def start_server(self) -> None:
        # Generate an SSH keypair or use an existing one
        server_key = asyncssh.generate_private_key("ssh-rsa")

        # Create a connection semaphore with the desired maximum number of
        # connections.
        connection_semaphore = Semaphore(50)

        server = await asyncssh.listen(
            self.host,
            self.port,
            server_host_keys=[server_key],
            server_factory=lambda: SSHServer(connection_semaphore),
            sftp_factory=SFTPServer,
        )
        # Just replace stop_event with self.stop_event

        async with server:
            try:
                await self.stop_event.wait()
            except asyncio.CancelledError:
                pass
            finally:
                server.close()
                await server.wait_closed()

    def start(self) -> None:
        self.loop.run_until_complete(self.start_server())

    def stop(self) -> None:
        self.loop.call_soon_threadsafe(self.stop_event.set)
