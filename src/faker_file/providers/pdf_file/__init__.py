from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    overload,
)

from faker import Faker
from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.python import Provider

from ...base import (
    DEFAULT_FORMAT_FUNC,
    BytesValue,
    DynamicTemplate,
    FileMixin,
    StringValue,
)
from ...constants import DEFAULT_TEXT_MAX_NB_CHARS
from ...helpers import load_class_from_path
from ...registry import FILE_REGISTRY
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage
from ..base.pdf_generator import BasePdfGenerator
from ..mixins.graphic_image_mixin import GraphicImageMixin

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "DEFAULT_PDF_GENERATOR",
    "GraphicPdfFileProvider",
    "PDFKIT_PDF_GENERATOR",
    "PIL_PDF_GENERATOR",
    "PdfFileProvider",
    "REPORTLAB_PDF_GENERATOR",
)

PDFKIT_PDF_GENERATOR = (
    "faker_file.providers.pdf_file.generators.pdfkit_generator"
    ".PdfkitPdfGenerator"
)
PIL_PDF_GENERATOR = (
    "faker_file.providers.pdf_file.generators.pil_generator.PilPdfGenerator"
)
REPORTLAB_PDF_GENERATOR = (
    "faker_file.providers.pdf_file.generators.reportlab_generator"
    ".ReportlabPdfGenerator"
)
DEFAULT_PDF_GENERATOR = PDFKIT_PDF_GENERATOR


class PdfFileProvider(BaseProvider, FileMixin):
    """PDF file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.pdf_file import PdfFileProvider

        FAKER = Faker()
        FAKER.add_provider(PdfFileProvider)

        file = FAKER.pdf_file()

    Usage example with options:

    .. code-block:: python

        file = FAKER.pdf_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

    .. code-block:: python

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.pdf_file(
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

    .. code-block:: python

        from faker_file.providers.pdf_file.generators import (
            reportlab_generator,
        )

        file = FAKER.pdf_file(
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
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[Union[str, DynamicTemplate]] = None,
        pdf_generator_cls: Optional[Union[str, Type[BasePdfGenerator]]] = (
            DEFAULT_PDF_GENERATOR
        ),
        pdf_generator_kwargs: Optional[Dict[str, Any]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def pdf_file(
        self: "PdfFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[Union[str, DynamicTemplate]] = None,
        pdf_generator_cls: Optional[Union[str, Type[BasePdfGenerator]]] = (
            DEFAULT_PDF_GENERATOR
        ),
        pdf_generator_kwargs: Optional[Dict[str, Any]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def pdf_file(
        self: "PdfFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[Union[str, DynamicTemplate]] = None,
        pdf_generator_cls: Optional[Union[str, Type[BasePdfGenerator]]] = (
            DEFAULT_PDF_GENERATOR
        ),
        pdf_generator_kwargs: Optional[Dict[str, Any]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a PDF file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param pdf_generator_cls: PDF generator class.
        :param pdf_generator_kwargs: PDF generator kwargs.
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

        if pdf_generator_cls is None:
            pdf_generator_cls = DEFAULT_PDF_GENERATOR

        if isinstance(pdf_generator_cls, str):
            pdf_generator_cls = load_class_from_path(pdf_generator_cls)

        if not pdf_generator_kwargs:
            pdf_generator_kwargs = {}

        pdf_generator_kwargs["content_specs"] = {
            "max_nb_chars": max_nb_chars,
            "wrap_chars_after": wrap_chars_after,
        }

        pdf_generator = pdf_generator_cls(
            generator=self.generator,
            **pdf_generator_kwargs,
        )
        data = {"content": "", "filename": filename, "storage": storage}
        if isinstance(content, DynamicTemplate):
            _content = content
        else:
            _content = self._generate_text_content(
                max_nb_chars=max_nb_chars,
                wrap_chars_after=wrap_chars_after,
                content=content,
                format_func=format_func,
            )
            data["content"] = _content

        _raw_content = pdf_generator.generate(
            content=_content,
            data=data,
            provider=self,
        )

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


class GraphicPdfFileProvider(BaseProvider, GraphicImageMixin):
    """Graphic PDF file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.pdf_file import GraphicPdfFileProvider

        FAKER = Faker()
        FAKER.add_provider(GraphicPdfFileProvider)

        file = FAKER.graphic_pdf_file()

    Usage example with options:

    .. code-block:: python

        file = FAKER.graphic_pdf_file(
            prefix="zzz",
            size=(800, 800),
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

    .. code-block:: python

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.graphic_pdf_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            basename="yyy",
            size=(1024, 1024),
        )
    """

    extension: str = "pdf"
    image_format: str = "pdf"

    @overload
    def graphic_pdf_file(
        self: "GraphicPdfFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        size: Tuple[int, int] = (256, 256),
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def graphic_pdf_file(
        self: "GraphicPdfFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        size: Tuple[int, int] = (256, 256),
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def graphic_pdf_file(
        self: "GraphicPdfFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        size: Tuple[int, int] = (256, 256),
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a graphic PDF file with random lines.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param size: Image size in pixels.
        :param hue: Read more about
            ://faker.readthedocs.io/en/dev/providers/faker.providers.color.html
        :param luminosity: If given, the output string would be separated
             by line breaks after the given position.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
        """
        return self._image_file(
            image_format=self.image_format,
            storage=storage,
            basename=basename,
            prefix=prefix,
            size=size,
            hue=hue,
            luminosity=luminosity,
            raw=raw,
            **kwargs,
        )
