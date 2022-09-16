#!/usr/bin/env python3

from datetime    import date
from collections import defaultdict

import black

from mistool.os_use import PPath as Path

from scraping import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

UPDATE_CREATIVE = UPDATE_OPENSOURCE = True

# UPDATE_OPENSOURCE = False # Debug mode.
# UPDATE_CREATIVE   = False # Debug mode.


FAILED_LICENSES = []


TODAY = date.today()


THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR

LICENSE_DIR       = PROJECT_DIR / 'src' / 'config' / 'license'
LICENSE_DATAS_DIR = LICENSE_DIR / 'datas'
PYFILE            = LICENSE_DIR / 'license.py'
FAIL_JSON_FILE    = THIS_DIR / 'failed_licenses.json'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

def tagfrom(shortid):
    tag = ''

    for c in shortid:
        if c in '. -':
            tag += '_'

        else:
            tag += c.upper()

    return tag


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ----------------------- #
# -- ARE WE CONNECTED? -- #
# ----------------------- #

try:
    getwebcontent("https://www.google.com/")

except ConnectionError:
    print(f"{TAB_1}* No internet connection.")
    exit()


# ------------------------------------------ #
# -- UPDATES FROM ``creativecommons.org`` -- #
# ------------------------------------------ #

if UPDATE_CREATIVE:
    print(f"{TAB_1}* Licenses on ``creativecommons.org``.")

    myCC = CreativeCommons(
        decotab_1   = f"{TAB_2}+",
        decotab_2   = f"{TAB_3}-",
        license_dir = LICENSE_DATAS_DIR,
    )
    myCC.build()

    FAILED_LICENSES += myCC.failed_licences


# ------------------------------------- #
# -- UPDATES FROM ``opensource.org`` -- #
# ------------------------------------- #

if UPDATE_OPENSOURCE:
    if UPDATE_CREATIVE:
        print()

    print(f"{TAB_1}* Licenses on ``opensource.org``.")

    myOpenSrc = OpenSource(
        decotab_1   = f"{TAB_2}+",
        decotab_2   = f"{TAB_3}-",
        license_dir = LICENSE_DATAS_DIR,
    )
    myOpenSrc.build()

    FAILED_LICENSES += myOpenSrc.failed_licences


# ------------------------------------- #
# -- UPDATE ``failed_licenses.json`` -- #
# ------------------------------------- #

if UPDATE_CREATIVE or UPDATE_OPENSOURCE:
    print()
    print(f"{TAB_1}* Updating ``failed_licenses.json``.")

# We want a deterministic output!
    FAILED_LICENSES.sort()

    with FAIL_JSON_FILE.open(
        encoding = 'utf-8',
        mode     = 'w',
    ) as f:
        f.write(
            dumps(FAILED_LICENSES)
        )


# ------------------------- #
# -- WHAT HAS BEEN DONE? -- #
# ------------------------- #

nb_licences = myCC.nb_success + myOpenSrc.nb_success

print(f"{TAB_1}* {nb_licences} licenses proposed online.")
