from typing import Optional, Sequence, Tuple, Union, overload

from faker import Faker

from ...base import BytesValue, FileMixin, StringValue
from ...registry import FILE_REGISTRY
from ...storages.base import BaseStorage
from ...storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("GraphicImageMixin",)


class GraphicImageMixin(FileMixin):
    """Graphic image mixin."""

    @overload
    def _image_file(
        self: "GraphicImageMixin",
        image_format: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        size: Tuple[int, int] = (256, 256),
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def _image_file(
        self: "GraphicImageMixin",
        image_format: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        size: Tuple[int, int] = (256, 256),
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def _image_file(
        self: "GraphicImageMixin",
        image_format: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        size: Tuple[int, int] = (256, 256),
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate an image file with random text.

        :param image_format: Image format. Can be any valid format to the
            underlying library like "tiff", "jpeg", "pdf" or "png" (default).
            Note that some formats need present system libraries prior to
            building the Python Image Library. Refer to
            ://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
            for details.
        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param size: Image size in pixels.
        :param hue: Read more about
            ://faker.readthedocs.io/en/dev/providers/faker.providers.color.html
        :param luminosity: If given, the output string would be separated
             by line breaks after the given position.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        if self.generator is None:
            self.generator = Faker()

        filename = storage.generate_filename(
            extension=self.extension,
            prefix=prefix,
            basename=basename,
        )

        data = {"filename": filename, "storage": storage}

        buffer = self.generator.image(
            size=size,
            image_format=image_format,
            hue=hue,
            luminosity=luminosity,
        )

        if raw:
            raw_content = BytesValue(buffer)
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, buffer)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
