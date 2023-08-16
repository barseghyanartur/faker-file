"""
Configuration hooks for pytest. Normally this wouldn't be necessary,
but since pytest-rst is used, we want to clean-up files generated by
running documentation tests. Therefore, this hook, which simply
calls the `clean_up` method of the `FILE_REGISTRY` instance.
"""
from faker_file.registry import FILE_REGISTRY

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "pytest_runtest_setup",
    "pytest_runtest_teardown",
)


def pytest_runtest_setup(item):
    """Setup before test runs."""
    try:
        from pytest_rst import RSTTestItem

        if isinstance(item, RSTTestItem):
            # Insert the setup logic here
            pass  # Replace with your desired setup actions
    except ImportError:
        pass


def pytest_runtest_teardown(item, nextitem):
    """Clean up after test ends."""
    try:
        from pytest_rst import RSTTestItem

        if isinstance(item, RSTTestItem):
            FILE_REGISTRY.clean_up()
    except ImportError:
        pass