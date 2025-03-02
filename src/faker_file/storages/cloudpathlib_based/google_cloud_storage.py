from cloudpathlib import GSPath
from google.cloud import storage
from google.oauth2 import service_account

from .cloud import CloudStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("GoogleCloudStorage",)


class GoogleCloudStorage(CloudStorage):
    """Google Cloud Storage.

    Usage example:

    .. code-block:: python

        from faker_file.storages.cloudpathlib_based.google_cloud_storage import (
            GoogleCloudStorage,
        )

        gs_storage = GoogleCloudStorage(
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = gs_storage.generate_filename(prefix="zzz_", extension="docx")
        gs_storage.write_text(file, "Lorem ipsum")
        gs_storage.write_bytes(file, b"Lorem ipsum")
    """  # noqa

    schema: str = "gs"

    def authenticate(self, json_file_path: str, **kwargs) -> None:
        """Authenticate to Google Cloud Storage."""
        credentials = service_account.Credentials.from_service_account_file(
            json_file_path
        )
        client = storage.Client(credentials=credentials)
        GSPath._client = client
