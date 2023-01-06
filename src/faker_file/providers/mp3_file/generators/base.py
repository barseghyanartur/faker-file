__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("BaseMp3Generator",)


class BaseMp3Generator:
    def __init__(self: "BaseMp3Generator", content: str):
        self.content = content

    def generate(self: "BaseMp3Generator") -> bytes:
        raise NotImplementedError("Method `generate` is not implemented.")
