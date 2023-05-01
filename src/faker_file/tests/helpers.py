from io import BytesIO

from odf.draw import Frame, Image
from odf.style import (
    Style,
    TableCellProperties,
    TableColumnProperties,
    TableRowProperties,
)
from odf.table import Table, TableCell, TableColumn, TableRow
from odf.text import P

from ..providers.jpeg_file import JpegFileProvider

__all__ = (
    "docx_add_table",
    "docx_add_picture",
    "odt_add_table",
    "odt_add_picture",
)


def docx_add_table(provider, document, data, counter, **kwargs):
    table = document.add_table(
        kwargs.get("rows", 3),
        kwargs.get("cols", 4),
    )
    if "content_modifiers" not in data:
        data["content_modifiers"] = {}
    if "add_table" not in data["content_modifiers"]:
        data["content_modifiers"]["add_table"] = {}
    if counter not in data["content_modifiers"]["add_table"]:
        data["content_modifiers"]["add_table"][counter] = []

    for row in table.rows:
        for cell in row.cells:
            text = provider.generator.paragraph()
            cell.text = text
            data["content_modifiers"]["add_table"][counter].append(text)
            data["content"] += "\r\n" + text


def docx_add_picture(provider, document, data, counter, **kwargs):
    jpeg_file = JpegFileProvider(provider.generator).jpeg_file(raw=True)
    document.add_picture(BytesIO(jpeg_file))
    if "content_modifiers" not in data:
        data["content_modifiers"] = {}
    if "add_picture" not in data["content_modifiers"]:
        data["content_modifiers"]["add_picture"] = {}
    if counter not in data["content_modifiers"]["add_picture"]:
        data["content_modifiers"]["add_picture"][counter] = []

    data["content_modifiers"]["add_picture"][counter].append(
        jpeg_file.data["content"]
    )
    data["content"] += "\r\n" + jpeg_file.data["content"]


def odt_add_table(provider, document, data, counter, **kwargs):
    rows = kwargs.get("rows", 3)
    cols = kwargs.get("cols", 4)
    table_col_style = Style(name="TableColumn", family="table-column")
    table_col_style.addElement(TableColumnProperties(columnwidth="2cm"))
    document.automaticstyles.addElement(table_col_style)

    table_row_style = Style(name="TableRow", family="table-row")
    table_row_style.addElement(TableRowProperties(rowheight="1cm"))
    document.automaticstyles.addElement(table_row_style)

    table_cell_style = Style(name="TableCell", family="table-cell")
    table_cell_style.addElement(
        TableCellProperties(padding="0.1cm", border="0.05cm solid #000000")
    )
    document.automaticstyles.addElement(table_cell_style)

    if "content_modifiers" not in data:
        data["content_modifiers"] = {}
    if "add_table" not in data["content_modifiers"]:
        data["content_modifiers"]["add_table"] = {}
    if counter not in data["content_modifiers"]["add_table"]:
        data["content_modifiers"]["add_table"][counter] = []

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


def odt_add_picture(
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
    if "content_modifiers" not in data:
        data["content_modifiers"] = {}
    if "add_picture" not in data["content_modifiers"]:
        data["content_modifiers"]["add_picture"] = {}
    if counter not in data["content_modifiers"]["add_picture"]:
        data["content_modifiers"]["add_picture"][counter] = []

    data["content_modifiers"]["add_picture"][counter].append(
        jpeg_file.data["content"]
    )
