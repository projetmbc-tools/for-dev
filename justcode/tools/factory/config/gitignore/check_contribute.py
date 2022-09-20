#!/usr/bin/env python3


# que si nouveau !!!"#$

# json à valider la classe

# mode validation via un drapeau !!! sinon on build


from mistool.os_use import PPath as Path
from orpyste.data import ReadBlock


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
    STATUS_TAG_NEW      := "new",
# No new rules, but maybe comments changed :
# see the value of the ``about-RULES-NAME`` key.
    STATUS_TAG_IN_API   := "inapi",
# Well named tags : this value are only changed
# by the author of the project.
    STATUS_TAG_REJECTED := "rejected",
    STATUS_TAG_ACCEPTED := "accepted",
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


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

def compare2api(contribpath, apipath):
    print(f"{TAB_3}- The file already exists in the API.")

    print(f"{contribpath = }")
    print(f"{apipath     = }")


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
    rules_filename_noext = p.name
    rules_filename       = p.stem

    print(f"{TAB_2}+ Checking ``{rules_filename_noext}``.")

    if (apipath := GIT_SRC_DATAS_DIR / rules_filename_noext).is_file():
        status = compare2api(
            contribpath = p,
            apipath     = apipath,
        )

    else:
        status = STATUS_TAG_NEW
