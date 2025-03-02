from cloudpathlib import AzureBlobPath

from .cloud import CloudStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("AzureCloudStorage",)


class AzureCloudStorage(CloudStorage):
    """Azure Cloud Storage.

    Usage example:

    .. code-block:: python

        from faker_file.storages.cloudpathlib_based.azure_cloud_storage import (
            AzureCloudStorage,
        )

        azure_storage = AzureCloudStorage(
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = azure_storage.generate_filename(prefix="zzz_", extension="docx")
        azure_storage.write_text(file, "Lorem ipsum")
        azure_storage.write_bytes(file, b"Lorem ipsum")
    """

    schema: str = "az"

    def authenticate(self, connection_string: str, **kwargs) -> None:
        """Authenticate to Azure Cloud Storage."""
        AzureBlobPath.set_connection_string(connection_string)
