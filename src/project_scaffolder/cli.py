import argparse
from project_scaffolder.pipeline import init_project


def main():
    parser = argparse.ArgumentParser(
        prog="project-scaffolder",
        description="Initialize a new data project structure"
    )

    parser.add_argument("project_name", help="Name of the project to create")
    parser.add_argument(
        "--with-sample-data",
        action="store_true",
        help="Generate sample CSV files"
    )

    args = parser.parse_args()

    init_project(
        project_name=args.project_name,
        with_sample_data=args.with_sample_data
    )