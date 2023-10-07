from faker import Faker
from faker_file.providers.txt_file import TxtFileProvider

FAKER = Faker()
FAKER.add_provider(TxtFileProvider)

txt_file = FAKER.txt_file(max_nb_chars=1024**2)  # 1 Mb
txt_file = FAKER.txt_file(max_nb_chars=3 * 1024**2)  # 3 Mb
txt_file = FAKER.txt_file(max_nb_chars=10 * 1024**2)  # 10 Mb

txt_file = FAKER.txt_file(max_nb_chars=1024)  # 1 Kb
txt_file = FAKER.txt_file(max_nb_chars=3 * 1024)  # 3 Kb
txt_file = FAKER.txt_file(max_nb_chars=10 * 1024)  # 10 Kb
