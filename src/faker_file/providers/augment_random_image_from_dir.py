import logging
import os
from pathlib import Path
from random import choice
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
    overload,
)

from faker.providers import BaseProvider

from ..base import BytesValue, FileMixin, StringValue
from ..helpers import random_pop
from ..registry import FILE_REGISTRY
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage
from .image.augment import augment_image_file

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("AugmentRandomImageFromDirProvider",)

LOGGER = logging.getLogger(__name__)

EXTENSIONS = {
    "bmp",
    "gif",
    # "ico",  # Not supported yet
    "jpeg",
    "jpg",
    "png",
    # "svg",  # Not supported yet
    "tiff",
    "webp",
}


class AugmentRandomImageFromDirProvider(BaseProvider, FileMixin):
    """Augment image from given directory provider.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.augment_random_image_from_dir import (
            AugmentRandomImageFromDirProvider
        )

        FAKER = Faker()
        FAKER.add_provider(AugmentRandomImageFromDirProvider)

        file = FAKER.augment_random_image_from_dir(
            source_dir_path="/tmp/tmp/"
        )

    Usage example with options:

    .. code-block:: python

        file = FAKER.augment_random_image_from_dir(
            source_dir_path="/tmp/tmp/",
            prefix="zzz",
            extensions={"jpeg", "png"},
        )
    """

    extension: str = ""

    @overload
    def augment_random_image_from_dir(
        self: "AugmentRandomImageFromDirProvider",
        source_dir_path: str,
        extensions: Optional[Iterable[str]] = None,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        augmentations: Optional[List[Tuple[Callable, Dict[str, Any]]]] = None,
        num_steps: Optional[int] = None,
        pop_func: Callable = random_pop,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def augment_random_image_from_dir(
        self: "AugmentRandomImageFromDirProvider",
        source_dir_path: str,
        extensions: Optional[Iterable[str]] = None,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        augmentations: Optional[List[Tuple[Callable, Dict[str, Any]]]] = None,
        num_steps: Optional[int] = None,
        pop_func: Callable = random_pop,
        **kwargs,
    ) -> StringValue:
        ...

    def augment_random_image_from_dir(
        self: "AugmentRandomImageFromDirProvider",
        source_dir_path: str,
        extensions: Optional[Iterable[str]] = None,
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        augmentations: Optional[List[Tuple[Callable, Dict[str, Any]]]] = None,
        num_steps: Optional[int] = None,
        pop_func: Callable = random_pop,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Augment a random image from given directory.

        :param source_dir_path: Source files directory.
        :param extensions: Allowed extensions.
        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param augmentations: List of tuples of callable augmentation
            functions and their respective keyword arguments. If not
            provided, the default augmentation functions will be used.
        :param num_steps: Number of augmentation steps (functions) to be
            applied. If not specified, the length of the `augmentations` list
            will be used.
        :param pop_func: Callable to pop items from `augmentations` list. By
            default, the `random_pop` is used, which pops items in random
            order. If you want the order of augmentations to be constant and
            as given, replace it with `list.pop` (`pop_func=list.pop`).
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        if extensions is None:
            extensions = EXTENSIONS

        # Specific
        source_file_choices = [
            os.path.join(source_dir_path, _f)
            for _f in os.listdir(source_dir_path)
            if (
                os.path.isfile(os.path.join(source_dir_path, _f))
                and os.path.splitext(_f)[1][1:] in extensions
            )
        ]
        source_file_path = choice(source_file_choices)
        source_file = Path(source_file_path)

        # Generic
        filename = storage.generate_filename(
            extension=source_file.suffix[1:],
            prefix=prefix,
            basename=basename,
        )
        data = {"filename": filename, "storage": storage}

        image_bytes = augment_image_file(
            image_path=source_file_path,
            augmentations=augmentations,
            num_steps=num_steps,
            pop_func=pop_func,
        )

        if raw:
            raw_content = BytesValue(image_bytes)
            raw_content.data = data
            return raw_content

        storage.write_bytes(filename, image_bytes)

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = data
        FILE_REGISTRY.add(file_name)
        return file_name
