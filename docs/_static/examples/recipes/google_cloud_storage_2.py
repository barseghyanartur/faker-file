from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)

from faker_file.storages.google_cloud_storage import GoogleCloudStorage

GC_STORAGE = GoogleCloudStorage(
    bucket_name="your-bucket-name",
    root_path="",
    rel_path="user/uploads",
)

# txt_file = FAKER.txt_file(storage=GC_STORAGE)
