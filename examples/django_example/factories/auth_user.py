from django.contrib.auth.models import User
from factory import Faker, PostGenerationMethodCall, Sequence, Trait
from factory.django import DjangoModelFactory

__all__ = (
    "TEST_PASSWORD",
    "TEST_USERNAME",
    "UserFactory",
)

TEST_USERNAME = "test_user"  # pragma: allowlist secret
TEST_PASSWORD = "test_password"  # pragma: allowlist secret


class AbstractUserFactory(DjangoModelFactory):
    """Abstract User factory."""

    password = PostGenerationMethodCall("set_password", TEST_PASSWORD)
    username = Sequence(lambda n: "user%d" % n)
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")

    is_active = False
    is_staff = False
    is_superuser = False

    class Meta:
        """Meta class."""

        model = User
        abstract = True
        django_get_or_create = ("username",)

    class Params:
        active = Trait(is_active=True)
        staff = Trait(is_staff=True)
        superuser = Trait(is_superuser=True)
        super_admin = Trait(
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        test_user = Trait(username=TEST_USERNAME)


class UserFactory(AbstractUserFactory):
    """Upload factory."""
