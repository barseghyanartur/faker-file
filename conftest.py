import pytest
from faker_file.tests._conftest import *  # noqa


@pytest.fixture()
def my_fixture() -> None:
    """My fixture used just as an example, since referred in agentic docs."""
    return None
