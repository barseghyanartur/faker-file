import importlib
from textwrap import wrap
from typing import Type

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "load_class_from_path",
    "wrap_text",
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
    except ImportError as e:
        raise ImportError(f"Error loading class from path '{full_path}': {e}")
