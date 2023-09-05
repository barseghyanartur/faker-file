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
                (add_paragraph, {),
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
"""
import logging
import textwrap
from io import BytesIO
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont

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
    # "add_table",
)

LOGGER = logging.getLogger(__name__)


def add_picture(
    provider,
    generator,
    document: ImageDraw,
    data,
    counter,
    **kwargs,
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for picture generation using PIL."""
    image_bytes = kwargs.get(
        "image_bytes", provider.generator.image()
    )  # Assuming image() returns bytes
    # Create a BytesIO object and load the image data
    with BytesIO(image_bytes) as input_stream:
        pil_image = Image.open(input_stream)

        # Resize the image
        new_width = 200
        new_height = 200
        pil_image = pil_image.resize((new_width, new_height))

        # Create a BytesIO object outside the 'with' statement
        output_stream = BytesIO()
        pil_image.save(output_stream, format="JPEG")
        output_stream.seek(0)  # Move to the start of the stream

    # X, Y coordinates where the text will be placed
    position = kwargs.get("position", (0, 0))

    # Calculate the remaining space on the current page
    remaining_space = generator.page_height - position[1]

    # Create a PIL Image object from bytes
    image_to_paste = Image.open(output_stream)

    # Check if the image will fit on the current page
    if remaining_space < image_to_paste.height:
        # Image won't fit; add the current page to the list and create a new one
        img = document._image
        generator.pages.append(img.copy())
        img = generator.create_image_instance()
        document = ImageDraw.Draw(img)

        # Reset position to start of new page
        position = (0, 0)

    # Paste the image into the document
    image_position = (
        position[0],
        position[1],
        position[0] + image_to_paste.width,
        position[1] + image_to_paste.height,
    )

    image = document._image
    # Ensure that the document and the image to paste have the same mode
    if image.mode != image_to_paste.mode:
        image_to_paste = image_to_paste.convert(image.mode)

    # Create a mask if the image has an alpha channel
    mask = None
    if "A" in image_to_paste.getbands():
        mask = image_to_paste.split()[3]

    image.paste(image_to_paste, position, mask)

    LOGGER.error(f"position: {image_position}")
    # If you want to keep track of the last position to place
    # another element, you can.
    # last_position = (position[0] + image.width, position[1] + image.height)
    last_position = (0, position[1] + image.height)

    # Meta-data (optional)
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_picture", {})
    data["content_modifiers"]["add_picture"].setdefault(counter, [])
    data["content_modifiers"]["add_picture"][counter].append("Image added")

    return False, last_position


def add_paragraph(
    provider,
    generator,
    document: ImageDraw,  # ImageDraw.Draw object for drawing
    data,
    counter,
    **kwargs,
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for paragraph generation using PIL."""
    content = kwargs.get("content", None)
    max_nb_chars = kwargs.get("max_nb_chars", 5_000)
    wrap_chars_after = kwargs.get("wrap_chars_after", None)
    # X, Y coordinates where the text will be placed
    position = kwargs.get("position", (0, 0))
    content_specs = kwargs.get("content_specs", {})
    format_func = kwargs.get(
        "format_func", None
    )  # Assuming DEFAULT_FORMAT_FUNC is somewhere defined

    _content = provider._generate_text_content(
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        format_func=format_func,
    )
    font = ImageFont.truetype(generator.font, generator.font_size)
    line_max_num_chars = generator.find_max_fit_for_multi_line_text(
        document,
        _content.split("\n"),
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
    LOGGER.error(f"position: {position}")
    for counter, line in enumerate(lines):
        text_width, text_height = document.textsize(
            line, font=font, spacing=generator.spacing
        )
        if y_text + text_height > generator.page_height:
            img = document._image
            generator.pages.append(img.copy())
            img = generator.create_image_instance()
            document = ImageDraw.Draw(img)
            y_text = 0

        document.text(
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
    last_position = (0, y_text)

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
    document: ImageDraw,  # ImageDraw.Draw object for drawing
    data,
    counter,
    **kwargs,
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for paragraph generation using PIL."""
    # position = kwargs.get("position", (0, 0))
    img = document._image
    generator.pages.append(img.copy())
    img = generator.create_image_instance()
    document = ImageDraw.Draw(img)

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
    document: "ImageDraw",  # ImageDraw.Draw object for drawing
    data,
    counter,
    **kwargs,
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for H1 heading generation using PIL."""
    content = kwargs.get("content", None)
    max_nb_chars = kwargs.get("max_nb_chars", 30)
    wrap_chars_after = kwargs.get("wrap_chars_after", None)
    format_func = kwargs.get("format_func", None)
    # X, Y coordinates where the text will be placed
    position = kwargs.get("position", (0, 0))
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
    document.text(
        (position[0], y),
        _content,
        fill=(0, 0, 0),
        font=font,
    )

    text_width, text_height = document.textsize(_content, font=font)
    y += text_height

    # If you want to keep track of the last position to place another
    # element, you can.
    # last_position = (position[0], y)
    last_position = (0, y)

    # Add meta-data, assuming data is a dictionary for tracking
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_heading", {})
    data["content_modifiers"]["add_heading"].setdefault(counter, [])
    data["content_modifiers"]["add_heading"][counter].append(_content)
    data.setdefault("content", "")
    data["content"] += "\r\n" + _content

    return False, last_position


def add_h1_heading(
    provider, generator, document: ImageDraw, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h1 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=1, **kwargs
    )


def add_h2_heading(
    provider, generator, document: ImageDraw, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h2 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=2, **kwargs
    )


def add_h3_heading(
    provider, generator, document: ImageDraw, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h3 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=3, **kwargs
    )


def add_h4_heading(
    provider, generator, document: ImageDraw, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h4 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=4, **kwargs
    )


def add_h5_heading(
    provider, generator, document: ImageDraw, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h5 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=5, **kwargs
    )


def add_h6_heading(
    provider, generator, document: ImageDraw, data, counter, **kwargs
) -> Tuple[bool, Tuple[int, int]]:
    """Callable responsible for the h6 heading generation."""
    return add_heading(
        provider, generator, document, data, counter, level=6, **kwargs
    )
