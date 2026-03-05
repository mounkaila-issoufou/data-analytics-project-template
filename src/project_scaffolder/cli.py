import argparse

from project_scaffolder.pipeline import init_project


def main():
    parser = argparse.ArgumentParser(
        prog="data-project",
        description="Generate a data analytics project structure",
    )

    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument(
        "--with-sample-data", action="store_true", help="Generate sample CSV files"
    )
    init_parser.add_argument("name", help="Project folder name")
    init_parser.add_argument(
        "--package", required=True, help="Python package name (e.g. sales_orders)"
    )

    args = parser.parse_args()

    if args.command == "init":
        init_project(
            project_name=args.name,
            with_sample_data=args.with_sample_data,
            package_name=args.package,
        )
