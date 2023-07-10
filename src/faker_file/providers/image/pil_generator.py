# import contextlib
# import io
# import logging
# from typing import Any, Dict, Union
#
# import imgkit
# from faker import Faker
# from faker.generator import Generator
# from faker.providers.python import Provider
#
# from ...constants import DEFAULT_FILE_ENCODING
# from ..base.image_generator import BaseImageGenerator
#
# __author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
# __copyright__ = "2022-2023 Artur Barseghyan"
# __license__ = "MIT"
# __all__ = ("PilImageGenerator",)
#
# LOGGER = logging.getLogger(__name__)
#
#
# class PilImageGenerator(BaseImageGenerator):
#     """PIL image generator.
#
#     Usage example:
#
#         from faker import Faker
#         from faker_file.providers.png_file import PngFileProvider
#         from faker_file.providers.images.generators import pil_generator
#
#         FAKER = Faker()
#
#         file = PngFileProvider(FAKER).png_file(
#             img_generator_cls=pil_generator.PilImageGenerator
#         )
#     """
#
#     encoding: str = DEFAULT_FILE_ENCODING
#
#     def handle_kwargs(self: "PilImageGenerator", **kwargs) -> None:
#         """Handle kwargs."""
#         if "encoding" in kwargs:
#             self.encoding = kwargs["encoding"]
#
#     def generate(
#         self: "PilImageGenerator",
#         content: str,
#         data: Dict[str, Any],
#         provider: Union[Faker, Generator, Provider],
#         **kwargs,
#     ) -> bytes:
#         """Generate image."""
#         with contextlib.redirect_stdout(io.StringIO()):
#             return imgkit.from_string(
#                 f"<pre>{content}</pre>",
#                 False,
#                 options={"format": provider.extension},
#             )
