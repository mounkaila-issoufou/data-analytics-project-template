# Contributing

Thank you for considering contributing to this project.

## Development setup

Clone the repository:

```bash
git clone <repo-url>
cd project-scaffolder
```
Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```

Install pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
Coding guidelines
```

Follow PEP8

- Use Black for formatting

- Use isort for import sorting

- Keep functions small and readable

Commit messages

We follow Conventional Commits:

Examples:

- feat: add docker template
- fix: correct scaffolder path
- docs: update README
- refactor: improve scaffolding logic

Pull requests

- Create a feature branch

- Commit your changes

- Push your branch

- Open a Pull Request