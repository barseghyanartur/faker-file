import importlib
import importlib.metadata
import mimetypes
import random
from textwrap import wrap
from typing import Any, Tuple, Type

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2025 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "load_class_from_path",
    "random_pop",
    "wrap_text",
    "get_mime_maintype_subtype",
)


def wrap_text(text: str, wrap_chars_after: int) -> str:
    return "\n".join(
        wrap(
            text=text,
            width=wrap_chars_after,
            replace_whitespace=False,
            # drop_whitespace=False,
        )
    )


def load_class_from_path(full_path: str) -> Type:
    """Load a class from a given full path string identifier.

    :param full_path: The full path to the class,
        e.g. 'module.submodule.MyClass'.
    :return: The loaded class.
    :raise: If the module cannot be found or the class does
        not exist in the module, it raises ImportError.

    Usage example:

    .. code-block:: python

        my_class = load_class_from_path("module.submodule.MyClass")
        instance = my_class()
    """
    try:
        module_name, class_name = full_path.rsplit(".", 1)
        module = importlib.import_module(module_name)

        if not hasattr(module, class_name):
            raise ImportError(
                f"Class '{class_name}' not found in module '{module_name}'"
            )

        loaded_class = getattr(module, class_name)

        if not isinstance(loaded_class, type):
            raise ImportError(f"'{full_path}' does not point to a class")

        return loaded_class
    except ImportError as err:
        raise ImportError(
            f"Error loading class from path '{full_path}': {err}"
        ) from err


def random_pop(lst: list) -> Any:
    """Randomly pops element from the given list. Alters the list.

    :param lst: List to pop element from.
    :return: A single element from the list.

    Usage example:

    .. code-block:: python

        from faker_file.helpers import random_pop
        my_list = [1, 2, 3, 4, 5]
        element = random_pop(my_list)
    """
    if len(lst) > 0:
        idx = random.randrange(len(lst))
        return lst.pop(idx)
    else:
        return None


# Missing/specific custom types
MISSING_MIMETYPES = {
    ".docx": "application/"
             "vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".pptx": "application/"
             "vnd.openxmlformats-officedocument.presentationml.presentation",
    ".xlsx": "application/"
             "vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".epub": "application/epub+zip",
    ".odt": "application/vnd.oasis.opendocument.text",
    ".rtf": "application/rtf",
}


def get_mime_maintype_subtype(path: str) -> Tuple[str, str]:
    """
    Determine the MIME maintype and subtype for the given file path,
    using Python's built-in mimetypes plus a few custom entries.

    :param path: Path to the file (extension is used for lookup).
    :return: (maintype, subtype) tuple, for example ("application", "pdf")
    """
    # Initialize the system-wide mappings
    mimetypes.init()

    for ext, ctype in MISSING_MIMETYPES.items():
        mimetypes.add_type(ctype, ext, strict=True)

    # Prefer `guess_file_type` on Python 3.13+, else `guess_type`
    if hasattr(mimetypes, "guess_file_type"):
        ctype, encoding = mimetypes.guess_file_type(path)
    else:
        ctype, encoding = mimetypes.guess_type(path)

    # If unknown or if an encoding hint was returned, fall back safely
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    # Split into maintype/subtype
    maintype, subtype = ctype.split("/", 1)
    return maintype, subtype
