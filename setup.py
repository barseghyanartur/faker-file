import os

from setuptools import find_packages, setup

version = "0.3"

try:
    readme = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()
except OSError:
    readme = ""

dependency_links = []

# Dependencies
install_requires = [
    "Faker",
]

tests_require = [
    "factory_boy",
    "parametrize",
    "pytest",
    "pytest-cov",
    "pytest-django",
    "pytest-pythonpath",
    "pytest-ordering",
    "coverage",
]

extras_require = (
    {
        "all": [
            "Faker",
            "imgkit",
            "openpyxl",
            "pdfkit",
            "python-docx",
            "python-pptx",
        ],
        "docx": ["python-docx"],
        "pptx": ["python-pptx"],
        "pdf": ["pdfkit"],
        "jpg": ["imgkit"],
        "png": ["imgkit"],
        "svg": ["imgkit"],
        "ico": ["imgkit"],
        "webp": ["imgkit"],
        "xlsx": ["openpyxl"],
        "django": ["Django>=2.2"],
        "sqlalchemy": ["SQLAlchemy>=1.0", "SQLAlchemy-Utils>=0.37.0"],
    },
)

setup(
    name="faker-file",
    version=version,
    description="Generate fake files.",
    long_description=f"{readme}",
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
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
    keywords="faker, faker-file, files, testing, factories",
    author="Artur Barseghyan",
    author_email="artur.barseghyan@gmail.com",
    url="https://github.com/barseghyanartur/faker-file/",
    package_dir={"": "src"},
    packages=find_packages(where="./src"),
    license="MIT",
    install_requires=install_requires,
    tests_require=tests_require,
    dependency_links=dependency_links,
    include_package_data=True,
)
