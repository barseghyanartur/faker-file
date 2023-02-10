__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("BaseTextAugmenter",)


class BaseTextAugmenter:
    """Base text augmenter."""

    def __init__(
        self: "BaseTextAugmenter",
        **kwargs,
    ) -> None:
        """Constructor.

        :param kwargs: Dictionary with parameters (for text extractor
            specific tuning).
        """
        self.handle_kwargs(**kwargs)

    def handle_kwargs(self: "BaseTextAugmenter", **kwargs):
        """Handle kwargs."""

    def augment(
        self: "BaseTextAugmenter",
        text: str,
    ) -> str:
        raise NotImplementedError("Method `augment` is not implemented.")
