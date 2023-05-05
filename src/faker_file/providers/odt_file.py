from io import BytesIO
from typing import Optional, Union, overload

from faker.providers import BaseProvider
from odf.opendocument import OpenDocumentText
from odf.text import P

from ..base import BytesValue, DynamicTemplate, FileMixin, StringValue
from ..constants import DEFAULT_TEXT_MAX_NB_CHARS
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("OdtFileProvider",)


class OdtFileProvider(BaseProvider, FileMixin):
    """ODT file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.odt_file import OdtFileProvider

        FAKER = Faker()

        file = OdtFileProvider(FAKER).odt_file()

    Usage example with options:

        file = OdtFileProvider(FAKER).odt_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = OdtFileProvider(FAKER).odt_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with content modifiers:

        from faker_file.base import DynamicTemplate
        from faker_file.providers.jpeg_file import JpegFileProvider
        from odf.draw import Frame, Image
        from odf.style import (
            Style, TextProperties,
            TableColumnProperties,
            TableRowProperties,
            TableCellProperties,
            GraphicProperties,
        )
        from odf.table import Table, TableRow, TableCell, TableColumn
        from odf.text import P

        def add_table(provider, document, data, counter, **kwargs):
            table = Table()
            rows = kwargs.get("rows", 3)
            cols = kwargs.get("cols", 4)
            table_col_style = Style(name="TableColumn", family="table-column")
            table_col_style.addElement(
                TableColumnProperties(columnwidth="2cm")
            )
            document.automaticstyles.addElement(table_col_style)

            table_row_style = Style(name="TableRow", family="table-row")
            table_row_style.addElement(TableRowProperties(rowheight="1cm"))
            document.automaticstyles.addElement(table_row_style)

            data.setdefault("content_modifiers", {})
            data["content_modifiers"].setdefault("add_table", {})
            data["content_modifiers"]["add_table"].setdefault(counter, [])

            table_cell_style = Style(name="TableCell", family="table-cell")
            table_cell_style.addElement(
                TableCellProperties(
                    padding="0.1cm", border="0.05cm solid #000000"
                )
            )
            document.automaticstyles.addElement(table_cell_style)

            # Create table
            table = Table()
            for i in range(rows):
                table.addElement(TableColumn(stylename=table_col_style))

            for row in range(cols):
                tr = TableRow(stylename=table_row_style)
                table.addElement(tr)
                for col in range(4):
                    tc = TableCell(stylename=table_cell_style)
                    tr.addElement(tc)
                    text = provider.generator.paragraph()
                    p = P(text=text)
                    tc.addElement(p)
                    data["content_modifiers"]["add_table"][counter].append(text)
                    data["content"] += "\r\n" + text

            document.text.addElement(table)

        def add_picture(
            provider,
            document,
            data,
            counter,
            width="10cm",
            height="5cm",
            **kwargs,
        ):
            paragraph = P()
            document.text.addElement(paragraph)
            jpeg_file = JpegFileProvider(provider.generator).jpeg_file()
            image_data = jpeg_file.data["content"]
            image_frame = Frame(
                width=width,
                height=height,
                x="56pt",
                y="56pt",
                anchortype="paragraph",
            )
            href = document.addPicture(jpeg_file.data["filename"])
            image_frame.addElement(Image(href=href))
            paragraph.addElement(image_frame)

            data["content"] += "\r\n" + jpeg_file.data["content"]
            data.setdefault("content_modifiers", {})
            data["content_modifiers"].setdefault("add_picture", {})
            data["content_modifiers"]["add_picture"].setdefault(counter, [])

            data["content_modifiers"]["add_picture"][counter].append(
                jpeg_file.data["content"]
            )

        file = OdtFileProvider(FAKER).odt_file(
            content=DynamicTemplate([(add_table, {}), (add_picture, {})])
        )
    """

    extension: str = "odt"

    @overload
    def odt_file(
        self: "OdtFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[Union[str, DynamicTemplate]] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def odt_file(
        self: "OdtFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[Union[str, DynamicTemplate]] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def odt_file(
        self: "OdtFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[Union[str, DynamicTemplate]] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate an ODT file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
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

        if isinstance(content, DynamicTemplate):
            _content = ""
        else:
            _content = self._generate_text_content(
                max_nb_chars=max_nb_chars,
                wrap_chars_after=wrap_chars_after,
                content=content,
            )
        data = {"content": _content, "filename": filename}

        with BytesIO() as _fake_file:
            document = OpenDocumentText()
            if _content:
                document.text.addElement(P(text=_content))
            elif isinstance(content, DynamicTemplate):
                for counter, (ct_modifier, ct_modifier_kwargs) in enumerate(
                    content.content_modifiers
                ):
                    ct_modifier(
                        self,
                        document,
                        data,
                        counter,
                        **ct_modifier_kwargs,
                    )

            document.save(_fake_file)

            if raw:
                raw_content = BytesValue(_fake_file.getvalue())
                raw_content.data = data
                return raw_content

            storage.write_bytes(filename, _fake_file.getvalue())

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        return file_name
