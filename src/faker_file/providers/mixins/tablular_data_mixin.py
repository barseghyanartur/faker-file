from typing import Dict, List, Optional, Union

from faker import Faker
from tablib import Dataset

from ...base import FileMixin, StringValue
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TabularDataMixin",)


class TabularDataMixin(FileMixin):
    """Tabular data mixin."""

    def _tabular_data_file(
        self: "TabularDataMixin",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        data_columns: Dict[str, str] = None,
        num_rows: int = 10,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
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
            default_data_columns = {
                "name": "{{name}}",
                "residency": "{{address}}",
            }
            data_columns: Union[List, Dict] = (
                data_columns if data_columns else default_data_columns
            )
            content = self.generator.json(
                data_columns=data_columns,
                num_rows=num_rows,
            )

        dataset = Dataset()
        dataset.load(content, format="json")

        storage.write_bytes(filename, dataset.export(self.extension))

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = {"content": content}
        return file_name
