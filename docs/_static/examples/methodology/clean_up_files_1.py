# Import instance at once
from faker_file.registry import FILE_REGISTRY

# Trigger the clean-up
FILE_REGISTRY.clean_up()
