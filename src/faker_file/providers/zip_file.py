import os
import zipfile
from io import BytesIO
from pathlib import Path
from typing import Any, Dict, Optional, Union, overload

from faker.providers import BaseProvider

from ..base import BytesValue, FileMixin, StringValue, returns_list
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage
from .helpers.inner import create_inner_txt_file

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("ZipFileProvider",)


class ZipFileProvider(BaseProvider, FileMixin):
    """ZIP file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.zip_file import ZipFileProvider

        FAKER = Faker()
        FAKER.add_provider(ZipFileProvider)

        file = FAKER.zip_file()

    Usage example with options:

    .. code-block:: python

        from faker_file.providers.helpers.inner import create_inner_docx_file

        file = FAKER.zip_file(
            prefix="zzz_archive_",
            options={
                "count": 5,
                "create_inner_file_func": create_inner_docx_file,
                "create_inner_file_args": {
                    "prefix": "zzz_docx_file_",
                    "max_nb_chars": 1_024,
                },
                "directory": "zzz",
            },
        )

    Usage example of nested ZIPs:

    .. code-block:: python

        from faker_file.providers.helpers.inner import create_inner_zip_file

        file = FAKER.zip_file(
            options={
                "create_inner_file_func": create_inner_zip_file,
                "create_inner_file_args": {
                    "options": {
                        "create_inner_file_func": create_inner_docx_file,
                    },
                },
            },
        )

    If you want to see, which files were included inside the ZIP, check
    the ``file.data["files"]``.
    """

    extension: str = "zip"

    @overload
    def zip_file(
        self: "ZipFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def zip_file(
        self: "ZipFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        ...

    def zip_file(
        self: "ZipFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a ZIP file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param options: Options (non-structured) for complex types, such as ZIP.
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

        data: Dict[str, Any] = {
            "inner": {},
            "files": [],
            "filename": filename,
            "storage": storage,
        }
        fs_storage = FileSystemStorage()

        # Specific
        if options:
            """
            A complex case. Could be initialized as follows:

            .. code-block:: python

                zip_file = FAKER.zip_file(
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
                    },
                )
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
            _kwargs = {"generator": self.generator}
            _kwargs.update(_create_inner_file_args)

            # If _create_inner_file_func returns a list of values
            if returns_list(_create_inner_file_func):
                _files = _create_inner_file_func(
                    storage=fs_storage,
                    **_kwargs,
                )
                for __file in _files:
                    data["inner"][str(__file)] = __file
                    __file_abs_path = fs_storage.abspath(__file)
                    __fake_file.write(
                        __file_abs_path,
                        arcname=Path(_directory) / Path(__file).name,
                    )
                    os.remove(__file_abs_path)  # Clean up temporary files
                    data["files"].append(Path(_directory) / Path(__file).name)

            # If _create_inner_file_func returns a single value
            else:
                for __i in range(_count):
                    __file = _create_inner_file_func(
                        storage=fs_storage,
                        **_kwargs,
                    )
                    data["inner"][str(__file)] = __file
                    __file_abs_path = fs_storage.abspath(__file)
                    __fake_file.write(
                        __file_abs_path,
                        arcname=Path(_directory) / Path(__file).name,
                    )
                    os.remove(__file_abs_path)  # Clean up temporary files
                    data["files"].append(Path(_directory) / Path(__file).name)

        if raw:
            raw_content = BytesValue(_zip_content.getvalue())
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, _zip_content.getvalue())

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
