from cloudpathlib import AzureBlobClient

from .cloudpathlib_cloud import CloudpathlibCloudStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("CloudpathlibAzureCloudStorage",)


class CloudpathlibAzureCloudStorage(CloudpathlibCloudStorage):
    """Azure Cloud Storage.

    Usage example:

    .. code-block:: python

        from faker_file.storages.cloudpathlib_azure_cloud_storage import (
            CloudpathlibAzureCloudStorage
        )

        azure_storage = CloudpathlibAzureCloudStorage(
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = azure_storage.generate_filename(prefix="zzz_", extension="docx")
        azure_storage.write_text(file, "Lorem ipsum")
        azure_storage.write_bytes(file, b"Lorem ipsum")
    """

    schema = "azure"

    def authenticate(
        self: "CloudpathlibAzureCloudStorage", connection_string: str, **kwargs
    ) -> None:
        """Authenticate to Azure Cloud Storage."""
        client = AzureBlobClient(connection_string=connection_string)
        client.set_as_default_client()
