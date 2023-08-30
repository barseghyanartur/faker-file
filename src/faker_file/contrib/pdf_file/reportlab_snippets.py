from io import BytesIO

from PIL import Image as PilImage
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, PageBreak, Paragraph, Table, TableStyle

from ...base import DEFAULT_FORMAT_FUNC

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


def add_table(
    provider,
    generator,
    story,
    data,
    counter,
    **kwargs,
):
    """Add table function."""
    rows = kwargs.get("rows", 3)
    cols = kwargs.get("cols", 4)
    font_name = kwargs.get("font_name", "Helvetica-Bold")
    font_size = kwargs.get("font_size", 14)
    align = kwargs.get("align", "CENTER")

    # Define your table headers
    headers = [f"Header {i + 1}" for i in range(cols)]

    # Generate the rest of the table data
    table_data = [
        [provider.generator.word() for _ in range(cols)] for _ in range(rows)
    ]

    # Add the headers to the table data
    table_data.insert(0, headers)

    # Create the table object
    table = Table(table_data)

    # Apply table styles
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), align),
                ("FONTNAME", (0, 0), (-1, 0), font_name),
                ("FONTSIZE", (0, 0), (-1, 0), font_size),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
    )

    # Add the table to the document and build it
    story.append(table)


def add_picture(
    provider,
    generator,
    story,
    data,
    counter,
    **kwargs,
):
    """Add picture function."""
    image = kwargs.get("image", provider.generator.image())

    # Create a BytesIO object and load the image data
    with BytesIO(image) as input_stream:
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
        img = Image(output_stream)
        img.width = new_width
        img.height = new_height
        story.append(img)


def add_page_break(
    provider,
    generator,
    story,
    data,
    counter,
    **kwargs,
):
    """Add page break function."""
    # Insert a page break
    story.append(PageBreak())


def add_paragraph(
    provider,
    generator,
    story,
    data,
    counter,
    **kwargs,
):
    """Add paragraph function."""
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

    # Insert a paragraph
    styles = getSampleStyleSheet()
    style_paragraph = styles["Normal"]
    style_paragraph.fontName = generator.font_name
    pdfmetrics.registerFont(TTFont(generator.font_name, generator.font_path))
    content = provider.generator.text(max_nb_chars=5_000)
    paragraph = Paragraph(content, style_paragraph)
    story.append(paragraph)

    # Meta-data
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_paragraph", {})
    data["content_modifiers"]["add_paragraph"].setdefault(counter, [])
    data["content_modifiers"]["add_paragraph"][counter].append(_content)
    data["content"] += "\r\n" + _content


def add_heading(
    provider,
    generator,
    story,
    data,
    counter,
    **kwargs,
):
    """Add heading function."""
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

    # Insert a heading
    styles = getSampleStyleSheet()

    # Define the heading style based on the level
    heading_style = ParagraphStyle(
        f"Heading{level}",
        parent=styles[f"Heading{level}"],
        fontSize=14 - level,
        spaceAfter=12,
    )

    heading_style.fontName = generator.font_name
    pdfmetrics.registerFont(TTFont(generator.font_name, generator.font_path))

    heading = Paragraph(_content, heading_style)
    story.append(heading)

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
