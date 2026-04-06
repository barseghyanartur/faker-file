---
name: update-documentation
description: Sync faker-file project documentation with source code. Scans code and docs, finds misalignments, and auto-fixes them. Pure agent-based - no Python scripts involved.
---

# Update Documentation Skill

**Operation mode**: Pure agent-based documentation synchronization.

When the user asks to `sync-documentation`, the agent:
1. Scans source code to extract ground truth (public API, CLI commands, exceptions)
2. Scans all documentation files
3. Identifies misalignments between code and docs
4. **Auto-fixes documentation** to match code (reports what was changed)

**This is NOT a Python script** - the agent performs all analysis and edits directly.

## Agent-Based Sync Process

When `sync-documentation` is invoked:

### Step 1: Extract Ground Truth from Code

Scan source code to identify:

- **Public API**: Exports from `__all__` in `src/faker_file/__init__.py` and provider `__init__.py` files
- **CLI commands**: Subcommands defined in `src/faker_file/cli/`
- **Exceptions**: Exception classes in provider files
- **Storage backends**: Classes in `src/faker_file/storages/`
- **Providers**: Classes in `src/faker_file/providers/`

### Step 2: Scan Documentation Files

Read and analyze:

- `README.rst` - Public API, CLI usage, quick start
- `AGENTS.md` - Architecture, code patterns, examples
- `ARCHITECTURE.rst` - Architecture, principles
- `CONTRIBUTING.rst` - Contribution workflow
- `SECURITY.rst` - Security policy and reporting
- `docs/*.rst` - Extended documentation

### Step 3: Identify Misalignments

Compare code ground truth against documentation:

- Missing file types in provider tables
- Undocumented CLI commands or options
- Missing storage backends
- Broken file path references
- Outdated information
- Missing code examples

### Step 4: Auto-Fix Documentation

**The agent directly edits documentation files** to align with code:

- Add missing entries to tables
- Update code examples
- Fix file references
- Add missing sections
- Update outdated information

**SKILL.md is NOT modified** - it remains the source of truth for the skill behavior.

### Step 5: Report Changes

After fixing, report:

- Which files were modified
- What changes were made
- Any issues that couldn't be auto-fixed

---

## Documentation Files Overview

| File | Audience | Purpose |
| ---- | -------- | ------- |
| `README.rst` | End users | Public API, quick start, usage examples |
| `AGENTS.md` | AI agents | Mission, architecture, agent workflow, code patterns |
| `ARCHITECTURE.rst` | Developers | Architecture, principles, design decisions |
| `CONTRIBUTING.rst` | Contributors | Contribution workflow, testing, release process |
| `SECURITY.rst` | Security researchers | Security policy, reporting vulnerabilities |
| `docs/*.rst` | Users/developers | Extended documentation, API reference |

## When to Update Each File

### README.rst

Update when:

- New file type providers are added
- New CLI commands or options
- Storage backends change
- Configuration options change

Structure to maintain:

- Features list
- Quick start examples
- Installation section
- Provider list
- Storage backends
- Configuration examples

### AGENTS.md

Update when:

- Architecture changes
- New providers or storages added
- Exception handling changes
- Testing workflow changes

Key sections:

- Project mission
- Architecture table
- Development principles
- Agent workflow section
- Testing rules

### ARCHITECTURE.rst

Update when:

- Architecture changes
- New components added
- Storage backends change

Key sections:

- Core philosophy
- Provider details
- Storage backends
- Configuration options

### CONTRIBUTING.rst

Update when:

- Contribution workflow changes
- Testing procedure changes
- Release process changes

### SECURITY.rst

Update when:

- Security policy changes
- Reporting process changes

---

## Code Block Naming Convention

AGENTS.md uses executable code blocks with `name=<test_name>` attributes:

````markdown
<!-- pytestfixture: my_fixture -->
<!-- TODO: Replace my_fixture with your actual fixture name from conftest.py -->
```python name=test_example
from faker_file.providers.txt_file import TxtFileProvider

faker = Faker()
faker.add_provider(TxtFileProvider)
result = faker.txt_file()
```
````

All code examples in README.rst (and other reStructuredText files) should be
runnable tests. Use the `:name:` attribute to prefix the block name with `test_`:

```rst
.. pytestfixture: my_fixture
.. code-block:: python
    :name: test_feature_name

   from faker_file.providers.txt_file import TxtFileProvider

   faker = Faker()
   faker.add_provider(TxtFileProvider)
   result = faker.txt_file()
```

---

## Validation Checklist

Before finishing documentation updates:

- [ ] README.rst examples match actual API
- [ ] AGENTS.md code blocks have proper `name=` attributes
- [ ] All providers are documented with their storage backends
- [ ] CONTRIBUTING.rst reflects current contribution process
- [ ] SECURITY.rst is up to date
- [ ] All RST files pass linting
- [ ] Cross-references between docs are valid
- [ ] File paths in docs match actual paths

---

**Use Agent-Based Sync (`sync-documentation`) when:**
- User explicitly asks to "sync documentation"
- You need documentation auto-fixed, not just validated
- You want an interactive, conversational workflow
