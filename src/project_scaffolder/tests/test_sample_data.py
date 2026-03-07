from project_scaffolder.data.sample_data import generate_sample_data


def test_generate_sample_data(tmp_path):
    package_name = "demo_project"

    generate_sample_data(tmp_path, package_name)

    data_dir = tmp_path / "data" / "raw"

    assert data_dir.exists()
