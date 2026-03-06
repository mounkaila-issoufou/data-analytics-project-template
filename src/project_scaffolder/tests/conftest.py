import pytest


@pytest.fixture
def temp_project(tmp_path):
    return tmp_path / "generated_project"
