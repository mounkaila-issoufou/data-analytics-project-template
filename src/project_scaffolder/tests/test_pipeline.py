from project_scaffolder.pipeline import init_project


def test_pipeline_init(tmp_path):

    project_path = tmp_path / "demo_project"

    init_project(
        project_name=str(project_path),
        package_name="demo_project",
        with_sample_data=False,
    )

    assert project_path.exists()
