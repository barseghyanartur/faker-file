import unittest

from PIL import Image, ImageDraw

from ..providers.image.augment import solarize

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestSolarizeFunction",)


class TestSolarizeFunction(unittest.TestCase):
    """Test `solarize` function."""

    def create_rgba_image(self):
        """Create a sample RGBA image."""
        img = Image.new("RGBA", (100, 100), (150, 60, 90, 255))
        draw = ImageDraw.Draw(img)
        draw.rectangle((25, 25, 75, 75), fill=(60, 170, 210, 200))
        return img

    def create_rgb_image(self):
        """Create a sample RGB image."""
        img = Image.new("RGB", (100, 100), (150, 60, 90))
        draw = ImageDraw.Draw(img)
        draw.rectangle((25, 25, 75, 75), fill=(60, 170, 210))
        return img

    def test_solarize_rgba(self):
        img = self.create_rgba_image()
        solarized_img = solarize(img)

        # Assuming values above 128 are inverted, check some pixel values
        self.assertEqual(solarized_img.getpixel((10, 10)), (105, 60, 90, 255))
        self.assertEqual(
            solarized_img.getpixel((50, 50)), (60, 85, 45, 200)
        )  # Alpha should remain unaffected

    def test_solarize_rgb(self):
        img = self.create_rgb_image()
        solarized_img = solarize(img)

        # Assuming values above 128 are inverted, check some pixel values
        self.assertEqual(solarized_img.getpixel((10, 10)), (105, 60, 90))
        self.assertEqual(solarized_img.getpixel((50, 50)), (60, 85, 45))
