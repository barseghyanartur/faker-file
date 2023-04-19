import logging
import subprocess
import unittest

from parametrize import parametrize

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestCLI",)

LOGGER = logging.getLogger(__name__)


def convert_value_to_cli_arg(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float, str)):
        return str(value)
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")


class TestCLI(unittest.TestCase):
    """CLI tests."""

    def setUp(self):
        """Set up."""

    @parametrize(
        "method_name, kwargs",
        [
            # BIN
            (
                "bin_file",
                {},
            ),
            (
                "bin_file",
                {"length": 1_024},
            ),
            # CSV
            (
                "csv_file",
                {},
            ),
            (
                "csv_file",
                {"num_rows": 20},
            ),
            # DOCX
            (
                "docx_file",
                {},
            ),
            (
                "docx_file",
                {"wrap_chars_after": 40},
            ),
            # EML
            (
                "eml_file",
                {},
            ),
            (
                "eml_file",
                {"wrap_chars_after": 40},
            ),
            # EPUB
            (
                "epub_file",
                {},
            ),
            (
                "epub_file",
                {"wrap_chars_after": 40},
            ),
            # ICO
            (
                "ico_file",
                {},
            ),
            (
                "ico_file",
                {"wrap_chars_after": 40},
            ),
            # JPEG
            (
                "jpeg_file",
                {},
            ),
            (
                "jpeg_file",
                {"wrap_chars_after": 40},
            ),
            # MP3
            (
                "mp3_file",
                {},
            ),
            (
                "mp3_file",
                {"max_nb_chars": 256},
            ),
            # ODP
            (
                "odp_file",
                {},
            ),
            (
                "odp_file",
                {"wrap_chars_after": 40},
            ),
            # ODS
            (
                "ods_file",
                {},
            ),
            (
                "ods_file",
                {"num_rows": 20},
            ),
            # ODT
            (
                "odt_file",
                {},
            ),
            (
                "odt_file",
                {"wrap_chars_after": 40},
            ),
            # PDF
            (
                "pdf_file",
                {},
            ),
            (
                "pdf_file",
                {"wrap_chars_after": 40},
            ),
            # PNG
            (
                "png_file",
                {},
            ),
            (
                "png_file",
                {"wrap_chars_after": 40},
            ),
            # PPTX
            (
                "pptx_file",
                {},
            ),
            (
                "pptx_file",
                {"wrap_chars_after": 40},
            ),
            # RTF
            (
                "rtf_file",
                {},
            ),
            (
                "rtf_file",
                {"wrap_chars_after": 40},
            ),
            # SVG
            (
                "svg_file",
                {},
            ),
            (
                "svg_file",
                {"wrap_chars_after": 40},
            ),
            # TAR
            (
                "tar_file",
                {},
            ),
            (
                "tar_file",
                {"prefix": "ttt_"},
            ),
            # TXT
            (
                "txt_file",
                {},
            ),
            (
                "txt_file",
                {"wrap_chars_after": 40},
            ),
            # # WEBP
            # (
            #     "webp_file",
            #     {},
            # ),
            # (
            #     "webp_file",
            #     {},
            # ),
            # XLSX
            (
                "xlsx_file",
                {},
            ),
            (
                "xlsx_file",
                {"num_rows": 20},
            ),
            # ZIP
            (
                "zip_file",
                {},
            ),
            (
                "zip_file",
                {"prefix": "ttt_"},
            ),
        ],
    )
    def test_cli(self: "TestCLI", method_name: str, kwargs: dict):
        """Test CLI."""
        # Convert kwargs to command-line arguments
        args = [
            f"--{key}={convert_value_to_cli_arg(value)}"
            for key, value in kwargs.items()
        ]

        # Merge the base command with the generated arguments
        cmd = ["faker-file", method_name] + args

        # Execute the command with the provided arguments
        res = subprocess.check_output(cmd).strip()
        self.assertTrue(res)

    def test_cli_error_no_provider(self: "TestCLI"):
        """Test CLI, no provider given."""
        with self.assertRaises(subprocess.CalledProcessError):
            res = subprocess.check_output(["faker-file"]).strip()
            self.assertFalse(res)
