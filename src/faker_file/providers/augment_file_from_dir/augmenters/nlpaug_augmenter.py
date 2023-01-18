import nlpaug.augmenter.word as naw

from .base import BaseTextAugmenter

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "ContextualWordEmbeddingsAugmenter",
    "DEFAULT_ACTION",
    "DEFAULT_MODEL_PATH",
)

DEFAULT_MODEL_PATH = "bert-base-multilingual-cased"
DEFAULT_ACTION = "substitute"


class ContextualWordEmbeddingsAugmenter(BaseTextAugmenter):
    """Text extractor based on `ContextualWordEmbsAug` of `nlpaug`.

    Usage example:

        from faker import Faker
        from faker_file.providers.augment_file_from_dir import (
            AugmentFileFromDirProvider,
        )
        from faker_file.providers.augment_file_from_dir.augmenters import (
            nlpaug_augmenter,
        )

        FAKER = Faker()

        file = AugmentFileFromDirProvider(FAKER).augment_file_from_dir(
            text_augmenter_cls=(
                nlpaug_augmenter.ContextualWordEmbeddingsAugmenter
            ),
            text_augmenter_kwargs={
                "model_path": "bert-base-uncased",
                "action": "substitute",
            }
        )

    Refer to `nlpaug` official documentation and check examples
    for `Textual augmenters`:

        https://nlpaug.readthedocs.io/en/latest/example/example.html

    Some well working options for `model_path` are:

        - bert-base-multilingual-cased
        - bert-base-multilingual-uncased
        - bert-base-cased
        - bert-base-uncased
        - bert-base-german-cased
        - GroNLP/bert-base-dutch-cased

    Options for `action` are:

        - insert
        - substitute
    """

    model_path: str = DEFAULT_MODEL_PATH
    action: str = DEFAULT_ACTION

    def handle_kwargs(
        self: "ContextualWordEmbeddingsAugmenter", **kwargs
    ) -> None:
        """Handle kwargs."""
        if "model_path" in kwargs:
            self.model_path = kwargs["model_path"]
        if "action" in kwargs:
            self.action = kwargs["action"]

    def augment(
        self: "ContextualWordEmbeddingsAugmenter",
        text: str,
    ) -> str:
        """Augment text."""
        aug = naw.ContextualWordEmbsAug(
            model_path=self.model_path,
            action=self.action,
        )
        return aug.augment(text)[0]
