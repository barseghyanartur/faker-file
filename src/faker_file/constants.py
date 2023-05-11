__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "DEFAULT_AUDIO_MAX_NB_CHARS",
    "DEFAULT_FILE_ENCODING",
    "DEFAULT_FONT_NAME",
    "DEFAULT_FONT_PATH",
    "DEFAULT_IMAGE_MAX_NB_CHARS",
    "DEFAULT_TEXT_CONTENT_TEMPLATE",
    "DEFAULT_TEXT_MAX_NB_CHARS",
    "DEFAULT_XML_DATA_COLUMNS",
)

DEFAULT_AUDIO_MAX_NB_CHARS = 500
DEFAULT_FILE_ENCODING = "utf-8"
DEFAULT_IMAGE_MAX_NB_CHARS = 5_000
DEFAULT_TEXT_CONTENT_TEMPLATE = """{{text}}"""
DEFAULT_TEXT_MAX_NB_CHARS = 10_000
DEFAULT_FONT_NAME = "Vera"
DEFAULT_FONT_PATH = "Vera.ttf"
DEFAULT_XML_DATA_COLUMNS = {
    "name": "{{name}}",
    "address": "{{address}}",
}
