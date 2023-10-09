from typing import Callable


def foo(bar: Callable[[str], int]) -> int:
    a = 42
    b = "Prism"
    return a + bar(b)
