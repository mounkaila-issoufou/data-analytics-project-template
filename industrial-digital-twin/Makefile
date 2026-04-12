
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
	python -m digital_twin

hooks:
	pre-commit install
