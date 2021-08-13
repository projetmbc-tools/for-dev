#!/usr/bin/env python3

###
# This module simplifies the import of the dev source of a project. 
###


from pathlib import Path
import sys


###
# prototype::
#     file    = ; // See Python typing...
#               just use the magic constant ``__file__`` when calling
#               this function.
#     project = ; // See Python typing...
#               the name of the project
#
#     :return: = ; // See Python typing...
#                the path of the project dir.
#
# This function adds the project folder path::``project`` to the path.
# 
# 
# Let's see a fictive example with the following tree structure.
#
# tree-dir::
#     + mymod
#         + doc
#         + dist
#         + src
#             * __init__.py
#             * ...
#         + tools
#             + debug 
#                 * cli.py
#
# The ¨python script path::``tools/debug/cli.py`` can easily load the local
# ¨python module ``src``. The code to use is the following one.
#
# python::
#     from cbdevtools import addfindsrc
#
#     MODULE_DIR = addfindsrc(
#         file    = __file__,
#         project = 'mymod',
#     )
#
#     from src import *
###

def addfindsrc(
    file   : str,
    project: str,
) -> Path:
    project_dir = Path(file).parent

    if not project in str(project_dir):
        raise Exception(
            'call the script from a working directory '
            'containing the project.'
        )

    while(not project_dir.name.startswith(project)):
        project_dir = project_dir.parent

    sys.path.append(str(project_dir))

    return project_dir
