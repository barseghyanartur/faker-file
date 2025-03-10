import os
import tempfile

import ffmpeg
from faker_file.providers.base.mp3_generator import BaseMp3Generator
from speak2mary import MaryTTS

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2025 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("MaryTtsMp3Generator",)


DEFAULT_LOCALE = "en_GB"
DEFAULT_VOICE = "dfki-spike-hsmm"


class MaryTtsMp3Generator(BaseMp3Generator):
    """MaryTTS Text-to-Speech generator.

    Usage example:

        from faker import Faker
        from faker_file.providers.mp3_file import Mp3FileProvider
        from marytts_mp3_generator import (
            MaryTtsMp3Generator,
        )

        FAKER = Faker()

        file = Mp3FileProvider(FAKER).mp3_file(
            mp3_generator_cls=MaryTtsMp3Generator,
            mp3_generator_kwargs={},
        )
    """

    locale: str = DEFAULT_LOCALE
    voice: str = DEFAULT_VOICE

    def handle_kwargs(self: "MaryTtsMp3Generator", **kwargs) -> None:
        if "locale" in kwargs:
            self.locale = kwargs["locale"]
        if "voice" in kwargs:
            self.voice = kwargs["voice"]

    def generate(self: "MaryTtsMp3Generator") -> bytes:
        """Generate MP3."""
        # Initialize with args
        mary_tts = MaryTTS(locale=self.locale, voice=self.voice)

        # Create temporary WAV file in memory
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav",
        ) as temp_wav:
            temp_wav.write(mary_tts.speak(self.content))
            temp_wav_path = temp_wav.name

        # Convert WAV to MP3 and store in memory
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3",
        ) as temp_mp3:
            ffmpeg.input(temp_wav_path).output(temp_mp3.name).run()

            # Read the MP3 file content into memory
            with open(temp_mp3.name, "rb") as mp3_file:
                mp3_content = mp3_file.read()

        # Clean up temporary files
        os.remove(temp_wav.name)
        os.remove(temp_mp3.name)

        return mp3_content

        # # Generate temporary filename for WAV file
        # filename = tempfile.NamedTemporaryFile(
        #     prefix="_merytts_", suffix=".wav"
        # ).name
        #
        # # Write WAV file
        # with open(filename, "wb") as file:
        #     file.write(mary_tts.speak(self.content))
        #
        # # Convert WAV to MP3
        # ffmpeg.input(filename).output(filename + ".mp3").run()
        #
        # with open(filename + ".mp3", "rb") as _fake_file:
        #     return_value = _fake_file.read()
        #
        # # Clean up temporary files
        # os.remove(filename)
        # os.remove(filename + ".mp3")
        #
        # return return_value
