import click

from project_scaffolder.pipeline import init_project


@click.group()
def main():
    pass


@main.command()
@click.argument("name")
@click.option("--with-sample-data", is_flag=True, help="Generate sample CSV files")
@click.option("--package", required=True, help="Python package name")
def init(name, with_sample_data, package):
    init_project(
        project_name=name,
        with_sample_data=with_sample_data,
        package_name=package,
    )
