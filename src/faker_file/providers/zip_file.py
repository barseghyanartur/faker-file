import os
import zipfile
from pathlib import Path
from typing import Any, Dict, Optional

from faker.providers import BaseProvider

from ..base import DEFAULT_REL_PATH, FileMixin, StringValue
from ..content_generators import BaseContentGenerator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "ZipFileProvider",
    "create_inner_txt_file",
    "create_inner_pdf_file",
    "create_inner_docx_file",
    "create_inner_pptx_file",
)


def create_inner_txt_file(
    max_nb_chars: int = 100_000,
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
    wrap_chars_after: Optional[int] = None,
    prefix: Optional[str] = None,
    content_generator: Optional[BaseContentGenerator] = None,
    content: Optional[str] = None,
):
    try:
        from .txt_file import TxtFileProvider
    except ImportError as err:
        raise err

    """Create inner TXT file."""
    return TxtFileProvider(None).txt_file(
        max_nb_chars=max_nb_chars,
        root_path=root_path,
        rel_path=rel_path,
        wrap_chars_after=wrap_chars_after,
        prefix=prefix,
        content_generator=content_generator,
        content=content,
    )


def create_inner_docx_file(
    max_nb_chars: int = 100_000,
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
    wrap_chars_after: Optional[int] = None,
    prefix: Optional[str] = None,
    content_generator: Optional[BaseContentGenerator] = None,
    content: Optional[str] = None,
):
    """Create inner DOCX file."""
    try:
        from .docx_file import DocxFileProvider
    except ImportError as err:
        raise err

    return DocxFileProvider(None).docx_file(
        max_nb_chars=max_nb_chars,
        root_path=root_path,
        rel_path=rel_path,
        wrap_chars_after=wrap_chars_after,
        prefix=prefix,
        content_generator=content_generator,
        content=content,
    )


def create_inner_pdf_file(
    max_nb_chars: int = 100_000,
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
    wrap_chars_after: Optional[int] = None,
    prefix: Optional[str] = None,
    content_generator: Optional[BaseContentGenerator] = None,
    content: Optional[str] = None,
):
    """Create inner PDF file."""
    try:
        from .pdf_file import PdfFileProvider
    except ImportError as err:
        raise err

    return PdfFileProvider(None).pdf_file(
        max_nb_chars=max_nb_chars,
        root_path=root_path,
        rel_path=rel_path,
        wrap_chars_after=wrap_chars_after,
        prefix=prefix,
        content_generator=content_generator,
        content=content,
    )


def create_inner_pptx_file(
    max_nb_chars: int = 100_000,
    root_path: str = None,
    rel_path: str = DEFAULT_REL_PATH,
    wrap_chars_after: Optional[int] = None,
    prefix: Optional[str] = None,
    content_generator: Optional[BaseContentGenerator] = None,
    content: Optional[str] = None,
):
    """Create inner PPTX file."""
    try:
        from .pptx_file import PptxFileProvider
    except ImportError as err:
        raise err

    return PptxFileProvider(None).pptx_file(
        max_nb_chars=max_nb_chars,
        root_path=root_path,
        rel_path=rel_path,
        wrap_chars_after=wrap_chars_after,
        prefix=prefix,
        content_generator=content_generator,
        content=content,
    )


class ZipFileProvider(BaseProvider, FileMixin):
    """ZIP file provider.

    Usage example:

        from faker_file.providers.zip_file import ZipFileProvider

        file = ZipFileProvider(None).zip_file()

    Usage example with options:

        from faker_file.providers.zip_file import (
            ZipFileProvider, create_inner_docx_file
        )

        file = ZipFileProvider(None).zip_file(
            prefix="zzz_archive_",
            options={
                "count": 5,
                "create_inner_file_func": create_inner_docx_file,
                "max_nb_chars": 1_024,
                "prefix": "zzz_docx_file_",
                "directory": "zzz",
            }
        )

    If you want to see, which files were included inside the zip, check
    the ``file.data["files"]``.
    """

    extension: str = "zip"

    def zip_file(
        self,
        root_path: Optional[str] = None,
        rel_path: str = DEFAULT_REL_PATH,
        prefix: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a file with random text.

        :param root_path:
        :param rel_path: Relative path (from Django MEDIA_ROOT directory).
        :param prefix: File name prefix.
        :param options: Options (non-structured) for complex types, such as zip.
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
        if options:
            """
            A complex case. Could be initialized as follows:

                zip_file = ZipFileProvider(None).file(
                    prefix="zzz_archive_",
                    options={
                        "count": 5,
                        "create_inner_file_func": create_inner_docx_file,
                        "max_nb_chars": 1_024,
                        "prefix": "zzz_file_",
                        "content_generator": DEFAULT_CONTENT_GENERATOR,
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
            _max_nb_chars = options.get("max_nb_chars", 1_024)
            _prefix = options.get("prefix", Path(file_name).stem)
            _content_generator = options.get("content_generator", None)
            _content = options.get("content", None)
            _dir_path = Path(os.path.join(root_path or "", rel_path)).parent
            _directory = options.get("directory", "")

        else:
            # Defaults
            _count = 5
            _create_inner_file_func = create_inner_txt_file
            _max_nb_chars = 1_024
            _prefix = None
            _content_generator = None
            _content = None
            _dir_path = Path("")
            _directory = ""

        with zipfile.ZipFile(file_name, "w") as __fake_file:
            data["files"] = []
            for __i in range(_count):
                __file = _create_inner_file_func(
                    max_nb_chars=_max_nb_chars,
                    rel_path=rel_path,
                    prefix=_prefix,
                    content_generator=_content_generator,
                    content=_content,
                )
                __fake_file.write(
                    _dir_path / __file,
                    arcname=Path(_directory) / Path(__file).name,
                )
                data["files"].append(Path(_directory) / Path(__file).name)

        # Generic
        file_name = StringValue(os.path.relpath(file_name, root_path))
        if data:
            file_name.data = data
        return file_name
