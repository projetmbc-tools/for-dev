#! /usr/bin/env python3

from pathlib import Path
from pprint  import pprint

from cbdevtools import *


# ----------------- #
# -- WHAT WE USE -- #
# ----------------- #

FILES_FOLDER_NB = "01"

DATAS_EXT = "yaml"
# DATAS_EXT = "json"
# DATAS_EXT = "py"

LAUNCH_PY = True
# LAUNCH_PY = False

TEMPL_EXT = "txt"


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src.jngbuild import *


# -------------- #
# -- LET'S GO -- #
# -------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

FILES_FOLDER_NAME = f"{DATAS_EXT}-{FILES_FOLDER_NB}"
FILES_FOLDER      = THIS_DIR / "files" / FILES_FOLDER_NAME


mybuilder = JNGBuilder(
    launch_py = LAUNCH_PY
)

template = FILES_FOLDER / f"template.{TEMPL_EXT}"
output   = template.parent / f"output.{TEMPL_EXT}"
datas    = FILES_FOLDER / f"datas.{DATAS_EXT}"

mybuilder.render(
    datas    = datas,
    template = template,
    output   = output
)

print()
print(
    f"Rendering from {DATAS_EXT} made in "
    f"the folder ``files/{FILES_FOLDER_NAME}``."
)
print()
