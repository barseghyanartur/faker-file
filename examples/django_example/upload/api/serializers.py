from rest_framework import serializers

from ..models import Upload

__all__ = (
    "UploadInSerializer",
    "UploadOutSerializer",
)


class UploadInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ["id", "name", "description", "file"]
        read_only_fields = ["id"]


class UploadOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ["id", "name", "description", "file"]
