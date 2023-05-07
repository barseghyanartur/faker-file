from typing import Optional, Union, overload

from faker import Faker
from faker.providers import BaseProvider

from ..base import BytesValue, FileMixin, StringValue
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("GenericFileProvider",)


class GenericFileProvider(BaseProvider, FileMixin):
    """Generic file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.generic_file import GenericFileProvider

        file = GenericFileProvider(Faker()).generic_file(
            content="<html><body><p>{{text}}</p></body></html>",
            extension="html",
        )

    Usage example with options:

        file = GenericFileProvider(Faker()).generic_file(
            content="<html><body><p>{{text}}</p></body></html>",
            extension="html",
            prefix="zzz",
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = GenericFileProvider(Faker()).generic_file(
            content="<html><body><p>{{text}}</p></body></html>",
            extension="html",
            basename="index",
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
        )

    Usage example with AWS S3 storage:

        from faker_file.storages.aws_s3 import AWSS3Storage

        file = GenericFileProvider(Faker()).generic_file(
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
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a generic file with given content.

        :param content: File content. If given, used as is.
        :param extension: File extension.
        :param storage: Storage class. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
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

        data = {"content": content, "filename": filename}

        if raw:
            if isinstance(content, bytes):
                raw_content = BytesValue(content)
            else:
                raw_content = BytesValue(content.encode())
            raw_content.data = data
            return raw_content

        if isinstance(content, bytes):
            storage.write_bytes(filename, content)
        else:
            storage.write_text(
                filename,
                self.generator.pystr_format(content),
            )

        # Generic
        filename = StringValue(storage.relpath(filename))
        filename.data = data
        return filename
