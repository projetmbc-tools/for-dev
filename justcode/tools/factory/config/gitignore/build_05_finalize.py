#!/usr/bin/env python3

from json import load, dumps

from mistool.os_use import PPath as Path

from core import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

DATAS_DIR = THIS_DIR / 'datas'

FINAL_DIR   = DATAS_DIR / 'final'
ONLINE_DIR  = DATAS_DIR / 'online'
CONTRIB_DIR = DATAS_DIR / 'contribute'


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


# ---------------------- #
# -- RULES OF THE API -- #
# ---------------------- #

print(
    f"{TAB_1}* Analyzing the rules inside the FINAL folder."
)

diffrules_online = []

for p in FINAL_DIR.glob('*'):
    name = p.name

    resume = {}


    apirules = set()

    for f in p.glob('*.txt'):
        apirules = apirules.union(
            usefulrulesfrom(f)
        )


    onlinefile = ONLINE_DIR / f"{name}.txt"

    if onlinefile.is_file():
        onlinerules = usefulrulesfrom(onlinefile)


    ignorefile = (FINAL_DIR / name / "0-ignore-0.txt")

    if ignorefile.is_file():
        toignore = ignorefile.read_text(
            encoding = 'utf-8'
        )

        toignore = set([
            l
            for l in toignore.split('\n')
            if(
                l.strip()
                and
                not l[0] == '#'
            )
        ])

    else:
        toignore = set()

    onlinerules -= toignore
    apirules    -= toignore

    if apirules == onlinerules:
        resume = {}

    else:
        diffrules_online.append(name)

        resume['api-online'] = sorted(list(apirules - onlinerules))
        resume['online-api'] = sorted(list(onlinerules - apirules))

    (FINAL_DIR / name / "resume.json").write_text(
        data = dumps(
            obj    = resume,
            indent = 4
        ),
        encoding = 'utf-8'
    )


if diffrules_online:
    print(
        f"{TAB_2}+ Different rules - API and online "
         "(see the ``resume.json`` files)"
    )

    diffrules_online.sort()

    for name in diffrules_online:
        print(
            f"{TAB_3}- {name}"
        )
