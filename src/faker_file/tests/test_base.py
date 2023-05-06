import sys
import unittest
from typing import List, Union

from ..base import BytesValue, StringList, StringValue, returns_list

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


class TestReturnsList(unittest.TestCase):
    def test_returns_list(self: "TestStringListTestCase") -> None:
        def func_1() -> Union[BytesValue, StringValue]:
            """Returns Union[BytesValue, StringValue]"""

        def func_2() -> Union[StringValue, BytesValue]:
            """Returns Union[StringValue, BytesValue]"""

        def func_3() -> List[Union[BytesValue, StringValue]]:
            """Returns List[Union[BytesValue, StringValue]]"""

        def func_4() -> List[Union[StringValue, BytesValue]]:
            """Returns List[Union[StringValue, BytesValue]]"""

        self.assertFalse(returns_list(func_1))
        self.assertFalse(returns_list(func_2))
        self.assertTrue(returns_list(func_3))
        self.assertTrue(returns_list(func_4))

    def test_no_return_hint(self):
        def func_no_hint(a, b):
            pass

        self.assertFalse(returns_list(func_no_hint))

    def test_incorrect_hint(self):
        def func_incorrect_hint(a) -> str:
            pass

        self.assertFalse(returns_list(func_incorrect_hint))

    def test_undefined_type_hint(self):
        def func_undefined_hint(
            a: "UndefinedType",  # noqa
        ) -> List[Union[BytesValue, StringValue]]:
            pass

        self.assertFalse(returns_list(func_undefined_hint))

    def test_correct_hint(self):
        def func_correct_hint(a) -> List[Union[BytesValue, StringValue]]:
            pass

        self.assertTrue(returns_list(func_correct_hint))

    def test_correct_hint_reversed(self):
        def func_correct_hint_reversed(
            a,
        ) -> List[Union[StringValue, BytesValue]]:
            pass

        self.assertTrue(returns_list(func_correct_hint_reversed))

    @unittest.skipIf(sys.version_info < (3, 9), "Skip on Python < 3.9")
    def test_correct_hint_builtin_list(self):
        def func_correct_hint_builtin_list(
            a,
        ) -> list[Union[BytesValue, StringValue]]:
            pass

        self.assertTrue(returns_list(func_correct_hint_builtin_list))

    @unittest.skipIf(sys.version_info < (3, 9), "Skip on Python < 3.9")
    def test_correct_hint_builtin_list_reversed(self):
        def func_correct_hint_builtin_list_reversed(
            a,
        ) -> list[Union[StringValue, BytesValue]]:
            pass

        self.assertTrue(returns_list(func_correct_hint_builtin_list_reversed))
