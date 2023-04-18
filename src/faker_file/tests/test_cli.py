import logging
import subprocess
import unittest

from parametrize import parametrize

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestCLI",)

LOGGER = logging.getLogger(__name__)


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
            # CSV
            (
                "csv_file",
                {},
            ),
            # DOCX
            (
                "docx_file",
                {},
            ),
            # EML
            (
                "eml_file",
                {},
            ),
            # EPUB
            (
                "epub_file",
                {},
            ),
            # ICO
            (
                "ico_file",
                {},
            ),
            # JPEG
            (
                "jpeg_file",
                {},
            ),
            # MP3
            (
                "mp3_file",
                {},
            ),
            # ODP
            (
                "odp_file",
                {},
            ),
            # ODS
            (
                "ods_file",
                {},
            ),
            # ODT
            (
                "odt_file",
                {},
            ),
            # PDF
            (
                "pdf_file",
                {},
            ),
            # PNG
            (
                "png_file",
                {},
            ),
            # PPTX
            (
                "pptx_file",
                {},
            ),
            # RTF
            (
                "rtf_file",
                {},
            ),
            # SVG
            (
                "svg_file",
                {},
            ),
            # TAR
            (
                "tar_file",
                {},
            ),
            # TXT
            (
                "txt_file",
                {},
            ),
            # # WEBP
            # (
            #     "webp_file",
            #     {},
            # ),
            # XLSX
            (
                "xlsx_file",
                {},
            ),
            # ZIP
            (
                "zip_file",
                {},
            ),
        ],
    )
    def test_cli(self: "TestCLI", method_name: str, kwargs: dict):
        """Test CLI."""
        res = subprocess.check_output(["faker-file", method_name]).strip()
        self.assertTrue(res)

    def test_cli_error_no_provider(self: "TestCLI"):
        """Test CLI, no provider given."""
        with self.assertRaises(subprocess.CalledProcessError):
            res = subprocess.check_output(["faker-file"]).strip()
            self.assertFalse(res)
