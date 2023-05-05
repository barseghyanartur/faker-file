import xml.etree.ElementTree as ET
from typing import Optional, Sequence, Tuple, Union, overload

from faker import Faker
from faker.providers import BaseProvider

from ..base import BytesValue, FileMixin, StringValue
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

        from faker import Faker
        from faker_file.providers.xml_file import XmlFileProvider

        file = XmlFileProvider(Faker()).xml_file()

    Usage example with options:

        from faker_file.providers.xml_file import XmlFileProvider

        file = XmlFileProvider(Faker()).xml_file(
            prefix="zzz",
            num_rows=100,
            data_columns=(
                ("name", "{{name}}"),
                ("sentence", "{{sentence}}"),
                ("address", "{{address}}"),
            ),
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = XmlFileProvider(Faker()).xml_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            num_rows=100,
        )

    Usage example with template:

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

        file = XmlFileProvider(Faker()).xml_file(content=XML_TEMPLATE)
    """

    extension: str = "xml"

    def _generate_xml_element(
        self, element_name: str, content_template: str
    ) -> ET.Element:
        element = ET.Element(element_name)
        element.text = self.generator.pystr_format(content_template)
        return element

    @overload
    def xml_file(
        self: "XmlFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        root_element: str = "root",
        row_element: str = "row",
        data_columns: Sequence[Tuple[str, str]] = (
            ("name", "{{name}}"),
            ("address", "{{address}}"),
        ),
        num_rows: int = 10,
        content: Optional[str] = None,
        encoding: Optional[str] = None,
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
        data_columns: Sequence[Tuple[str, str]] = (
            ("name", "{{name}}"),
            ("address", "{{address}}"),
        ),
        num_rows: int = 10,
        content: Optional[str] = None,
        encoding: Optional[str] = None,
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
        data_columns: Sequence[Tuple[str, str]] = (
            ("name", "{{name}}"),
            ("address", "{{address}}"),
        ),
        num_rows: int = 10,
        content: Optional[str] = None,
        encoding: Optional[str] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate an XML file with random text."""

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
            root = ET.Element(root_element)
            for _ in range(num_rows):
                row = ET.SubElement(root, row_element)
                for col_name, col_template in data_columns:
                    row.append(
                        self._generate_xml_element(col_name, col_template)
                    )
            content = ET.tostring(root, encoding="utf-8").decode("utf-8")
        else:
            content = self.generator.pystr_format(content)

        data = {"content": content, "filename": filename}

        if raw:
            raw_content = BytesValue(content.encode("utf8"))
            raw_content.data = data
            return raw_content

        storage.write_text(filename, content, encoding=encoding)

        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        return file_name
