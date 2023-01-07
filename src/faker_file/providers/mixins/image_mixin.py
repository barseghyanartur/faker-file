import contextlib
import io
from typing import Optional

import imgkit

from ...base import FileMixin, StringValue
from ...constants import DEFAULT_IMAGE_MAX_NB_CHARS
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("ImageMixin",)


class ImageMixin(FileMixin):
    """Image mixin."""

    def _image_file(
        self: "ImageMixin",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate an image file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        filename = storage.generate_filename(
            prefix=prefix,
            extension=self.extension,
        )

        content = self._generate_text_content(
            max_nb_chars=max_nb_chars,
            wrap_chars_after=wrap_chars_after,
            content=content,
        )

        with contextlib.redirect_stdout(io.StringIO()):
            storage.write_bytes(
                filename,
                imgkit.from_string(
                    f"<pre>{content}</pre>",
                    False,
                    options={"format": self.extension},
                ),
            )

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = {"content": content}
        return file_name
