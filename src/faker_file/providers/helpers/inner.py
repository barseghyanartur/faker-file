from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from faker import Faker
from faker.providers.python import Provider

from ...base import StringValue
from ...constants import (
    DEFAULT_AUDIO_MAX_NB_CHARS,
    DEFAULT_IMAGE_MAX_NB_CHARS,
    DEFAULT_TEXT_MAX_NB_CHARS,
)
from ...storages.base import BaseStorage
from ..mp3_file.generators.base import BaseMp3Generator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "create_inner_bin_file",
    "create_inner_csv_file",
    "create_inner_docx_file",
    "create_inner_eml_file",
    "create_inner_epub_file",
    "create_inner_ico_file",
    "create_inner_jpeg_file",
    "create_inner_mp3_file",
    "create_inner_ods_file",
    "create_inner_pdf_file",
    "create_inner_png_file",
    "create_inner_pptx_file",
    "create_inner_rtf_file",
    "create_inner_svg_file",
    "create_inner_txt_file",
    "create_inner_webp_file",
    "create_inner_xlsx_file",
    "create_inner_zip_file",
)


def create_inner_bin_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    length: int = (1 * 1024 * 1024),
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner BIN file."""
    try:
        from ..bin_file import BinFileProvider
    except ImportError as err:
        raise err

    return BinFileProvider(generator).bin_file(
        storage=storage,
        prefix=prefix,
        length=length,
        content=content,
        **kwargs,
    )


def create_inner_csv_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    header: Optional[Sequence[str]] = None,
    data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
    num_rows: int = 10,
    include_row_ids: bool = False,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner CSV file."""
    try:
        from ..csv_file import CsvFileProvider
    except ImportError as err:
        raise err

    return CsvFileProvider(generator).csv_file(
        storage=storage,
        prefix=prefix,
        header=header,
        data_columns=data_columns,
        num_rows=num_rows,
        include_row_ids=include_row_ids,
        content=content,
        **kwargs,
    )


def create_inner_docx_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner DOCX file."""
    try:
        from ..docx_file import DocxFileProvider
    except ImportError as err:
        raise err

    return DocxFileProvider(generator).docx_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_eml_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    options: Optional[Dict[str, Any]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner EML file."""
    try:
        from ..eml_file import EmlFileProvider
    except ImportError as err:
        raise err
    return EmlFileProvider(generator).eml_file(
        storage=storage,
        prefix=prefix,
        options=options,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_epub_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    title: Optional[str] = None,
    chapter_title: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner EPUB file."""
    try:
        from ..epub_file import EpubFileProvider
    except ImportError as err:
        raise err

    return EpubFileProvider(generator).epub_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        title=title,
        chapter_title=chapter_title,
        **kwargs,
    )


def create_inner_ico_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner ICO file."""
    try:
        from ..ico_file import IcoFileProvider
    except ImportError as err:
        raise err

    return IcoFileProvider(generator).ico_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_jpeg_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner JPEG file."""
    try:
        from ..jpeg_file import JpegFileProvider
    except ImportError as err:
        raise err

    return JpegFileProvider(generator).jpeg_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_mp3_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_AUDIO_MAX_NB_CHARS,
    content: Optional[str] = None,
    mp3_generator_cls: Type[BaseMp3Generator] = None,
    **kwargs,
) -> StringValue:
    """Create inner ODS file."""
    try:
        from ..mp3_file import Mp3FileProvider
    except ImportError as err:
        raise err

    return Mp3FileProvider(generator).mp3_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        content=content,
        mp3_generator_cls=mp3_generator_cls,
        **kwargs,
    )


def create_inner_ods_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    data_columns: Dict[str, str] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner ODS file."""
    try:
        from ..ods_file import OdsFileProvider
    except ImportError as err:
        raise err

    return OdsFileProvider(generator).ods_file(
        storage=storage,
        prefix=prefix,
        data_columns=data_columns,
        num_rows=num_rows,
        content=content,
        **kwargs,
    )


def create_inner_pdf_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner PDF file."""
    try:
        from ..pdf_file import PdfFileProvider
    except ImportError as err:
        raise err

    return PdfFileProvider(generator).pdf_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_png_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner PNG file."""
    try:
        from ..png_file import PngFileProvider
    except ImportError as err:
        raise err

    return PngFileProvider(generator).png_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_pptx_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner PPTX file."""
    try:
        from ..pptx_file import PptxFileProvider
    except ImportError as err:
        raise err

    return PptxFileProvider(generator).pptx_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_rtf_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner RTF file."""
    try:
        from ..rtf_file import RtfFileProvider
    except ImportError as err:
        raise err

    """Create inner RTF file."""
    return RtfFileProvider(generator).rtf_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_svg_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner SVG file."""
    try:
        from ..svg_file import SvgFileProvider
    except ImportError as err:
        raise err

    return SvgFileProvider(generator).svg_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_txt_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner TXT file."""
    try:
        from ..txt_file import TxtFileProvider
    except ImportError as err:
        raise err

    """Create inner TXT file."""
    return TxtFileProvider(generator).txt_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_webp_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner WEBP file."""
    try:
        from ..webp_file import WebpFileProvider
    except ImportError as err:
        raise err

    return WebpFileProvider(generator).webp_file(
        storage=storage,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_xlsx_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    data_columns: Dict[str, str] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    """Create inner XLSX file."""
    try:
        from ..xlsx_file import XlsxFileProvider
    except ImportError as err:
        raise err

    return XlsxFileProvider(generator).xlsx_file(
        storage=storage,
        prefix=prefix,
        data_columns=data_columns,
        num_rows=num_rows,
        content=content,
        **kwargs,
    )


def create_inner_zip_file(
    storage: BaseStorage = None,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    options: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> StringValue:
    """Create inner ZIP file."""
    try:
        from ..zip_file import ZipFileProvider
    except ImportError as err:
        raise err
    return ZipFileProvider(generator).zip_file(
        storage=storage,
        prefix=prefix,
        options=options,
        **kwargs,
    )
