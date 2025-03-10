import importlib.metadata
from typing import Union

from packaging import version

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2025 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("is_legacy_pathy_version",)


def is_legacy_pathy_version() -> Union[bool, None]:
    """Check if a pathy version is less than 0.11.

    :return: True if `pathy` version is less than 0.11.
        False if `pathy` version is greater or equal than 0.11.
        None if `pathy` is not installed.
    :rtype: Union[bool, None]
    """
    try:
        current_version = importlib.metadata.version("pathy")
    except importlib.metadata.PackageNotFoundError:
        return None
    return version.parse(current_version) < version.parse("0.11")
