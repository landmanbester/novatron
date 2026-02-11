"""CLI for novatron."""

import typer

app = typer.Typer(
    name="tron",
    help="Next Generation Transient Observations for Newbies",
    no_args_is_help=True,
)


@app.callback()
def callback() -> None:
    """Next Generation Transient Observations for Newbies"""
    pass


# Register subcommands below. Imports go here (bottom) to avoid circular imports.
from novatron.cli.hello_world import hello_world  # noqa: E402

app.command(name="hello-world")(hello_world)

__all__ = ["app"]
