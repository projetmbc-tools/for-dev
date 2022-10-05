#!/usr/bin/env python3

import black

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


GITIGNORE_DIR = PROJECT_DIR / 'src' / 'config' / 'gitignore' / 'datas'
INIT_FILE     = GITIGNORE_DIR / '__init__.py'

FINAL_DIR       = THIS_DIR / 'datas' / 'final'
IGNORE_TXT_FILE = 'ignore.txt'


TEMPL_API_RULES = f"""
#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``{THIS_FILE_REL_PROJECT_DIR}``

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
        return ''

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
    comment_rules = []

    comment  = []
    lofrules = []

    for l in prettyrules:
        if not l:
            continue

        if l[0] == '#':
            if lofrules:
                comment_rules.append({
                    'comment': '\n'.join(comment),
                    'rules'  : lofrules,
                })

                comment  = []
                lofrules = []

            comment.append(l)

        else:
            lofrules.append(l)

    if lofrules:
        comment_rules.append({
            'comment': '\n'.join(comment),
            'rules'  : lofrules,
        })


# Rules
    return {
        'desc' : desc,
        'rules': comment_rules,
    }



def update(rules, ctxts, content):
    firstctxt, *otherctxts = ctxts
    firstctxt = firstctxt.lower()

    if otherctxts:
        if not firstctxt in rules:
            rules[firstctxt] = dict()

        update(rules[firstctxt], otherctxts, content)

    else:
        rules[firstctxt] = content


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

    ctxts = ctxts.with_ext('') \
                 .parts

    update(API_RULES, ctxts, content)


# ! -- DEBUGGING -- ! #
# Clear the terminal.
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

print(f"{TAB_1}* Update of the Python files.")

for mainctxt, subctxts in API_RULES.items():
    subctxts = black.format_file_contents(
        repr(subctxts),
        fast = False,
        mode = black.FileMode()
    ).strip()

    (GITIGNORE_DIR / f'{mainctxt}.py').write_text(
        encoding = 'utf-8',
        data     = TEMPL_API_RULES.format(
            subctxts = subctxts
        )
    )
