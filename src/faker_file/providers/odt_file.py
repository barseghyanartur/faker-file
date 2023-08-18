from io import BytesIO
from typing import Callable, Optional, Union, overload

from faker import Faker
from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.python import Provider
from odf.opendocument import OpenDocumentText
from odf.text import P

from ..base import (
    DEFAULT_FORMAT_FUNC,
    BytesValue,
    DynamicTemplate,
    FileMixin,
    StringValue,
)
from ..constants import DEFAULT_TEXT_MAX_NB_CHARS
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("OdtFileProvider",)


class OdtFileProvider(BaseProvider, FileMixin):
    """ODT file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.odt_file import OdtFileProvider

        FAKER = Faker()
        FAKER.add_provider(OdtFileProvider)

        file = FAKER.odt_file()

    Usage example with options:

    .. code-block:: python

        file = FAKER.odt_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

    .. code-block:: python

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.odt_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with content modifiers:

    .. code-block:: python

        from faker_file.base import DynamicTemplate
        from faker_file.providers.jpeg_file import JpegFileProvider
        from faker_file.contrib.odt_file import (
            add_h1_heading,
            add_h2_heading,
            add_h3_heading,
            add_h4_heading,
            add_h5_heading,
            add_h6_heading,
            add_page_break,
            add_paragraph,
            add_picture,
            add_table,
        )

        file = FAKER.odt_file(
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

    extension: str = "odt"

    @overload
    def odt_file(
        self: "OdtFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[Union[str, DynamicTemplate]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def odt_file(
        self: "OdtFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[Union[str, DynamicTemplate]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def odt_file(
        self: "OdtFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[Union[str, DynamicTemplate]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate an ODT file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
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

        if isinstance(content, DynamicTemplate):
            _content = ""
        else:
            _content = self._generate_text_content(
                max_nb_chars=max_nb_chars,
                wrap_chars_after=wrap_chars_after,
                content=content,
                format_func=format_func,
            )
        data = {"content": _content, "filename": filename, "storage": storage}

        with BytesIO() as _fake_file:
            document = OpenDocumentText()
            if _content:
                document.text.addElement(P(text=_content))
            elif isinstance(content, DynamicTemplate):
                for counter, (ct_modifier, ct_modifier_kwargs) in enumerate(
                    content.content_modifiers
                ):
                    ct_modifier(
                        self,
                        document,
                        data,
                        counter,
                        **ct_modifier_kwargs,
                    )

            document.save(_fake_file)

            if raw:
                raw_content = BytesValue(_fake_file.getvalue())
                raw_content.data = data
                return raw_content

            storage.write_bytes(filename, _fake_file.getvalue())

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
