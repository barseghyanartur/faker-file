import base64

from pdf2image import convert_from_bytes
from weasyprint import HTML

from ...base import DEFAULT_FORMAT_FUNC

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"


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

    pdf_bytes = HTML(string=generator.wrap(table_html)).write_pdf()
    generator.pages.extend(convert_from_bytes(pdf_bytes))


def add_picture(
    provider,
    generator,
    document,
    data,
    counter,
    **kwargs,
):
    """Callable responsible for the picture generation using pdfkit."""
    image = kwargs.get("image", provider.generator.image())
    data_url = create_data_url(image, "png")
    image_html = f"<img src='{data_url}' alt='Inline Image' />"

    pdf_bytes = HTML(string=generator.wrap(image_html)).write_pdf()
    generator.pages.extend(convert_from_bytes(pdf_bytes))


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
    pdf_bytes = HTML(string=generator.wrap(page_break_html)).write_pdf()
    generator.pages.extend(convert_from_bytes(pdf_bytes))


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

    _content = provider._generate_text_content(
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        format_func=format_func,
    )

    paragraph_html = f"<div><p>{_content}</p></div>"
    pdf_bytes = HTML(string=generator.wrap(paragraph_html)).write_pdf()
    generator.pages.extend(convert_from_bytes(pdf_bytes))

    # Meta-data
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_paragraph", {})
    data["content_modifiers"]["add_paragraph"].setdefault(counter, [])
    data["content_modifiers"]["add_paragraph"][counter].append(_content)
    data["content"] += "\r\n" + _content


def add_heading(
    provider,
    generator,
    document,
    data,
    counter,
    **kwargs,
):
    """Callable responsible for heading generation using pdfkit."""
    content = kwargs.get("content", None)
    max_nb_chars = kwargs.get("max_nb_chars", 30)
    wrap_chars_after = kwargs.get("wrap_chars_after", None)
    format_func = kwargs.get("format_func", DEFAULT_FORMAT_FUNC)
    level = kwargs.get("level", 1)
    if level < 1 or level > 6:
        level = 1

    _content = provider._generate_text_content(
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        format_func=format_func,
    )

    heading_html = f"<div><h{level}>{_content}</h{level}></div>"
    pdf_bytes = HTML(string=generator.wrap(heading_html)).write_pdf()
    generator.pages.extend(convert_from_bytes(pdf_bytes))

    # Meta-data
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_heading", {})
    data["content_modifiers"]["add_heading"].setdefault(counter, [])
    data["content_modifiers"]["add_heading"][counter].append(_content)
    data["content"] += "\r\n" + _content


def add_h1_heading(provider, generator, document, data, counter, **kwargs):
    """Callable responsible for the h1 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=1, **kwargs
    )


def add_h2_heading(provider, generator, document, data, counter, **kwargs):
    """Callable responsible for the h2 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=2, **kwargs
    )


def add_h3_heading(provider, generator, document, data, counter, **kwargs):
    """Callable responsible for the h3 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=3, **kwargs
    )


def add_h4_heading(provider, generator, document, data, counter, **kwargs):
    """Callable responsible for the h4 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=4, **kwargs
    )


def add_h5_heading(provider, generator, document, data, counter, **kwargs):
    """Callable responsible for the h5 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=5, **kwargs
    )


def add_h6_heading(provider, generator, document, data, counter, **kwargs):
    """Callable responsible for the h6 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=6, **kwargs
    )
