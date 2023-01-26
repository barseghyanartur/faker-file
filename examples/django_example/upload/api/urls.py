from django.urls import include, re_path
from rest_framework import routers

from .views import UploadViewSet

__all__ = ("urlpatterns",)

app_name = "api"
router = routers.DefaultRouter()
router.register(r"upload", UploadViewSet)

urlpatterns = [
    re_path("^upload/", include(router.urls)),
]
