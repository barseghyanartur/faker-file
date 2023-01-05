from io import BytesIO
from typing import Optional

from faker.providers import BaseProvider
from gtts import gTTS

from ..base import FileMixin, StringValue
from ..constants import DEFAULT_AUDIO_MAX_NB_CHARS
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("Mp3FileProvider",)


class Mp3FileProvider(BaseProvider, FileMixin):
    """MP3 file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.mp3_file import Mp3FileProvider

        file = Mp3FileProvider(Faker()).mp3_file()

    Usage example with options:

        file = Mp3FileProvider(Faker()).mp3_file(
            prefix="zzz",
            max_nb_chars=500,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = Mp3FileProvider(Faker()).mp3_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            max_nb_chars=500,
        )
    """

    extension: str = "mp3"

    def mp3_file(
        self: "Mp3FileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_AUDIO_MAX_NB_CHARS,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a MP3 file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
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

        content = self._generate_text_content(
            max_nb_chars=max_nb_chars,
            content=content,
        )

        tts = gTTS(content)

        with BytesIO() as __fake_file:
            tts.write_to_fp(__fake_file)
            __fake_file.seek(0)
            storage.write_bytes(filename, __fake_file.read())

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = {"content": content}
        return file_name
