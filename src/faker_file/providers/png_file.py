import os
from typing import Optional

import imgkit
from faker.providers import BaseProvider

from ..base import DEFAULT_REL_PATH, FileMixin, StringValue
from ..constants import DEFAULT_IMAGE_MAX_NB_CHARS
from ..content_generators import BaseContentGenerator
from ..helpers import wrap_text

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("PngFileProvider",)


class PngFileProvider(BaseProvider, FileMixin):
    """PNG file provider.

        Usage example:

        from faker_file.providers.png_file import PngFileProvider

        file = PngFileProvider(None).png_file()

    Usage example with options:

        from faker_file.providers.png_file import PngFileProvider

        file = PngFileProvider(None).png_file(
            max_nb_chars=100_000,
            wrap_chars_after=80,
            prefix="zzz",
        )
    """

    extension: str = "png"

    def png_file(
        self,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        root_path: str = None,
        rel_path: str = DEFAULT_REL_PATH,
        wrap_chars_after: Optional[int] = None,
        prefix: Optional[str] = None,
        content_generator: Optional[BaseContentGenerator] = None,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a file with random text.

        :param max_nb_chars: Max number of chars for the content.
        :param root_path: Path of your files root directory (in case of Django
            it would be `settings.MEDIA_ROOT`).
        :param rel_path: Relative path (from root directory).
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param prefix: File name prefix.
        :param content_generator: Content generator.
        :param content: File content. If given, used as is.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        file_name = self._generate_filename(
            root_path=root_path,
            rel_path=rel_path,
            prefix=prefix,
        )
        data = {}

        # Specific
        if content is not None:
            if wrap_chars_after:
                content = wrap_text(content, wrap_chars_after)
        else:
            content = self._generate_content(
                max_nb_chars,
                wrap_chars_after=wrap_chars_after,
                content_generator=content_generator,
            )
        imgkit.from_string(content, file_name)

        # Generic
        file_name = StringValue(os.path.relpath(file_name, root_path))
        if data:
            file_name.data = data
        return file_name
