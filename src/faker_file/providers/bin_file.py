from typing import Optional

from faker import Faker
from faker.providers import BaseProvider

from ..base import FileMixin, StringValue
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("BinFileProvider",)


class BinFileProvider(BaseProvider, FileMixin):
    """BIN file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.bin_file import BinFileProvider

        file = BinFileProvider(Faker()).bin_file()

    Usage example with options:

        file = BinFileProvider(Faker()).bin_file(
            prefix="zzz",
            length=1024**2,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = BinFileProvider(Faker()).bin_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            length=1024**2,
        )

    Usage example with AWS S3 storage:

        from faker_file.storages.aws_s3 import AWSS3Storage

        file = BinFileProvider(Faker()).bin_file(
            storage=AWSS3Storage(bucket_name="My-test-bucket"),
            prefix="zzz",
            length=1024**2,
        )
    """

    extension: str = "bin"

    def bin_file(
        self: "BinFileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        length: int = (1 * 1024 * 1024),
        content: Optional[bytes] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a CSV file with random text.

        :param storage: Storage class. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param length:
        :param content: File content. If given, used as is.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        filename = storage.generate_filename(
            prefix=prefix,
            extension=self.extension,
        )

        if self.generator is None:
            self.generator = Faker()

        # Specific
        if content is None:
            content = self.generator.binary(length=length)

        storage.write_bytes(filename, content)

        # Generic
        filename = StringValue(storage.relpath(filename))
        filename.data = {"content": content}
        return filename
