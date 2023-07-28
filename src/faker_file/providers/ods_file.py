from typing import Callable, Dict, Optional, Union, overload

from faker import Faker
from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.python import Provider

from ..base import DEFAULT_FORMAT_FUNC, BytesValue, StringValue
from ..storages.base import BaseStorage
from .mixins.tablular_data_mixin import TabularDataMixin

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("OdsFileProvider",)


class OdsFileProvider(BaseProvider, TabularDataMixin):
    """ODS file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.ods_file import OdsFileProvider

        FAKER = Faker()
        FAKER.add_provider(OdsFileProvider)

        file = FAKER.ods_file()

    Usage example with options:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.ods_file import OdsFileProvider

        file = FAKER.ods_file(
            prefix="zzz",
            num_rows=100,
            data_columns={
                "name": "{{name}}",
                "residency": "{{address}}",
            },
            include_row_ids=True,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

    .. code-block:: python

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.ods_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            num_rows=100,
            data_columns={
                "name": "{{name}}",
                "residency": "{{address}}",
            },
            include_row_ids=True,
        )
    """

    extension: str = "ods"

    @overload
    def ods_file(
        self: "OdsFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        data_columns: Optional[Dict[str, str]] = None,
        num_rows: int = 10,
        content: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def ods_file(
        self: "OdsFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        data_columns: Optional[Dict[str, str]] = None,
        num_rows: int = 10,
        content: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def ods_file(
        self: "OdsFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        data_columns: Optional[Dict[str, str]] = None,
        num_rows: int = 10,
        content: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate an ODS file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param data_columns: The ``data_columns`` argument expects a list or a
            tuple of string tokens, and these string tokens will be passed to
            :meth:`pystr_format()
            <faker.providers.python.Provider.pystr_format>`
            for data generation. Argument Groups are used to pass arguments
            to the provider methods. Both ``header`` and ``data_columns`` must
            be of the same length.
        :param num_rows: The ``num_rows`` argument controls how many rows of
            data to generate, and the ``include_row_ids`` argument may be set
            to ``True`` to include a sequential row ID column.
        :param content: List of dicts with content (JSON-like format).
            If given, used as is.
        :param format_func: Callable responsible for formatting template
            strings.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
        """
        return self._tabular_data_file(
            storage=storage,
            basename=basename,
            prefix=prefix,
            data_columns=data_columns,
            num_rows=num_rows,
            content=content,
            format_func=format_func,
            raw=raw,
            **kwargs,
        )
