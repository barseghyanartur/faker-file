import unittest
from copy import deepcopy

from ..helpers import random_pop

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("HelpersTestCase",)


class HelpersTestCase(unittest.TestCase):
    """Test StringList test case."""

    def test_random_pop_empty_list(self: "HelpersTestCase") -> None:
        """Test `random_pop`."""
        my_list = []
        element = random_pop(my_list)
        self.assertIsNone(element)

    def test_random_pop(self: "HelpersTestCase") -> None:
        """Test `random_pop`."""
        my_list = [1, 2, 3, 4, 5]
        orig_my_list = deepcopy(my_list)
        while len(my_list):
            element = random_pop(my_list)
            self.assertIn(element, orig_my_list)
            self.assertNotIn(element, my_list)
