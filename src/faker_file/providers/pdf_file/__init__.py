from typing import Any, Dict, Optional, Type, Union, overload

from faker.providers import BaseProvider

from ...base import BytesValue, FileMixin, StringValue
from ...constants import DEFAULT_TEXT_MAX_NB_CHARS
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage
from ..base.pdf_generator import BasePdfGenerator
from .generators.pdfkit_generator import PdfkitPdfGenerator

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

    Default PDF generator class is `PdfkitPdfGenerator` which uses `pdfkit`
    Python package and `wkhtmltopdf` system package for generating PDFs from
    randomly generated text. The quality of the produced PDFs is very good,
    but it's less performant than `ReportlabPdfGenerator` (factor 40x), which
    does not require additional system dependencies to run. To use it, pass
    `ReportlabPdfGenerator` class in `pdf_generator_cls` argument.

        from faker_file.providers.pdf_file.generators import (
            reportlab_generator,
        )

        file = PdfFileProvider(None).pdf_file(
            max_nb_chars=1_000,
            wrap_chars_after=80,
            pdf_generator_cls=reportlab_generator.ReportlabPdfGenerator,
        )
    """

    extension: str = "pdf"

    @overload
    def pdf_file(
        self: "PdfFileProvider",
        storage: Optional[BaseStorage] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        pdf_generator_cls: Optional[Type[BasePdfGenerator]] = (
            PdfkitPdfGenerator
        ),
        pdf_generator_kwargs: Optional[Dict[str, Any]] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def pdf_file(
        self: "PdfFileProvider",
        storage: Optional[BaseStorage] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        pdf_generator_cls: Optional[Type[BasePdfGenerator]] = (
            PdfkitPdfGenerator
        ),
        pdf_generator_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def pdf_file(
        self: "PdfFileProvider",
        storage: Optional[BaseStorage] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        pdf_generator_cls: Optional[Type[BasePdfGenerator]] = (
            PdfkitPdfGenerator
        ),
        pdf_generator_kwargs: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a PDF file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param pdf_generator_cls: PDF generator class.
        :param pdf_generator_kwargs: PDF generator kwargs.
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

        if pdf_generator_cls is None:
            pdf_generator_cls = PdfkitPdfGenerator

        if not pdf_generator_kwargs:
            pdf_generator_kwargs = {}
        pdf_generator = pdf_generator_cls(
            generator=self.generator,
            **pdf_generator_kwargs,
        )
        _raw_content = pdf_generator.generate(
            content=content,
        )

        if raw:
            raw_content = BytesValue(_raw_content)
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, _raw_content)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        return file_name
