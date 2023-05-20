from random import choice
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    overload,
)

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider
from typing_extensions import Literal

from ...base import BytesValue, StringValue
from ...constants import (
    DEFAULT_AUDIO_MAX_NB_CHARS,
    DEFAULT_IMAGE_MAX_NB_CHARS,
    DEFAULT_TEXT_MAX_NB_CHARS,
)
from ...storages.base import BaseStorage
from ..base.mp3_generator import BaseMp3Generator
from ..base.pdf_generator import BasePdfGenerator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "create_inner_bin_file",
    "create_inner_csv_file",
    "create_inner_docx_file",
    "create_inner_eml_file",
    "create_inner_epub_file",
    "create_inner_generic_file",
    "create_inner_ico_file",
    "create_inner_jpeg_file",
    "create_inner_mp3_file",
    "create_inner_odp_file",
    "create_inner_ods_file",
    "create_inner_odt_file",
    "create_inner_pdf_file",
    "create_inner_png_file",
    "create_inner_pptx_file",
    "create_inner_rtf_file",
    "create_inner_svg_file",
    "create_inner_tar_file",
    "create_inner_txt_file",
    "create_inner_webp_file",
    "create_inner_xlsx_file",
    "create_inner_xml_file",
    "create_inner_zip_file",
    "fuzzy_choice_create_inner_file",
    "list_create_inner_file",
)


# ************************************************
# ********************* BIN **********************
# ************************************************


@overload
def create_inner_bin_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    length: int = (1 * 1024 * 1024),
    content: Optional[bytes] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_bin_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    length: int = (1 * 1024 * 1024),
    content: Optional[bytes] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_bin_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    length: int = (1 * 1024 * 1024),
    content: Optional[bytes] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner BIN file."""
    try:
        from ..bin_file import BinFileProvider
    except ImportError as err:
        raise err

    return BinFileProvider(generator).bin_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        length=length,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* CSV **********************
# ************************************************


@overload
def create_inner_csv_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    header: Optional[Sequence[str]] = None,
    data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
    num_rows: int = 10,
    include_row_ids: bool = False,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_csv_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    header: Optional[Sequence[str]] = None,
    data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
    num_rows: int = 10,
    include_row_ids: bool = False,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_csv_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    header: Optional[Sequence[str]] = None,
    data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
    num_rows: int = 10,
    include_row_ids: bool = False,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner CSV file."""
    try:
        from ..csv_file import CsvFileProvider
    except ImportError as err:
        raise err

    return CsvFileProvider(generator).csv_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        header=header,
        data_columns=data_columns,
        num_rows=num_rows,
        include_row_ids=include_row_ids,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ******************** DOCX **********************
# ************************************************


@overload
def create_inner_docx_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_docx_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_docx_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner DOCX file."""
    try:
        from ..docx_file import DocxFileProvider
    except ImportError as err:
        raise err

    return DocxFileProvider(generator).docx_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* EML **********************
# ************************************************


@overload
def create_inner_eml_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    options: Optional[Dict[str, Any]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_eml_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    options: Optional[Dict[str, Any]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_eml_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    options: Optional[Dict[str, Any]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner EML file."""
    try:
        from ..eml_file import EmlFileProvider
    except ImportError as err:
        raise err
    return EmlFileProvider(generator).eml_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        options=options,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ******************** EPUB **********************
# ************************************************


