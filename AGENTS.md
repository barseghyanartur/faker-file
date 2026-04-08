# AGENTS.md — faker-file

**Package version**: See pyproject.toml
**Repository**: https://github.com/barseghyanartur/faker-file
**Maintainer**: Artur Barseghyan <artur.barseghyan@gmail.com>

This file is for AI agents and developers using AI assistants to work on or with
faker-file. It covers two distinct roles: **using** the package in application code,
and **developing/extending** the package itself.

---

## 1. Project Mission (Never Deviate)

> Generate realistic fake files for testing purposes with support for multiple file formats, data augmentation, and cloud storage backends.

Core principles:

- **Reliability** — Files should be generated deterministically when possible for reproducible tests.
- **Realism** — Generated content should be realistic and useful for testing.
- **Extensibility** — Easy to add new file types and storage backends.
- **No side effects** — Generation should not modify external state.

---

## 2. Using faker-file in Application Code

> **Note:** `<!-- pytestfixture: my_fixture -->` is given as an example.
> It might be relevant if test uses cloud storages (in that case `mock_aws`
> fixture is handy to use) or other cases requiring pytest magic. It's
> fully optional and might not be alawys needed. Feel free to remove.

### Simple case

<!-- pytestfixture: Faker -->
```python name=test_simple_case
from faker_file.providers.txt_file import TxtFileProvider

faker = Faker()  # from Faker
faker.add_provider(TxtFileProvider)

file_path = faker.txt_file()
```

### With custom configuration

<!-- pytestfixture: Faker -->
```python name=test_with_config
from faker_file.providers.docx_file import DocxFileProvider

faker = Faker()  # from Faker
faker.add_provider(DocxFileProvider)

file_path = faker.docx_file(content="{first_name} {last_name}")
```

### With storage

<!-- pytestfixture: Faker -->
<!-- pytestfixture: aws_mock -->
```python name=test_with_storage
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.storages.aws_s3 import AWSS3Storage

storage = AWSS3Storage(bucket_name="my-test-bucket")
faker = Faker()
faker.add_provider(TxtFileProvider)

file_path = faker.txt_file(storage=storage)
```

### Configuration reference

| Parameter | Type | Default |
| --- | --- | --- |
| `content` | str | Generated text |
| `prefix` | str | Random prefix |
| `max_nb_chars` | int | 65536 |
| `storage` | Storage | FileSystemStorage |

---

## 3. Architecture

### Key files

| File | Purpose |
| --- | --- |
| `src/faker_file/base.py` | Base classes for providers and storages |
| `src/faker_file/providers/` | File type providers (txt, pdf, docx, etc.) |
| `src/faker_file/storages/` | Storage backends (filesystem, S3, Azure, GCS) |
| `src/faker_file/registry.py` | Provider registry |
| `src/faker_file/cli/` | CLI implementation |
| `pyproject.toml` | Build and tool configuration |
| `README.rst` | Usage documentation |

### Provider structure

Each provider extends `BaseProvider` and implements file generation:

- `TxtFileProvider` — Plain text files
- `PdfFileProvider` — PDF files (multiple backends: reportlab, pdfkit, pil)
- `DocxFileProvider` — Word documents
- `XlsxFileProvider` — Excel files
- `CsvFileProvider` — CSV files
- And many more...

### Storage backends

- `FileSystemStorage` — Local filesystem (default)
- `AWS S3Storage` — Amazon S3
- `AzureBlobStorage` — Azure Blob Storage
- `GoogleCloudStorage` — Google Cloud Storage
- `SFTPStorage` — SFTP server

---

## 4. Development Principles

**1. Backward compatibility first.**
    Never break existing public APIs. Deprecate gently with warnings.

**2. Provider isolation.**
    Each file type provider should be self-contained with no cross-dependencies.

**3. Storage abstraction.**
    All storage operations go through the storage interface. Providers don't access files directly.

**4. Deterministic when possible.**
    Use seed-aware faker for reproducible output in tests.

**5. No external network calls during generation.**
    Unless explicitly requested (e.g., `file_from_url` provider).

---

## 5. Known Intentional Behaviors — Do Not Treat as Bugs

### Behavior 1: File cleanup is opt-in

Generated files are not automatically deleted. Call `storage.delete()` explicitly or use context managers.

### Behavior 2: Large file generation may be slow

Some providers (pdf, docx) generate real content which takes time. Use `max_nb_chars` to limit size.

### Behavior 3: S3 mocking required for tests

Tests that use S3 storage should use `moto` or similar mocking.

---

## 6. Agent Workflow: Adding Features or Fixing Bugs

When asked to add a feature or fix a bug, follow these steps in order:

1. **Understand the scope** — Does the change fit the project mission?
2. **Identify the correct module** — Where should the change live?
3. **For bug fixes: write the regression test first** — The test must fail before your fix.
4. **Implement the change** in the correct file.
5. **Export** new public symbols from `__init__.py` and `__all__`.
6. **Write tests:**
   - Unit test in the relevant `test_*.py` file.
   - Integration test if applicable.
   - Test for the legitimate-input happy path.
7. **Update documentation** if you modify the public API.
8. **Run tests:** `make docker-test` or `make test-env ENV=py312`
9. **Run linting:** `make pre-commit`.

### Acceptable new features

- New file type providers (txt, csv, json, pdf, docx, etc.)
- New storage backends
- Data augmentation capabilities
- CLI enhancements

### Forbidden

- Adding external dependencies without discussion.
- Removing existing provider functionality.
- Weakening type safety.

---

## 7. Testing Rules

### Running tests

```sh
make docker-test              # full matrix
make docker-test-env ENV=py312  # single version
make docker-shell             # interactive shell
```

### Test layout

```text
src/faker_file/tests/
    conftest.py          — test fixtures
    test_base.py
    test_helpers.py
    test_registry.py
    ...
```

The **root `conftest.py`** (project root) is for `pytest-codeblock` documentation
testing only. Do not add unit test fixtures there.

### Required assertions

```python
# 1. pytest.raises wraps the full operation
with pytest.raises(Exception):
    result = function_under_test(input_data)

# 2. Verify the file was created
assert file_path.exists()
```

---

## 8. Coding Conventions

Run all linting checks:

```sh
make pre-commit
```

### Formatting

- Line length: **80 characters** (ruff).
- Import sorting: `isort`.
- Target: `py39`+.

### Ruff rules in effect

`B`, `C4`, `E`, `F`, `G`, `I`, `ISC`, `INP`, `N`, `PERF`, `Q`, `SIM`.

### Style

- Every non-test module should have `__all__`, `__author__`, `__copyright__`,
  `__license__` at module level where appropriate.
- Type annotations on all public functions.
- Chain exceptions: `raise X(...) from exc`.

### Pull requests

Target the `main` branch for releases. Use feature branches for development.

---

## 9. Prompt Templates

**Explaining usage to a user:**
> You are an expert in faker-file. Explain how to use faker-file
> for [task]. Start with secure/complete defaults. Include exception handling.

**Implementing a new provider:**
> Add a new [file type] provider to faker-file. Follow the AGENTS.md agent workflow:
> implement the provider, add tests, update README.

**Fixing a bug:**
> Reproduce [bug] with a new test. The test must fail before the fix.
> Then fix in the correct module. Add tests asserting correct behavior
> and that legitimate use cases still work.

**Reviewing a change:**
> Review this faker-file change against AGENTS.md: Does it preserve
> core principles? Does it follow the testing and coding conventions?
