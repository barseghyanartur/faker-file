from multiprocessing import Pool

from faker import Faker
from faker_file.providers.helpers.inner import create_inner_docx_file
from faker_file.storages.filesystem import FileSystemStorage

FAKER = Faker()
STORAGE = FileSystemStorage()

# Document template
TEMPLATE = "Hey {{name}},\n{{text}},\nBest regards\n{{name}}"

with Pool(processes=2) as pool:
    for _ in range(10):  # Number of times we want to run our function
        pool.apply_async(
            create_inner_docx_file,
            # Apply async doesn't support kwargs. We have to pass all
            # arguments.
            [STORAGE, "mp", FAKER, None, None, TEMPLATE],
        )
    pool.close()
    pool.join()
