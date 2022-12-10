import os
import zipfile
from pathlib import Path
from typing import Any, Dict, Optional, Sequence, Tuple, Union

from faker import Faker
from faker.providers import BaseProvider
from faker.providers.python import Provider

from ..base import DEFAULT_REL_PATH, FileMixin, StringValue
from ..constants import DEFAULT_IMAGE_MAX_NB_CHARS, DEFAULT_TEXT_MAX_NB_CHARS

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
    "create_inner_svg_file",
    "create_inner_txt_file",
    "create_inner_webp_file",
    "create_inner_xlsx_file",
    "create_inner_zip_file",
)


def create_inner_bin_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        length=length,
        content=content,
        **kwargs,
    )


def create_inner_csv_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        header=header,
        data_columns=data_columns,
        num_rows=num_rows,
        include_row_ids=include_row_ids,
        content=content,
        **kwargs,
    )


def create_inner_docx_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_ico_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_jpeg_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_ods_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        data_columns=data_columns,
        num_rows=num_rows,
        content=content,
        **kwargs,
    )


def create_inner_pdf_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_png_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_pptx_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_svg_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_txt_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
    wrap_chars_after: Optional[int] = None,
    content: Optional[str] = None,
    **kwargs,
) -> StringValue:
    try:
        from .txt_file import TxtFileProvider
    except ImportError as err:
        raise err

    """Create inner TXT file."""
    return TxtFileProvider(generator).txt_file(
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_webp_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        max_nb_chars=max_nb_chars,
        wrap_chars_after=wrap_chars_after,
        content=content,
        **kwargs,
    )


def create_inner_xlsx_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
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
        root_path=root_path,
        rel_path=rel_path,
        prefix=prefix,
        data_columns=data_columns,
        num_rows=num_rows,
        content=content,
        **kwargs,
    )


def create_inner_zip_file(
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
    prefix: Optional[str] = None,
    generator: Union[Provider, Faker] = None,
    options: Optional[Dict[str, Any]] = None,
    **kwargs,
) -> StringValue:
    """Create inner ZIP file."""
    return ZipFileProvider(generator).zip_file(
        root_path=root_path,
        rel_path=rel_path,
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
        root_path: Optional[str] = None,
        rel_path: str = DEFAULT_REL_PATH,
        prefix: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a ZIP file with random text.

        :param root_path: Path of your files root directory (in case of Django
            it would be `settings.MEDIA_ROOT`).
        :param rel_path: Relative path (from root directory).
        :param prefix: File name prefix.
        :param options: Options (non-structured) for complex types, such as zip.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        file_name = self._generate_filename(
            root_path=root_path,
            rel_path=rel_path,
            prefix=prefix,
        )
        data = {}

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
            _dir_path = Path(os.path.join(root_path or "", rel_path)).parent
            _directory = options.get("directory", "")

        else:
            # Defaults
            _count = 5
            _create_inner_file_func = create_inner_txt_file
            _create_inner_file_args = {}
            _dir_path = Path("")
            _directory = ""

        with zipfile.ZipFile(file_name, "w") as __fake_file:
            data["files"] = []
            _kwargs = {"generator": self.generator}
            _kwargs.update(_create_inner_file_args)
            for __i in range(_count):
                __file = _create_inner_file_func(
                    rel_path=rel_path,
                    **_kwargs,
                )
                __fake_file.write(
                    _dir_path / __file,
                    arcname=Path(_directory) / Path(__file).name,
                )
                os.remove(__file)  # Clean up temporary files
                data["files"].append(Path(_directory) / Path(__file).name)

        # Generic
        file_name = StringValue(os.path.relpath(file_name, root_path))
        if data:
            file_name.data = data
        return file_name
