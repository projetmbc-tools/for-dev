#! /usr/bin/env python3

from pathlib import Path
from pprint  import pprint

from cbdevtools import *


# ----------------- #
# -- WHAT WE USE -- #
# ----------------- #

FILES_FOLDER_NAME = "case-01"
EXTENSION         = "txt"


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src.build import *


# -------------- #
# -- LET'S GO -- #
# -------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

FILES_FOLDER = THIS_DIR / "files" / FILES_FOLDER_NAME


mybuilder = Builder()

template = FILES_FOLDER / f"template.{EXTENSION}"
datas    = FILES_FOLDER / "datas.json"

output = mybuilder.render(
    datas    = datas,
    template = template,
)

print()
print(
    f"Rendering from JSON made in the folder ``files/{FILES_FOLDER_NAME}."
)
print()
