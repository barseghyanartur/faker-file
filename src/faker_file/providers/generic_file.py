from typing import Callable, Optional, Union, overload

from faker import Faker
from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.python import Provider

from ..base import DEFAULT_FORMAT_FUNC, BytesValue, FileMixin, StringValue
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("GenericFileProvider",)


class GenericFileProvider(BaseProvider, FileMixin):
    """Generic file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.generic_file import GenericFileProvider

        FAKER = Faker()
        FAKER.add_provider(GenericFileProvider)

        file = FAKER.generic_file(
            content="<html><body><p>{{text}}</p></body></html>",
            extension="html",
        )

    Usage example with options:

    .. code-block:: python

        file = FAKER.generic_file(
            content="<html><body><p>{{text}}</p></body></html>",
            extension="html",
            prefix="zzz",
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

    .. code-block:: python

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.generic_file(
            content="<html><body><p>{{text}}</p></body></html>",
            extension="html",
            basename="index",
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
        )

    Usage example with AWS S3 storage:

    .. code-block:: python

        from faker_file.storages.aws_s3 import AWSS3Storage

        file = FAKER.generic_file(
            storage=AWSS3Storage(bucket_name="My-test-bucket"),
            content="<html><body><p>{{text}}</p></body></html>",
            extension="html",
        )
    """

    extension: str = None

    @overload
    def generic_file(
        self: "GenericFileProvider",
        content: Union[bytes, str],
        extension: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def generic_file(
        self: "GenericFileProvider",
        content: Union[bytes, str],
        extension: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def generic_file(
        self: "GenericFileProvider",
        content: Union[bytes, str],
        extension: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a generic file with given content.

        :param content: File content. If given, used as is.
        :param extension: File extension.
        :param storage: Storage class. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param format_func: Callable responsible for formatting template
            strings.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
        """
        self.extension = extension

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

        data = {"content": content, "filename": filename, "storage": storage}

        if raw:
            if isinstance(content, bytes):
                raw_content = BytesValue(content)
            else:
                raw_content = BytesValue(
                    format_func(self.generator, content).encode()
                )
            raw_content.data = data
            return raw_content

        if isinstance(content, bytes):
            storage.write_bytes(filename, content)
        else:
            storage.write_text(
                filename,
                format_func(self.generator, content),
            )

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
