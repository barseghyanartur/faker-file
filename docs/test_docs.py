import logging
from pathlib import Path
from unittest import mock
from unittest.mock import create_autospec

import paramiko
import pytest
from django.test import override_settings
from faker_file.registry import FILE_REGISTRY
from moto import mock_s3

# Walk through the directory and all subdirectories for .py files
example_dir = Path("docs/_static/examples")
py_files = sorted([str(p) for p in example_dir.rglob("*.py")])


@pytest.fixture
def mock_gcs():
    """Mock Google Cloud Storage."""
    with mock.patch("google.cloud.storage.Client") as mock_client:
        yield mock_client


@pytest.fixture
def mock_paramiko():
    """Mock paramiko."""
    mock_transport = create_autospec(paramiko.Transport)
    mock_transport.return_value.send = mock.Mock(return_value=42)

    mock_sftp_client = create_autospec(paramiko.SFTPClient)
    mock_sftp_client.from_transport.return_value = mock_sftp_client

    with mock.patch("paramiko.Transport", mock_transport), mock.patch(
        "paramiko.SFTPClient", mock_sftp_client
    ):
        yield


# We have to apply `moto` mocking to all test functions, because in some
# we have boto dependant code.
@mock_s3
def execute_file(file_path, caplog):
    """Dynamic test function."""
    global_vars = {}
    # Set the log level to WARNING for this block
    with caplog.at_level(logging.WARNING):
        with open(file_path, "r") as f:
            code = f.read()
        exec(code, global_vars)


@pytest.mark.django_db
@pytest.mark.parametrize("file_path", py_files)
@override_settings(AWS_STORAGE_BUCKET_NAME="testing")
def test_dynamic_files(file_path, caplog, mock_gcs, mock_paramiko):
    execute_file(file_path, caplog)
    FILE_REGISTRY.clean_up()
