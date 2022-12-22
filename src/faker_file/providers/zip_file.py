import os
import zipfile
from io import BytesIO
from pathlib import Path
from typing import Any, Dict, Optional, Sequence, Tuple, Union

from faker import Faker
from faker.providers import BaseProvider
from faker.providers.python import Provider

from ..base import FileMixin, StringValue
from ..constants import DEFAULT_IMAGE_MAX_NB_CHARS, DEFAULT_TEXT_MAX_NB_CHARS
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "ZipFileProvider",
    "create_inner_bin_file",
    "create_inner_csv_file",
    "create_inner_docx_file",
    "create_inner_ico_file",
    "create_inner_jpeg_file",
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
        from .bin_file import BinFileProvider
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
        from .csv_file import CsvFileProvider
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
        from .docx_file import DocxFileProvider
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
        from .ico_file import IcoFileProvider
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
        from .jpeg_file import JpegFileProvider
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
        from .ods_file import OdsFileProvider
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
        from .pdf_file import PdfFileProvider
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
        from .png_file import PngFileProvider
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
        from .pptx_file import PptxFileProvider
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
        from .rtf_file import RtfFileProvider
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
        from .svg_file import SvgFileProvider
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
        from .txt_file import TxtFileProvider
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
        from .webp_file import WebpFileProvider
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
        from .xlsx_file import XlsxFileProvider
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
    return ZipFileProvider(generator).zip_file(
        storage=storage,
        prefix=prefix,
        options=options,
        **kwargs,
    )


class ZipFileProvider(BaseProvider, FileMixin):
    """ZIP file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.zip_file import ZipFileProvider

        FAKER = Faker()

        file = ZipFileProvider(FAKER).zip_file()

    Usage example with options:

        from faker_file.providers.zip_file import (
            ZipFileProvider, create_inner_docx_file
        )

        file = ZipFileProvider(FAKER).zip_file(
            prefix="zzz_archive_",
            options={
                "count": 5,
                "create_inner_file_func": create_inner_docx_file,
                "create_inner_file_args": {
                    "prefix": "zzz_docx_file_",
                    "max_nb_chars": 1_024,
                },
                "directory": "zzz",
            }
        )

    Usage example of nested ZIPs:

        file = ZipFileProvider(FAKER).zip_file(
            options={
                "create_inner_file_func": create_inner_zip_file,
                "create_inner_file_args": {
                    "options": {
                        "create_inner_file_func": create_inner_docx_file,
                    }
                }
            }
        )

    If you want to see, which files were included inside the zip, check
    the ``file.data["files"]``.
    """

    extension: str = "zip"

    def zip_file(
        self: "ZipFileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a ZIP file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param options: Options (non-structured) for complex types, such as zip.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        filename = storage.generate_filename(
            prefix=prefix,
            extension=self.extension,
        )
        data = {}
        fs_storage = FileSystemStorage()

        # Specific
        if options:
            """
            A complex case. Could be initialized as follows:

                zip_file = ZipFileProvider(None).file(
                    prefix="zzz_archive_",
                    options={
                        "count": 5,
                        "create_inner_file_func": create_inner_docx_file,
                        "create_inner_file_args": {
                            "prefix": "zzz_file_",
                            "max_nb_chars": 1_024,
                            "content": "{{date}}\r\n{{text}}\r\n{{name}}",
                        },
                        "directory": "zzz",
                    }
                )

            If you want file content/text to be static, replace send some text
            in ``content`` key instead and omit ``content_generator``.
            """
            _count = options.get("count", 5)
            _create_inner_file_func = options.get(
                "create_inner_file_func", create_inner_txt_file
            )
            _create_inner_file_args = options.get("create_inner_file_args", {})
            _dir_path = Path("")
            _directory = options.get("directory", "")

        else:
            # Defaults
            _count = 5
            _create_inner_file_func = create_inner_txt_file
            _create_inner_file_args = {}
            _dir_path = Path("")
            _directory = ""

        _zip_content = BytesIO()
        with zipfile.ZipFile(_zip_content, "w") as __fake_file:
            data["files"] = []
            _kwargs = {"generator": self.generator}
            _kwargs.update(_create_inner_file_args)
            for __i in range(_count):
                __file = _create_inner_file_func(
                    storage=fs_storage,
                    **_kwargs,
                )
                __file_abs_path = fs_storage.abspath(__file)
                __fake_file.write(
                    __file_abs_path,
                    arcname=Path(_directory) / Path(__file).name,
                )
                os.remove(__file_abs_path)  # Clean up temporary files
                data["files"].append(Path(_directory) / Path(__file).name)
            _zip_content.seek(0)
            storage.write_bytes(filename, _zip_content.read())

        # Generic
        file_name = StringValue(storage.relpath(filename))
        if data:
            file_name.data = data
        return file_name
