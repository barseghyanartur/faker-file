from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Upload
from .serializers import UploadInSerializer, UploadOutSerializer

__all__ = ("UploadViewSet",)


@extend_schema(tags=[_("Upload")])
@extend_schema_view(
    create=extend_schema(
        tags=[_("Upload")],
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "format": "string",
                    },
                    "description": {
                        "type": "string",
                        "format": "string",
                    },
                    "file": {
                        "type": "string",
                        "format": "binary",
                    },
                },
            }
        },
    ),
)
class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = default_serializer_class = UploadInSerializer
    serializer_classes = {
        "list": UploadOutSerializer,
        "create": UploadInSerializer,
        "retrieve": UploadOutSerializer,
        "update": UploadOutSerializer,
        "partial_update": UploadOutSerializer,
        "destroy": UploadOutSerializer,
    }
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        return self.serializer_classes.get(
            self.action, self.default_serializer_class
        )
