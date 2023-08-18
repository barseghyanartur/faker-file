import sys
import unittest
from typing import List, Union

from ..base import BytesValue, StringList, StringValue, returns_list

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("StringListTestCase",)


class StringListTestCase(unittest.TestCase):
    """StringList test case."""

    def test_string_list(self: "StringListTestCase") -> None:
        my_string = StringList(["apple", "banana", "cherry"], separator=" | ")

        self.assertEqual(str(my_string), "apple | banana | cherry")

        my_string.add_string("orange")
        self.assertEqual(str(my_string), "apple | banana | cherry | orange")

        my_string.remove_string("banana")
        self.assertEqual(str(my_string), "apple | cherry | orange")

        my_string += "grape"
        self.assertEqual(str(my_string), "apple | cherry | orange | grape")
        self.assertEqual(repr(my_string), "apple | cherry | orange | grape")


class ReturnsListTestCase(unittest.TestCase):
    def test_returns_list(self: "ReturnsListTestCase") -> None:
        def func_1() -> Union[BytesValue, StringValue]:
            """Returns Union[BytesValue, StringValue]"""
            return StringValue("func_1")

        def func_2() -> Union[StringValue, BytesValue]:
            """Returns Union[StringValue, BytesValue]"""
            return BytesValue(b"func_2")

        def func_3() -> List[Union[BytesValue, StringValue]]:
            """Returns List[Union[BytesValue, StringValue]]"""
            return [BytesValue(b"func_3"), StringValue("func_3")]

        def func_4() -> List[Union[StringValue, BytesValue]]:
            """Returns List[Union[StringValue, BytesValue]]"""
            return [StringValue("func_4"), BytesValue(b"func_4")]

        self.assertFalse(returns_list(func_1))
        self.assertFalse(returns_list(func_2))
        self.assertTrue(returns_list(func_3))
        self.assertTrue(returns_list(func_4))

    def test_no_return_hint(self: "ReturnsListTestCase"):
        def func_no_hint(a, b):
            pass

        self.assertFalse(returns_list(func_no_hint))

    def test_incorrect_hint(self: "ReturnsListTestCase"):
        def func_incorrect_hint(a) -> str:
            return "func_incorrect_hint"

        self.assertFalse(returns_list(func_incorrect_hint))

    def test_undefined_type_hint(self: "ReturnsListTestCase"):
        def func_undefined_hint(
            a: "UndefinedType",  # noqa
        ) -> List[Union[BytesValue, StringValue]]:
            return [BytesValue(b"fn_undef_hint"), StringValue("fn_undef_hint")]

        self.assertFalse(returns_list(func_undefined_hint))

    def test_correct_hint(self: "ReturnsListTestCase"):
        def func_correct_hint(a) -> List[Union[BytesValue, StringValue]]:
            return [BytesValue(b"fn_corr_hint"), StringValue("fn_corr_hint")]

        self.assertTrue(returns_list(func_correct_hint))

    def test_correct_hint_reversed(self: "ReturnsListTestCase"):
        def func_correct_hint_reversed(
            a,
        ) -> List[Union[StringValue, BytesValue]]:
            return [BytesValue(b"fn_corr_hint"), StringValue("fn_corr_hint")]

        self.assertTrue(returns_list(func_correct_hint_reversed))

    @unittest.skipIf(sys.version_info < (3, 9), "Skip on Python < 3.9")
    def test_correct_hint_builtin_list(self: "ReturnsListTestCase"):
        def func_correct_hint_builtin_list(
            a,
        ) -> list[Union[BytesValue, StringValue]]:
            return [BytesValue(b"fn_corr_hint"), StringValue("fn_corr_hint")]

        self.assertTrue(returns_list(func_correct_hint_builtin_list))

    @unittest.skipIf(sys.version_info < (3, 9), "Skip on Python < 3.9")
    def test_correct_hint_builtin_list_reversed(self: "ReturnsListTestCase"):
        def func_correct_hint_builtin_list_reversed(
            a,
        ) -> list[Union[StringValue, BytesValue]]:
            return [BytesValue(b"fn_corr_hint"), StringValue("fn_corr_hint")]

        self.assertTrue(returns_list(func_correct_hint_builtin_list_reversed))
