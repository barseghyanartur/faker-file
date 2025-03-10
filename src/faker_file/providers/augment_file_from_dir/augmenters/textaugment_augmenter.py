from typing import Any, Dict, Type

import nltk
from textaugment import EDA

from ...base.text_augmenter import BaseTextAugmenter

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2025 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "EDATextaugmentAugmenter",
    "DEFAULT_ACTION",
)

DEFAULT_ACTION = "synonym_replacement"


class EDATextaugmentAugmenter(BaseTextAugmenter):
    """Text extractor based on `ContextualWordEmbsAug` of `nlpaug`.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.augment_file_from_dir import (
            AugmentFileFromDirProvider,
        )
        from faker_file.providers.augment_file_from_dir.augmenters import (
            textaugment_augmenter,
        )

        FAKER = Faker()
        FAKER.add_provider(AugmentFileFromDirProvider)

        file = FAKER.augment_file_from_dir(
            source_dir_path="/tmp/tmp/",
            text_augmenter_cls=(
                textaugment_augmenter.EDATextaugmentAugmenter
            ),
            text_augmenter_kwargs={
                "action": "random_insertion",
            }
        )

    Refer to `textaugment` official documentation and check examples for `EDA`:

        ://github.com/dsfsi/textaugment/blob/master/examples/eda_example.ipynb

    Options for `action` are:

        - random_deletion
        - random_insertion
        - random_swap
        - synonym_replacement
    """

    action: str = DEFAULT_ACTION
    kwargs: Dict[str, Any] = {}
    _data_downloaded: bool = False

    def handle_kwargs(self: "EDATextaugmentAugmenter", **kwargs) -> None:
        """Handle kwargs."""
        if "action" in kwargs:
            self.action = kwargs["action"]
        if "kwargs" in kwargs:
            self.kwargs = kwargs["kwargs"]
        self.__class__.init()

    @classmethod
    def init(cls: Type["EDATextaugmentAugmenter"]) -> None:
        """Initialize the class. Should be run only once."""
        if not cls._data_downloaded:
            nltk.download("punkt")
            nltk.download("wordnet")
            nltk.download("stopwords")
            cls._data_downloaded = True

    def augment(self: "EDATextaugmentAugmenter", text: str) -> str:
        """Augment text."""
        aug = EDA()
        func = getattr(aug, self.action)
        return func(text, **self.kwargs)
