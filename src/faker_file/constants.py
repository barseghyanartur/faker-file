__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "DEFAULT_IMAGE_MAX_NB_CHARS",
    "DEFAULT_TEXT_MAX_NB_CHARS",
    "DEFAULT_TEXT_CONTENT_TEMPLATE",
    "DEFAULT_FILE_ENCODING",
)

DEFAULT_IMAGE_MAX_NB_CHARS = 5_000
DEFAULT_TEXT_MAX_NB_CHARS = 10_000
DEFAULT_TEXT_CONTENT_TEMPLATE = """{{text}}"""
DEFAULT_FILE_ENCODING = "utf-8"
