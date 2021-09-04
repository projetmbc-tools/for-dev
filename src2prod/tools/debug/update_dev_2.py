#!/usr/bin/env python3

from cbdevtools import *

# projectname = 'cbdevtools'
# projectname = 'multimd'
# projectname = 'spkpb'

projectname = 'src2prod'


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
    project = MONOREPO_DIR / PROJECT_DIR,
    source  = 'src',
    target  = projectname.lower(),
    ignore  = MONOREPO_DIR / 'ignore-for-prod.txt',
    usegit  = True,
    readme  = 'readme'
)

project.update(safemode = False)
