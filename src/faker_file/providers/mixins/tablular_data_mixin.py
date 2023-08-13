from typing import Callable, Dict, Optional, Union, overload

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider
from tablib import Dataset

from ...base import DEFAULT_FORMAT_FUNC, BytesValue, FileMixin, StringValue
from ...registry import FILE_REGISTRY
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
    def _tabular_data_file(
        self: "TabularDataMixin",
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

    def _tabular_data_file(
        self: "TabularDataMixin",
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
        """Generate a tabular data file with random text.

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

        data = {"content": content, "filename": filename, "storage": storage}

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
        FILE_REGISTRY.add(file_name)
        return file_name
