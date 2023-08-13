import xml.etree.ElementTree as ET
from typing import Callable, Dict, Optional, Union, overload

from faker import Faker
from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.python import Provider

from ..base import DEFAULT_FORMAT_FUNC, BytesValue, FileMixin, StringValue
from ..constants import DEFAULT_XML_DATA_COLUMNS
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("XmlFileProvider",)

FAKER = Faker()


class XmlFileProvider(BaseProvider, FileMixin):
    """XML file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.xml_file import XmlFileProvider

        FAKER = Faker()
        FAKER.add_provider(XmlFileProvider)

        file = FAKER.xml_file()

    Usage example with options:

    .. code-block:: python

        file = FAKER.xml_file(
            prefix="zzz",
            num_rows=100,
            data_columns={
                "name": "{{name}}",
                "sentence": "{{sentence}}",
                "address": "{{address}}",
            },
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

    .. code-block:: python

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.xml_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            num_rows=100,
        )

    Usage example with template:

    .. code-block:: python

        XML_TEMPLATE = '''
        <books>
            <book>
                <name>{{sentence}}</name>
                <description>{{paragraph}}</description>
                <isbn>{{isbn13}}</isbn>
            </book>
            <book>
                <name>{{sentence}}</name>
                <description>{{paragraph}}</description>
                <isbn>{{isbn13}}</isbn>
            </book>
            <book>
                <name>{{sentence}}</name>
                <description>{{paragraph}}</description>
                <isbn>{{isbn13}}</isbn>
            </book>
        </books>
        '''

        file = FAKER.xml_file(content=XML_TEMPLATE)
    """

    extension: str = "xml"

    def _generate_xml_element(
        self,
        element_name: str,
        content_template: str,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
    ) -> ET.Element:
        element = ET.Element(element_name)
        element.text = format_func(self.generator, content_template)
        return element

    @overload
    def xml_file(
        self: "XmlFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        root_element: str = "root",
        row_element: str = "row",
        data_columns: Optional[Dict[str, str]] = None,
        num_rows: int = 10,
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
    def xml_file(
        self: "XmlFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        root_element: str = "root",
        row_element: str = "row",
        data_columns: Optional[Dict[str, str]] = None,
        num_rows: int = 10,
        content: Optional[str] = None,
        encoding: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def xml_file(
        self,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        root_element: str = "root",
        row_element: str = "row",
        data_columns: Optional[Dict[str, str]] = None,
        num_rows: int = 10,
        content: Optional[str] = None,
        encoding: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate an XML file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param root_element: Root XML element.
        :param row_element: Row XML element.
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
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param encoding: Encoding.
        :param format_func: Callable responsible for formatting template
            strings.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
        """

        if storage is None:
            storage = FileSystemStorage()

        filename = storage.generate_filename(
            extension=self.extension,
            prefix=prefix,
            basename=basename,
        )

        if self.generator is None:
            self.generator = Faker()

        if content is None:
            data_columns = (
                data_columns if data_columns else DEFAULT_XML_DATA_COLUMNS
            )
            root = ET.Element(root_element)
            for _ in range(num_rows):
                row = ET.SubElement(root, row_element)
                for col_name, col_template in data_columns.items():
                    row.append(
                        self._generate_xml_element(
                            col_name, col_template, format_func=format_func
                        )
                    )
            content = ET.tostring(root, encoding="utf-8").decode("utf-8")
        else:
            content = format_func(self.generator, content)

        data = {"content": content, "filename": filename, "storage": storage}

        if raw:
            raw_content = BytesValue(content.encode("utf8"))
            raw_content.data = data
            return raw_content

        storage.write_text(filename, content, encoding=encoding)

        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
