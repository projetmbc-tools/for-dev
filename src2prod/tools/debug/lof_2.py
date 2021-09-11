#!/usr/bin/env python3

from cbdevtools import *


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

PROJECT_DIR = Path("/Users/projetmbc/Google Drive/git[NEW]/coding/tools/for-latex") / 'bdoc'

project = Project(
    project = PROJECT_DIR,
    source  = PROJECT_DIR / 'src',
    target  = '',
    ignore  = '''
        tool_*/
        tool_*.*

        test_*/
        test_*.*
    ''',
    usegit = True
)

project.build()

print('---')

for f in project.lof:
    print(f)
