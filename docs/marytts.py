"""
Created for testing purposes to mock out imaginary MaryTTS module
that is referenced in documentation examples.
"""


class MaryTTS:
    def __init__(self, locale: str, voice: str) -> None:
        self.locale = locale
        self.voice = voice

    def synth_mp3(self, content: str) -> bytes:
        return bytes()
