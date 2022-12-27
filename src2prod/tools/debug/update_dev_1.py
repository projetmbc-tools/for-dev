#!/usr/bin/env python3

from cbdevtools import *

projectname = 'src2prod'
# projectname = 'spkpb'
# projectname = 'cbdevtools'
projectname = 'jinjaNG'
# projectname = 'multimd'


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'src2prod',
)


# -------------- #
# -- LET'S GO -- #
# -------------- #

from src import *

MONOREPO_DIR = MODULE_DIR.parent
PROJECT_DIR  = Path(projectname)

project = Project(
    project = MONOREPO_DIR,
    source  = PROJECT_DIR / 'src',
    target  = PROJECT_DIR / projectname.lower(),
    ignore  = '''
        tool_*/
        tool_*.*

        test_*/
        test_*.*
    ''',
    usegit = True,
    readme = PROJECT_DIR / 'README.md'
)

project.update(safemode = False)
