#!/usr/bin/env python3

###
# This module implements the [C]-ommand [L]-ine [I]-nterface of ¨multimd.
###

import                        typer
from typing_extensions import Annotated
import                        rich

# from .multimdbuild import *


# --------- #
# -- CLI -- #
# --------- #

app = typer.Typer()

###
# prototype::
#     ...
###

@app.command(
    help = "Awesome CLI user manager."
)
def multimd_CLI(
    name: Annotated[
        str,
        typer.Option(
            '-n',
            help = "The name to say hi to.")
    ] = "World",
) -> None:
    rich.print({"a": f"Hello {name}"})
