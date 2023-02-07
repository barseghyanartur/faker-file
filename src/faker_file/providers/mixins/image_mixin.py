import contextlib
import io
from typing import Optional, Union, overload

import imgkit

from ...base import BytesValue, FileMixin, StringValue
from ...constants import DEFAULT_IMAGE_MAX_NB_CHARS
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("ImageMixin",)


class ImageMixin(FileMixin):
    """Image mixin."""

    @overload
    def _image_file(
        self: "ImageMixin",
        storage: Optional[BaseStorage] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def _image_file(
        self: "ImageMixin",
        storage: Optional[BaseStorage] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def _image_file(
        self: "ImageMixin",
        storage: Optional[BaseStorage] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate an image file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
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

        data = {"content": content, "filename": filename}

        with contextlib.redirect_stdout(io.StringIO()):
            buffer = imgkit.from_string(
                f"<pre>{content}</pre>",
                False,
                options={"format": self.extension},
            )

        if raw:
            raw_content = BytesValue(buffer)
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, buffer)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        return file_name
