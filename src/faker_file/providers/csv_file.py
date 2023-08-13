from typing import Callable, Optional, Sequence, Tuple, Union, overload

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
__all__ = ("CsvFileProvider",)


FAKER = Faker()


class CsvFileProvider(BaseProvider, FileMixin):
    """CSV file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.csv_file import CsvFileProvider

        FAKER = Faker()
        FAKER.add_provider(CsvFileProvider)

        file = FAKER.csv_file()

    Usage example with options:

    .. code-block:: python

        file = FAKER.csv_file(
            prefix="zzz",
            num_rows=100,
            data_columns=('{{name}}', '{{sentence}}', '{{address}}'),
            include_row_ids=True,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

    .. code-block:: python

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.csv_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            num_rows=100,
        )
    """

    extension: str = "csv"

    @overload
    def csv_file(
        self: "CsvFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, ...] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
        content: Optional[str] = None,
        encoding: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def csv_file(
        self: "CsvFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, ...] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
        content: Optional[str] = None,
        encoding: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def csv_file(
        self: "CsvFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, ...] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
        content: Optional[str] = None,
        encoding: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a CSV file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param header: The ``header`` argument expects a list or a tuple of
            strings that will serve as the header row if supplied.
        :param data_columns: The ``data_columns`` argument expects a list or a
            tuple of string tokens, and these string tokens will be passed to
            :meth:`parse()
            <faker.providers.python.Provider.parse>`
            for data generation. Argument Groups are used to pass arguments
            to the provider methods. Both ``header`` and ``data_columns`` must
            be of the same length.
        :param num_rows: The ``num_rows`` argument controls how many rows of
            data to generate, and the ``include_row_ids`` argument may be set
            to ``True`` to include a sequential row ID column.
        :param include_row_ids:
        :param content: File content. If given, used as is.
        :param encoding: Encoding.
        :param format_func: Callable responsible for formatting template
            strings.
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
            content = self.generator.csv(
                header=header,
                data_columns=data_columns,
                num_rows=num_rows,
                include_row_ids=include_row_ids,
            )
        else:
            content = format_func(self.generator, content)

        data = {"content": content, "filename": filename, "storage": storage}

        if raw:
            raw_content = BytesValue(content.encode("utf8"))
            raw_content.data = data
            return raw_content

        storage.write_text(filename, content, encoding=encoding)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
