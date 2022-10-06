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

JSON_REPORT     = THIS_DIR / 'diff-contexts.json'
DIFF_JSON_FILE  = 'diff-resume.json'
IGNORE_TXT_FILE = 'ignore.txt'

TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

def ignorethisname(name):
    for toremove in '-':
        name = name.replace(toremove, '')

    return (
        name == '.DS_Store'
        or
        not name.isupper()
    )


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

    if ignorethisname(name):
        continue

    resume = {}


    apirules = set()

    for f in p.glob('**/*.txt'):
        if ignorethisname(f.stem):
            continue

        apirules = apirules.union(
            usefulrulesfrom(f)
        )


    onlinefile = ONLINE_DIR / f"{name}.txt"

    if onlinefile.is_file():
        onlinerules = usefulrulesfrom(onlinefile)

    else:
        onlinerules = set()


    ignorefile = FINAL_DIR / name / IGNORE_TXT_FILE

    if not ignorefile.is_file():
        toignore = set()

    else:
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


    onlinerules -= toignore
    apirules    -= toignore

    if apirules == onlinerules:
        resume = {}

    else:
        diffrules_online.append(name)

        resume['api-online'] = sorted(list(apirules - onlinerules))
        resume['online-api'] = sorted(list(onlinerules - apirules))

    (FINAL_DIR / name / DIFF_JSON_FILE).write_text(
        data = dumps(
            obj    = resume,
            indent = 4
        ),
        encoding = 'utf-8'
    )


if diffrules_online:
    print(
        f"{TAB_2}+ API and online have different rules. See the files below.",
            f"{TAB_3}- ``{JSON_REPORT.name}``: the list of contexts concerned.",
            f"{TAB_3}- ``<<context-name>> / {DIFF_JSON_FILE}``: a resume of the differences.",
        sep = "\n"
    )

    diffrules_online.sort()

    JSON_REPORT.write_text(
        encoding = 'utf-8',
        data     = dumps(
            diffrules_online,
            indent = 4
        ),
    )
