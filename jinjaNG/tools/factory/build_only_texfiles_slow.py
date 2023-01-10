#!/usr/bin/env python3

import os

from cbdevtools.addfindsrc import addfindsrc


# --------------- #
# -- CONSTANTS -- #
# --------------- #

JINJANG_DIR = addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)


# -------------- #
# -- SPEAKING -- #
# -------------- #

TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

def recufiles(folder):
    for path in folder.glob('*'):
        if path.is_file():
            yield path

        else:
            yield from recufiles(path)


# ---------------- #
# -- LET'S WORK -- #
# ---------------- #

print(f'{TAB_1}* Just keep TEX files.')

cdir = os.curdir

for p in recufiles(JINJANG_DIR):
    if p.suffix != '.tex':
        continue

    os.chdir(p.parent)

    os.system(f'latexmk -C "{p.name}" > /dev/null 2>&1')

os.chdir(cdir)
