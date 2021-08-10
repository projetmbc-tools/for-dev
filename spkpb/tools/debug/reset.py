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

PROJECT_NAME = 'spkpb'
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

project = BaseCom(
    Problems(
        Speaker(
            logfile = Path('mylog.log'),
            style   = GLOBAL_STYLE_COLOR,
        )
    )
)

project.new_warning(
    what = Path('one/strange/file.txt'),
    info = "some strange behaviors."
)

project.reset()

project.new_error(
    what = Path('one/bad/file.txt'),
    info = "bad things appear."
)

project.resume()
