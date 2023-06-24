import base64

from faker_file.providers.jpeg_file import JpegFileProvider

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "add_page_break",
    "add_paragraph",
    "add_picture",
    "add_table",
)


def create_data_url(image_bytes: bytes, image_format: str) -> str:
    """Create data URL."""
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:image/{image_format};base64,{encoded_image}"


def add_table(
    provider,
    generator,
    document,
    data,
    counter,
    **kwargs,
):
    """Add table function."""
    rows = kwargs.get("rows", 3)
    cols = kwargs.get("cols", 4)

    # Begin the HTML table
    table_html = "<table>"

    for row_num in range(rows):
        table_html += "<tr>"

        for col_num in range(cols):
            text = provider.generator.paragraph()
            table_html += f"<td>{text}</td>"

            data.setdefault("content_modifiers", {})
            data["content_modifiers"].setdefault("add_table", {})
            data["content_modifiers"]["add_table"].setdefault(counter, [])
            data["content_modifiers"]["add_table"][counter].append(text)

        table_html += "</tr>"

    # End the HTML table
    table_html += "</table>"

    document += "\r\n" + table_html


def add_picture(
    provider,
    generator,
    document,
    data,
    counter,
    **kwargs,
):
    """Add picture function."""
    jpeg_file = JpegFileProvider(provider.generator).jpeg_file(raw=True)
    data_url = create_data_url(jpeg_file, "jpg")
    document += f"<img src='{data_url}' alt='Inline Image' />"
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_picture", {})
    data["content_modifiers"]["add_picture"].setdefault(counter, [])
    data["content_modifiers"]["add_picture"][counter].append(
        jpeg_file.data["content"]
    )
    data["content"] += "\r\n" + jpeg_file.data["content"]


def add_page_break(
    provider,
    generator,
    document,
    data,
    counter,
    **kwargs,
):
    """Add page break."""
    page_break_html = "<div style='page-break-before: always;'></div>"
    document += "\r\n" + page_break_html


def add_paragraph(
    provider,
    generator,
    document,
    data,
    counter,
    **kwargs,
):
    """Add a paragraph."""
    content = provider.generator.text(max_nb_chars=5_000)
    paragraph_html = f"<div><p>{content}</p></div>"
    document += "\r\n" + paragraph_html
