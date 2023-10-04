#!/usr/bin/env python3

###
# This module implements the [C]-ommand [L]-ine [I]-nterface of ¨src2prod.
###


from typing import Union

import                        typer
from typing_extensions import Annotated

from .project import *


# --------- #
# -- CLI -- #
# --------- #

CLI = typer.Typer()

###
# prototype::
#     project : the path of the project folder.
#     src     : the **relative** path of the source dir (regarding the project
#               folder).
#     dest    : the **relative** path of the final product dir (regarding the
#               project folder).
#     ignore  : the rules for ignoring files in addition to what ¨git does.
#               You can use this argument even if you don't work with
#     usegit  : ''True'' asks to use ¨git contrary to ''False''.
#     readme  : '''''' is if you don't need to import an external
#               path::''README'' file, otherwise give a **relative** path.
#
#     :action: this function allows to update a project from a terminal.
###
@CLI.command(
    context_settings = dict(
        help_option_names = ['--help', '-h']
    ),
    help = 'Update your "source-to-product" projects.'
)
def _CLI(
    project: Annotated[
        Path,
        typer.Argument(
            help = "Path of the project folder."
    )],
    src    : Annotated[
        Path,
        typer.Option(
            '--src', '-s',
            help = 'Relative path of the source folder of the project. '
                   'The default value is "src".'
    )] = Path("src"),
    dest   : Annotated[
        Path,
        typer.Option(
            '--dest', '-d',
            help = 'Relative path of the product folder of the project. '
                   'The default value ''None'' indicates  to use '
                   'the lower case name of the project.'
    )] = None,
    ignore : Annotated[
        Path,
        typer.Option(
            '--ignore', '-i',
            help = 'Path to a file with the rules for ignoring files '
                   'in addition to what git does. '
                   'The default value '''''' indicates to not use '
                   'any rule.'
    )] = '',
    usegit : Annotated[
        bool,
        typer.Option(
            '--usegit', '-g',
            help = 'This flag is to use git.'
    )] = True,
    readme : Annotated[
        Union[None, Path],
        typer.Option(
            '--readme', '-r',
            help = 'Relative path of an external "README" file, or '
                   'a "readme" folder. '
                   'The default value ''None'' indicates to not use '
                   'any external "README" file.'
    )] = None,
    erase  : Annotated[
        bool,
        typer.Option(
            '--erase', '-e',
            help = 'TO USE WITH A LOT OF CAUTION! '
                   'This flag allows to remove a none empty target folder.'
    )] = False,
) -> None:
# We take care of the user...
    if not erase:
        print('WARNING: Using ''--erase'' can be dangerous.')

# What is the target?
    if dest == None:
        dest = Path(project.name.lower())

# Let the class Project does the job.
    Project(
        project = project,
        src    = src,
        dest   = dest,
        ignore = ignore,
        usegit = usegit,
        readme = readme,
    ).update(erase)
