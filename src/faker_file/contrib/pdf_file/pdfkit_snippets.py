import base64

from ...base import DEFAULT_FORMAT_FUNC

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
    """Callable responsible for the table generation using pdfkit."""
    rows = kwargs.get("rows", 3)
    cols = kwargs.get("cols", 4)

    # Begin the HTML table
    table_html = "<table>"

    for row_num in range(rows):
        table_html += "<tr>"

        for col_num in range(cols):
            text = provider.generator.paragraph()
            table_html += f"<td>{text}</td>"

            # Meta-data
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
    """Callable responsible for the picture generation using pdfkit."""
    png_raw = provider.generator.image()
    data_url = create_data_url(png_raw, "png")
    document += f"<img src='{data_url}' alt='Inline Image' />"


def add_page_break(
    provider,
    generator,
    document,
    data,
    counter,
    **kwargs,
):
    """Callable responsible for the page break insertion using pdfkit."""
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
    """Callable responsible for paragraph generation using pdfkit."""
    content = kwargs.get("content", None)
    max_nb_chars = kwargs.get("content", 5_000)
    wrap_chars_after = kwargs.get("wrap_chars_after", None)
    format_func = kwargs.get("format_func", DEFAULT_FORMAT_FUNC)

    if content:
        _content = provider._generate_text_content(
            max_nb_chars=max_nb_chars,
            wrap_chars_after=wrap_chars_after,
            content=content,
            format_func=format_func,
        )
    else:
        _content = provider.generator.text(max_nb_chars=5_000)

    paragraph_html = f"<div><p>{_content}</p></div>"
    document += "\r\n" + paragraph_html

    # Meta-data
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_paragraph", {})
    data["content_modifiers"]["add_paragraph"].setdefault(counter, [])
    data["content_modifiers"]["add_paragraph"][counter].append(_content)
    data["content"] += "\r\n" + _content
