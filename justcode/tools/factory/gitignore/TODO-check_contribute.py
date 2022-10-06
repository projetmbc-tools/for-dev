#!/usr/bin/env python3


# que si nouveau !!!"#$

# json à valider la classe

# mode validation via un drapeau !!! sinon on build


from mistool.os_use import PPath as Path
from orpyste.data import ReadBlock

from core.extract import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = PROJECT_DIR = Path(THIS_FILE).parent

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


GIT_SRC_DIR       = PROJECT_DIR / 'src' / 'config' / 'gitignore'
GIT_SRC_DATAS_DIR = GIT_SRC_DIR / 'datas'

GIT_CONTRIB_DIR       = PROJECT_DIR / 'contribute' / 'api' / 'gitignore'
GIT_CONTRIB_DATAS_DIR = GIT_CONTRIB_DIR / 'datas'


ALL_STATUS_TAGS = [
# New rules.
    STATUS_TAG_NEW         := "new",
# No new rule, but the formatting is different.
    STATUS_TAG_SAME_IN_API := "same-in-api",
# The file is already in the API (same rules and
# formatting).
    STATUS_TAG_IN_API      := "in-api",
# Well named tags : this values are only changed
# by the author of the project.
    STATUS_TAG_REJECTED    := "rejected",
    STATUS_TAG_ACCEPTED    := "accepted",
]


STATUS_FILE = THIS_DIR / 'contrib-status.peuf'

if STATUS_FILE.is_file():
    with ReadBlock(
        content = STATUS_FILE,
        mode    = {
            "keyval:: =": "status",
        }
    ) as datas:
        LAST_STATUS_INFOS = datas.mydict("tree std nosep nonb")
        LAST_STATUS_INFOS = LAST_STATUS_INFOS["status"]

else:
    LAST_STATUS_INFOS = dict()


API_CONTENTS = dict()
API_RULES    = dict()

for apipath in GIT_SRC_DATAS_DIR.walk("file::**.txt"):
    name = apipath.stem


    content = getcontent(apipath)

    assert not content in API_CONTENTS, \
           f"same content for ``{name}`` and ``{API_CONTENTS[content]}``."

    API_CONTENTS[content] = name


    repr_rules = repr(rulesfrom(content))

    assert not repr_rules in API_RULES, \
           f"similar contents for ``{name}`` and ``{API_RULES[repr_rules]}``."

    API_RULES[repr_rules] = name


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

def compare2api(contribpath):
    contrib_content = getcontent(contribpath)

    if contrib_content in API_CONTENTS:
        return STATUS_TAG_IN_API

    repr_rules = repr(rulesfrom(contrib_content))

    if repr_rules in API_RULES:
        return STATUS_TAG_SAME_IN_API

    return STATUS_TAG_NEW


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ------------------------------- #
# -- LOOKING FOR CONTRIBUTIONS -- #
# ------------------------------- #

print(f"{TAB_1}* GITIGNORE rules - Looking for contributions.")

# ! -- DEBUGGING -- ! #
# print(f"{LAST_STATUS_INFOS = }")
# ! -- DEBUGGING -- ! #

code = []

allpaths = [p for p in GIT_CONTRIB_DATAS_DIR.walk("file::**.txt")]
allpaths.sort()

for p in allpaths:
    print(f"{TAB_2}+ Checking ``{p.stem}``.")

    status = compare2api(p)

    if status == STATUS_TAG_NEW:
        print(f"{TAB_3}- New rules found.")

    elif status == STATUS_TAG_SAME_IN_API:
        api_name = API_RULES[repr(rulesfrom(getcontent(p)))]

        print(f"{TAB_3}- Similar rules in the API : see ``{api_name}`` .")
