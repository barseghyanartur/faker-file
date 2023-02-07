from typing import Dict, Optional, Union, overload

from faker import Faker
from tablib import Dataset

from ...base import BytesValue, FileMixin, StringValue
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TabularDataMixin",)


class TabularDataMixin(FileMixin):
    """Tabular data mixin."""

    @overload
    def _tabular_data_file(
        self: "TabularDataMixin",
        storage: Optional[BaseStorage] = None,
        prefix: Optional[str] = None,
        data_columns: Optional[Dict[str, str]] = None,
        num_rows: int = 10,
        content: Optional[str] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def _tabular_data_file(
        self: "TabularDataMixin",
        storage: Optional[BaseStorage] = None,
        prefix: Optional[str] = None,
        data_columns: Optional[Dict[str, str]] = None,
        num_rows: int = 10,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def _tabular_data_file(
        self: "TabularDataMixin",
        storage: Optional[BaseStorage] = None,
        prefix: Optional[str] = None,
        data_columns: Optional[Dict[str, str]] = None,
        num_rows: int = 10,
        content: Optional[str] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a tabular data file with random text.

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
            prefix=prefix,
            extension=self.extension,
        )

        if self.generator is None:
            self.generator = Faker()

        # Specific
        if content is None:
            default_data_columns = {
                "name": "{{name}}",
                "residency": "{{address}}",
            }
            data_columns = (
                data_columns if data_columns else default_data_columns
            )
            content = self.generator.json(
                data_columns=data_columns,
                num_rows=num_rows,
            )

        data = {"content": content, "filename": filename}

        dataset = Dataset()
        dataset.load(content, format="json")

        _raw_content = dataset.export(self.extension)

        if raw:
            raw_content = BytesValue(_raw_content)
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, _raw_content)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        return file_name
