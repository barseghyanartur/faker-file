import os
import shutil
import tempfile
from typing import Callable, Optional, Union, overload

import xml2epub
from faker import Faker
from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.python import Provider

from ..base import DEFAULT_FORMAT_FUNC, BytesValue, FileMixin, StringValue
from ..constants import DEFAULT_TEXT_MAX_NB_CHARS
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("EpubFileProvider",)


class EpubFileProvider(BaseProvider, FileMixin):
    """EPUB file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.epub_file import EpubFileProvider

        FAKER = Faker()
        FAKER.add_provider(EpubFileProvider)

        file = FAKER.epub_file()

    Usage example with options:

    .. code-block:: python

        file = FAKER.epub_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

    .. code-block:: python

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.epub_file(
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

    @overload
    def epub_file(
        self: "EpubFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        title: Optional[str] = None,
        chapter_title: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def epub_file(
        self: "EpubFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        title: Optional[str] = None,
        chapter_title: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def epub_file(
        self: "EpubFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        title: Optional[str] = None,
        chapter_title: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a EPUB file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
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
        :param format_func: Callable responsible for formatting template
            strings.
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
            extension=self.extension,
            prefix=prefix,
            basename=basename,
        )

        content = self._generate_text_content(
            max_nb_chars=max_nb_chars,
            wrap_chars_after=wrap_chars_after,
            content=content,
            format_func=format_func,
        ).replace("\n", "<br>")

        title = self._generate_text_content(
            max_nb_chars=50,
            content=title,
            format_func=format_func,
        )

        chapter_title = self._generate_text_content(
            max_nb_chars=50,
            content=chapter_title,
            format_func=format_func,
        )

        _book = xml2epub.Epub(title)
        _chapter = xml2epub.create_chapter_from_string(
            content, title=chapter_title
        )
        _book.add_chapter(_chapter)
        _local_file_name = _book.create_epub(tempfile.gettempdir())

        data = {
            "content": content,
            "title": title,
            "chapter_title": chapter_title,
            "filename": filename,
            "storage": storage,
        }

        _raw_content = bytes()
        with open(_local_file_name, "rb") as fakefile:
            _raw_content = fakefile.read()
            os.remove(_local_file_name)
            shutil.rmtree(_book.EPUB_DIR)

        if raw:
            raw_content = BytesValue(_raw_content)
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, _raw_content)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
