#!/usr/bin/env python3

from pathlib import Path
import sys


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR = Path(__file__).parent


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

PROJECT_NAME = 'src2prod'
MODULE_DIR   = THIS_DIR

if not PROJECT_NAME in str(MODULE_DIR):
    raise Exception(
        "call the script from a working directory containing the project."
    )

while(not MODULE_DIR.name.startswith(PROJECT_NAME)):
    MODULE_DIR = MODULE_DIR.parent

sys.path.append(str(MODULE_DIR))


# -------------- #
# -- LET'S GO -- #
# -------------- #

from src import *

PROJECT_DIR = MODULE_DIR.parent

project = Project(
    project = PROJECT_DIR,
    source  = Path('spkpb') / 'src',
    target  = '',
    ignore  = '''
        tool_*/
        tool_*.*
    ''',
    usegit = True
)

project.build()

print('---')

for f in project.lof:
    print(f)

