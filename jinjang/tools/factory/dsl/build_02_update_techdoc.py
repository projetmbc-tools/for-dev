#!/usr/bin/env python3

from btools.B01 import *


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

FORCE_TOC_UPDATE = False
# FORCE_TOC_UPDATE = True


THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'jinjaNG'):
   PROJECT_DIR = PROJECT_DIR.parent

THIS_FILE_REL_SRC_PATH    = Path(__file__) - PROJECT_DIR
THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR


DOC_DIR               = PROJECT_DIR / 'doc' / 'content'
SPECS_CONTENT_TNSFILE = DOC_DIR / 'specs.txt'
SPECS_DOC_DIR         = DOC_DIR / 'specs'

DEFAULT_FILES = {
    (TAG_VARS   := 'variables'   ): TAG_FLAVOUR_ASCII,
    (TAG_INSTR  := 'instructions'): TAG_FLAVOUR_ASCII,
    (TAG_COMMENT:= 'comments'    ): TAG_FLAVOUR_ASCII,
     TAG_TOOLS                    : TAG_FLAVOUR_HTML,
    (TAG_LISTEXT:= 'extensions'  ): TAG_FLAVOUR_ASCII,
}

DEFAULT_FILES = [
    SPECS_DOC_DIR / p / f'{n}.txt'
    for n, p in DEFAULT_FILES.items()
]


# ----------- #
# -- TOOLS -- #
# ----------- #

def tnstitle(title):
    deco  = '='*len(title)

    return f'{deco}\n{title}\n{deco}'


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

    title = f"La saveur ``{flavour}``"

    return TEMPL_TOC.format(
        flavour = flavour,
        title   = tnstitle(title),
        toc     = toc,
    )


TEMPL_EXT = """
this::
    date = {date}


{title}

<:explanations:> à la saveur ``{flavour}``<:extra:>.

/* -- AUTO LIST - START -- */
/* -- AUTO LIST - END -- */
"""

ACTION_ADDING   = "adding"
ACTION_UPDATING = "updating"
ACTION_NOTHING  = ""

def build_ext(flavour, specs, dest_file):
    today = date.today()

# Content
    if dest_file.is_file():
        action  = ACTION_UPDATING
        content = dest_file.read_text(encoding = 'utf-8')

    else:
        action = ACTION_ADDING

        title = f"Fichiers ¨auto^t associés à la saveur ``{flavour}``"

        content = TEMPL_EXT.format(
            date    = today,
            title   = tnstitle(title),
            flavour = flavour,
        )

# Last extensions
    before, lastext , after = between(
        text = content,
        seps = [
            '/* -- AUTO LIST - START -- */',
            '/* -- AUTO LIST - END -- */'
        ],
        keepseps = True,
    )

    lastext = extract_lastext(lastext)
    newext  = specs[TAG_EXT]

    if same_ext(lastext, newext):
        return ACTION_NOTHING

# Some new extensions
    if action == ACTION_ADDING:
        if len(newext) == 1:
            explanations = "Un seul type de fichier est automatiquement associé"
            extra        = ""

        else:
            explanations = "Voici les types de fichier automatiquement associés"
            extra        =" (la recherche se fait dans l'ordre indiquée, et s'arrête dès la première concordance trouvée)"

        before = before.replace(
            "<:explanations:>",
            explanations
        ).replace(
            "<:extra:>",
            extra
        )

    newext = [
        ' '*4 + f"* path::``{e}``"
        for e in newext
    ]
    newext = '\n'.join(newext)

# Uodating the date
    if action == ACTION_UPDATING:
        newbefore = []

        for line in before.split('\n'):
            if re.match(DATE_PATTERN, line):
                line = ' '*4 + f"date = {today}"

            newbefore.append(line)

        before = '\n'.join(newbefore)

# New content.
    content = dest_file.write_text(
        data     = f"{before}\n{newext}\n{after}",
        encoding = 'utf-8'
    )

# All job done.
    return action


def extract_lastext(lastext):
    listext = []

    for line in lastext.split('\n'):
        line = line.strip()

        if line:
            line = line[1:].strip()

        for toremove in [
            "path::",
            "``"
        ]:
            line = line.replace(toremove, "")

        if line:
            listext.append(line)

    return listext


def same_ext(lastext, newext):
    l_1 = lastext.copy()
    l_1.sort()

    l_2 = newext.copy()
    l_2.sort()

    return l_1 == l_2


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

        if df.stem == TAG_LISTEXT:
            action = build_ext(flavour, specs, dest_file)

            if action:
                print(f"{TAB_2}+ {action.title()} the file ``{df.name}``.")

            continue

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

        precontent = build_predoc(
            df.read_text(
                encoding = 'utf-8'
            )
        )

        dest_file.create('file')
        dest_file.write_text(
            data     = precontent,
            encoding = 'utf-8'
        )


# TOC
    tocfile = SPECS_DOC_DIR / f"{flavour}.txt"

    if FORCE_TOC_UPDATE or not tocfile.is_file():
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
