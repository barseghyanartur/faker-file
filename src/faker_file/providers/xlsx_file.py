from typing import Dict, Optional

from faker.providers import BaseProvider

from ..base import StringValue
from ..storages.base import BaseStorage
from .mixins.tablular_data_mixin import TabularDataMixin

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("XlsxFileProvider",)


class XlsxFileProvider(BaseProvider, TabularDataMixin):
    """XLSX file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.xlsx_file import XlsxFileProvider

        file = XlsxFileProvider(Faker()).xlsx_file()

    Usage example with options:

        from faker import Faker
        from faker_file.providers.xlsx_file import XlsxFileProvider

        file = XlsxFileProvider(Faker()).xlsx_file(
            prefix="zzz",
            num_rows=100,
            data_columns={
                "name": "{{name}}",
                "residency": "{{address}}",
            },
            include_row_ids=True,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = XlsxFileProvider(Faker()).xlsx_file(
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

    extension: str = "xlsx"

    def xlsx_file(
        self: "XlsxFileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        data_columns: Dict[str, str] = None,
        num_rows: int = 10,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a XLSX file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
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
        :param prefix: File name prefix.
        :param content: List of dicts with content (JSON-like format).
            If given, used as is.
        :return: Relative path (from root directory) of the generated file.
        """
        return self._tabular_data_file(
            storage=storage,
            prefix=prefix,
            data_columns=data_columns,
            num_rows=num_rows,
            content=content,
            **kwargs,
        )
