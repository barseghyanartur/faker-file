# import mimetypes
import os
from email.message import EmailMessage
from email.policy import default
from typing import Any, Dict, Optional

from faker.providers import BaseProvider

from ..base import FileMixin, StringValue
from ..constants import DEFAULT_TEXT_MAX_NB_CHARS
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

        from faker import Faker
        from faker_file.providers.eml_file import EmlFileProvider

        FAKER = Faker()

        file = EmlFileProvider(FAKER).eml_file()

    Usage example with attachments:

        from faker_file.providers.helpers.inner import create_inner_docx_file
        from faker_file.providers.eml_file import EmlFileProvider

        file = EmlFileProvider(FAKER).eml_file(
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

        from faker_file.providers.helpers.inner import create_inner_eml_file

        file = EmlFileProvider(FAKER).eml_file(
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

    def eml_file(
        self: "EmlFileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate an EML file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param options: Options (non-structured) for complex types, such as ZIP.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        filename = storage.generate_filename(
            prefix=prefix,
            extension=self.extension,
        )
        fs_storage = FileSystemStorage()

        content = self._generate_text_content(
            max_nb_chars=max_nb_chars,
            wrap_chars_after=wrap_chars_after,
            content=content,
        )
        data = {
            "content": content,
            "inner": {},
        }

        msg = EmailMessage()
        msg["To"] = self.generator.email()
        msg["From"] = self.generator.email()
        msg["Subject"] = self.generator.sentence()
        msg.set_content(content)
        data.update(
            {
                "to": msg["To"],
                "from": msg["From"],
                "subject": msg["Subject"],
                "content": content,
            }
        )

        # Specific
        if options:
            """
            A complex case. Could be initialized as follows:

                eml_file = EmlFileProvider(FAKER).eml_file(
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

        for __i in range(_count):
            __file = _create_inner_file_func(
                storage=fs_storage,
                **_kwargs,
            )
            data["inner"][str(__file)] = __file
            __file_abs_path = fs_storage.abspath(__file)
            # _content_type, _encoding = mimetypes.guess_type(__file_abs_path)
            # if _content_type is None or _encoding is not None:
            #     # No guess could be made, or the file is
            #     # encoded (compressed), so use a generic bag-of-bits type.
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

        storage.write_bytes(filename, msg.as_bytes(policy=default))

        # Generic
        file_name = StringValue(storage.relpath(filename))
        if data:
            file_name.data = data
        return file_name
