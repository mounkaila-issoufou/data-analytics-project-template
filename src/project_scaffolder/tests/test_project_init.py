from project_scaffolder.project_init import init_project


def test_project_creation(tmp_path):

    project_name = "demo_project"
    package_name = "demo_project"

    init_project(project_name, package_name, base_path=tmp_path)

    project_dir = tmp_path / project_name

    assert project_dir.exists()
