import random
import socket

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "AutoIncPortInt",
    "AutoFreePortInt",
)


class AutoIncPortInt(int):
    """Automatically incremented integer value.

    Contains state of issued values. Starts from 2223. Every time
    initialized, value increases.

    Usage example:

        port = AutoInt()  # 2223
        port = AutoInt()  # 2224
        port = AutoInt()  # 2225

    For the rest, it behaves like a normal integer.

    For better integration, it's recommended to cast the value to `int`,
    like this:

        port = int(AutoInt())
    """

    # This is a class attribute that keeps the current state
    _next_value: int = 2223

    def __new__(cls, *args, **kwargs) -> "AutoIncPortInt":
        """Create a new instance of AutoInt with the next value."""
        # Use __new__ because int is immutable, so we need to set the value
        # before creating the instance.
        instance = super().__new__(cls, cls._next_value)
        # Increment the class attribute for the next instance
        cls._next_value += 1
        # Return the new instance
        return instance


class AutoFreePortInt(int):
    """Automatically and randomly picks a free port within a specified range.

    For instance:

        # Random free port between default range 2223 and 5000
        port = AutoFreePortInt()

        # Random free port between 3000 and 4000
        port = AutoFreePortInt(min_port=3000, max_port=4000)

    For the rest, it behaves like a normal integer.

    For better integration, it's recommended to cast the value to `int`,
    like this:

        port = int(AutoFreePortInt())
    """

    # Default port range
    DEFAULT_MIN_PORT: int = 2223
    DEFAULT_MAX_PORT: int = 5000

    @staticmethod
    def _is_port_free(host: str, port: int) -> bool:
        """Check if the given port is free."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                # Try to bind the socket to the port
                s.bind((host, port))
                return True
            except OSError:
                return False

    def __new__(
        cls,
        min_port: int = DEFAULT_MIN_PORT,
        max_port: int = DEFAULT_MAX_PORT,
        host: str = "localhost",
        *args,
        **kwargs,
    ) -> "AutoFreePortInt":
        """Create a new instance of `AutoFreePortInt`.

        With a free random port within the specified range.
        """
        # Validate the range
        if not (
            isinstance(min_port, int)
            and isinstance(max_port, int)
            and min_port <= max_port
        ):
            raise ValueError("Invalid port range specified")

        # Pick a random port within the specified range and check if it's free
        while True:
            port = random.randint(min_port, max_port)
            if cls._is_port_free(host, port):
                break

        # Use __new__ to create the instance with the free port as the value
        instance = super().__new__(cls, port)
        return instance
