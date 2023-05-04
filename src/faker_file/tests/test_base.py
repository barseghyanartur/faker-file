import unittest

from ..base import StringList

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestStringListTestCase",)


class TestStringListTestCase(unittest.TestCase):
    """Test StringList test case."""

    def test_string_list(self: "TestStringListTestCase") -> None:
        my_string = StringList(["apple", "banana", "cherry"], separator=" | ")

        self.assertEqual(str(my_string), "apple | banana | cherry")

        my_string.add_string("orange")
        self.assertEqual(str(my_string), "apple | banana | cherry | orange")

        my_string.remove_string("banana")
        self.assertEqual(str(my_string), "apple | cherry | orange")

        my_string += "grape"
        self.assertEqual(str(my_string), "apple | cherry | orange | grape")
        self.assertEqual(repr(my_string), "apple | cherry | orange | grape")
