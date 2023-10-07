from factory import Faker
from factory.django import DjangoModelFactory
from faker_file.providers.odt_file import OdtFileProvider

from upload.models import Upload

Faker._DEFAULT_LOCALE = "hy_AM"  # Set locale to Armenian

Faker.add_provider(OdtFileProvider)


class UploadFactory(DjangoModelFactory):
    """Base Upload factory."""

    name = Faker("text", max_nb_chars=100)
    description = Faker("text", max_nb_chars=1000)
    file = Faker("odt_file")

    class Meta:
        """Meta class."""

        model = Upload


# Example usage
upload = UploadFactory()
