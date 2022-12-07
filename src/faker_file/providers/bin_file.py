import os
from typing import Optional

from faker import Faker
from faker.providers import BaseProvider

from ..base import DEFAULT_REL_PATH, FileMixin, StringValue

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("BinFileProvider",)


FAKER = Faker()


class BinFileProvider(BaseProvider, FileMixin):
    """BIN file provider.

    Usage example:

        from faker_file.providers.bin_file import BinFileProvider

        file = BinFileProvider(None).bin_file()

    Usage example with options:

        from faker_file.providers.bin_file import BinFileProvider

        file = BinFileProvider(None).bin_file(
            prefix="zzz",
            length=1024**2,
        )
    """

    extension: str = "bin"

    def bin_file(
        self,
        root_path: str = None,
        rel_path: str = DEFAULT_REL_PATH,
        prefix: Optional[str] = None,
        length: int = (1 * 1024 * 1024),
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a CSV file with random text.

        :param root_path: Path of your files root directory (in case of Django
            it would be `settings.MEDIA_ROOT`).
        :param rel_path: Relative path (from root directory).
        :param prefix: File name prefix.
        :param length:
        :param content: File content. If given, used as is.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        file_name = self._generate_filename(
            root_path=root_path,
            rel_path=rel_path,
            prefix=prefix,
        )

        # Specific
        if content is None:
            content = FAKER.binary(length=length)

        file_mode = "w"  # str
        if isinstance(content, bytes):
            file_mode = "wb"
        with open(file_name, file_mode) as fakefile:
            fakefile.write(content)

        # Generic
        file_name = StringValue(os.path.relpath(file_name, root_path))
        file_name.data = {"content": content}
        return file_name
