#!/usr/bin/env python3

import                          black
from collections         import defaultdict
from concurrent.futures  import ThreadPoolExecutor
from datetime            import date
from requests            import (
    ConnectionError,
    get as getwebcontent
)

from bs4 import BeautifulSoup

from mistool.os_use import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

UPDATE_ONLINE = True
# UPDATE_ONLINE = False # Debug mode.

NB_WORKERS = 5
# NB_WORKERS = 1 # Debug mode.


GITIGNORE_IO_URL      = "https://www.gitignore.io"
GITIGNORE_IO_BASE_URL = GITIGNORE_IO_URL + "/api/{urlparam}"

GITHUB_URL           = "https://github.com"
GITHUB_TEMPLATES_URL = f"{GITHUB_URL}/toptal/gitignore/tree/master/templates"
GITHUB_RAW_BASE_URL  = "https://raw.githubusercontent.com/toptal/gitignore/master/templates"


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

def pyname(name):
    cname = ""

    for c in name:
        if c in "-+":
            c = "_"

        cname += c

    cname = cname.upper()

    if cname == "C__":
        cname = "CPP"

    elif cname == "TLA_":
        cname = "TLA_PLUS"

    return cname


def allurls():
    bs = BeautifulSoup(
        getwebcontent(GITHUB_TEMPLATES_URL).text,
        "html.parser"
    )

    urls = []

    for elt in bs.select('a'):
        href = elt['href']

        if href.endswith('.gitignore'):
            rule = Path(href).stem

            urls.append(f"{GITHUB_RAW_BASE_URL}/{rule}.gitignore")

    return urls


def rulesfrom(content: str) -> set:
    rules = set()

    for line in content.splitlines():
        if(
            not line
            or
            line[0] in ['#']
        ):
            continue

        rules.add(line)

    return rules


def extractrules(urlraw):
# Some constants.
    rulename = str(Path(urlraw).stem)
    rulename = rulename.replace("%2B", "+")

    whichrules   = f"{TAB_2}+ ``{rulename}``"
    project_file = GITIGNORE_ONLINE_DIR / f"{rulename}.txt"

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
    resp = getwebcontent(urlraw)

    if resp.status_code != 200:
        raise Exception('AIE !')

    web_content = resp.text
    web_rules   = rulesfrom(web_content)

# New rules or removed ones?
    weird_rules = set(['Icon\r\r'])
    newrules    = web_rules - project_rules - weird_rules
    nb_newrules = len(newrules)

    weird_rules  = set(['Icon'])
    lostrules    = project_rules - web_rules - weird_rules
    nb_lostrules = len(lostrules)

# Nothing has changed.
    if (
        nb_newrules == 0
        and
        nb_lostrules == 0
    ):
        print(
            whichrules,
            f"{TAB_3}- No new rule found.",
            f"{TAB_3}- No rule removed.",
            sep = "\n"
        )
        return

# ! -- DEBUGGING -- ! #
    # print(f"{web_rules = }")
    # print(f"{project_rules = }")
    # exit(1)
# ! -- DEBUGGING -- ! #

# Something has changed...
    infos = []

    for (nb, xtra, kind) in [
        (nb_newrules , "new", "found"  ),
        (nb_lostrules, ""   , "removed"),
    ]:
        if xtra:
            xtra += " "

        if nb == 0:
            infos.append(
                f"{TAB_3}- No {xtra}rule {kind}."
            )

        else:
            plurial = "" if nb == 1 else "s"

            infos.append(
                f"{TAB_3}- {nb} {xtra} rule{plurial} {kind}."
            )

    infos = "\n".join(infos)

    print(
        whichrules,
        infos,
        f"{TAB_3}- Updating the file ``{rulename}.txt``.",
        sep = "\n"
    )

    web_content = f"""
# Modification made at {TODAY}.
#
# This rules come from the project gitignore.io. See :
# https://github.com/toptal/gitignore.io

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


# ----------------------- #
# -- ARE WE CONNECTED? -- #
# ----------------------- #

try:
    getwebcontent("https://www.google.com/")

except ConnectionError:
    print(f"{TAB_1}* No internet connection.")
    exit(1)


# ----------------------------------- #
# -- UPDATES FROM ``gitignore.io`` -- #
# ----------------------------------- #

if UPDATE_ONLINE:
    print(f"{TAB_1}* Looking for rules on ``github.com``.")

    urls = allurls()

    print(f"{TAB_1}* {len(urls)} rules found.")

    print(f"{TAB_1}* Rules made by ``gitignore.io``.")

    with ThreadPoolExecutor(max_workers = NB_WORKERS) as exe:
        exe.map(extractrules, urls)


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

TAG_ONLINE  = '__online__'
TAG_SPECIAL = '__special__'

for kind in [
    TAG_ONLINE,
    TAG_SPECIAL,
]:
    sortednames = sorted(
        gitignores_by_kind[kind],
        key = lambda n: pyname(n)
    )

    code_EACH_TAG.append(kind)

    code_EACH_TAG += [
        f'TAG_GITIGNORE_{pyname(n)} := "{n}",'
        for n in sortednames
    ]

    code_EACH_TAG.append('')


code_EACH_TAG = '\n    '.join(code_EACH_TAG[:-1])


for kind in [
    TAG_ONLINE,
    TAG_SPECIAL,
]:
    ctitle = kind.replace('_', '').title()

    code_EACH_TAG = code_EACH_TAG.replace(
        kind,
        f"# {ctitle}"
    )


code = f"""
#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``{THIS_FILE_REL_PROJECT_DIR}``

# ALL THE TAGS

ALL_GITIGNORES = [
    {code_EACH_TAG}
]
        """.strip() + '\n'

code = code.replace(
    "    #",
    "#"
)

with PYFILE.open(
    encoding = 'utf8',
    mode     = 'w',
) as f:
    f.write(code)
