#!/usr/bin/env python3

from cbdevtools import *

projectname = 'TeXitEasy'


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

MONOREPO_DIR = MODULE_DIR.parent.parent / 'tools-for-latex'
PROJECT_DIR  = MONOREPO_DIR / Path(projectname)

project = Project(
    project = PROJECT_DIR,
    source  = 'src',
    target  = projectname.lower(),
    ignore  = MONOREPO_DIR / 'ignore-for-prod.txt',
    usegit  = True,
    readme  = 'readme'
)

project.update(safemode = False)
