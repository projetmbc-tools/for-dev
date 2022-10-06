#!/usr/bin/env python3

from mistool.os_use import PPath as Path

from scraping import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

UPDATE_CREATIVE = UPDATE_OPENSOURCE = True

# UPDATE_OPENSOURCE = False # Debug mode.
# UPDATE_CREATIVE   = False # Debug mode.


FAILED_LICENSES = []


THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR

LICENSE_DIR       = PROJECT_DIR / 'src' / 'config' / 'license'
LICENSE_DATAS_DIR = LICENSE_DIR / 'datas'

NO_CONTENT_JSON_FILE = THIS_DIR / 'report-no-content.json'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# --------------- #
# -- LET'S GO! -- #
# --------------- #

if not(UPDATE_CREATIVE or UPDATE_OPENSOURCE):
    exit()

nb_licences = 0


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
    nb_licences     += myCC.nb_success


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
    nb_licences     += myOpenSrc.nb_success


# ------------------------------------- #
# -- UPDATE ``failed_licenses.json`` -- #
# ------------------------------------- #

print()
print(f"{TAB_1}* Updating ``{NO_CONTENT_JSON_FILE.name}``.")

# We want a deterministic output!
FAILED_LICENSES.sort()
FAILED_LICENSES = {
    s: l
    for s, l in FAILED_LICENSES
}

NO_CONTENT_JSON_FILE.write_text(
    encoding = 'utf-8',
    data     = dumps(
        obj    = FAILED_LICENSES,
        indent = 4
    )
)


# ------------------------- #
# -- WHAT HAS BEEN DONE? -- #
# ------------------------- #

print(f"{TAB_1}* {nb_licences} licenses proposed online.")
