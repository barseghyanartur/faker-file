import os

__all__ = (
    "project_dir",
    "gettext",
    "PROJECT_DIR",
)


def project_dir(base: str) -> str:
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), base).replace("\\", "/")
    )


def gettext(s: str) -> str:
    return s


PROJECT_DIR = project_dir
