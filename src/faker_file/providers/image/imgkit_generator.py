import contextlib
import io
import logging
from typing import Any, Dict, Union

import imgkit
from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider

from ...base import DynamicTemplate, StringList
from ...constants import DEFAULT_FILE_ENCODING
from ..base.image_generator import BaseImageGenerator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("ImgkitImageGenerator",)

LOGGER = logging.getLogger(__name__)


class ImgkitImageGenerator(BaseImageGenerator):
    """Imgkit image generator.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.png_file import PngFileProvider
        from faker_file.providers.image.imgkit_generator import (
            ImgkitImageGenerator
        )

        FAKER = Faker()
        FAKER.add_provider(PngFileProvider)

        file = FAKER.png_file(
            img_generator_cls=ImgkitImageGenerator
        )


    Using `DynamicTemplate`:

    .. code-block:: python

        from faker_file.base import DynamicTemplate
        from faker_file.contrib.image.imgkit_snippets import (
            add_h1_heading,
            add_h2_heading,
            add_h3_heading,
            add_h4_heading,
            add_h5_heading,
            add_h6_heading,
            add_heading,
            add_page_break,
            add_paragraph,
            add_picture,
            add_table,
        )

        # Create a file with lots of elements
        file = FAKER.png_file(
            image_generator_cls=ImgkitImageGenerator,
            content=DynamicTemplate(
                [
                    (add_h1_heading, {}),
                    (add_paragraph, {}),
                    (add_h2_heading, {}),
                    (add_h3_heading, {}),
                    (add_h4_heading, {}),
                    (add_h5_heading, {}),
                    (add_h6_heading, {}),
                    (add_paragraph, {}),
                    (add_picture, {}),
                    (add_page_break, {}),
                    (add_h6_heading, {}),
                    (add_table, {}),
                    (add_paragraph, {}),
                ]
            )
        )
    """

    encoding: str = DEFAULT_FILE_ENCODING

    def handle_kwargs(self: "ImgkitImageGenerator", **kwargs) -> None:
        """Handle kwargs."""

    def generate(
        self: "ImgkitImageGenerator",
        content: str,
        data: Dict[str, Any],
        provider: Union[Faker, Generator, Provider],
        **kwargs,
    ) -> bytes:
        """Generate image."""
        with contextlib.redirect_stdout(io.StringIO()):
            if isinstance(content, DynamicTemplate):
                _content = StringList()
                for counter, (ct_modifier, ct_modifier_kwargs) in enumerate(
                    content.content_modifiers
                ):
                    ct_modifier(
                        provider,
                        self,
                        _content,
                        data,
                        counter,
                        **ct_modifier_kwargs,
                    )
            else:
                _content = (
                    f"<pre style='white-space: pre-wrap;'>{content}</pre>"
                )

            return imgkit.from_string(
                str(_content),
                False,
                options={"format": provider.extension},
            )