@overload
def create_inner_epub_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    title: Optional[str] = None,
    chapter_title: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_epub_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    title: Optional[str] = None,
    chapter_title: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_epub_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    title: Optional[str] = None,
    chapter_title: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner EPUB file."""
    try:
        from ..epub_file import EpubFileProvider
    except ImportError as err:
        raise err

    return EpubFileProvider(generator).epub_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        title=title,
        chapter_title=chapter_title,
        **kwargs,
    )  # type: ignore


# ************************************************
# ******************** Generic *******************
# ************************************************


@overload
def create_inner_generic_file(
    content: Union[bytes, str],
    extension: str,
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_generic_file(
    content: Union[bytes, str],
    extension: str,
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_generic_file(
    content: Union[bytes, str],
    extension: str,
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner generic file."""
    try:
        from ..generic_file import GenericFileProvider
    except ImportError as err:
        raise err

    return GenericFileProvider(generator).generic_file(
        content=content,
        extension=extension,
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* ICO **********************
# ************************************************


@overload
def create_inner_ico_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_ico_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_ico_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner ICO file."""
    try:
        from ..ico_file import IcoFileProvider
    except ImportError as err:
        raise err

    return IcoFileProvider(generator).ico_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ******************** JPEG **********************
# ************************************************


@overload
def create_inner_jpeg_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_jpeg_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_jpeg_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner JPEG file."""
    try:
        from ..jpeg_file import JpegFileProvider
    except ImportError as err:
        raise err

    return JpegFileProvider(generator).jpeg_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* MP3 **********************
# ************************************************


@overload
def create_inner_mp3_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_AUDIO_MAX_NB_CHARS,
    content: Optional[str] = None,
    mp3_generator_cls: Optional[Union[str, Type[BaseMp3Generator]]] = None,
    mp3_generator_kwargs: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_mp3_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_AUDIO_MAX_NB_CHARS,
    content: Optional[str] = None,
    mp3_generator_cls: Optional[Union[str, Type[BaseMp3Generator]]] = None,
    mp3_generator_kwargs: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_mp3_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_AUDIO_MAX_NB_CHARS,
    content: Optional[str] = None,
    mp3_generator_cls: Optional[Union[str, Type[BaseMp3Generator]]] = None,
    mp3_generator_kwargs: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner ODS file."""
    try:
        from ..mp3_file import Mp3FileProvider
    except ImportError as err:
        raise err

    return Mp3FileProvider(generator).mp3_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        content=content,
        mp3_generator_cls=mp3_generator_cls,
        mp3_generator_kwargs=mp3_generator_kwargs,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* ODP **********************
# ************************************************


@overload
def create_inner_odp_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_odp_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    ...


def create_inner_odp_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner ODP file."""
    try:
        from ..odp_file import OdpFileProvider
    except ImportError as err:
        raise err

    return OdpFileProvider(generator).odp_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* ODS **********************
# ************************************************


@overload
def create_inner_ods_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    data_columns: Optional[Dict[str, str]] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_ods_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    data_columns: Optional[Dict[str, str]] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_ods_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    data_columns: Optional[Dict[str, str]] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner ODS file."""
    try:
        from ..ods_file import OdsFileProvider
    except ImportError as err:
        raise err

    return OdsFileProvider(generator).ods_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        data_columns=data_columns,
        num_rows=num_rows,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* ODT **********************
# ************************************************


@overload
def create_inner_odt_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_odt_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_odt_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner ODT file."""
    try:
        from ..odt_file import OdtFileProvider
    except ImportError as err:
        raise err

    return OdtFileProvider(generator).odt_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* PDF **********************
# ************************************************


@overload
def create_inner_pdf_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    pdf_generator_cls: Optional[Union[str, Type[BasePdfGenerator]]] = None,
    pdf_generator_kwargs: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_pdf_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    pdf_generator_cls: Optional[Union[str, Type[BasePdfGenerator]]] = None,
    pdf_generator_kwargs: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_pdf_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    pdf_generator_cls: Optional[Union[str, Type[BasePdfGenerator]]] = None,
    pdf_generator_kwargs: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner PDF file."""
    try:
        from ..pdf_file import PdfFileProvider
    except ImportError as err:
        raise err

    return PdfFileProvider(generator).pdf_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        pdf_generator_cls=pdf_generator_cls,
        pdf_generator_kwargs=pdf_generator_kwargs,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* PNG **********************
# ************************************************


@overload
def create_inner_png_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_png_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_png_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner PNG file."""
    try:
        from ..png_file import PngFileProvider
    except ImportError as err:
        raise err

    return PngFileProvider(generator).png_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ******************** PPTX **********************
# ************************************************


@overload
def create_inner_pptx_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_pptx_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_pptx_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner PPTX file."""
    try:
        from ..pptx_file import PptxFileProvider
    except ImportError as err:
        raise err

    return PptxFileProvider(generator).pptx_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* RTF **********************
# ************************************************


@overload
def create_inner_rtf_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_rtf_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_rtf_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner RTF file."""
    try:
        from ..rtf_file import RtfFileProvider
    except ImportError as err:
        raise err

    return RtfFileProvider(generator).rtf_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* SVG **********************
# ************************************************


@overload
def create_inner_svg_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_svg_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_svg_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner SVG file."""
    try:
        from ..svg_file import SvgFileProvider
    except ImportError as err:
        raise err

    return SvgFileProvider(generator).svg_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* TAR **********************
# ************************************************


@overload
def create_inner_tar_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    options: Optional[Dict[str, Any]] = None,
    compression: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_tar_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    options: Optional[Dict[str, Any]] = None,
    compression: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_tar_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    options: Optional[Dict[str, Any]] = None,
    compression: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner TAR file."""
    try:
        from ..tar_file import TarFileProvider
    except ImportError as err:
        raise err
    return TarFileProvider(generator).tar_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        options=options,
        compression=compression,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* TXT **********************
# ************************************************


@overload
def create_inner_txt_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_txt_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_txt_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner TXT file."""
    try:
        from ..txt_file import TxtFileProvider
    except ImportError as err:
        raise err

    return TxtFileProvider(generator).txt_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ******************** WEBP **********************
# ************************************************


@overload
def create_inner_webp_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_webp_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_webp_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner WEBP file."""
    try:
        from ..webp_file import WebpFileProvider
    except ImportError as err:
        raise err

    return WebpFileProvider(generator).webp_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ******************** XLSX **********************
# ************************************************


@overload
def create_inner_xlsx_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    data_columns: Optional[Dict[str, str]] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_xlsx_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    data_columns: Optional[Dict[str, str]] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_xlsx_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    data_columns: Optional[Dict[str, str]] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner XLSX file."""
    try:
        from ..xlsx_file import XlsxFileProvider
    except ImportError as err:
        raise err

    return XlsxFileProvider(generator).xlsx_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        data_columns=data_columns,
        num_rows=num_rows,
        content=content,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* XML **********************
# ************************************************


@overload
def create_inner_xml_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    root_element: str = "root",
    row_element: str = "row",
    data_columns: Optional[Dict[str, str]] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    encoding: Optional[str] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_xml_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    root_element: str = "root",
    row_element: str = "row",
    data_columns: Optional[Dict[str, str]] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    encoding: Optional[str] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_xml_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    root_element: str = "root",
    row_element: str = "row",
    data_columns: Optional[Dict[str, str]] = None,
    num_rows: int = 10,
    content: Optional[str] = None,
    encoding: Optional[str] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner XML file."""
    try:
        from ..xml_file import XmlFileProvider
    except ImportError as err:
        raise err

    return XmlFileProvider(generator).xml_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        root_element=root_element,
        row_element=row_element,
        data_columns=data_columns,
        num_rows=num_rows,
        content=content,
        encoding=encoding,
        **kwargs,
    )  # type: ignore


