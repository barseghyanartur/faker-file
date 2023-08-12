from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union, overload

from faker.providers import BaseProvider

from ..base import BytesValue, FileMixin, StringValue
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage
from .image.augment import augment_image_file

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("AugmentImageFromPathProvider",)

EXTENSIONS = {
    "bmp",
    "gif",
    "ico",
    "jpeg",
    "jpg",
    "png",
    "svg",
    "tiff",
    "webp",
}


class AugmentImageFromPathProvider(BaseProvider, FileMixin):
    """Augment image from given path provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.augment_image_from_path import (
            AugmentImageFromPathProvider
        )

        FAKER = Faker()
        FAKER.add_provider(AugmentImageFromPathProvider)

        file = FAKER.augment_image_from_path(
            path="/path/to/image.png"
        )

    Usage example with options:

        .. code-block:: python

        file = FAKER.augment_image_from_path(
            path="/path/to/image.png",
            prefix="zzz",
        )
    """

    extension: str = ""

    @overload
    def augment_image_from_path(
        self: "AugmentImageFromPathProvider",
        path: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        augmentations: Optional[List[Tuple[Callable, Dict[str, Any]]]] = None,
        num_steps: Optional[int] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def augment_image_from_path(
        self: "AugmentImageFromPathProvider",
        path: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        augmentations: Optional[List[Tuple[Callable, Dict[str, Any]]]] = None,
        num_steps: Optional[int] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def augment_image_from_path(
        self: "AugmentImageFromPathProvider",
        path: str,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        augmentations: Optional[List[Tuple[Callable, Dict[str, Any]]]] = None,
        num_steps: Optional[int] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Augment an image from given path.

        :param path: Path to source file.
        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param augmentations: List of tuples of callable augmentation
            functions and their respective keyword arguments. If not
            provided, the default augmentation functions will be used.
        :param num_steps: Number of augmentation steps (functions) to be
            applied. If not specified, the length of the `augmentations` list
            will be used.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        # Specific
        source_file = Path(path)

        # Generic
        filename = storage.generate_filename(
            extension=source_file.suffix[1:],
            prefix=prefix,
            basename=basename,
        )
        data = {"filename": filename, "storage": storage}

        image_bytes = augment_image_file(
            image_path=path,
            augmentations=augmentations,
            num_steps=num_steps,
        )

        if raw:
            raw_content = BytesValue(image_bytes)
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, image_bytes)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data

        return file_name
