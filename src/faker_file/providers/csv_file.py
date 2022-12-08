import os
from typing import Optional, Sequence, Tuple

from faker import Faker
from faker.providers import BaseProvider

from ..base import DEFAULT_REL_PATH, FileMixin, StringValue

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("CsvFileProvider",)


FAKER = Faker()


class CsvFileProvider(BaseProvider, FileMixin):
    """CSV file provider.

    Usage example:

        from faker_file.providers.csv_file import CsvFileProvider

        file = CsvFileProvider(None).csv_file()

    Usage example with options:

        from faker_file.providers.csv_file import CsvFileProvider

        file = CsvFileProvider(None).csv_file(
            prefix="zzz",
            num_rows=100,
            data_columns=('{{name}}', '{{sentence}}', '{{address}}'),
            include_row_ids=True,
        )
    """

    extension: str = "csv"

    def csv_file(
        self: "CsvFileProvider",
        root_path: str = None,
        rel_path: str = DEFAULT_REL_PATH,
        prefix: Optional[str] = None,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a CSV file with random text.

        :param root_path: Path of your files root directory (in case of Django
            it would be `settings.MEDIA_ROOT`).
        :param rel_path: Relative path (from root directory).
        :param header: The ``header`` argument expects a list or a tuple of
            strings that will serve as the header row if supplied.
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
        :param include_row_ids:
        :param prefix: File name prefix.
        :param content: File content. If given, used as is.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        file_name = self._generate_filename(
            root_path=root_path,
            rel_path=rel_path,
            prefix=prefix,
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
            content = self.generator.pystr_format(content)

        with open(file_name, "w") as fakefile:
            fakefile.write(content)

        # Generic
        file_name = StringValue(os.path.relpath(file_name, root_path))
        file_name.data = {"content": content}
        return file_name
