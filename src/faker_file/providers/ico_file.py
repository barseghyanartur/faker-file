import os
from typing import Optional

import imgkit
from faker.providers import BaseProvider

from ..base import DEFAULT_REL_PATH, FileMixin, StringValue
from ..constants import DEFAULT_IMAGE_MAX_NB_CHARS

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("IcoFileProvider",)


class IcoFileProvider(BaseProvider, FileMixin):
    """ICO file provider.

        Usage example:

        from faker_file.providers.png_file import IcoFileProvider

        file = IcoFileProvider(None).ico_file()

    Usage example with options:

        from faker_file.providers.ico_file import IcoFileProvider

        file = IcoFileProvider(None).ico_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )
    """

    extension: str = "ico"

    def ico_file(
        self: "IcoFileProvider",
        root_path: str = None,
        rel_path: str = DEFAULT_REL_PATH,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate an ICO file with random text.

        :param root_path: Path of your files root directory (in case of Django
            it would be `settings.MEDIA_ROOT`).
        :param rel_path: Relative path (from root directory).
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        file_name = self._generate_filename(
            root_path=root_path,
            rel_path=rel_path,
            prefix=prefix,
        )

        content = self._generate_text_content(
            max_nb_chars=max_nb_chars,
            wrap_chars_after=wrap_chars_after,
            content=content,
        )

        imgkit.from_string(f"<pre>{content}</pre>", file_name)

        # Generic
        file_name = StringValue(os.path.relpath(file_name, root_path))
        file_name.data = {"content": content}
        return file_name
