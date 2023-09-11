from typing import Any, Callable, Dict, Optional, Type, Union, overload

from faker import Faker
from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.python import Provider

from ...base import DEFAULT_FORMAT_FUNC, BytesValue, FileMixin, StringValue
from ...constants import DEFAULT_AUDIO_MAX_NB_CHARS
from ...helpers import load_class_from_path
from ...registry import FILE_REGISTRY
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage
from ..base.mp3_generator import BaseMp3Generator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "DEFAULT_MP3_GENERATOR",
    "EDGE_TTS_MP3_GENERATOR",
    "GTTS_MP3_GENERATOR",
    "Mp3FileProvider",
)

GTTS_MP3_GENERATOR = (
    "faker_file.providers.mp3_file.generators.gtts_generator.GttsMp3Generator"
)
EDGE_TTS_MP3_GENERATOR = (
    "faker_file.providers.mp3_file.generators.edge_tts_generator"
    ".EdgeTtsMp3Generator"
)
DEFAULT_MP3_GENERATOR = GTTS_MP3_GENERATOR


class Mp3FileProvider(BaseProvider, FileMixin):
    """MP3 file provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.mp3_file import Mp3FileProvider

        FAKER = Faker()
        FAKER.add_provider(Mp3FileProvider)

        file = FAKER.mp3_file()

    Usage example with options:

    .. code-block:: python

        file = FAKER.mp3_file(
            prefix="zzz",
            max_nb_chars=500,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

    .. code-block:: python

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.mp3_file(
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

    .. code-block:: python

        # Imaginary `marytts` Python library
        from marytts import MaryTTS

        # Import BaseMp3Generator
        from faker_file.providers.base.mp3_generator import (
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
        file = FAKER.mp3_file(
            mp3_generator_cls=MaryTtsMp3Generator,
        )
    """

    extension: str = "mp3"

    @overload
    def mp3_file(
        self: "Mp3FileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_AUDIO_MAX_NB_CHARS,
        content: Optional[str] = None,
        mp3_generator_cls: Optional[
            Union[str, Type[BaseMp3Generator]]
        ] = DEFAULT_MP3_GENERATOR,
        mp3_generator_kwargs: Optional[Dict[str, Any]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def mp3_file(
        self: "Mp3FileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_AUDIO_MAX_NB_CHARS,
        content: Optional[str] = None,
        mp3_generator_cls: Optional[
            Union[str, Type[BaseMp3Generator]]
        ] = DEFAULT_MP3_GENERATOR,
        mp3_generator_kwargs: Optional[Dict[str, Any]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def mp3_file(
        self: "Mp3FileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_AUDIO_MAX_NB_CHARS,
        content: Optional[str] = None,
        mp3_generator_cls: Optional[
            Union[str, Type[BaseMp3Generator]]
        ] = DEFAULT_MP3_GENERATOR,
        mp3_generator_kwargs: Optional[Dict[str, Any]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a MP3 file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param mp3_generator_cls: Mp3 generator class.
        :param mp3_generator_kwargs: Mp3 generator kwargs.
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

        content = self._generate_text_content(
            max_nb_chars=max_nb_chars,
            content=content,
            format_func=format_func,
        )
        data = {"content": content, "filename": filename, "storage": storage}

        if mp3_generator_cls is None:
            mp3_generator_cls = DEFAULT_MP3_GENERATOR

        if isinstance(mp3_generator_cls, str):
            mp3_generator_cls = load_class_from_path(mp3_generator_cls)

        if not mp3_generator_kwargs:
            mp3_generator_kwargs = {}
        mp3_generator = mp3_generator_cls(
            content=content,
            generator=self.generator,
            **mp3_generator_kwargs,
        )
        _raw_content = mp3_generator.generate()

        if raw:
            raw_content = BytesValue(_raw_content)
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, _raw_content)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
