from pathlib import Path

from project_scaffolder.config import README_LOCATIONS, NOTEBOOKS
from project_scaffolder.templates.readme_template import build_project_readme
from project_scaffolder.templates.precommit_template import build_project_precommit 
from project_scaffolder.templates.docker_compose_tempale import build_project_docker_compose 
from project_scaffolder.templates.changelog_template import build_project_changelog 

# ============================================================
# README FILES (folders)
# ============================================================

def create_readmes(base_path: Path):
    for location in README_LOCATIONS:
        readme_path = base_path / location / "README.md"
        readme_path.parent.mkdir(parents=True, exist_ok=True)
        readme_path.touch(exist_ok=True)


# ============================================================
# NOTEBOOKS
# ============================================================

def create_notebooks(base_path: Path):
    notebooks_path = base_path / "notebooks"
    notebooks_path.mkdir(parents=True, exist_ok=True)

    for nb in NOTEBOOKS:
        (notebooks_path / nb).touch(exist_ok=True)


# ============================================================
# ROOT FILES
# ============================================================

def create_root_files(base_path: Path, project_name: str, package_name: str):

    # ---------- Main README ----------
    readme_path = base_path / "README.md"

    if not readme_path.exists():
        readme_content = build_project_readme(project_name, package_name)
        readme_path.write_text(readme_content, encoding="utf-8")

    # ---------- .gitignore ----------
    gitignore = base_path / ".gitignore"

    if not gitignore.exists():
        gitignore.write_text(
            "# Python\n"
            "__pycache__/\n"
            ".venv/\n"
            ".env\n"
            "*.pyc\n"
            ".ipynb_checkpoints/\n"
            "logs/\n",
            encoding="utf-8",
        )

    # ---------- Other root files ----------
    (base_path / "requirements.txt").touch(exist_ok=True)
    (base_path / "pyproject.toml").touch(exist_ok=True)
    (base_path / ".pre-commit-config.yaml").touch(exist_ok=True)
    (base_path / ".pre-commit-config.yaml").write_text(build_project_precommit(project_name, package_name), encoding="utf-8")
    (base_path / "docker-compose.yaml").touch(exist_ok=True)
    (base_path / "docker-compose.yaml").write_text(build_project_docker_compose(project_name, package_name), encoding="utf-8")
    (base_path / "CHANGELOG.md").touch(exist_ok=True)
    (base_path / "CHANGELOG.md").write_text(build_project_changelog(project_name, package_name), encoding="utf-8")