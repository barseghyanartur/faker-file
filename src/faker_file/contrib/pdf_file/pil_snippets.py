import logging
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

LOGGER = logging.getLogger(__name__)


def add_picture(
    provider,
    generator,
    document: "ImageDraw",  # ImageDraw.Draw object for drawing
    data,
    counter,
    position=(0, 0),  # X, Y coordinates where the image will be placed
    **kwargs,
):
    """Callable responsible for picture generation using PIL."""
    image_bytes = kwargs.get(
        "image_bytes", provider.generator.image()
    )  # Assuming image() returns bytes

    # Create a PIL Image object from bytes
    image_to_paste = Image.open(BytesIO(image_bytes))

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
    last_position = (position[0] + image.width, position[1] + image.height)

    # Meta-data (optional)
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_picture", {})
    data["content_modifiers"]["add_picture"].setdefault(counter, [])
    data["content_modifiers"]["add_picture"][counter].append("Image added")

    return last_position


def add_paragraph(
    provider,
    generator,
    document: "ImageDraw",  # ImageDraw.Draw object for drawing
    data,
    counter,
    position=(0, 0),  # X, Y coordinates where the text will be placed
    **kwargs,
):
    """Callable responsible for paragraph generation using PIL."""
    content = kwargs.get("content", None)
    max_nb_chars = kwargs.get("max_nb_chars", 5_000)
    wrap_chars_after = kwargs.get("wrap_chars_after", None)
    format_func = kwargs.get(
        "format_func", None
    )  # Assuming DEFAULT_FORMAT_FUNC is somewhere defined

    _content = provider._generate_text_content(
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        format_func=format_func,
    )
    LOGGER.error(f"_content: {_content}")

    lines = _content.split("\n")
    LOGGER.error(f"lines: {lines}")

    # Load a truetype or opentype font file, and create a font object.
    font = ImageFont.truetype(generator.font, generator.font_size)

    y = position[1]
    LOGGER.error(f"position: {position}")
    for line in lines:
        document.text(
            (position[0], y),
            line,
            fill=(0, 0, 0),
            spacing=generator.spacing,
            font=font,
        )
        text_width, text_height = document.textsize(line, font=font)
        y += text_height  # Move down for next line
        # y += 14  # Move down for next line

    # If you want to keep track of the last position to place another
    # element, you can.
    last_position = (position[0], y)

    # Add meta-data, assuming data is a dictionary for tracking
    data.setdefault("content_modifiers", {})
    data["content_modifiers"].setdefault("add_paragraph", {})
    data["content_modifiers"]["add_paragraph"].setdefault(counter, [])
    data["content_modifiers"]["add_paragraph"][counter].append(_content)
    data.setdefault("content", "")
    data["content"] += "\r\n" + _content

    return last_position