# ************************************************
# ********************* ZIP **********************
# ************************************************


@overload
def create_inner_zip_file(
    raw: Literal[True],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    options: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> BytesValue:
    ...


@overload
def create_inner_zip_file(
    raw: Literal[False],
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    options: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> StringValue:
    ...


def create_inner_zip_file(
    raw: bool = False,
    storage: Optional[BaseStorage] = None,
    basename: Optional[str] = None,
    prefix: Optional[str] = None,
    generator: Optional[Union[Faker, Generator, Provider]] = None,
    options: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner ZIP file."""
    try:
        from ..zip_file import ZipFileProvider
    except ImportError as err:
        raise err
    return ZipFileProvider(generator).zip_file(
        raw=raw,
        storage=storage,
        basename=basename,
        prefix=prefix,
        options=options,
        **kwargs,
    )  # type: ignore


# ************************************************
# ******************** OTHER *********************
# ************************************************


def fuzzy_choice_create_inner_file(
    func_choices: List[Tuple[Callable, Dict[str, Any]]],
    **kwargs,
) -> Union[BytesValue, StringValue]:
    """Create inner file from given list of function choices.

    :param func_choices: List of functions to choose from.
    :return: StringValue.

    Usage example:

        from faker import Faker
        from faker_file.providers.helpers.inner import (
            create_inner_docx_file,
            create_inner_epub_file,
            create_inner_txt_file,
            fuzzy_choice_create_inner_file,
        )
        from faker_file.storages.filesystem import FileSystemStorage

        FAKER = Faker()
        STORAGE = FileSystemStorage()

        kwargs = {"storage": STORAGE, "generator": FAKER}
        file = fuzzy_choice_create_inner_file(
            [
                (create_inner_docx_file, kwargs),
                (create_inner_epub_file, kwargs),
                (create_inner_txt_file, kwargs),
            ]
        )

    You could use it in archives to make a variety of different file types
    within the archive.

        from faker import Faker
        from faker_file.providers.helpers.inner import (
            create_inner_docx_file,
            create_inner_epub_file,
            create_inner_txt_file,
            fuzzy_choice_create_inner_file,
        )
        from faker_file.providers.zip_file import ZipFileProvider
        from faker_file.storages.filesystem import FileSystemStorage

        FAKER = Faker()
        STORAGE = FileSystemStorage()

        kwargs = {"storage": STORAGE, "generator": FAKER}
        file = ZipFileProvider(FAKER).zip_file(
            prefix="zzz_archive_",
            options={
                "count": 50,
                "create_inner_file_func": fuzzy_choice_create_inner_file,
                "create_inner_file_args": {
                    "func_choices": [
                        (create_inner_docx_file, kwargs),
                        (create_inner_epub_file, kwargs),
                        (create_inner_txt_file, kwargs),
                    ],
                },
                "directory": "zzz",
            }
        )
    """
    _func, _kwargs = choice(func_choices)
    return _func(**_kwargs)


def list_create_inner_file(
    func_list: List[Tuple[Callable, Dict[str, Any]]],
    **kwargs,
) -> List[Union[BytesValue, StringValue]]:
    """Generates multiple files based on the provided list of functions
    and arguments.

    :param func_list: List of tuples, each containing a function to generate a
        file and its arguments.
    :return: List of generated file names.

    Usage example:

        from faker import Faker
        from faker_file.providers.helpers.inner import (
            create_inner_docx_file,
            create_inner_xml_file,
            list_create_inner_file,
        )
        from faker_file.providers.zip_file import ZipFileProvider
        from faker_file.storages.filesystem import FileSystemStorage

        FAKER = Faker()
        STORAGE = FileSystemStorage()

        kwargs = {"storage": STORAGE, "generator": FAKER}
        file = ZipFileProvider(FAKER).zip_file(
            basename="alice-looking-through-the-glass",
            options={
                "create_inner_file_func": list_create_inner_file,
                "create_inner_file_args": {
                    "func_list": [
                        (create_inner_docx_file, {"basename": "doc"}),
                        (create_inner_xml_file, {"basename": "doc_metadata"}),
                        (create_inner_xml_file, {"basename": "doc_isbn"}),
                    ],
                },
            }
        )

    Note, that while all other inner functions return
    back `Union[BytesValue, StringValue]` value, `list_create_inner_file`
    returns back a `List[Union[BytesValue, StringValue]]` value.

    Notably, all inner functions were designed to support archives (such as
    ZIP, TAR and EML, but the list may grow in the future). If the inner
    function passed in the `create_inner_file_func` argument returns a List
    of `Union[BytesValue, StringValue]` values, the `option` argument is being
    ignored and generated files are simply limited to what has been passed
    in the `func_list` list of tuples.
    """
    created_files = []
    for func, kwargs in func_list:
        file = func(**kwargs)
        created_files.append(file)
    return created_files
