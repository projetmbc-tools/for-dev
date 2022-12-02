#!/usr/bin/env python3

from cbdevtools.addfindsrc import addfindsrc
from mistool.os_use        import PPath as Path

addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src.config.flavour import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'jinjaNG'):
   PROJECT_DIR = PROJECT_DIR.parent

THIS_FILE_REL_SRC_PATH    = Path(__file__) - PROJECT_DIR
THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR


SPECS_DOC_DIR = PROJECT_DIR / 'doc' / 'content' / 'specs'

DEFAULT_FILES


# ------------------- #
# -- DEFAULT FILES -- #
# ------------------- #


# ---------------- #
# -- LET'S WORK -- #
# ---------------- #

for flavour, specs in SETTINGS.items():
    if flavour == TAG_FLAVOUR_ASCII:
        continue

    print(flavour)
