import base64
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
from PIL import Image as PilImage
from reportlab.lib import colors
from reportlab.platypus import Image as PdfImage
from reportlab.platypus import Table as PdfTable
from reportlab.platypus import TableStyle as PdfTableStyle

from ..providers.jpeg_file import JpegFileProvider

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "docx_add_picture",
    "docx_add_table",
    "odt_add_picture",
    "odt_add_table",
    "pdf_pdfkit_add_picture",
    "pdf_pdfkit_add_table",
    "pdf_reportlab_add_picture",
    "pdf_reportlab_add_table",
)


def docx_add_table(provider, document, data, counter, **kwargs):
    """Callable responsible for the table generation."""
    table = document.add_table(
        kwargs.get("rows", 3),
        kwargs.get("cols", 4),
    )

    # Modifications of `data` is not required for generation
    # of the file, but is useful for when you want to get
    # the text content of the file.
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_table", {})
    data["content_modifiers"]["add_table"].setdefault(counter, [])

    for row in table.rows:
        for cell in row.cells:
            text = provider.generator.paragraph()
            cell.text = text
            # Useful when you want to get the text content of the file.
            data["content_modifiers"]["add_table"][counter].append(text)
            data["content"] += "\r\n" + text


def docx_add_picture(provider, document, data, counter, **kwargs):
    """Callable responsible for the picture generation."""
    jpeg_file = JpegFileProvider(provider.generator).jpeg_file(raw=True)
    document.add_picture(BytesIO(jpeg_file))

    # Modifications of `data` is not required for generation
    # of the file, but is useful for when you want to get
    # the text content of the file.
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_picture", {})
    data["content_modifiers"]["add_picture"].setdefault(counter, [])
    data["content_modifiers"]["add_picture"][counter].append(
        jpeg_file.data["content"]
    )
    data["content"] += "\r\n" + jpeg_file.data["content"]


def odt_add_table(provider, document, data, counter, **kwargs):
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


def odt_add_picture(provider, document, data, counter, **kwargs):
    """Callable responsible for the picture generation."""
    width = kwargs.get("width", "10cm")
    height = kwargs.get("height", "5cm")
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

    # Modifications of `data` is not required for generation
    # of the file, but is useful for when you want to get
    # the text content of the file.
    data["content"] += "\r\n" + jpeg_file.data["content"]
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_picture", {})
    data["content_modifiers"]["add_picture"].setdefault(counter, [])
    data["content_modifiers"]["add_picture"][counter].append(
        jpeg_file.data["content"]
    )


def create_data_url(image_bytes, image_format):
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:image/{image_format};base64,{encoded_image}"


def pdf_pdfkit_add_table(provider, document, data, counter, **kwargs):
    """Callable responsible for the table generation."""
    rows = kwargs.get("rows", 3)
    cols = kwargs.get("cols", 4)

    # Begin the HTML table
    table_html = "<table>"

    for row_num in range(rows):
        table_html += "<tr>"

        for col_num in range(cols):
            text = provider.generator.paragraph()
            table_html += f"<td>{text}</td>"

            # Modifications of `data` is not required for generation
            # of the file, but is useful for when you want to get
            # the text content of the file.
            data.setdefault("content_modifiers", {})
            data["content_modifiers"].setdefault("add_table", {})
            data["content_modifiers"]["add_table"].setdefault(counter, [])
            data["content_modifiers"]["add_table"][counter].append(text)

        table_html += "</tr>"

    # End the HTML table
    table_html += "</table>"

    document += "\r\n" + table_html


def pdf_pdfkit_add_picture(provider, document, data, counter, **kwargs):
    """Callable responsible for the picture generation."""
    jpeg_file = JpegFileProvider(provider.generator).jpeg_file(raw=True)
    data_url = create_data_url(jpeg_file, "jpg")
    document += f"<img src='{data_url}' alt='Inline Image' />"

    # Modifications of `data` is not required for generation
    # of the file, but is useful for when you want to get
    # the text content of the file.
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_picture", {})
    data["content_modifiers"]["add_picture"].setdefault(counter, [])
    data["content_modifiers"]["add_picture"][counter].append(
        jpeg_file.data["content"]
    )
    data["content"] += "\r\n" + jpeg_file.data["content"]


def pdf_reportlab_add_table(provider, story, data, counter, **kwargs):
    """
    Callable responsible for the table generation when using reportlab
    PDF generator.
    """
    rows = kwargs.get("rows", 3)
    cols = kwargs.get("cols", 4)

    # Define your table headers
    headers = [f"Header {i + 1}" for i in range(cols)]

    # Generate the rest of the table data
    table_data = [
        [provider.generator.word() for _ in range(cols)] for _ in range(rows)
    ]

    # Add the headers to the table data
    table_data.insert(0, headers)

    # Modifications of `data` is not required for generation
    # of the file, but is useful for when you want to get
    # the text content of the file.
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_table", {})
    data["content_modifiers"]["add_table"].setdefault(counter, [])
    data["content_modifiers"]["add_table"][counter].append(
        "\n".join([" ".join(row) for row in table_data])
    )

    # Create the table object
    table = PdfTable(table_data)

    # Apply table styles
    table.setStyle(
        PdfTableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 14),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
    )

    # Add the table to the document and build it
    story.append(table)


def pdf_reportlab_add_picture(provider, story, data, counter, **kwargs):
    """
    Callable responsible for the picture generation when using reportlab
    PDF generator.
    """
    jpeg_file = JpegFileProvider(provider.generator).jpeg_file(raw=True)

    # Create a BytesIO object and load the image data
    with BytesIO(jpeg_file) as input_stream:
        pil_image = PilImage.open(input_stream)

        # Resize the image
        new_width = 400
        new_height = 400
        pil_image = pil_image.resize((new_width, new_height))

        # Create a BytesIO object outside the 'with' statement
        output_stream = BytesIO()
        pil_image.save(output_stream, format="JPEG")
        output_stream.seek(0)  # Move to the start of the stream

        # Now you can use output_stream as your image data
        img = PdfImage(output_stream)
        img.width = new_width
        img.height = new_height
        story.append(img)

    # Modifications of `data` is not required for generation
    # of the file, but is useful for when you want to get
    # the text content of the file.
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_picture", {})
    data["content_modifiers"]["add_picture"].setdefault(counter, [])
    data["content_modifiers"]["add_picture"][counter].append(
        jpeg_file.data["content"]
    )
    data["content"] += "\r\n" + jpeg_file.data["content"]
