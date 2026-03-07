from project_scaffolder.cli import main


def test_cli_runs(monkeypatch):

    monkeypatch.setattr(
        "sys.argv",
        ["project_scaffolder", "init", "demo_project"],
    )

    try:
        main()
    except SystemExit:
        pass
