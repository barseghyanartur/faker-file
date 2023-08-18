# import mimetypes
import os
from email.message import EmailMessage
from email.policy import default
from typing import Any, Callable, Dict, Optional, Union, overload

from faker import Faker
from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.python import Provider

from ..base import (
    DEFAULT_FORMAT_FUNC,
    BytesValue,
    FileMixin,
    StringValue,
    returns_list,
)
from ..constants import DEFAULT_TEXT_MAX_NB_CHARS
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage
from .helpers.inner import create_inner_txt_file

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("EmlFileProvider",)


class EmlFileProvider(BaseProvider, FileMixin):
    """EML file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.eml_file import EmlFileProvider

        FAKER = Faker()
        FAKER.add_provider(EmlFileProvider)

        file = FAKER.eml_file()

    Usage example with attachments:

    .. code-block:: python

        from faker_file.providers.helpers.inner import create_inner_docx_file

        file = FAKER.eml_file(
            prefix="zzz_email_",
            options={
                "count": 5,
                "create_inner_file_func": create_inner_docx_file,
                "create_inner_file_args": {
                    "prefix": "zzz_docx_file_",
                    "max_nb_chars": 1_024,
                },
            }
        )

    Usage example of nested EMLs attachments:

    .. code-block:: python

        from faker_file.providers.helpers.inner import create_inner_eml_file

        file = FAKER.eml_file(
            options={
                "create_inner_file_func": create_inner_eml_file,
                "create_inner_file_args": {
                    "options": {
                        "create_inner_file_func": create_inner_docx_file,
                    }
                }
            }
        )

    If you want to see, which files were included inside the EML, check
    the ``file.data["files"]``.
    """

    extension: str = "eml"

    @overload
    def eml_file(
        self: "EmlFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        subject: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def eml_file(
        self: "EmlFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        subject: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def eml_file(
        self: "EmlFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        subject: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate an EML file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param options: Options (non-structured) for complex types, such as ZIP.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param subject: Email subject. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
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
        fs_storage = FileSystemStorage()

        content = self._generate_text_content(
            max_nb_chars=max_nb_chars,
            wrap_chars_after=wrap_chars_after,
            content=content,
            format_func=format_func,
        )
        subject = self._generate_text_content(
            max_nb_chars=20,
            wrap_chars_after=wrap_chars_after,
            content=subject,
            format_func=format_func,
        )
        data: Dict[str, Any] = {
            "content": f"{subject}\n {content}",
            "inner": {},
            "filename": filename,
            "storage": storage,
        }

        msg = EmailMessage()
        msg["To"] = self.generator.email()
        msg["From"] = self.generator.email()
        msg["Subject"] = subject
        msg.set_content(content)
        data.update(
            {
                "to": msg["To"],
                "from": msg["From"],
                "subject": msg["Subject"],
                "body": content,
            }
        )

        # Specific
        if options:
            """
            A complex case. Could be initialized as follows:

            .. code-block:: python

                eml_file = FAKER.eml_file(
                    prefix="zzz_email_",
                    options={
                        "count": 5,
                        "create_inner_file_func": create_inner_docx_file,
                        "create_inner_file_args": {
                            "prefix": "zzz_file_",
                            "max_nb_chars": 1_024,
                            "content": "{{date}}\r\n{{text}}\r\n{{name}}",
                        },
                    }
                )
            """
            _count = options.get("count", 5)
            _create_inner_file_func = options.get(
                "create_inner_file_func", create_inner_txt_file
            )
            _create_inner_file_args = options.get("create_inner_file_args", {})

        else:
            # Defaults
            _count = 0
            _create_inner_file_func = create_inner_txt_file
            _create_inner_file_args = {}

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
                # _content_type, _encoding = mimetypes.guess_type(
                #     __file_abs_path
                # )
                # if _content_type is None or _encoding is not None:
                #     # No guess could be made, or the file is
                #     # encoded (compressed), so use a generic bag-of-bits
                #     # type.
                #     _content_type = "application/octet-stream"
                _content_type = "application/octet-stream"
                _maintype, _subtype = _content_type.split("/", 1)
                with open(__file_abs_path, "rb") as _fp:
                    _file_data = _fp.read()
                    msg.add_attachment(
                        _file_data,
                        maintype=_maintype,
                        subtype=_subtype,
                        filename=os.path.basename(__file),
                    )
                os.remove(__file_abs_path)  # Clean up temporary files
        # If _create_inner_file_func returns a single value
        else:
            for __i in range(_count):
                __file = _create_inner_file_func(
                    storage=fs_storage,
                    **_kwargs,
                )
                data["inner"][str(__file)] = __file
                __file_abs_path = fs_storage.abspath(__file)
                # _content_type, _encoding = mimetypes.guess_type(
                #     __file_abs_path
                # )
                # if _content_type is None or _encoding is not None:
                #     # No guess could be made, or the file is
                #     # encoded (compressed), so use a generic bag-of-bits
                #     # type.
                #     _content_type = "application/octet-stream"
                _content_type = "application/octet-stream"
                _maintype, _subtype = _content_type.split("/", 1)
                with open(__file_abs_path, "rb") as _fp:
                    _file_data = _fp.read()
                    msg.add_attachment(
                        _file_data,
                        maintype=_maintype,
                        subtype=_subtype,
                        filename=os.path.basename(__file),
                    )
                os.remove(__file_abs_path)  # Clean up temporary files

        if raw:
            raw_content = BytesValue(msg.as_bytes(policy=default))
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, msg.as_bytes(policy=default))

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
