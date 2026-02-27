import random

from faker import Faker

from ...base.text_augmenter import BaseTextAugmenter

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2025 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "FakerWordAugmenter",
    "DEFAULT_AUGMENTATION_PROBABILITY",
    "DEFAULT_POOL_SIZE",
)

DEFAULT_AUGMENTATION_PROBABILITY = 0.2
DEFAULT_POOL_SIZE = 1000


class FakerWordAugmenter(BaseTextAugmenter):
    """Text augmenter that randomly replaces words with Faker-generated words.

    Usage example:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.augment_file_from_dir import (
            AugmentFileFromDirProvider,
        )
        from faker_file.providers.augment_file_from_dir.augmenters import (
            faker_augmenter,
        )

        FAKER = Faker()
        FAKER.add_provider(AugmentFileFromDirProvider)

        file = FAKER.augment_file_from_dir(
            source_dir_path="/tmp/tmp/",
            text_augmenter_cls=faker_augmenter.FakerWordAugmenter,
            text_augmenter_kwargs={
                "augmentation_probability": 0.3,
                "pool_size": 500,
                "locale": "en_US",
            }
        )

    You may also pass an existing ``Faker`` instance via ``generator``,
    which is useful when you want the augmenter to share the same Faker
    instance as the rest of your application:

    .. code-block:: python

        from faker import Faker
        from faker_file.providers.augment_file_from_dir import (
            AugmentFileFromDirProvider,
        )
        from faker_file.providers.augment_file_from_dir.augmenters import (
            faker_augmenter,
        )

        MY_FAKER = Faker("de_DE")

        FAKER = Faker()
        FAKER.add_provider(AugmentFileFromDirProvider)

        file = FAKER.augment_file_from_dir(
            source_dir_path="/tmp/tmp/",
            text_augmenter_cls=faker_augmenter.FakerWordAugmenter,
            text_augmenter_kwargs={
                "generator": MY_FAKER,
                "augmentation_probability": 0.3,
                "pool_size": 500,
            }
        )

    Options:

        - ``augmentation_probability`` (float, default 0.2): probability that
          any given word will be replaced with a randomly chosen Faker word.
        - ``pool_size`` (int, default 1000): number of words pre-generated
          from Faker to draw replacements from. A larger pool increases
          variety; a smaller pool improves startup time.
        - ``locale`` (str, default ``None``): Faker locale used when building
          the word pool (e.g. ``"en_US"``, ``"de_DE"``). When ``None``, the
          default Faker locale is used. Ignored when ``generator`` is given.
        - ``generator`` (``Faker``, default ``None``): an existing Faker
          instance to use for building the word pool. When provided, a new
          Faker instance is not created and ``locale`` is ignored.
    """

    augmentation_probability: float = DEFAULT_AUGMENTATION_PROBABILITY
    pool_size: int = DEFAULT_POOL_SIZE
    locale: str = None
    generator: Faker = None
    _word_pool: list = []

    def handle_kwargs(self: "FakerWordAugmenter", **kwargs) -> None:
        """Handle kwargs."""
        if "augmentation_probability" in kwargs:
            self.augmentation_probability = kwargs["augmentation_probability"]
        if "pool_size" in kwargs:
            self.pool_size = kwargs["pool_size"]
        if "locale" in kwargs:
            self.locale = kwargs["locale"]
        if "generator" in kwargs:
            self.generator = kwargs["generator"]
        self._build_word_pool()

    def _build_word_pool(self: "FakerWordAugmenter") -> None:
        """Pre-generate a pool of words using Faker."""
        if self.generator is not None:
            fake = self.generator
        elif self.locale:
            fake = Faker(self.locale)
        else:
            fake = Faker()
        self._word_pool = [fake.word() for _ in range(self.pool_size)]

    def augment(self: "FakerWordAugmenter", text: str) -> str:
        """Augment text by randomly replacing words with Faker-generated ones."""
        if not text:
            return text

        if not self._word_pool:
            self._build_word_pool()

        words = text.split()
        augmented_words = [
            random.choice(self._word_pool)
            if random.random() < self.augmentation_probability
            else word
            for word in words
        ]

        return " ".join(augmented_words)
