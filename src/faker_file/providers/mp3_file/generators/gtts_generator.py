from io import BytesIO

from gtts import gTTS

from ...base.mp3_generator import BaseMp3Generator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("GttsMp3Generator",)


DEFAULT_LANG = "en"
DEFAULT_TLD = "com"


class GttsMp3Generator(BaseMp3Generator):
    """Google Text-to-Speech generator.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.mp3_file import Mp3FileProvider
        from faker_file.providers.mp3_file.generators.gtts_generator import (
            GttsMp3Generator,
        )

        FAKER = Faker()
        FAKER.add_provider(Mp3FileProvider)

        file = FAKER.mp3_file(
            mp3_generator_cls=GttsMp3Generator
        )
    """

    lang: str = DEFAULT_LANG
    tld: str = DEFAULT_TLD

    def handle_kwargs(self: "GttsMp3Generator", **kwargs) -> None:
        if "lang" in kwargs:
            self.lang = kwargs["lang"]
        if "tld" in kwargs:
            self.tld = kwargs["tld"]

    def generate(self: "GttsMp3Generator", **kwargs) -> bytes:
        """Generate MP3."""
        with BytesIO() as __fake_file:
            tts = gTTS(self.content, lang=self.lang, tld=self.tld)
            tts.write_to_fp(__fake_file)
            return __fake_file.getvalue()
