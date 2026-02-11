from pathlib import Path
from typing import Annotated, NewType

import typer
from hip_cargo.utils.decorators import stimela_cab, stimela_output

File = NewType("File", Path)


@stimela_cab(
    name="hello_world",
    info="hip-cargo hello world example",
)
@stimela_output(
    dtype="File",
    name="greetingto",
    info="A file to write the greeting to. Written to stdout by default.",
)
def hello_world(
    name: Annotated[
        str,
        typer.Option(
            help="A name to say hello to",
        ),
    ] = "world",
    extra: Annotated[
        str,
        typer.Option(
            help="An extra message to include in the greeting.",
        ),
        {
            "stimela": {
                "this-is-arbitrary": True,
            },
        },
    ] = "hip-cargo for the win!",
    greetingto: Annotated[
        File | None,
        typer.Option(
            parser=Path,
            help="A file to write the greeting to. Written to stdout by default.",
        ),
    ] = None,
):
    """
    hip-cargo hello world example
    """
    # Lazy import the core implementation
    from novatron.core.hello_world import hello_world as hello_world_core  # noqa: E402

    # Call the core function with all parameters
    hello_world_core(
        name=name,
        extra=extra,
        greetingto=greetingto,
    )
