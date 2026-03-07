from project_scaffolder.scaffold.directories import create_directories


def test_create_directories(tmp_path):
    package_name = "test_project"

    project_path = tmp_path / package_name

    create_directories(project_path, package_name)

    assert project_path.exists()
