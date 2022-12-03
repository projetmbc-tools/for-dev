#!/usr/bin/env python3

import re

from cbdevtools.addfindsrc import addfindsrc
from mistool.os_use        import PPath as Path
from mistool.string_use    import between

addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src.config.flavour import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'jinjaNG'):
   PROJECT_DIR = PROJECT_DIR.parent

THIS_FILE_REL_SRC_PATH    = Path(__file__) - PROJECT_DIR
THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR


SPECS_CONTENT_TNSFILE = PROJECT_DIR / 'doc' / 'content' / 'specs.txt'
SPECS_DOC_DIR         = PROJECT_DIR / 'doc' / 'content' / 'specs'

DEFAULT_FILES = {
    (TAG_VARS   := 'variables'   ): TAG_FLAVOUR_ASCII,
    (TAG_INSTR  := 'instructions'): TAG_FLAVOUR_ASCII,
    (TAG_COMMENT:= 'comments'    ): TAG_FLAVOUR_ASCII,
     TAG_TOOLS                    : TAG_FLAVOUR_HTML,
}

DEFAULT_FILES = [
    SPECS_DOC_DIR / p / f'{n}.txt'
    for n, p in DEFAULT_FILES.items()
]


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

DATE_PATTERN       = re.compile(r"\s+date\s*=.*")
DECO_TITLE_PATTERN = re.compile(r"={3,}")

def build_predoc(srctext):
    srctext     = srctext.rstrip()
    newtxt      = []
    datetofind  = False
    nbdecotitle = 0

    for line in srctext.split('\n'):
        line = line.rstrip()

# Date
        if line == "this::":
            datetofind = True

        elif(
            datetofind
            and
            re.match(DATE_PATTERN, line)
        ):
            line = ' '*4 + 'date = ?'
            datetofind = False

# After the main title
        elif(
            nbdecotitle < 2
            and
            re.match(DECO_TITLE_PATTERN, line)
        ):
            nbdecotitle += 1

            if nbdecotitle == 2:
                newtxt += [
                    line,
                    '',
                    'TODO',
                    '',
                ]

                line = '/* Text already used that can help you for a new doc.'

# Keep this line to help the writing of new docs.
        newtxt.append(line)

# Nothin new to do.
    newtxt.append('*/')
    newtxt = '\n'.join(newtxt)

    return newtxt


TEMPL_TOC = """
abrev::
    content = /{flavour}


{title}

content::
    {toc}
""".strip()

def build_toc(flavour, specs):
    deco  = '='*len(flavour)
    title = f'{deco}\n{flavour}\n{deco}'

    toc = []

    for p in DEFAULT_FILES:
        if(
            p.stem == TAG_TOOLS
            and
            not specs[TAG_TOOLS]
        ):
            continue

        toc.append(f'¨content/{p.name}')

    toc = ('\n' + ' '*4).join(toc)

    return TEMPL_TOC.format(
        flavour = flavour,
        title   = title,
        toc     = toc,
    )


# ---------------------------- #
# -- PREPARING THE CONTENTS -- #
# ---------------------------- #

MAIN_TOC = []

for flavour in sorted(SETTINGS):
    if flavour == TAG_FLAVOUR_ASCII:
        continue

    MAIN_TOC.append(flavour)

    print(f'{TAB_1}* Missing doc for the flavour ``{flavour}``?')

    nothingdone = True

# The contents
    specs    = SETTINGS[flavour]
    dest_dir = SPECS_DOC_DIR / flavour

    for df in DEFAULT_FILES:
        dest_file = dest_dir / df.name

        if dest_file.is_file():
            continue

        if (
            df.stem == TAG_TOOLS
            and
            specs[TAG_TOOLS] == False
        ):
            continue

        nothingdone = False

        print(f"{TAB_2}+ Adding the file ``{df.name}``.")

        todo_content = build_predoc(
            df.read_text(
                encoding = 'utf-8'
            )
        )

        dest_file.create('file')
        dest_file.write_text(
            data     = todo_content,
            encoding = 'utf-8'
        )


# TOC
    tocfile = SPECS_DOC_DIR / f"{flavour}.txt"

    if not tocfile.is_file():
        nothingdone = False

        print(f"{TAB_2}+ TOC - Adding ``{flavour}.txt``.")

        toc = build_toc(flavour, specs)

        tocfile.touch()
        tocfile.write_text(
            data     = toc,
            encoding = 'utf-8'
        )


    if nothingdone:
        print(f"{TAB_2}+ No file added.")


# ----------------------------------------- #
# -- UPDATING THE TOC OF MAIN SPECS FILE -- #
# ----------------------------------------- #

print(f'{TAB_1}* Updating the TOC for all the flavours.')

content = SPECS_CONTENT_TNSFILE.read_text(encoding = 'utf-8')

before, _ , after = between(
    text = content,
    seps = [
        '/* -- AUTO CONTENT - START -- */',
        '/* -- AUTO CONTENT - END -- */'
    ],
    keepseps = True,
)

toc = [' '*4 + f'¨content/{f}.txt' for f in MAIN_TOC]
toc = '\n'.join(toc)

SPECS_CONTENT_TNSFILE.write_text(
    data     = f"{before}\n{toc}\n{after}",
    encoding = 'utf-8'
)
