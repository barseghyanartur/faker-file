from cloudpathlib import GSClient
from google.oauth2 import service_account

from .cloudpathlib_cloud import CloudpathlibCloudStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("CloudpathlibGoogleCloudStorage",)


class CloudpathlibGoogleCloudStorage(CloudpathlibCloudStorage):
    """Google Cloud Storage.

    Usage example:

    .. code-block:: python

        from faker_file.storages.cloudpathlib_google_cloud_storage import (
            CloudpathlibGoogleCloudStorage
        )

        gs_storage = CloudpathlibGoogleCloudStorage(
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = gs_storage.generate_filename(prefix="zzz_", extension="docx")
        gs_storage.write_text(file, "Lorem ipsum")
        gs_storage.write_bytes(file, b"Lorem ipsum")
    """

    schema = "gs"

    def authenticate(
        self: "CloudpathlibGoogleCloudStorage", json_file_path: str, **kwargs
    ) -> None:
        """Authenticate to Google Cloud Storage."""
        credentials = service_account.Credentials.from_service_account_file(
            json_file_path
        )
        client = GSClient(credentials=credentials)
        client.set_as_default_client()
