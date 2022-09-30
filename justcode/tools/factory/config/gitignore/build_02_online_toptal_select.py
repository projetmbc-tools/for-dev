#!/usr/bin/env python3

from json import dumps

from mistool.os_use import PPath as Path

from core import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

DATAS_DOWNLOADED_DIR = THIS_DIR / 'datas' / 'online'
JSON_TO_IGNORE       = DATAS_DOWNLOADED_DIR / '0-to-ignore-0.json'
JSON_USEFULL         = DATAS_DOWNLOADED_DIR / '0-rules-0.json'

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


# -------------------- #
# -- RELEVANT RULES -- #
# -------------------- #

print(
    f"{TAB_1}* Search for relevant rules among those that have been downloaded."
)

all_usefull_rules = {}
to_ignore         = []
nb_downloaded     = 0
nb_ignored        = 0


allpaths = [
    p
    for p in DATAS_DOWNLOADED_DIR.glob('*.txt')
]
allpaths.sort()


for onepath in allpaths:
    nb_downloaded += 1

    usefulrules = usefulrulesfrom(onepath)
    rulesname   = onepath.stem

    if usefulrules:
        usefulrules = list(usefulrules) # Cf. JSON...
        usefulrules.sort()

        all_usefull_rules[rulesname] = usefulrules

    else:
        nb_ignored += 1

        to_ignore.append(rulesname)

print(
    f"{TAB_1}* {nb_ignored} ignored / {nb_downloaded} downloaded."
)


# ------------------------------ #
# -- UPDATE OF THE JSON FILES -- #
# ------------------------------ #

for jsfile, jsdatas in [
    (JSON_TO_IGNORE, to_ignore),
    (JSON_USEFULL  , all_usefull_rules),
]:
    jsfile.write_text(
        data = dumps(
            obj    = jsdatas,
            indent = 4
        ),
        encoding = 'utf-8'
    )

    print(
        f"{TAB_1}* JSON file ``{jsfile.name}`` has been updated."
    )
