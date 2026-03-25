# hello-world

A tiny Python starter project that gives newcomers a clean, batteries-included baseline:

- package layout under `src/`
- CLI entry point (`hello-world`)
- basic tests with `pytest`
- clear local development commands

## Project structure

```text
hello-world/
├── pyproject.toml
├── README.md
├── src/
│   └── hello_world/
│       ├── __init__.py
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

### 2) Install in editable mode with test dependencies

```bash
pip install -e .[dev]
```

### 3) Run the CLI

```bash
hello-world
# or
python -m hello_world.main
```

### 4) Run tests

```bash
pytest
```

## What to learn next

1. **Packaging basics**
   - Understand `pyproject.toml` metadata and entry points.
2. **Testing workflow**
   - Add edge-case tests and learn fixtures.
3. **Linting & formatting**
   - Add `ruff` or `black` and enforce style in CI.
4. **CI/CD**
   - Add a GitHub Actions workflow to run tests on every PR.
5. **Release workflow**
   - Add semantic versioning and publish to an internal or public package index.

## Suggested follow-up tasks

- Add command-line arguments (`argparse` or `typer`).
- Add logging configuration.
- Add a `Makefile` (`make test`, `make lint`, `make run`).
- Add GitHub Actions CI.
