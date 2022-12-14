from google.oauth2 import service_account
from pathy import set_client_params

from .cloud import CloudStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("GoogleCloudStorage",)


class GoogleCloudStorage(CloudStorage):
    """Google Cloud Storage.

    Usage example:

        from faker_file.storages.google_cloud_storage import GoogleCloudStorage

        gs_storage = GoogleCloudStorage(
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = gs_storage.generate_filename(prefix="zzz_", extension="docx")
        gs_storage.write_text(file, "Lorem ipsum")
        gs_storage.write_bytes(file, b"Lorem ipsum")
    """

    schema = "gs"

    def authenticate(
        self: "GoogleCloudStorage", json_file_path: str, **kwargs
    ) -> None:
        """Authenticate to Google Cloud Storage."""
        credentials = service_account.Credentials.from_service_account_file(
            json_file_path
        )
        set_client_params("gs", credentials=credentials)
