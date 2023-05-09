#!/usr/bin/env python3

###
# This module implements the [C]-ommand [L]-ine [I]-nterface of ¨multimd.
###

from pathlib import Path

import                        typer
from typing_extensions import Annotated

from .mmdbuild import MMDBuilder


# --------- #
# -- CLI -- #
# --------- #

mmd_CLI = typer.Typer()

###
# prototype::
#     src  : the path of the source directory with the MD chunks to be merged.
#     dest : the path of the final MD file to build.
#
#     :action: :see: mmdbuild.MMDBuilder
###
@mmd_CLI.command(
    context_settings = dict(
        help_option_names = ['--help', '-h']
    ),
    help = "Merging MD chunks into a single MD file."
)
def _mmd_CLI(
    src: Annotated[
        Path,
        typer.Option(
            '--src', '-s',
            help = "Path of the source directory with "
                   "the MD chunks to be merged."
    )],
    dest: Annotated[
        Path,
        typer.Option(
            '--dest', '-d',
            help = "Path of the final MD file to build."
    )],
) -> None:
    kwargs = {
        "src" : src,
        "dest": dest,
    }

# Relative to absolute?
    cwd = Path.cwd()

    for k, p in kwargs.items():
        if not p.is_absolute():
            kwargs[k] = cwd / p

# Let's call our worker.
    MMDBuilder(
        src  = src,
        dest = dest,
    ).build()
