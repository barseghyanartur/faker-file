from io import BytesIO

from gtts import gTTS

from .base import BaseMp3Generator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("GttsMp3Generator",)


class GttsMp3Generator(BaseMp3Generator):
    """Google Text-to-Speech generator.

    Usage example:

        from faker import Faker
        from faker_file.providers.mp3_file import Mp3FileProvider
        from faker_file.providers.mp3_file.generators.gtts_generator import (
            GttsMp3Generator,
        )

        FAKER = Faker()

        file = Mp3FileProvider(FAKER).mp3_file(
            mp3_generator_cls=GttsMp3Generator
        )
    """

    def generate(self: "GttsMp3Generator") -> bytes:
        with BytesIO() as __fake_file:
            tts = gTTS(self.content)
            tts.write_to_fp(__fake_file)
            __fake_file.seek(0)
            return __fake_file.read()
