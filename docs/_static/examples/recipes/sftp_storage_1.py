from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.storages.sftp_storage import SFTPStorage

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)

SFTP_STORAGE = SFTPStorage(
    host="your-sftp-host.domain",
    port=22,
    username="your-sftp-username",
    password="your-sftp-password",
    root_path="/dir-name",
)

# txt_file = FAKER.txt_file(storage=SFTP_STORAGE)
