import asyncio
import logging
from io import BytesIO

import edge_tts

from ...base.mp3_generator import BaseMp3Generator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("EdgeTtsMp3Generator",)

DEFAULT_VOICE = "en-GB-SoniaNeural"
LOGGER = logging.getLogger(__name__)


class EdgeTtsMp3Generator(BaseMp3Generator):
    """Edge Text-to-Speech generator.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.mp3_file import Mp3FileProvider
        from faker_file.providers.mp3_file.generators import edge_tts_generator

        FAKER = Faker()
        FAKER.add_provider(Mp3FileProvider)

        file = FAKER.mp3_file(
            mp3_generator_cls=edge_tts_generator.EdgeTtsMp3Generator
        )
    """

    voice: str = DEFAULT_VOICE

    def handle_kwargs(self: "EdgeTtsMp3Generator", **kwargs) -> None:
        if "voice" in kwargs:
            self.voice = kwargs["voice"]

    def generate(self: "EdgeTtsMp3Generator", **kwargs) -> bytes:
        """Generate MP3."""
        with BytesIO() as _fake_file:

            async def _generate():
                """Async generate.

                edge-tts is an async library. We can't use it in non-async
                context. Therefore, this trick.
                """
                async for chunk in edge_tts.Communicate(
                    self.content, self.voice
                ).stream():
                    if chunk["type"] == "audio":
                        _fake_file.write(chunk["data"])
                    elif chunk["type"] == "WordBoundary":
                        LOGGER.debug(f"WordBoundary: {chunk}")

            # Run the async function
            loop = asyncio.get_event_loop_policy().new_event_loop()
            loop.run_until_complete(_generate())
            # Return result
            loop.close()
            return _fake_file.getvalue()
