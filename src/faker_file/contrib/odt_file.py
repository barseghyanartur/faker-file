from odf.draw import Frame, Image
from odf.style import (
    ParagraphProperties,
    Style,
    TableCellProperties,
    TableColumnProperties,
    TableRowProperties,
)
from odf.table import Table, TableCell, TableColumn, TableRow
from odf.text import H, P

from ..base import DEFAULT_FORMAT_FUNC

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "add_h1_heading",
    "add_h2_heading",
    "add_h3_heading",
    "add_h4_heading",
    "add_h5_heading",
    "add_h6_heading",
    "add_heading",
    "add_page_break",
    "add_paragraph",
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
    image = kwargs.get("image", provider.generator.image())
    image_frame = Frame(
        width=width,
        height=height,
        x="56pt",
        y="56pt",
        anchortype="paragraph",
    )
    href = document.addPicture(filename="image.png", content=image)
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


# Define a style for a page break
page_break_style = Style(name="PageBreak", family="paragraph")
page_break_style.addElement(ParagraphProperties(breakbefore="page"))


def add_page_break(provider, document, data, counter, **kwargs):
    """Callable responsible for page break generation."""
    # Insert a page break
    document.styles.addElement(page_break_style)
    # Insert a page break
    page_break = P(stylename=page_break_style)
    document.text.addElement(page_break)


def add_paragraph(provider, document, data, counter, **kwargs):
    """Callable responsible for the paragraph generation."""
    content = kwargs.get("content", None)
    max_nb_chars = kwargs.get("content", 5_000)
    wrap_chars_after = kwargs.get("wrap_chars_after", None)
    format_func = kwargs.get("format_func", DEFAULT_FORMAT_FUNC)

    _content = provider._generate_text_content(
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        format_func=format_func,
    )
    # Add some text to the first page
    paragraph = P(text=_content)
    document.text.addElement(paragraph)

    # Meta-data
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_paragraph", {})
    data["content_modifiers"]["add_paragraph"].setdefault(counter, [])
    data["content_modifiers"]["add_paragraph"][counter].append(_content)
    data["content"] += "\r\n" + _content


def add_heading(provider, document, data, counter, **kwargs):
    """Callable responsible for the heading generation."""
    content = kwargs.get("content", None)
    max_nb_chars = kwargs.get("content", 30)
    wrap_chars_after = kwargs.get("wrap_chars_after", None)
    format_func = kwargs.get("format_func", DEFAULT_FORMAT_FUNC)
    level = kwargs.get("level", 1)

    _content = provider._generate_text_content(
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        format_func=format_func,
    )
    # Add a heading to the document
    heading = H(outlinelevel=level, text=_content)
    document.text.addElement(heading)

    # Meta-data
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_heading", {})
    data["content_modifiers"]["add_heading"].setdefault(counter, [])
    data["content_modifiers"]["add_heading"][counter].append(_content)
    data["content"] += "\r\n" + _content


def add_h1_heading(provider, document, data, counter, **kwargs):
    """Callable responsible for the h1 heading generation."""
    return add_heading(provider, document, data, counter, level=1, **kwargs)


def add_h2_heading(provider, document, data, counter, **kwargs):
    """Callable responsible for the h2 heading generation."""
    return add_heading(provider, document, data, counter, level=2, **kwargs)


def add_h3_heading(provider, document, data, counter, **kwargs):
    """Callable responsible for the h3 heading generation."""
    return add_heading(provider, document, data, counter, level=3, **kwargs)


def add_h4_heading(provider, document, data, counter, **kwargs):
    """Callable responsible for the h4 heading generation."""
    return add_heading(provider, document, data, counter, level=4, **kwargs)


def add_h5_heading(provider, document, data, counter, **kwargs):
    """Callable responsible for the h5 heading generation."""
    return add_heading(provider, document, data, counter, level=5, **kwargs)


def add_h6_heading(provider, document, data, counter, **kwargs):
    """Callable responsible for the h6 heading generation."""
    return add_heading(provider, document, data, counter, level=6, **kwargs)
