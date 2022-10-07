#!/usr/bin/env python3

from json import load

from mistool.os_use     import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = PROJECT_DIR = Path(THIS_FILE).parent

USEDBY_JSON = THIS_DIR / 'usedby.json'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ------------------------------- #
# -- LOOKING FOR CONTRIBUTIONS -- #
# ------------------------------- #

print(f"{TAB_1}* Rules in several contexts?")

with USEDBY_JSON.open(
    encoding = 'utf-8',
    mode     = 'r',
) as f:
    usedby = load(f)

multiusedrules = {}

for onerule, ctxts in usedby.items():
    if len(ctxts) > 2:
        multiusedrules[onerule] = ctxts

if len(multiusedrules) == 0:
    print(f"{TAB_2}+ OK - No rule used in several contexts.")

else:
    TODO
