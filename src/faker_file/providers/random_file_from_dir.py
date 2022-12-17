import os
import shutil
from pathlib import Path
from random import choice
from typing import Optional

from faker.providers import BaseProvider

from ..base import DEFAULT_REL_PATH, FileMixin, StringValue

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("RandomFileFromDirProvider",)


class RandomFileFromDirProvider(BaseProvider, FileMixin):
    """Random file from given directory provider.

    Usage example:

        from faker_file.providers.random_file_from_dir import (
            RandomFileFromDirProvider,
        )

        file = RandomFileFromDirProvider(None).random_file_from_dir(
            source_dir_path="/tmp/tmp/",
        )

    Usage example with options:

        from faker_file.providers.random_file_from_dir import (
            RandomFileFromDirProvider,
        )

        file = RandomFileFromDirProvider(None).random_file_from_dir(
            source_dir_path="/tmp/tmp/",
            prefix="zzz",
        )
    """

    extension: str = ""

    def random_file_from_dir(
        self: "RandomFileFromDirProvider",
        source_dir_path: str,
        root_path: str = None,
        rel_path: str = DEFAULT_REL_PATH,
        prefix: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Pick a random file from given directory.

        :param source_dir_path: Source files directory.
        :param root_path: Path of your files root directory (in case of Django
            it would be `settings.MEDIA_ROOT`).
        :param rel_path: Relative path (from root directory).
        :param prefix: File name prefix.

        :return: Relative path (from root directory) of the generated file.
        """
        source_file_choices = [
            os.path.join(source_dir_path, _f)
            for _f in os.listdir(source_dir_path)
            if os.path.isfile(os.path.join(source_dir_path, _f))
        ]
        source_file_path = choice(source_file_choices)
        source_file = Path(source_file_path)

        # Generic
        file_name = self._generate_filename(
            root_path=root_path,
            rel_path=rel_path,
            prefix=prefix,
            extension=source_file.suffix[1:],
        )
        shutil.copyfile(source_file_path, file_name)

        # Generic
        file_name = StringValue(os.path.relpath(file_name, root_path))
        return file_name
