from textwrap import wrap

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("wrap_text",)


def wrap_text(text: str, wrap_chars_after: int) -> str:
    return "\n".join(
        wrap(
            text=text,
            width=wrap_chars_after,
            replace_whitespace=False,
            # drop_whitespace=False,
        )
    )
