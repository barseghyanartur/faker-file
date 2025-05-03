import re
from pathlib import Path

from setuptools import find_packages, setup


def clean_readme(text: str) -> str:
    # Pattern to match ":emphasize-lines:" followed by digits
    emphasize_lines_pattern = r":emphasize-lines: \d+"
    text = re.sub(emphasize_lines_pattern, "", text)

    # # Pattern to match ":name:" followed by any characters to the line end
    # name_lines_pattern = r":name: .*$"
    # text = re.sub(name_lines_pattern, "", text, flags=re.MULTILINE)

    return text


version = "0.18.2"

try:
    readme_path = Path(__file__).parent / "README.rst"
    readme = clean_readme(readme_path.read_text())
except FileNotFoundError:
    readme = ""

dependency_links = []

# Dependencies
install_requires = [
    "Faker",
]

tests_require = [
    "asyncssh",  # SFTP
    "coverage",  # coverage
    "factory_boy",  # factories
    "fuzzywuzzy[speedup]",  # data integrity
    "parametrize",  # testing
    "pytest",  # pytest
    "pytest-cov",  # pytest add-on, coverage
    "pytest-django",  # pytest add-on, django
    "pytest-ordering",  # pytest add-on
    "pytest-pythonpath",  # pytest add-on
    "pytest-codeblock",  # pytest add-on
    "moto>=5.0.0",  # testing documentation
]

_common = [
    "Faker",  # core
    "WeasyPrint",  # BMP, GIF, TIFF
    "imgkit",  # images: ICO, JPEG, PNG, SVG, WEBP
    "odfpy",  # ODP, ODS, ODT
    "openpyxl",  # XLSX
    "pathy[all]>=0.10.0,<0.12.0",  # remote storages: Azure, GCS, S3
    "paramiko",  # SFTP storage
    "pdf2image",  # BMP, GIF, TIFF
    "pdfkit",  # PDF
    "reportlab",  # PDF
    "python-docx",  # DOCX
    "python-pptx",  # PPTX
    "tablib",  # ODS, XLSX
    "xml2epub",  # EPUB
    "gtts",  # MP3
    "edge-tts",  # MP3
]

_ml = [
    "nlpaug",  # data-augmentation
    "nltk",  # data-augmentation
    "textaugment",  # data-augmentation
    "textblob>=0.17,<0.18",
    "tika",  # data-augmentation
    "torch",  # data-augmentation
    "transformers",  # data-augmentation
]

extras_require = {
    "all": _common + _ml,
    "common": _common,
    "azure": ["pathy[azure]>=0.10.0,<0.12.0"],
    "bmp": ["WeasyPrint", "pdf2image"],
    "django": ["Django>=2.2"],
    "docx": ["python-docx"],
    "epub": ["xml2epub"],
    "gcs": ["pathy[gcs]>=0.10.0,<0.12.0"],
    "gif": ["WeasyPrint", "pdf2image"],
    "images": ["imgkit"],
    "mp3": ["gtts", "edge-tts"],
    "odp": ["odfpy"],
    "ods": ["tablib", "odfpy"],
    "odt": ["odfpy"],
    "pdf": ["pdfkit", "reportlab"],
    "pptx": ["python-pptx"],
    "s3": ["pathy[s3]>=0.10.0,<0.12.0"],
    "sftp": ["paramiko"],
    "sqlalchemy": ["SQLAlchemy>=1.0", "SQLAlchemy-Utils>=0.37.0"],
    "tiff": ["WeasyPrint", "pdf2image"],
    "xlsx": ["tablib", "openpyxl"],
    "data-augmentation": _ml,
}

setup(
    name="faker-file",
    version=version,
    description="Generate files with fake data.",
    long_description=f"{readme}",
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/barseghyanartur/faker-file/issues",
        "Documentation": "https://faker-file.readthedocs.io/",
        "Source Code": "https://github.com/barseghyanartur/faker-file",
        "Changelog": "https://faker-file.readthedocs.io/"
        "en/latest/changelog.html",
    },
    keywords=(
        ", ".join(
            [
                "factories",
                "fake file",
                "fake files",
                "fake-file-generator",
                "fake-files-generator",
                "faker",
                "faker-file",
                "file-generator",
                "files",
                "files-generator",
                "test file",
                "test files",
                "test-file-generator",
                "test-files-generator",
                "testing",
            ]
        )
    ),
    author="Artur Barseghyan",
    author_email="artur.barseghyan@gmail.com",
    url="https://github.com/barseghyanartur/faker-file/",
    package_dir={"": "src"},
    packages=find_packages(where="./src"),
    entry_points={
        "console_scripts": ["faker-file = faker_file.cli.command:main"]
    },
    license="MIT",
    python_requires=">=3.9",
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    dependency_links=dependency_links,
    include_package_data=True,
)
