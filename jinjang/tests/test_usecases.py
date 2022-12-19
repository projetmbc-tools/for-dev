#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from collections import defaultdict
from pathlib     import Path

from cbdevtools.addfindsrc import addfindsrc


# ------------------- #
# -- MODULE TESTED -- #
# ------------------- #

addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src import *


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR = Path(__file__).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'jinjaNG'):
   PROJECT_DIR = PROJECT_DIR.parent


CONTRIB_DSL_DIR = PROJECT_DIR / 'contribute' / 'api' / 'dsl'


# ---------------------- #
# --  USECASE FOLDERS -- #
# ---------------------- #

def yielddirs(pdir):
    if not pdir.is_dir():
        raise Exception(
            f"one dir expected, see:\n{pdir}"
        )

    for subdir in pdir.glob('*'):
        if(
            subdir.is_dir()
            and not subdir.name.startswith('.')
            and not subdir.name.startswith('x-')
        ):
            yield subdir


USECASE_FOLDERS = defaultdict(list)

for pdir in yielddirs(CONTRIB_DSL_DIR):
    flavour = pdir.name

    usecases_dir = pdir / "usecases"

    if not usecases_dir.is_dir():
        raise Exception(
            f"invalid contribution for the flavour ''{flavour}''."
        )

    for tdir in yielddirs(usecases_dir):
        USECASE_FOLDERS[flavour].append(tdir.name)


# -------------------- #
# -- WRITE AND READ -- #
# -------------------- #

def test_ioview_list_texts():
    ...
