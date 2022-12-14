from pathy import set_client_params

from .cloud import CloudStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("AzureCloudStorage",)


class AzureCloudStorage(CloudStorage):
    """Azure Cloud Storage.

    Usage example:

        from faker_file.storages.azure_cloud_storage import AzureCloudStorage

        azure_storage = AzureCloudStorage(
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = azure_storage.generate_filename(prefix="zzz_", extension="docx")
        azure_storage.write_text(file, "Lorem ipsum")
        azure_storage.write_bytes(file, b"Lorem ipsum")
    """

    schema = "azure"

    def authenticate(
        self: "AzureCloudStorage", connection_string: str, **kwargs
    ) -> None:
        """Authenticate to Azure Cloud Storage."""
        set_client_params("azure", connection_string=connection_string)
