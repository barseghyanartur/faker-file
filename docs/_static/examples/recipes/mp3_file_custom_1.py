from faker import Faker
from faker_file.providers.base.mp3_generator import BaseMp3Generator
from faker_file.providers.mp3_file import Mp3FileProvider
from marytts import MaryTTS  # Imaginary `marytts` Python library

FAKER = Faker()
FAKER.add_provider(Mp3FileProvider)


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
mp3_file = FAKER.mp3_file(
    mp3_generator_cls=MaryTtsMp3Generator,
)
