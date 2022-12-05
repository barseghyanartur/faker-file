import os
from typing import Optional

from docx import Document
from faker.providers import BaseProvider

from ..base import DEFAULT_REL_PATH, FileMixin, StringValue
from ..content_generators import BaseContentGenerator
from ..helpers import wrap_text

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("DocxFileProvider",)


class DocxFileProvider(BaseProvider, FileMixin):
    """DOCX file provider.

        Usage example:

        from faker_file.providers.docx_file import DocxFileProvider

        file = DocxFileProvider(None).docx_file()

    Usage example with options:

        from faker_file.providers.docx_file import DocxFileProvider

        file = DocxFileProvider(None).docx_file(
            max_nb_chars=100_000,
            wrap_chars_after=80,
            prefix="zzz",
        )
    """

    extension: str = "docx"

    def docx_file(
        self,
        max_nb_chars: int = 100_000,
        root_path: str = None,
        rel_path: str = DEFAULT_REL_PATH,
        wrap_chars_after: Optional[int] = None,
        prefix: Optional[str] = None,
        content_generator: Optional[BaseContentGenerator] = None,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a file with random text.

        :param max_nb_chars: File size in bytes. Note, that it might not be the
            exact file size. When working with more specific file formats,
            such as `docx` or `pdf`, size would be the number of generated
            characters. For random bytes (not `docx` or `pdf`) it would be
            the exact file size.
        :param root_path:
        :param rel_path: Relative path (from Django MEDIA_ROOT directory).
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param prefix: File name prefix.
        :param content_generator:
        :param content:
        :return: Relative path (from Django MEDIA_ROOT directory) of the
            generated file.
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
        document = Document()
        document.add_paragraph(content)
        document.save(file_name)

        # Generic
        file_name = StringValue(os.path.relpath(file_name, root_path))
        if data:
            file_name.data = data
        return file_name
