from typing import Any, Callable, Dict, Optional, Type, Union, overload

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider

from ...base import (
    DEFAULT_FORMAT_FUNC,
    BytesValue,
    DynamicTemplate,
    FileMixin,
    StringValue,
)
from ...constants import DEFAULT_IMAGE_MAX_NB_CHARS
from ...helpers import load_class_from_path
from ...registry import FILE_REGISTRY
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage
from ..base.image_generator import BaseImageGenerator

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "ImageMixin",
    "DEFAULT_IMAGE_GENERATOR",
    "IMAGEKIT_IMAGE_GENERATOR",
    "PIL_IMAGE_GENERATOR",
    "WEASYPRINT_IMAGE_GENERATOR",
)

IMAGEKIT_IMAGE_GENERATOR = (
    "faker_file.providers.image.imgkit_generator.ImgkitImageGenerator"
)
PIL_IMAGE_GENERATOR = (
    "faker_file.providers.image.pil_generator.PilImageGenerator"
)
WEASYPRINT_IMAGE_GENERATOR = (
    "faker_file.providers.image.weasyprint_generator.WeasyPrintImageGenerator"
)

DEFAULT_IMAGE_GENERATOR = IMAGEKIT_IMAGE_GENERATOR


class ImageMixin(FileMixin):
    """Image mixin."""

    @overload
    def _image_file(
        self: "ImageMixin",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        image_generator_cls: Optional[Union[str, Type[BaseImageGenerator]]] = (
            DEFAULT_IMAGE_GENERATOR
        ),
        image_generator_kwargs: Optional[Dict[str, Any]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def _image_file(
        self: "ImageMixin",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        image_generator_cls: Optional[Union[str, Type[BaseImageGenerator]]] = (
            DEFAULT_IMAGE_GENERATOR
        ),
        image_generator_kwargs: Optional[Dict[str, Any]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def _image_file(
        self: "ImageMixin",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        image_generator_cls: Optional[Union[str, Type[BaseImageGenerator]]] = (
            DEFAULT_IMAGE_GENERATOR
        ),
        image_generator_kwargs: Optional[Dict[str, Any]] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate an image file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
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

        if image_generator_cls is None:
            image_generator_cls = DEFAULT_IMAGE_GENERATOR

        if isinstance(image_generator_cls, str):
            image_generator_cls = load_class_from_path(image_generator_cls)

        if not image_generator_kwargs:
            image_generator_kwargs = {}

        image_generator_kwargs["content_specs"] = {
            "max_nb_chars": max_nb_chars,
            "wrap_chars_after": wrap_chars_after,
        }

        image_generator = image_generator_cls(
            generator=self.generator,
            **image_generator_kwargs,
        )
        data = {"content": "", "filename": filename, "storage": storage}
        if isinstance(content, DynamicTemplate):
            _content = content
        else:
            _content = self._generate_text_content(
                max_nb_chars=max_nb_chars,
                wrap_chars_after=wrap_chars_after,
                content=content,
                format_func=format_func,
            )
            data["content"] = _content

        _raw_content = image_generator.generate(
            content=_content,
            data=data,
            provider=self,
        )

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
