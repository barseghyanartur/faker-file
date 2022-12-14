from typing import Optional

from faker.providers import BaseProvider

from ..base import StringValue
from ..constants import DEFAULT_IMAGE_MAX_NB_CHARS
from ..storages.base import BaseStorage
from .mixins.image_mixin import ImageMixin

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("IcoFileProvider",)


class IcoFileProvider(BaseProvider, ImageMixin):
    """ICO file provider.

        Usage example:

        from faker import Faker
        from faker_file.providers.png_file import IcoFileProvider

        file = IcoFileProvider(Faker()).ico_file()

    Usage example with options:

        file = IcoFileProvider(Faker()).ico_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = IcoFileProvider(Faker()).ico_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )
    """

    extension: str = "ico"

    def ico_file(
        self: "IcoFileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate an ICO file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :return: Relative path (from root directory) of the generated file.
        """
        return self._image_file(
            storage=storage,
            prefix=prefix,
            max_nb_chars=max_nb_chars,
            wrap_chars_after=wrap_chars_after,
            content=content,
            **kwargs,
        )
