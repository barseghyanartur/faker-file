from typing import Optional

import pdfkit
from faker.providers import BaseProvider

from ..base import FileMixin, StringValue
from ..constants import DEFAULT_FILE_ENCODING, DEFAULT_TEXT_MAX_NB_CHARS
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("PdfFileProvider",)


class PdfFileProvider(BaseProvider, FileMixin):
    """PDF file provider.

        Usage example:

        from faker_file.providers.pdf_file import PdfFileProvider

        file = PdfFileProvider(None).pdf_file()

    Usage example with options:

        from faker_file.providers.pdf_file import PdfFileProvider

        file = PdfFileProvider(None).pdf_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = PdfFileProvider(Faker()).pdf_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )
    """

    extension: str = "pdf"

    def pdf_file(
        self: "PdfFileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        encoding: Optional[str] = DEFAULT_FILE_ENCODING,
        **kwargs,
    ) -> StringValue:
        """Generate a PDF file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param encoding: Encoding of the file.
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

        options = {"quiet": ""}
        if encoding is not None:
            options["encoding"] = encoding

        raw_content = pdfkit.from_string(
            f"<pre style='white-space: pre-wrap;'>{content}</pre>",
            options=options,
        )

        storage.write_bytes(filename, raw_content)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = {"content": content}
        return file_name
