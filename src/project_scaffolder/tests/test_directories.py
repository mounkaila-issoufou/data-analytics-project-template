from project_scaffolder.scaffold.directories import create_directories


def test_create_directories(package_name: str, tmp_path):
    project_path = tmp_path / "test_project"

    create_directories(project_path, package_name)

    assert project_path.exists()
