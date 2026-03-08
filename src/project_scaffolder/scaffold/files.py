from pathlib import Path

from project_scaffolder.config import NOTEBOOKS, README_LOCATIONS
from project_scaffolder.templates.changelog_template import build_project_changelog
from project_scaffolder.templates.ci_template import build_project_ci
from project_scaffolder.templates.contributing_template import (
    build_project_contributing,
)
from project_scaffolder.templates.docker_compose_tempale import (
    build_project_docker_compose,
)
from project_scaffolder.templates.gitignore_template import build_project_gitignore
from project_scaffolder.templates.license_template import build_project_license
from project_scaffolder.templates.makefile_template import build_project_makefile
from project_scaffolder.templates.precommit_template import build_project_precommit
from project_scaffolder.templates.pyproject_template import build_project_pyproject
from project_scaffolder.templates.readme_template import build_project_readme

# ============================================================
# README FILES (folders)
# ============================================================


def create_readmes(base_path: Path):

    for location in README_LOCATIONS:
        readme_path = base_path / location / "README.md"

        readme_path.parent.mkdir(parents=True, exist_ok=True)

        if not readme_path.exists():
            readme_path.touch()


# ============================================================
# NOTEBOOKS
# ============================================================


def create_notebooks(base_path: Path):

    notebooks_path = base_path / "notebooks"
    notebooks_path.mkdir(parents=True, exist_ok=True)

    for nb in NOTEBOOKS:
        notebook = notebooks_path / nb

        if not notebook.exists():
            notebook.touch()


# ============================================================
# ROOT FILES
# ============================================================


def create_root_files(base_path: Path, project_name: str, package_name: str):

    # ---------- Main README ----------
    readme_path = base_path / "README.md"

    if not readme_path.exists():
        readme_content = build_project_readme(project_name, package_name)
        readme_path.write_text(readme_content, encoding="utf-8")

    # ---------- requirements ----------
    requirements = base_path / "requirements.txt"

    if not requirements.exists():
        requirements.touch()

    # ---------- pre-commit ----------
    precommit = base_path / ".pre-commit-config.yaml"

    if not precommit.exists():
        precommit.write_text(
            build_project_precommit(project_name, package_name),
            encoding="utf-8",
        )

    # ---------- docker compose ----------
    docker_compose = base_path / "docker-compose.yaml"

    if not docker_compose.exists():
        docker_compose.write_text(
            build_project_docker_compose(project_name, package_name),
            encoding="utf-8",
        )

    # ---------- changelog ----------
    changelog = base_path / "CHANGELOG.md"

    if not changelog.exists():
        changelog.write_text(
            build_project_changelog(project_name, package_name),
            encoding="utf-8",
        )
    # ---------- LICENSE ----------
    license_file = base_path / "LICENSE"

    if not license_file.exists():
        license_file.write_text(
            build_project_license(project_name, package_name),
            encoding="utf-8",
        )

    # ---------- CONTRIBUTING ----------
    contributing_file = base_path / "CONTRIBUTING.md"

    if not contributing_file.exists():
        contributing_file.write_text(
            build_project_contributing(project_name, package_name),
            encoding="utf-8",
        )

    # ---------- gitignore ----------
    gitignore = base_path / ".gitignore"

    if not gitignore.exists():
        gitignore.write_text(
            build_project_gitignore(project_name, package_name),
            encoding="utf-8",
        )

    # ---------- Makefile ----------
    makefile = base_path / "Makefile"

    if not makefile.exists():
        makefile.write_text(
            build_project_makefile(project_name, package_name),
            encoding="utf-8",
        )

    # ---------- ci ----------
    ci_path = base_path / ".github" / "workflows"
    ci_path.mkdir(parents=True, exist_ok=True)
    ci_file = ci_path / "ci.yaml"
    if not ci_file.exists():
        ci_file.write_text(
            build_project_ci(project_name, package_name),
            encoding="utf-8",
        )
    # ---------- pyprojec.toml ----------
    pyproject = base_path / "pyproject.toml"

    if not pyproject.exists():
        pyproject.write_text(
            build_project_pyproject(project_name, package_name),
            encoding="utf-8",
        )
