from pathlib import Path

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "DEFAULT_AUDIO_MAX_NB_CHARS",
    "DEFAULT_FILE_ENCODING",
    "DEFAULT_IMAGE_MAX_NB_CHARS",
    "DEFAULT_TEXT_CONTENT_TEMPLATE",
    "DEFAULT_TEXT_MAX_NB_CHARS",
    "DEFAULT_FONT_PATH",
    "DEFAULT_FONT_NAME",
)

DEFAULT_AUDIO_MAX_NB_CHARS = 500
DEFAULT_FILE_ENCODING = "utf-8"
DEFAULT_IMAGE_MAX_NB_CHARS = 5_000
DEFAULT_TEXT_CONTENT_TEMPLATE = """{{text}}"""
DEFAULT_TEXT_MAX_NB_CHARS = 10_000

FONTS_DIR = Path(__file__).resolve().parent / "fonts"

DEFAULT_FONT_NAME = "DejaVuSansCondensed"
DEFAULT_FONT_PATH = FONTS_DIR / "DejaVuSansCondensed.ttf"
