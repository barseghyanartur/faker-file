import nlpaug.augmenter.word as naw

from .base import BaseTextAugmenter

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("NlpAugContextualWordEmbsAug",)


class NlpAugContextualWordEmbsAug(BaseTextAugmenter):
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
            text_augmenter_cls=nlpaug_augmenter.NlpAugContextualWordEmbsAug
        )
    """

    def handle_kwargs(self: "NlpAugContextualWordEmbsAug", **kwargs) -> None:
        """Handle kwargs."""

    def augment(
        self: "NlpAugContextualWordEmbsAug",
        text: str,
    ) -> str:
        """Augment text."""
        aug = naw.ContextualWordEmbsAug(
            model_path="bert-base-cased",
            action="substitute",
        )
        return aug.augment(text)[0]
