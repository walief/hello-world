# hello-world

A tiny Python starter project that gives newcomers a clean, batteries-included baseline:

- package layout under `src/`
- CLI entry point (`hello-world`)
- basic tests with `pytest`
- linting with `ruff`
- CI with GitHub Actions
- clear local development commands

## Project structure

```text
hello-world/
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyproject.toml
├── README.md
├── src/
│   └── hello_world/
│       ├── __init__.py
│       ├── __main__.py
│       └── main.py
└── tests/
    └── test_main.py
```

## Quick start

### 1) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install in editable mode with development dependencies

```bash
pip install -e .[dev]
```

### 3) Run the CLI

```bash
hello-world
# or
python -m hello_world
```

Use `--name` to customize the greeting:

```bash
hello-world --name Python
# Hello, Python!
```

### 4) Run local checks

```bash
ruff check .
pytest
```

## Continuous integration

The GitHub Actions workflow in `.github/workflows/ci.yml` installs the package with development dependencies, runs `ruff check .`, and runs `pytest` for pushes to `main` and pull requests.

## What to learn next

1. **Packaging basics**
   - Understand `pyproject.toml` metadata, package discovery, and entry points.
2. **Testing workflow**
   - Add edge-case tests and learn fixtures.
3. **Linting & formatting**
   - Expand `ruff` rules or add a formatter.
4. **CI/CD**
   - Add build artifacts, coverage reporting, or release checks.
5. **Release workflow**
   - Add semantic versioning and publish to an internal or public package index.

## Suggested follow-up tasks

- Add logging configuration.
- Add a `Makefile` (`make test`, `make lint`, `make run`).
- Add coverage reporting.
- Add a release workflow.
