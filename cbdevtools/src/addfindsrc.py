#!/usr/bin/env python3

###
# This module simplifies the import of the dev source of a project. 
###


from pathlib import Path
import sys


###
# prototype::
#     file    = ; // See Python typing...
#               ???
#     project = ; // See Python typing...
#               ???
#
# This function does two things.
#
#     1) ????
#
#     2) ????
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
