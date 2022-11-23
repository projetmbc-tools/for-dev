#!/usr/bin/env python3

from mistool.os_use import PPath as Path
from yaml import (
    safe_load as yaml_load,
    dump      as yaml_dump
)


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'jinjaNG'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR


SPECS_SRC_DIR  = PROJECT_DIR / 'src' / 'config' / 'flavour'
SPECS_SRC_FILE = SPECS_SRC_DIR / 'specs.py'

CONTRIB_DSL_DIR   = PROJECT_DIR / 'contribute' / 'api' / 'dsl'
SPECS_STATUS_YAML = THIS_DIR / 'validated.yaml'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


DEFAULT_STATUS_CONTENT = {
    "status" : 'pending',
    "comment": (
        'This specs are pending. '
        'The author of jinjaNG will contact you later.'
    )
}


# ----------------------- #
# -- THE SPECS DEFINED -- #
# ----------------------- #

if not SPECS_STATUS_YAML.is_file():
    SPECS_STATUS_YAML.touch()


allspecs = {}

for specfile in CONTRIB_DSL_DIR.rglob("*/*specs.yaml"):
    specdir = specfile.parent
    name    = specdir.name

    specstatus_yaml = specdir / "status.yaml"

    if not specstatus_yaml.is_file():
        specstatus_yaml.touch()

        with specstatus_yaml.open(
            mode     = "w",
            encoding = "utf-8"
        ) as f:
            yaml_dump(DEFAULT_STATUS_CONTENT, f)

    with specstatus_yaml.open(
        mode     = "r",
        encoding = "utf-8"
    ) as f:
        allspecs[name] = {
            'dir'   : specdir,
            'status': yaml_load(f)['status'],
        }


# ---------------------- #
# -- TOOLS FOR SOURCE -- #
# ---------------------- #

def update_src(hardspec):
    print(f"{TAB_2}+ Updating the source code...")

    print('SRC >',hardspec)

    exit()


# ------------------- #
# -- TOOLS FOR DOC -- #
# ------------------- #

def update_doc(hardspec):
    print(f"{TAB_2}+ Updating the doc...")

    print('DOC >',hardspec)


# ------------------------ #
# -- THE SPECS ACCEPTED -- #
# ------------------------ #

for name, infos in allspecs.items():
    if infos['status'] != 'ok':
        print(f"{TAB_1}* REJECTED: {name}.")
        continue

    print(f"{TAB_1}* ACCEPTED: {name}.")

    specdir = infos['dir']

    with (specdir / 'specs.yaml').open(
        mode     = "r",
        encoding = "utf-8"
    ) as f:
        hardspec = yaml_load(f)

    update_src(hardspec)
    update_doc(hardspec)
