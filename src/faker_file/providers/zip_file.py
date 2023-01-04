import os
import zipfile
from io import BytesIO
from pathlib import Path
from typing import Any, Dict, Optional

from faker.providers import BaseProvider

from ..base import FileMixin, StringValue
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage
from .helpers.inner import create_inner_txt_file

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("ZipFileProvider",)


class ZipFileProvider(BaseProvider, FileMixin):
    """ZIP file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.zip_file import ZipFileProvider

        FAKER = Faker()

        file = ZipFileProvider(FAKER).zip_file()

    Usage example with options:

        from faker_file.providers.helpers.inner import create_inner_docx_file
        from faker_file.providers.zip_file import ZipFileProvider

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

        from faker_file.providers.helpers.inner import create_inner_zip_file

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

    If you want to see, which files were included inside the ZIP, check
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
        :param options: Options (non-structured) for complex types, such as ZIP.
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

                zip_file = ZipFileProvider(None).zip_file(
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
