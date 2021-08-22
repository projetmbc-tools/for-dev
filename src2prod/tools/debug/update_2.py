#!/usr/bin/env python3

from cbdevtools import *


# projectname = 'spkpb'
# projectname = 'cbdevtools'
projectname = 'monorepo'

# projectname = 'multimd'

# projectname = 'src2prod'


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
    project = PROJECT_DIR,
    source  = 'src',
    target  = projectname.lower(),
    ignore  = MONOREPO_DIR / 'ignore-for-prod.txt',
    usegit  = True,
    # readme  = 'README.md',
    readme  = 'readme',
)

project.update(safemode = False)
