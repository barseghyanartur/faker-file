from django.db import models


class Upload(models.Model):
    """Upload model."""

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    # File
    file = models.FileField(null=True)

    class Meta:
        app_label = "uploads"  # Ignore this line when copying
        verbose_name = "Upload"
        verbose_name_plural = "Upload"

    def __str__(self):
        return self.name
