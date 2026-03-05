.PHONY: install lint format test run

install:
	pip install -e .

lint:
	ruff src

format:
	black src
	isort src

test:
	pytest

run:
	python -m project_scaffolder

hooks:
	pre-commit install