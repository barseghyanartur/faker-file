import io
import logging
import unittest

from faker import Faker

from ..providers.txt_file import TxtFileProvider
from ..registry import FILE_REGISTRY, LOGGER

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("RegistryTestCase",)


FAKER = Faker()
FAKER.add_provider(TxtFileProvider)


class RegistryTestCase(unittest.TestCase):
    """Test `registry` module."""

    def test_integration(self: "RegistryTestCase") -> None:
        """Test `add`."""
        # Create a TXT file.
        txt_file_1 = FAKER.txt_file()

        with self.subTest("Check if `add` works"):
            # Check if `add` works (the file is in the registry)
            self.assertIn(txt_file_1, FILE_REGISTRY._registry)

        with self.subTest("Check if `search` works"):
            # Check if `search` works
            res = FILE_REGISTRY.search(str(txt_file_1))
            self.assertIsNotNone(res)
            self.assertEqual(res, txt_file_1)

        with self.subTest("Check if `remove` by `StringValue` works"):
            # Check if `remove` by `StringValue`.
            FILE_REGISTRY.remove(txt_file_1)
            self.assertNotIn(txt_file_1, FILE_REGISTRY._registry)

        with self.subTest("Check if `remove` by `str` works"):
            # Create another TXT file and check if `remove` by `str` works.
            txt_file_2 = FAKER.txt_file()
            self.assertIn(txt_file_2, FILE_REGISTRY._registry)
            FILE_REGISTRY.remove(str(txt_file_2))
            self.assertNotIn(txt_file_2, FILE_REGISTRY._registry)

        with self.subTest("Check if `clean_up` works"):
            # Check if `clean_up` works
            txt_file_3 = FAKER.txt_file()
            txt_file_4 = FAKER.txt_file()
            txt_file_5 = FAKER.txt_file()
            self.assertIn(txt_file_3, FILE_REGISTRY._registry)
            self.assertIn(txt_file_4, FILE_REGISTRY._registry)
            self.assertIn(txt_file_5, FILE_REGISTRY._registry)

            FILE_REGISTRY.clean_up()
            self.assertNotIn(txt_file_3, FILE_REGISTRY._registry)
            self.assertNotIn(txt_file_4, FILE_REGISTRY._registry)
            self.assertNotIn(txt_file_5, FILE_REGISTRY._registry)

    def test_remove_by_string_not_found(self):
        res = FILE_REGISTRY.remove("i_do_not_exist.ext")
        self.assertFalse(res)

    def test_remove_exceptions(self):
        txt_file = FAKER.txt_file()
        txt_file.data["storage"].unlink(txt_file)

        res = FILE_REGISTRY.remove(txt_file)
        self.assertFalse(res)

    def test_clean_up_exceptions(self):
        # Redirect logger output to a string stream
        log_stream = io.StringIO()
        handler = logging.StreamHandler(log_stream)
        LOGGER.addHandler(handler)
        txt_file = FAKER.txt_file()
        txt_file.data["storage"].unlink(txt_file)

        # Clean up registry
        FILE_REGISTRY.clean_up()

        # Check the content of the logging output
        log_output = log_stream.getvalue()
        self.assertIn(
            f"Failed to unlink file {txt_file.data['filename']}",
            log_output,
        )

        # Clean up by removing the handler
        LOGGER.removeHandler(handler)
