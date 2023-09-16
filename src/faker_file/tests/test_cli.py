import logging
import re
import subprocess
import unittest
from importlib import import_module, reload
from typing import Union

from parametrize import parametrize

from ..cli.command import main
from ..registry import FILE_REGISTRY
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestCLI",)

LOGGER = logging.getLogger(__name__)


VERSION_PATTERN = re.compile(r"^\d+(\.\d+){0,2}$")
FS_STORAGE = FileSystemStorage()
FILE_PATH_PATTERN = re.compile(r"/.+")


def convert_value_to_cli_arg(value) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float, str)):
        return str(value)
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")


def extract_filename(val) -> Union[str, None]:
    match = FILE_PATH_PATTERN.search(val)
    if match:
        extracted_path = match.group(0)
        return extracted_path


class TestCLI(unittest.TestCase):
    """CLI tests."""

    def tearDown(self) -> None:
        super().tearDown()
        FILE_REGISTRY.clean_up()

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
            # Generic
            (
                "generic_file",
                {
                    "content": "<html><body><p>{{text}}</p></body></html>",
                    "extension": "html",
                },
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
    def test_cli(self: "TestCLI", method_name: str, kwargs: dict) -> None:
        """Test CLI."""
        # Convert kwargs to command-line arguments
        args = [
            f"--{key}={convert_value_to_cli_arg(value)}"
            for key, value in kwargs.items()
        ]

        # Merge the base command with the generated arguments
        cmd = ["faker-file", method_name] + args
        # LOGGER.debug(f"cmd: {cmd}")
        # Execute the command with the provided arguments
        res = subprocess.check_output(cmd).strip()

        # Extract the filename to verify existence and clean-up
        filename = extract_filename(res.decode())
        # LOGGER.debug(f"filename: {filename}")
        self.assertTrue(filename)
        self.assertTrue(FS_STORAGE.exists(filename))
        FS_STORAGE.unlink(filename)

    def test_cli_error_no_provider(self: "TestCLI") -> None:
        """Test CLI, no provider given."""
        with self.assertRaises(subprocess.CalledProcessError):
            res = subprocess.check_output(["faker-file"]).strip()
            self.assertFalse(res)

    def test_cli_generate_completion(self: "TestCLI") -> None:
        """Test CLI, generate-completion."""
        cmd = ["faker-file", "generate-completion"]
        res = subprocess.check_output(cmd).strip()
        self.assertTrue(res)

    def test_cli_version(self: "TestCLI") -> None:
        """Test CLI, version."""
        cmd = ["faker-file", "version"]
        res = subprocess.check_output(cmd).strip()
        self.assertTrue(VERSION_PATTERN.match(res.decode()))

    def test_broken_imports(self: "TestCLI") -> None:
        """Test broken imports."""
        _module = import_module("faker_file.cli.helpers")
        del _module.__dict__["PROVIDERS"]
        with self.assertRaises(SystemExit):
            main()
        reload(_module)
