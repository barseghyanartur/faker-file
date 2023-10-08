from factory import Faker
from factory.django import DjangoModelFactory
from faker_file.providers.odt_file import OdtFileProvider

from upload.models import Upload


class UploadFactory(DjangoModelFactory):
    """Base Upload factory."""

    name = Faker("text", max_nb_chars=100)
    description = Faker("text", max_nb_chars=1000)
    file = Faker("odt_file")

    class Meta:
        """Meta class."""

        model = Upload


# Example usage
with Faker.override_default_locale("hy_AM"):  # Set locale to Armenian
    Faker.add_provider(OdtFileProvider)
    upload = UploadFactory()
