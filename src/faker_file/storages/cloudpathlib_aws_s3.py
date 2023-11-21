from cloudpathlib import S3Client

from .cloudpathlib_cloud import CloudpathlibCloudStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("CloudpathlibAWSS3Storage",)


class CloudpathlibAWSS3Storage(CloudpathlibCloudStorage):
    """AWS S3 Storage.

    Usage example:

    .. code-block:: python

        from faker_file.storages.cloudpathlib_aws_s3 import (
            CloudpathlibAWSS3Storage
        )

        s3_storage = CloudpathlibAWSS3Storage(
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = s3_storage.generate_filename(prefix="zzz_", extension="docx")
        s3_storage.write_text(file, "Lorem ipsum")
        s3_storage.write_bytes(file, b"Lorem ipsum")
    """

    schema: str = "s3"

    def authenticate(
        self: "CloudpathlibAWSS3Storage",
        key_id: str,
        key_secret: str,
        **kwargs,
    ) -> None:
        """Authenticate to AWS S3."""
        client = S3Client(
            aws_access_key_id=key_id,
            aws_secret_access_key=key_secret,
        )
        client.set_as_default_client()
