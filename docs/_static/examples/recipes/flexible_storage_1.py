from django.conf import settings
from django.core.files.storage import default_storage
from faker_file.storages.aws_s3 import AWSS3Storage
from faker_file.storages.filesystem import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage

# Faker doesn't know anything about Django. That's why, if we want to
# support remote storages, we need to manually check which file storage
# backend is used. If `Boto3` storage backend (of the `django-storages`
# package) is used we use the correspondent `AWSS3Storage` class of the
# `faker-file`.
# Otherwise, fall back to native file system storage (`FileSystemStorage`)
# of the `faker-file`.
if isinstance(default_storage, S3Boto3Storage):
    STORAGE = AWSS3Storage(
        bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
        credentials={
            "key_id": settings.AWS_ACCESS_KEY_ID,
            "key_secret": settings.AWS_SECRET_ACCESS_KEY,
        },
        root_path="",
        rel_path="tmp",
    )
else:
    STORAGE = FileSystemStorage(
        root_path=settings.MEDIA_ROOT,
        rel_path="tmp",
    )
