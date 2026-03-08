def build_project_makefile(project_name: str, package_name: str) -> str:
    return rf"""
.PHONY: install lint format test run

install:
	pip install -e .

lint:
	ruff src

format:
	black src
	isort src

test:
	pytest -v

run:
	python -m {package_name}

hooks:
	pre-commit install
"""
