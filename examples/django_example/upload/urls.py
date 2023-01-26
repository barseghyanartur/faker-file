from django.urls import path

from .api import API

__all__ = ("urlpatterns",)

urlpatterns = [
    path("", API.urls),
]
