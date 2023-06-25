from blacksheepcli.common import click
from blacksheepcli.create.cli import create_project
from blacksheepcli.templates.cli import templates


@click.group()
def main():
    """
    🛠️  CLI to start BlackSheep projects.
    """


main.add_command(create_project)
main.add_command(templates)
