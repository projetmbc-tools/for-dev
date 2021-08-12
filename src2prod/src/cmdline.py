#! /usr/bin/env python3

###
# This module implements a Comand Line Interface.
###

import click

from .project import *


# --------- #
# -- CLI -- #
# --------- #

###
# prototype::
#     project = ; // See Python typing...
#               the folder project that will be used to communicate during 
#               the analysis.
#     src     = ; // See Python typing...
#               the **relative** path of the source dir (regarding the project
#               folder).
#     target  = ; // See Python typing...
#               the **relative** path of the final product dir (regarding the
#               project folder).
#     ignore  = ( '' ) ; // See Python typing...
#               the rules for ignoring files in addition to what ¨git does.
#               You can use this argument even if you don't work with 
#     usegit  = ( False ) ; // See Python typing...
#               ``True`` asks to use ¨git contrary to ``False``.
#     readme  = ( '' ) ; // See Python typing...
#               ``''`` is if you don't need to import an external 
#               path::``README`` file, otherwise give a **relative** path.
#
# This function...
###
@click.command()
@click.argument('project')
@click.option('--src',
              default = 'src',
              help    = 'Relative path of the source folder of the project.'
                        'The default value is "src".')
@click.option('--target',
              default = '',
              help    = 'Relative path of the targer folder of the project. '
                        'The default value "", an empty string, indicates '
                        'to use the name, in lower case, of the project.')
@click.option('--ignore',
              default = '',
              help    = 'Relative path to a file with the rules for ignoring '
                        'files in addition to what git does.'
                        'The default value "", an empty string, indicates '
                        'to not use any rule.')
@click.option('--usegit',
              default = False,
              help    = 'Contrary to True, the default value False asks to not '
                        'use git.')
@click.option('--readme',
              default = '',
              help    = 'Relative path of an external README file. '
                        'The default value "", an empty string, indicates '
                        'to not use any external README file.')
@click.option('--safemode',
              default = True,
              help    = 'Contrary to False, the default value True leaves the user '
                        'decides to apply or not the "dangerous" changes.')
def update(
    project : str,
    src     : str,
    target  : str,
    ignore  : str,
    usegit  : bool,
    readme  : str,
    safemode: bool,
):
    """
    Update your "source-to-product" like projects using the Python module 
    src2prod. 

    PROJECT: the path of the project to update.
    """
    print(project)

