"""
.. code-block:: python

    from faker import Faker
    from faker_file.base import DynamicTemplate
    from faker_file.contrib.pdf_file.pil_snippets import *
    from faker_file.providers.pdf_file import PdfFileProvider
    from faker_file.providers.pdf_file.generators.pil_generator import (
        PilPdfGenerator
    )

    FAKER = Faker()
    FAKER.add_provider(PdfFileProvider)

    file = FAKER.pdf_file(
        pdf_generator_cls=PilPdfGenerator,
        content=DynamicTemplate(
            [
                (add_h1_heading, {}),
                (add_paragraph, {"max_nb_chars": 500}),
                (add_paragraph, {"max_nb_chars": 500}),
                (add_paragraph, {"max_nb_chars": 500}),
                (add_paragraph, {"max_nb_chars": 500}),
            ]
        )
    )

    file = FAKER.pdf_file(
        pdf_generator_cls=PilPdfGenerator,
        content=DynamicTemplate(
            [
                (add_h1_heading, {}),
                (add_paragraph, {}),
                (add_picture, {}),
                (add_paragraph, {}),
                (add_picture, {}),
                (add_paragraph, {}),
                (add_picture, {}),
                (add_paragraph, {}),
            ]
        )
    )

    file = FAKER.pdf_file(
        pdf_generator_cls=PilPdfGenerator,
        content=DynamicTemplate(
            [
                (add_h1_heading, {}),
                (add_picture, {}),
                (add_paragraph, {"max_nb_chars": 500}),
                (add_picture, {}),
                (add_paragraph, {"max_nb_chars": 500}),
                (add_picture, {}),
                (add_paragraph, {"max_nb_chars": 500}),
                (add_picture, {}),
                (add_paragraph, {"max_nb_chars": 500}),
            ]
        )
    )

    file = FAKER.pdf_file(
        pdf_generator_cls=PilPdfGenerator,
        content=DynamicTemplate(
            [
                (add_h1_heading, {}),
                (add_picture, {}),
                (add_paragraph, {"max_nb_chars": 500}),
                (add_table, {"rows": 5, "cols": 4}),
            ]
        )
    )

    file = FAKER.pdf_file(
        pdf_generator_cls=PilPdfGenerator,
        content=DynamicTemplate(
            [
                (add_h1_heading, {"margin": (2, 2)}),
                (add_picture, {"margin": (2, 2)}),
                (add_paragraph, {"max_nb_chars": 500, "margin": (2, 2)}),
                (add_picture, {"margin": (2, 2)}),
                (add_paragraph, {"max_nb_chars": 500, "margin": (2, 2)}),
                (add_picture, {"margin": (2, 2)}),
                (add_paragraph, {"max_nb_chars": 500, "margin": (2, 2)}),
                (add_picture, {"margin": (2, 2)}),
                (add_paragraph, {"max_nb_chars": 500, "margin": (2, 2)}),
            ]
        )
    )
"""
import logging
import textwrap
from collections import namedtuple
from io import BytesIO
from typing import Tuple, Union

from PIL import Image, ImageFont

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

LOGGER = logging.getLogger(__name__)


def expand_margin(
    margin: Union[Tuple[int, int], Tuple[int, int, int, int]]
) -> Tuple[int, int, int, int]:
    """Utility function to expand the margin tuple."""
    if len(margin) == 2:
        top, right = margin
        return top, right, top, right
    elif len(margin) == 4:
        return margin


