def build_project_pyproject(project_name: str, package_name: str) -> str:
    return f"""
[project]
name = "{project_name}"
version = "0.1.0"
description = "CLI tool to initialize a modular data project"
authors = [{{name = "abdoul"}}]
requires-python = ">=3.10"

[project.scripts]
project-scaffolder = "{package_name}.cli:main"

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

# -----------------
# Black configuration
# -----------------
[tool.black]
line-length = 88
target-version = ["py310"]

# -----------------
# Ruff configuration
# -----------------
[tool.ruff]
line-length = 88
target-version = ["py310"]
select = ["E", "F", "I"]
fix = true
ignore = ["E501"]
quote-style = "double"
indent-style = "space"

[tool.pytest.ini_options]
testpaths = [
    "src/{package_name}/tests"
]
"""
