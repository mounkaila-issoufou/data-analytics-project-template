import runpy


def test_main_module_runs():
    try:
        runpy.run_module("project_scaffolder", run_name="__main__")
    except SystemExit:
        pass
