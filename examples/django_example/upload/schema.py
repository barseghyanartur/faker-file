from ninja import ModelSchema

from .models import Upload

__all__ = (
    "UploadIn",
    "UploadOut",
)


class UploadIn(ModelSchema):
    """Upload input schema."""

    class Config:
        model = Upload
        model_fields = [
            "name",
            "description",
        ]


class UploadOut(ModelSchema):
    """Upload output schema."""

    class Config:
        model = Upload
        model_fields = "__all__"
