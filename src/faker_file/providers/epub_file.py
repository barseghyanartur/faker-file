import os
import shutil
import tempfile
from typing import Optional

import xml2epub
from faker.providers import BaseProvider

from ..base import FileMixin, StringValue
from ..constants import DEFAULT_TEXT_MAX_NB_CHARS
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("EpubFileProvider",)


class EpubFileProvider(BaseProvider, FileMixin):
    """EPUB file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.epub_file import EpubFileProvider

        file = EpubFileProvider(Faker()).epub_file()

    Usage example with options:

        file = EpubFileProvider(Faker()).epub_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = EpubFileProvider(Faker()).epub_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )
    """

    extension: str = "epub"

    def epub_file(
        self: "EpubFileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        title: Optional[str] = None,
        chapter_title: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a EPUB file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param title: E-book title. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param chapter_title: Chapter title. Might contain dynamic elements,
            which are then replaced by correspondent fixtures.
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

        title = self._generate_text_content(
            max_nb_chars=50,
            content=title,
        )

        chapter_title = self._generate_text_content(
            max_nb_chars=50,
            content=chapter_title,
        )

        _book = xml2epub.Epub(title)
        _chapter = xml2epub.create_chapter_from_string(
            content, title=chapter_title
        )
        _book.add_chapter(_chapter)
        _local_file_name = _book.create_epub(tempfile.gettempdir())

        with open(_local_file_name, "rb") as fakefile:
            storage.write_bytes(filename, fakefile.read())
        os.remove(_local_file_name)
        shutil.rmtree(_book.EPUB_DIR)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = {
            "content": content,
            "title": title,
            "chapter_title": chapter_title,
        }
        return file_name
