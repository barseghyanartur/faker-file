from django.contrib import admin

from .models import Upload

__all__ = ("UploadAdmin",)


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    """Upload admin."""

    list_display = (
        "name",
        "description",
        "file",
    )
