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


TEX_SUFFIX      = '.tex'
OUTPUT_TEX_FILE = 'output.tex'

# HOOKS_TESTS_SUBDIRNAMES = ['post', 'pre', 'pre-n-post']
# HOOKS_TESTS_MAINDIR     = '02-cli'


# -------------- #
# -- SPEAKING -- #
# -------------- #

TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

# def testinghooks_file(path):
#     if path.name != OUTPUT_TEX_FILE:
#         return False

#     # oneparent = path.parent.parent

#     # if oneparent.name not in HOOKS_TESTS_SUBDIRNAMES:
#     #     return False

#     # oneparent = oneparent.parent.parent

#     # if oneparent.name != HOOKS_TESTS_MAINDIR:
#     #     return False

#     return True


def recufiles(folder):
    for path in folder.glob('*'):
# We only seek for TEX files.
        if (
            path.is_file()
            and
            path.suffix == TEX_SUFFIX
        ):
# PDFs are kept for test hooks.
            # opt = '-c' if testinghooks_file(path) else '-C'
            opt = '-C'

            yield opt, path

# One folder to explore...
        else:
            yield from recufiles(path)


# ---------------- #
# -- LET'S WORK -- #
# ---------------- #

print(f'{TAB_1}* Just keep TEX files.')

cdir = os.curdir

for opt, p in recufiles(JINJANG_DIR):
    os.chdir (p.parent)
    os.system(f'latexmk {opt} "{p.name}" > /dev/null 2>&1')

os.chdir(cdir)
