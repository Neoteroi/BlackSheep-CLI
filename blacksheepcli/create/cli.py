from typing import Optional

import questionary
from pathvalidate import is_valid_filename

from blacksheepcli.common import click
from blacksheepcli.create.domain import ProjectManager
from blacksheepcli.templates.cli import get_template_by_name, prompt_template


def print_instructions(destination: str):
    from rich.console import Console

    console = Console()

    console.rule()
    console.print(f"[bold green]🏗️  Project created in {destination}")
    console.rule()
    console.print("-- What's next:")
    console.print(f"\tcd {destination}")

    console.print("\tpip install -r requirements.txt\n\tpython dev.py")


@click.command(name="create")
@click.argument("name", required=False)
@click.option(
    "--destination",
    "-d",
    help=(
        "Destination file path, if not provided, the project "
        "is created in a new folder in CWD."
    ),
    default=None,
    required=False,
)
@click.option(
    "--template",
    "-t",
    help="Project template name.",
    required=False,
)
def create_project(
    name: Optional[str] = None,
    destination: Optional[str] = None,
    template: Optional[str] = None,
):
    """
    Create a new project, with the given NAME, from a template.

    Examples:

        blacksheep create my-proj

        blacksheep create my-proj --template basic
    """
    while not name:
        # unsafe_ask because we let Click handle user cancellation
        name = questionary.text("Project name:", qmark="✨").unsafe_ask()

    if not is_valid_filename(name):
        raise click.ClickException(
            "Invalid name. The provided name must be a valid folder name."
        )

    if destination is None:
        destination = name

    if template:
        template_obj = get_template_by_name(template)
    else:
        template_obj = prompt_template()

    assert destination is not None
    ProjectManager().bootstrap(
        template_obj.source, template_obj.tag or None, {"project_name": name}
    )

    print_instructions(destination)
