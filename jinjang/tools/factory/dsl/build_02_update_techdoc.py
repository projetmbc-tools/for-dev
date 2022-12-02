#!/usr/bin/env python3

from cbdevtools.addfindsrc import addfindsrc
from mistool.os_use        import PPath as Path
from mistool.string_use    import between

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


SPECS_DOC_DIR         = PROJECT_DIR / 'doc' / 'content' / 'specs'
SPECS_CONTENT_TNSFILE = SPECS_DOC_DIR / 'specs.txt'

DEFAULT_FILES = {
    'variables'   : SPECS_DOC_DIR / TAG_FLAVOUR_ASCII,
    'instructions': SPECS_DOC_DIR / TAG_FLAVOUR_ASCII,
    'commments'   : SPECS_DOC_DIR / TAG_FLAVOUR_ASCII,
    'tools'       : SPECS_DOC_DIR / TAG_FLAVOUR_HTML,
}

DEFAULT_FILES = {
    n: p / f'{n}.txt'
    for n, p in DEFAULT_FILES.items()
}


# ---------------- #
# -- LET'S WORK -- #
# ---------------- #

MAIN_TOC = []

for flavour in sorted(SETTINGS):
    if flavour == TAG_FLAVOUR_ASCII:
        continue

    MAIN_TOC.append(flavour)

    specs = SETTINGS[flavour]



    print(flavour)
