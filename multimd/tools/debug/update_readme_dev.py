#!/usr/bin/env python3

from cbdevtools import *

projectname = 'about'


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'multimd',
)

MONOREPO_DIR = MODULE_DIR.parent
PROJECT_DIR  = MONOREPO_DIR / Path(projectname)


# -------------- #
# -- LET'S GO -- #
# -------------- #

from src import *

Builder(
    output  = PROJECT_DIR / 'README.md',
    content = PROJECT_DIR / 'readme',
).build()
