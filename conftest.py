from typing import Type

import pytest
from faker import Faker as FakerClass
from faker_file.tests._conftest import *  # noqa
from moto import mock_aws as moto_mock_aws


@pytest.fixture()
def my_fixture() -> None:
    """My fixture used just as an example, since referred in agentic docs."""
    return None


@pytest.fixture()
def Faker() -> Type[FakerClass]:  # noqa
    """Faker class for documentation tests."""
    return FakerClass


@pytest.fixture
def aws_mock():
    """Mock AWS."""
    with moto_mock_aws() as _:
        yield
