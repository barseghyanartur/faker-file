from django.db import models

__all__ = ("Upload",)


class Upload(models.Model):
    """Upload model."""

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField()

    class Meta:
        verbose_name = "Upload"
        verbose_name_plural = "Upload"

    def __str__(self: "Upload") -> str:
        return self.name  # noqa
