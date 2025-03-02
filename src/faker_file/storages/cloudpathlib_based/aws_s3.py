import boto3
from cloudpathlib import S3Path

from .cloud import CloudStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("AWSS3Storage",)


class AWSS3Storage(CloudStorage):
    """AWS S3 Storage.

    Usage example:

    .. code-block:: python

        from faker_file.storages.cloudpathlib_based.aws_s3 import AWSS3Storage

        s3_storage = AWSS3Storage(
            bucket_name="artur-testing-1",
            rel_path="tmp",
        )
        file = s3_storage.generate_filename(prefix="zzz_", extension="docx")
        s3_storage.write_text(file, "Lorem ipsum")
        s3_storage.write_bytes(file, b"Lorem ipsum")
    """

    schema: str = "s3"

    def authenticate(
        self: "AWSS3Storage",
        key_id: str,
        key_secret: str,
        **kwargs,
    ) -> None:
        """Authenticate to AWS S3 using boto3 and set the default session
        for S3Path.
        """
        session = boto3.Session(
            aws_access_key_id=key_id,
            aws_secret_access_key=key_secret,
            **kwargs
        )
        S3Path.DEFAULT_SESSION = session
