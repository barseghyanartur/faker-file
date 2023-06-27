from odf.draw import Frame, Image
from odf.style import (
    Style,
    TableCellProperties,
    TableColumnProperties,
    TableRowProperties,
)
from odf.table import Table, TableCell, TableColumn, TableRow
from odf.text import P

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "add_picture",
    "add_table",
)


def add_table(provider, document, data, counter, **kwargs):
    """Callable responsible for the table generation."""
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

    # Modifications of `data` is not required for generation
    # of the file, but is useful for when you want to get
    # the text content of the file.
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_table", {})
    data["content_modifiers"]["add_table"].setdefault(counter, [])

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
            # Useful when you want to get the text content of the file.
            data["content_modifiers"]["add_table"][counter].append(text)
            data["content"] += "\r\n" + text

    document.text.addElement(table)


def add_picture(provider, document, data, counter, **kwargs):
    """Callable responsible for the picture generation."""
    width = kwargs.get("width", "10cm")
    height = kwargs.get("height", "5cm")
    paragraph = P()
    document.text.addElement(paragraph)
    png_raw = provider.generator.image()
    image_frame = Frame(
        width=width,
        height=height,
        x="56pt",
        y="56pt",
        anchortype="paragraph",
    )
    href = document.addPicture(filename="image.png", content=png_raw)
    image_frame.addElement(Image(href=href))
    paragraph.addElement(image_frame)

    # # Modifications of `data` is not required for generation
    # # of the file, but is useful for when you want to get
    # # the text content of the file.
    # data["content"] += "\r\n" + jpeg_file.data["content"]
    # data.setdefault("content_modifiers", {})
    # data["content_modifiers"].setdefault("add_picture", {})
    # data["content_modifiers"]["add_picture"].setdefault(counter, [])
    # data["content_modifiers"]["add_picture"][counter].append(
    #     jpeg_file.data["content"]
    # )
