from textwrap import wrap

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("wrap_text",)


def wrap_text(text: str, wrap_chars_after: int) -> str:
    return "\n".join(wrap(text, wrap_chars_after))
