#!/usr/bin/env python3

import                  black
from collections import defaultdict
from json        import (
    dumps,
    load
)

from mistool.os_use import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR

GITIGNORE_DIR   = PROJECT_DIR / 'src' / 'config' / 'gitignore' / 'cli'
TREEVIEW_PYFILE = GITIGNORE_DIR / 'treeview.py'
USEDBY_PYFILE   = GITIGNORE_DIR / 'usedby.py'

USEDBY_JSON     = THIS_DIR / 'usedby.json'
JSON_RULES_FILE = THIS_DIR / 'apirules.json'

with JSON_RULES_FILE.open(
    encoding = 'utf-8',
    mode     = 'r'
) as f:
    API_RULES = load(f)


ALL_TAGS = [
    TAG_DESC           := ':desc:',
    TAG_RULES          := ':rules:',
    TAG_COMMENTS       := ':comments:',
    TAG_RULES_COMMENTS := f'{TAG_RULES[:-1]}-n-{TAG_COMMENTS[1:]}',
]


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

def build_treeview(deps):
    if TAG_DESC in deps:
        return {}

    return {
        main: build_treeview(sub)
        for main, sub in deps.items()
    }


def exctractrules(ctxt, usedby, strpath):
    for k, v in ctxt.items():
        if k == TAG_DESC:
            continue

        if k == TAG_RULES_COMMENTS:
            for r_c in ctxt[TAG_RULES_COMMENTS]:
                for r in r_c[TAG_RULES]:
                    usedby[r].append(strpath)

        else:
            strpath += f'/{k}'

            exctractrules(v, usedby, strpath)


def build_usedby(apirules):
    usedby = defaultdict(list)

    exctractrules(
        ctxt    = apirules,
        usedby  = usedby,
        strpath = ''
    )

    return dict(usedby)


def load_usedby(_):
    with USEDBY_JSON.open(
        encoding = 'utf-8',
        mode     = 'r',
    ) as f:
        return load(f)


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ------------------------- #
# -- UPDATING JSON FILES -- #
# ------------------------- #

print(f"{TAB_1}* Update of some JSON files.")

for target, builder in [
    (TREEVIEW_PYFILE, build_treeview),
    (USEDBY_JSON    , build_usedby  ),
    (USEDBY_PYFILE  , load_usedby   ),
]:
    print(f"{TAB_2}* Update of ``{target.name}``.")

    if target.ext == 'json':
        content = dumps(
            obj    = builder(API_RULES),
            indent = 4
        )


    else:
        content = black.format_file_contents(
            f"{target.stem.upper()} = {builder(API_RULES)}",
            fast = False,
            mode = black.FileMode()
        ).strip() + '\n'*2


    target.write_text(
        data     = content,
        encoding = 'utf-8'
    )
