#!/usr/bin/env python3

import           black
from json import dumps

from mistool.os_use     import PPath as Path
from mistool.string_use import between
from orpyste.data       import ReadBlock

from core import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR


JSON_RULES_FILE = THIS_DIR / 'apirules.json'

ALL_TAGS = [
    TAG_DESC           := ':desc:',
    TAG_RULES          := ':rules:',
    TAG_COMMENTS       := ':comments:',
    TAG_RULES_COMMENTS := f'{TAG_RULES[:-1]}-n-{TAG_COMMENTS[1:]}',
]

TAGS_VARNAMES = {
    'TAG_' + t.replace(':', '')  \
              .replace('-', '_') \
              .upper(): t
    for t in ALL_TAGS
}

PYCODE_TAGS = f"""
#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``{THIS_FILE_REL_PROJECT_DIR}``

"""

for varname, tag in TAGS_VARNAMES.items():
    PYCODE_TAGS += f'{varname} = "{tag}"'
    PYCODE_TAGS += '\n'


GITIGNORE_DIR       = PROJECT_DIR / 'src' / 'config' / 'gitignore'
GITIGNORE_DATAS_DIR = GITIGNORE_DIR / 'datas'

TAGS_FILE  = GITIGNORE_DATAS_DIR / 'TAGS.py'
# INIT_FILE     = GITIGNORE_DATAS_DIR / '__init__.py'

FINAL_DIR       = THIS_DIR / 'datas' / 'final'
IGNORE_TXT_FILE = 'ignore.txt'


TEMPL_API_RULES = f"""
#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``{THIS_FILE_REL_PROJECT_DIR}``

from .TAGS import *

RULES = {{subctxts}}
""".strip() + '\n'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

def ignorethisname(onepath):
    return onepath.name == IGNORE_TXT_FILE


COMMENT_TITLE_1 = '#'*4

def buildapirules(content, ctxts):
# Metainfos, and rules to analyze.
    before, metainfos, rules = between(
        text = content,
        seps = ['###', '###']
    )

    before    = before.strip()
    metainfos = metainfos.strip()
    rules     = rules.strip()

    assert not before, \
           (
             'illegal text before the first ``###`` '
            f'in ``{ctxts}``.'
           )

# Metainfos
    peuflines = []

    for l in metainfos.split('\n'):
        l = l.strip()

        assert (
                l == '#'
                or
                l.startswith('# ')
               ), \
               (
                 'metainfos must use leading ``# ``.'
                 '\n'
                f'See ``{l}`` in ``{ctxts}``.'
               )

# We just need to work with the block ``this``.
        l = l[2:]

        if not l:
            break

        peuflines.append(l)


    with ReadBlock(
        content = '\n'.join(peuflines),
        mode    = {
            "keyval:: =": "this",
        }
    ) as datas:
        infos = datas.mydict("tree std nosep nonb")

    infos = infos['this']
    desc  = '\n'.join(
        f'{COMMENT_TITLE_1} {l}'
        for l in infos['desc'].split('\n')
    )

# Rules
    if not rules:
        return {}

    prettyrules = []

    for l in rules.split('\n'):
        l = l.strip()

        if not l:
            continue

        if l.startswith('#'):
            l = f'#{l}'

            prettyrules.append('')

        prettyrules.append(l)

    while(prettyrules and not prettyrules[0]):
        prettyrules.pop(0)

# Comments and list of rules.
    commentedrules = []

    comment  = []
    lofrules = []

    for l in prettyrules:
        if not l:
            continue

        if l[0] == '#':
            if lofrules:
                updatectxtapi(
                    commentedrules,
                    comment,
                    lofrules
                )

                comment  = []
                lofrules = []

            comment.append(l)

        else:
            lofrules.append(l)

    if lofrules:
        updatectxtapi(
            commentedrules,
            comment,
            lofrules
        )


# Rules
    return {
        TAG_DESC          : desc,
        TAG_RULES_COMMENTS: commentedrules,
    }


def update(rules, ctxts, content):
    firstctxt, *otherctxts = ctxts
    firstctxt = firstctxt.lower()

    if otherctxts:
        if not firstctxt in rules:
            rules[firstctxt] = dict()

        update(rules[firstctxt], otherctxts, content)

    elif content:
        rules[firstctxt] = content


def updatectxtapi(commentedrules, comment, lofrules):
    commentedrules.append({
        TAG_COMMENTS: '\n'.join(comment),
        TAG_RULES   : lofrules,
    })


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

print(f"{TAB_1}* Preparing the code for the API rules.")

API_RULES = {}

for p in FINAL_DIR.glob('**/*.txt'):
    if ignorethisname(p):
        continue

    ctxts = p - FINAL_DIR

    content = buildapirules(
        p.read_text(encoding = 'utf-8'),
        ctxts
    )

    if content:
        ctxts = ctxts.with_ext('') \
                    .parts

        update(API_RULES, ctxts, content)


# ! -- DEBUGGING -- ! #
# from pprint import pprint
# print("API_RULES")
# pprint(API_RULES)

# print(API_RULES["translate"]["gettext"])

# print(API_RULES["python"]["dev"]["rope"])
# exit()
# ! -- DEBUGGING -- ! #


# ----------------------- #
# -- UPDATING PY FILES -- #
# ----------------------- #

print(f"{TAB_1}* Update of {len(API_RULES)} Python files in the source.")

for mainctxt, subctxts in API_RULES.items():
    subctxts_code = black.format_file_contents(
        repr(subctxts),
        fast = False,
        mode = black.FileMode()
    ).strip()

    for varname, tag in TAGS_VARNAMES.items():
        subctxts_code = subctxts_code.replace(
            f'"{tag}"',
            varname
        )

    (GITIGNORE_DATAS_DIR / f'{mainctxt}.py').write_text(
        encoding = 'utf-8',
        data     = TEMPL_API_RULES.format(
            subctxts = subctxts_code
        )
    )


# ----------------------- #
# -- UPDATING PY FILES -- #
# ----------------------- #

print(f"{TAB_1}* Update of ``{TAGS_FILE.name}`` in the source.")

TAGS_FILE.write_text(
    encoding = 'utf-8',
    data     = PYCODE_TAGS
)


# ------------------------ #
# -- UPDATING JSON FILE -- #
# ------------------------ #

print(f"{TAB_1}* Update of ``{JSON_RULES_FILE.name}`` in teh factory.")

JSON_RULES_FILE.write_text(
    data = dumps(
        obj    = API_RULES,
        indent = 4
    ),
    encoding = 'utf-8'
)
