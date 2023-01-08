from typing import Any, Dict, Optional, Type

from faker.providers import BaseProvider

from ...base import FileMixin, StringValue
from ...constants import DEFAULT_AUDIO_MAX_NB_CHARS
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage
from .generators.base import BaseMp3Generator
from .generators.gtts_generator import GttsMp3Generator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("Mp3FileProvider",)


class Mp3FileProvider(BaseProvider, FileMixin):
    """MP3 file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.mp3_file import Mp3FileProvider

        FAKER = Faker()
        file = Mp3FileProvider(FAKER).mp3_file()

    Usage example with options:

        file = Mp3FileProvider(FAKER).mp3_file(
            prefix="zzz",
            max_nb_chars=500,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = Mp3FileProvider(FAKER).mp3_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            max_nb_chars=500,
        )

    Default MP3 generator class is `GttsMp3Generator` which uses Google
    Text-to-Speech services to generate an MP3 file from given or
    randomly generated text. It does not require additional services to
    run and the only dependency here is the `gtts` package. You can
    however implement your own custom MP3 generator class and pass it to
    te `mp3_file` method in `mp3_generator_cls` argument instead of the
    default `GttsMp3Generator`.

    Usage with custom MP3 generator class.

        # Imaginary `marytts` Python library
        from marytts import MaryTTS

        # Import BaseMp3Generator
        from faker_file.providers.mp3_file.generators.base import (
            BaseMp3Generator,
        )

        # Define custom MP3 generator
        class MaryTtsMp3Generator(BaseMp3Generator):

            locale: str = "cmu-rms-hsmm"
            voice: str = "en_US"

            def handle_kwargs(self, **kwargs) -> None:
                # Since it's impossible to unify all TTS systems it's allowed
                # to pass arbitrary arguments to the `BaseMp3Generator`
                # constructor. Each implementation class contains its own
                # additional tuning arguments. Check the source code of the
                # implemented MP3 generators as an example.
                if "locale" in kwargs:
                    self.locale = kwargs["locale"]
                if "voice" in kwargs:
                    self.voice = kwargs["voice"]

            def generate(self) -> bytes:
                # Your implementation here. Note, that `self.content`
                # in this context is the text to make MP3 from.
                # `self.generator` would be the `Faker` or `Generator`
                # instance from which you could extract information on
                # active locale.
                # What comes below is pseudo implementation.
                mary_tts = MaryTTS(locale=self.locale, voice=self.voice)
                return mary_tts.synth_mp3(self.content)

        # Generate MP3 file from random text
        file = Mp3FileProvider(FAKER).mp3_file(
            mp3_generator_cls=MaryTtsMp3Generator,
        )
    """

    extension: str = "mp3"

    def mp3_file(
        self: "Mp3FileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_AUDIO_MAX_NB_CHARS,
        content: Optional[str] = None,
        mp3_generator_cls: Type[BaseMp3Generator] = GttsMp3Generator,
        mp3_generator_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> StringValue:
        """Generate a MP3 file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param mp3_generator_cls: Mp3 generator class.
        :param mp3_generator_kwargs: Mp3 generator kwargs.
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

        if mp3_generator_cls is None:
            mp3_generator_cls = GttsMp3Generator

        if not mp3_generator_kwargs:
            mp3_generator_kwargs = {}
        mp3_generator = mp3_generator_cls(
            content=content,
            generator=self.generator,
            **mp3_generator_kwargs,
        )
        storage.write_bytes(filename, mp3_generator.generate())

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = {"content": content}
        return file_name