def add_picture(
    provider,
    generator,
    data,
    counter,
    **kwargs,
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for picture generation using PIL."""
    # Extract margin values
    margin = kwargs.get("margin", (0, 0))
    top_margin, right_margin, bottom_margin, left_margin = expand_margin(margin)

    image_bytes = kwargs.get(
        "image_bytes", provider.generator.image()
    )  # Assuming image() returns bytes
    # Create a BytesIO object and load the image data
    with BytesIO(image_bytes) as input_stream:
        pil_image = Image.open(input_stream)

        # Resize the image
        new_width = kwargs.get("image_width", 200)
        new_height = kwargs.get("image_height", 200)
        if new_width > generator.page_width:
            new_width = generator.page_width
        if new_height > generator.page_height:
            new_height = generator.page_height
        pil_image = pil_image.resize((new_width, new_height))

        # Create a BytesIO object outside the 'with' statement
        output_stream = BytesIO()
        pil_image.save(output_stream, format="PNG")
        output_stream.seek(0)  # Move to the start of the stream

    # X, Y coordinates where the text will be placed
    # position = kwargs.get("position", (0, 0))
    # Adjust the position with margin for the left and top
    position = (
        kwargs.get("position", (0, 0))[0] + left_margin,
        kwargs.get("position", (0, 0))[1] + top_margin,
    )

    # Calculate the remaining space on the current page
    remaining_space = generator.page_height - position[1]

    # Create a PIL Image object from bytes
    image_to_paste = Image.open(output_stream)

    # Check if the image will fit on the current page
    # LOGGER.debug(f"image_to_paste.height: {image_to_paste.height}")
    # LOGGER.debug(f"remaining_space: {remaining_space}")
    if remaining_space < image_to_paste.height:
        # Image won't fit; add the current page to the list and create a new one
        generator.save_and_start_new_page()

        # Reset position to start of new page
        position = (0, 0)

    # Ensure that the document and the image to paste have the same mode
    if generator.img.mode != image_to_paste.mode:
        image_to_paste = image_to_paste.convert(generator.img.mode)

    # Create a mask if the image has an alpha channel
    mask = None
    if "A" in image_to_paste.getbands():
        mask = image_to_paste.split()[3]

    # Paste the image into the document
    generator.img.paste(image_to_paste, position, mask)

    # If you want to keep track of the last position to place
    # another element, you can.
    # last_position = (
    #     position[0] + image.width, position[1] + image_to_paste.height
    # )
    last_position = (0, position[1] + image_to_paste.height + bottom_margin)

    # Meta-data (optional)
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_picture", {})
    data["content_modifiers"]["add_picture"].setdefault(counter, [])
    data["content_modifiers"]["add_picture"][counter].append("Image added")

    return False, last_position


def add_paragraph(
    provider,
    generator,
    data,
    counter,
    **kwargs,
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for paragraph generation using PIL."""
    # Extract margin values
    margin = kwargs.get("margin", (0, 0))
    top_margin, right_margin, bottom_margin, left_margin = expand_margin(margin)
    content = kwargs.get("content", None)
    max_nb_chars = kwargs.get("max_nb_chars", 5_000)
    wrap_chars_after = kwargs.get("wrap_chars_after", None)
    # X, Y coordinates where the text will be placed
    # position = kwargs.get("position", (0, 0))
    # position = kwargs.get("position", (0, 0))
    # Adjust the position with margin for the left and top
    position = (
        kwargs.get("position", (0, 0))[0] + left_margin,
        kwargs.get("position", (0, 0))[1] + top_margin,
    )
    content_specs = kwargs.get("content_specs", {})
    format_func = kwargs.get("format_func", DEFAULT_FORMAT_FUNC)

    _content = provider._generate_text_content(
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        format_func=format_func,
    )
    font = ImageFont.truetype(generator.font, generator.font_size)
    lines = _content.split("\n")
    line_max_num_chars = generator.find_max_fit_for_multi_line_text(
        generator.draw,
        lines,
        font,
        generator.page_width,
    )
    wrap_chars_after = content_specs.get("wrap_chars_after")
    if (
        not wrap_chars_after
        or wrap_chars_after
        and (wrap_chars_after > line_max_num_chars)
    ):
        lines = textwrap.wrap(_content, line_max_num_chars)

    # Load a truetype or opentype font file, and create a font object.
    font = ImageFont.truetype(generator.font, generator.font_size)

    y_text = position[1]
    # LOGGER.debug(f"position: {position}")
    for counter, line in enumerate(lines):
        text_width, text_height = generator.draw.textsize(
            line, font=font, spacing=generator.spacing
        )
        if y_text + text_height > generator.page_height:
            generator.save_and_start_new_page()
            y_text = 0

        generator.draw.text(
            (position[0], y_text),
            line,
            fill=(0, 0, 0),
            spacing=generator.spacing,
            font=font,
        )
        # Move down for next line
        y_text += text_height + generator.line_height

    # If you want to keep track of the last position to place another
    # element, you can.
    # last_position = (position[0], y_text)
    # last_position = (0, y_text)
    last_position = (0, y_text + bottom_margin)

    # Add meta-data, assuming data is a dictionary for tracking
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_paragraph", {})
    data["content_modifiers"]["add_paragraph"].setdefault(counter, [])
    data["content_modifiers"]["add_paragraph"][counter].append(_content)
    data.setdefault("content", "")
    data["content"] += "\r\n" + _content

    return False, last_position


def add_page_break(
    provider,
    generator,
    data,
    counter,
    **kwargs,
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for paragraph generation using PIL."""
    generator.save_and_start_new_page()

    # If you want to keep track of the last position to place another
    # element, you can.
    # last_position = (position[0], 0)
    last_position = (0, 0)

    return False, last_position


def get_heading_font_size(base_size: int, heading_level: int) -> int:
    return base_size * (8 - heading_level) // 2


def add_heading(
    provider,
    generator,
    data,
    counter,
    **kwargs,
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for H1 heading generation using PIL."""
    # Extract margin values
    margin = kwargs.get("margin", (0, 0))
    top_margin, right_margin, bottom_margin, left_margin = expand_margin(margin)
    content = kwargs.get("content", None)
    max_nb_chars = kwargs.get("max_nb_chars", 30)
    wrap_chars_after = kwargs.get("wrap_chars_after", None)
    format_func = kwargs.get("format_func", DEFAULT_FORMAT_FUNC)
    # X, Y coordinates where the text will be placed
    # position = kwargs.get("position", (0, 0))
    # Adjust the position with margin for the left and top
    position = (
        kwargs.get("position", (0, 0))[0] + left_margin,
        kwargs.get("position", (0, 0))[1] + top_margin,
    )
    level = kwargs.get("level", 1)
    if level < 1 or level > 6:
        level = 1

    font_size = get_heading_font_size(generator.font_size, level)

    _content = provider._generate_text_content(
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        format_func=format_func,
    )

    # Here, you'll specify a different font size for heading
    font = ImageFont.truetype(generator.font, font_size)

    y = position[1]
    generator.draw.text(
        (position[0], y),
        _content,
        fill=(0, 0, 0),
        font=font,
    )

    text_width, text_height = generator.draw.textsize(_content, font=font)
    y += text_height

    # If you want to keep track of the last position to place another
    # element, you can.
    # last_position = (position[0], y)
    # last_position = (0, y)
    last_position = (0, y + bottom_margin)

    # Add meta-data, assuming data is a dictionary for tracking
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_heading", {})
    data["content_modifiers"]["add_heading"].setdefault(counter, [])
    data["content_modifiers"]["add_heading"][counter].append(_content)
    data.setdefault("content", "")
    data["content"] += "\r\n" + _content

    return False, last_position


def add_h1_heading(
    provider, generator, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h1 heading generation."""
    return add_heading(provider, generator, data, counter, level=1, **kwargs)


def add_h2_heading(
    provider, generator, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h2 heading generation."""
    return add_heading(provider, generator, data, counter, level=2, **kwargs)


def add_h3_heading(
    provider, generator, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h3 heading generation."""
    return add_heading(provider, generator, data, counter, level=3, **kwargs)


def add_h4_heading(
    provider, generator, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h4 heading generation."""
    return add_heading(provider, generator, data, counter, level=4, **kwargs)


def add_h5_heading(
    provider, generator, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h5 heading generation."""
    return add_heading(provider, generator, data, counter, level=5, **kwargs)


def add_h6_heading(
    provider, generator, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h6 heading generation."""
    return add_heading(provider, generator, data, counter, level=6, **kwargs)


# This is a simple placeholder for your table object
Table = namedtuple("Table", ["data"])


def draw_table_cell(document, cell_content, position, cell_size, font):
    """Draw a table cell."""
    x, y = position
    width, height = cell_size
    border_color = (0, 0, 0)
    fill_color = (255, 255, 255)

    # Draw the rectangle
    document.rectangle(
        [position, (x + width, y + height)],
        fill=fill_color,
        outline=border_color,
    )

    # Draw text in the rectangle
    text_width, text_height = document.textsize(cell_content, font=font)
    text_position = (
        x + (width - text_width) // 2,
        y + (height - text_height) // 2,
    )
    document.text(text_position, cell_content, fill=(0, 0, 0), font=font)


def add_table(
    provider,
    generator,
    data,
    counter,
    **kwargs,
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for table generation using PIL."""
    # X, Y coordinates where the table will be placed
    position = kwargs.get("position", (0, 0))

    # Default cell dimensions
    cell_width = kwargs.get("cell_width", 100)
    cell_height = kwargs.get("cell_height", 30)

    # Font for the table cells
    font = ImageFont.truetype(generator.font, generator.font_size)

    # Extract or generate table data
    rows = kwargs.get("rows", 3)
    cols = kwargs.get("cols", 4)
    headers = [f"Header {i + 1}" for i in range(cols)]
    table_data = [
        [provider.generator.word() for _ in range(cols)] for _ in range(rows)
    ]
    table_data.insert(0, headers)
    table = Table(table_data)

    y = position[1]
    for row in table.data:
        x = position[0]
        for cell_content in row:
            cell_position = (x, y)
            draw_table_cell(
                generator.draw,
                cell_content,
                cell_position,
                (cell_width, cell_height),
                font,
            )
            x += cell_width
        y += cell_height

    last_position = (0, y)

    # Add meta-data, assuming data is a dictionary for tracking
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_table", {})
    data["content_modifiers"]["add_table"].setdefault(counter, [])
    data["content_modifiers"]["add_table"][counter].append("Table added")

    return False, last_position
