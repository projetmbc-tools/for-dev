#!/usr/bin/env python3

import                          black
from collections         import defaultdict
from concurrent.futures  import ThreadPoolExecutor
from datetime            import date
from requests            import get as getwebcontent

from mistool.os_use import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

UPDATE_ONLINE = True
# UPDATE_ONLINE = False # Debug mode.

GITIGNORE_IO_BASE_URL = "https://www.gitignore.io/api/{urlparam}"

GITIGNORE_IO_WEBSITE = [
# LaTeX
    'latex',
# Python
    'python',
    'jupyternotebooks',
# OS
    'windows',
    'osx',
    'linux',
]



TODAY = date.today()


THIS_FILE = Path(__file__)

PROJECT_DIR = Path(THIS_FILE).parent

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR

GITIGNORE_DIR        = PROJECT_DIR / 'src' / 'config' / 'gitignore'
GITIGNORE_ONLINE_DIR = GITIGNORE_DIR / 'online'
PYFILE               = GITIGNORE_DIR / 'gitignore.py'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

def rulesfrom(content: str) -> set:
    rules = set()

    for line in content.split('\n'):
        if(
            not line
            or
            line[0] == '#'
        ):
            continue

        rules.add(line)

    return rules


def extractrules(urlparam):
    whichrules = f"{TAB_2}+ ``{urlparam}``"

    project_file = GITIGNORE_ONLINE_DIR / f"{urlparam}.txt"

# Rules in the project.
    if project_file.is_file():
        with project_file.open(
            encoding = 'utf-8',
            mode     = 'r',
        ) as f:
            project_rules = rulesfrom(f.read())

    else:
        project_rules = set()

# Rules on ``gitignore.io``.
    web_content = getwebcontent(
        GITIGNORE_IO_BASE_URL.format(urlparam = urlparam)
    )

    web_content = web_content.text
    web_rules   = rulesfrom(web_content)

# New rules?
    newrules    = web_rules - project_rules
    nb_newrules = len(newrules)

    if (
        (nb_newrules) == 0
        or
        (nb_newrules == 1 and newrules == set(['Icon\r\r']))
    ):
        print(
            whichrules,
            f"{TAB_3}- No new rule found.",
            sep = "\n"
        )
        return

# ! -- DEBUGGING -- ! #
    # print(f"{web_rules - project_rules = }")
# ! -- DEBUGGING -- ! #

    plurial = "" if nb_newrules == 1 else "s"

    print(
        whichrules,
        f"{TAB_3}- {nb_newrules} new rule{plurial} found.",
        f"{TAB_3}- Updating the file ``{urlparam}.txt``.",
        sep = "\n"
    )

    web_content = f"""
# Modification made at {TODAY}.
{web_content}
    """.strip() + "\n"
    with project_file.open(
        encoding = 'utf-8',
        mode     = 'w',
    ) as f:
        project_rules = f.write(web_content)


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ----------------------------------- #
# -- UPDATES FROM ``gitignore.io`` -- #
# ----------------------------------- #

if UPDATE_ONLINE:
    print(f"{TAB_1}* Rules on ``gitignore.io``.")

    with ThreadPoolExecutor(max_workers = 5) as exe:
        exe.map(extractrules, GITIGNORE_IO_WEBSITE)


# ----------------------------- #
# -- UPDATE ``gitignore.py`` -- #
# ----------------------------- #

print(f"{TAB_1}* Updating ``gitignore.py``.")

gitignores_found   = set()
gitignores_by_kind = defaultdict(list)

for f in GITIGNORE_DIR.walk("file::**.txt"):
    name = f.stem
    kind = f'__{f.parent.name}__'

    assert not name in gitignores_found, \
           (
            f"name ``{name}`` already used in another kind."
             "\n"
            f"See the folder ``{kind.replace('_', '')}``."
           )

    gitignores_found.add(name)

    gitignores_by_kind[kind].append(name)


code_EACH_TAG = []

ALL_GITIGNORES = []

TAG_ONLINE  = '__online__'
TAG_SPECIAL = '__special__'

for kind in [
    TAG_ONLINE,
    TAG_SPECIAL,
]:
    sortednames = sorted(gitignores_by_kind[kind])

    ALL_GITIGNORES.append(kind)
    ALL_GITIGNORES += sortednames

    code_EACH_TAG.append(kind)

    code_EACH_TAG += [
        f'TAG_GITIGNORE_{n.upper()} = "{n}"'
        for n in sortednames
    ]

    code_EACH_TAG.append('')


code_ALL_TAGS = f"{ALL_GITIGNORES = }"

code_ALL_TAGS = black.format_file_contents(
    code_ALL_TAGS,
    fast = False,
    mode = black.FileMode()
)


code_EACH_TAG = '\n'.join(code_EACH_TAG)


for kind in [
    TAG_ONLINE,
    TAG_SPECIAL,
]:
    ctitle = kind.replace('_', '').title()

    code_ALL_TAGS = code_ALL_TAGS.replace(
        ' '*4 + f'"{kind}",',
        f"# {ctitle}"
    )

    code_EACH_TAG = code_EACH_TAG.replace(
        kind,
        f"# {ctitle}"
    )

for n in ALL_GITIGNORES:
    code_ALL_TAGS = code_ALL_TAGS.replace(
        f'"{n}"',
        f'TAG_GITIGNORE_{n.upper()}'
    )


with PYFILE.open(
    encoding = 'utf8',
    mode     = 'w',
) as f:
    f.write(
        f"""
#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``{THIS_FILE_REL_PROJECT_DIR}``

# EACH TAG

{code_EACH_TAG}

# ALL THE TAGS

{code_ALL_TAGS}
        """.strip()
        +
        '\n'
    )
