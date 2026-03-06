from project_scaffolder.project_init import init_project


def test_project_creation(tmp_path, package_name: str):

    project_name = "demo_project"
    package = package_name

    init_project(project_name, package, base_path=tmp_path)

    project_dir = tmp_path / project_name

    assert project_dir.exists()
    assert (project_dir / "src").exists()
    assert (project_dir / "data").exists()
