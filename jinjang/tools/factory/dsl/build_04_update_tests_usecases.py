#!/usr/bin/env python3

from btools.B01 import *


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


CONTRIB_DSL_DIR    = PROJECT_DIR / 'contribute' / 'api' / 'dsl'
TESTS_USECASES_DIR = PROJECT_DIR / 'tests' / 'usecases' / 'datas'


FLAVOURS_STATUS_YAML = THIS_DIR / 'flavours.yaml'


# ----------------------- #
# -- SPECS STATUS YAML -- #
# ----------------------- #

print(f"{TAB_1}* Updating the tests build on the usecases.")


with FLAVOURS_STATUS_YAML.open(
    mode     = "r",
    encoding = "utf-8"
) as f:
    flavours_OK = yaml_load(f)[STATUS_OK]


for fl in flavours_OK:
    srcfiles = []

    usecase_dir = CONTRIB_DSL_DIR / fl / 'usecases'

    for pdir in usecase_dir.glob('*'):
        if(
            not pdir.is_dir()
            or
            pdir.name.startswith('.')
            or
            pdir.name.startswith('x-')
        ):
            continue

        dest_dir = TESTS_USECASES_DIR / fl

        if dest_dir.is_dir():
            dest_dir.remove()

        for pfile in pdir.glob('*'):
            name = pfile.stem

            if(
                not pfile.is_file()
                or
                not name in ['datas', 'output', 'template']
            ):
                continue

            dest = TESTS_USECASES_DIR / fl / (pfile - usecase_dir)

            pfile.copy_to(dest)
