from typing import Optional, Union, overload

from faker import Faker
from faker.providers import BaseProvider

from ..base import BytesValue, FileMixin, StringValue
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("BinFileProvider",)


class BinFileProvider(BaseProvider, FileMixin):
    """BIN file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.bin_file import BinFileProvider

        FAKER = Faker()
        FAKER.add_provider(BinFileProvider)

        file = FAKER.bin_file()

    Usage example with options:

    .. code-block:: python

        file = FAKER.bin_file(
            prefix="zzz",
            length=1024**2,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

    .. code-block:: python

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.bin_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            length=1024**2,
        )

    Usage example with AWS S3 storage:

    .. code-block:: python

        from faker_file.storages.aws_s3 import AWSS3Storage

        file = FAKER.bin_file(
            storage=AWSS3Storage(bucket_name="My-test-bucket"),
            prefix="zzz",
            length=1024**2,
        )
    """

    extension: str = "bin"

    @overload
    def bin_file(
        self: "BinFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        length: int = (1 * 1024 * 1024),
        content: Optional[bytes] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def bin_file(
        self: "BinFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        length: int = (1 * 1024 * 1024),
        content: Optional[bytes] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def bin_file(
        self: "BinFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        length: int = (1 * 1024 * 1024),
        content: Optional[bytes] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a BIN file with random bytes.

        :param storage: Storage class. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param length:
        :param content: File content. If given, used as is.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        filename = storage.generate_filename(
            extension=self.extension,
            prefix=prefix,
            basename=basename,
        )

        if self.generator is None:
            self.generator = Faker()

        # Specific
        if content is None:
            content = self.generator.binary(length=length)

        data = {"content": content, "filename": filename, "storage": storage}

        if raw:
            raw_content = BytesValue(content)
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, content)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
