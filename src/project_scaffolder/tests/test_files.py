from project_scaffolder.scaffold.files import create_root_files


def test_create_root_files(tmp_path):

    project_name = "demo_project"
    package_name = "demo_project"

    create_root_files(tmp_path, project_name, package_name)

    expected_files = [
        "README.md",
        ".gitignore",
        "requirements.txt",
        "pyproject.toml",
        ".pre-commit-config.yaml",
        "docker-compose.yaml",
        "CHANGELOG.md",
    ]

    for file in expected_files:
        assert (tmp_path / file).exists()
