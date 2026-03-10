# sanjjay

An eDEX-UI inspired terminal portfolio CLI package for **Sanjjay**.

After installation, launch with:

```bash
sanjjay
```

## Features

- Cinematic boot sequence with progress animation
- Interactive command dashboard with futuristic styling
- Rich panels, tables, separators, and system telemetry
- Command-driven portfolio sections (about, skills, projects, socials, etc.)
- Modern Python packaging with `pyproject.toml`
- Console entry point via `[project.scripts]`

## Installation

### From local source

```bash
python -m pip install .
```

### From PyPI (after publishing)

```bash
pip install sanjjay
```

## Usage

Run:

```bash
sanjjay
```

Available commands:

- `help`
- `about`
- `skills`
- `projects`
- `github`
- `linkedin`
- `contact`
- `resume`
- `clear`
- `whoami`
- `socials`
- `banner`
- `system`
- `exit`

## Project Structure

```text
.
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
└── sanjjay/
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    ├── ui.py
    ├── data.py
    └── commands.py
```

## Editing Portfolio Content

Edit `sanjjay/data.py` to update:

- Name, role, and bio
- Skills and projects
- Social links
- Contact information
- Certifications and education

## Adding New Commands

1. Add a description in `COMMAND_DESCRIPTIONS` in `sanjjay/data.py`.
2. Add a handler method in `CommandHandler` in `sanjjay/commands.py`.
3. Register that method in the `handlers` dict in `CommandHandler.execute`.

## Build Package

```bash
python -m pip install --upgrade build
python -m build
```

This generates wheel and source distributions in `dist/`.

## Publish Updates to PyPI

1. Update `version` in `pyproject.toml`.
2. Rebuild distributions:
   ```bash
   rm -rf dist/
   python -m build
   ```
3. Upload with Twine:
   ```bash
   python -m pip install --upgrade twine
   python -m twine upload dist/*
   ```

For TestPyPI:

```bash
python -m twine upload --repository testpypi dist/*
```

## License

MIT License (see `LICENSE`).
