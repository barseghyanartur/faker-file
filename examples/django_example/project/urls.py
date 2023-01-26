from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

__all__ = ("urlpatterns",)

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    # API schema
    re_path("^api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    re_path(
        "^api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    re_path(
        "^api/redoc/",
        SpectacularRedocView.as_view(url_name="api-schema"),
        name="api-redoc",
    ),
    # Upload API
    re_path(r"^api/", include("upload.api.urls", namespace="api")),
]

# Serving media and static in debug/developer mode.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
