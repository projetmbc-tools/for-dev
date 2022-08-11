#!/usr/bin/env python3

from datetime import date
from operator import is_
from pathlib  import Path
from requests import get as getfile

# --------------- #
# -- CONSTANTS -- #
# --------------- #

GITIGNORE_IO_BASE_URL = "https://www.gitignore.io/api/{urlparams}"

GITIGNORE_IO_WEBSITE = {
    n: n
    for n in [
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
}


TODAY = date.today()


SRC_DIR = Path(__file__).parent

while(SRC_DIR.name != 'inipro'):
   SRC_DIR = SRC_DIR.parent

SRC_DIR /= 'src'

GITIGNORE_DIR = SRC_DIR / 'config' / 'gitignore' / 'io'


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

# ----------------------------------- #
# -- UPDATES FROM ``gitignore.io`` -- #
# ----------------------------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #

print(f"{TAB_1}* Rules on ``gitignore.io``...")

for filename, urlparams in GITIGNORE_IO_WEBSITE.items():
    print(f"{TAB_2}+ Looking for ``{filename}`` with ``urlparams = {urlparams}``.")

    project_file = GITIGNORE_DIR / f"{filename}.txt"

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
    resp = getfile(
        GITIGNORE_IO_BASE_URL.format(urlparams = urlparams)
    )

    web_content = resp.text
    web_rules   = rulesfrom(web_content)

# New rules?
    if (
        (nb_newrules := len(newrules :=web_rules - project_rules)) == 0
        or
        (nb_newrules == 1 and newrules == set(['Icon\r\r']))
    ):
        print(f"{TAB_3}- No new new rule found.")
        continue

# ! -- DEBUGGING -- ! #
    print(f"{web_rules - project_rules = }")
# ! -- DEBUGGING -- ! #

    plurial = "" if nb_newrules == 1 else "s"

    print(f"{TAB_3}- {nb_newrules} new rule{plurial} found.")

    print(f"{TAB_3}- Updating the file ``{filename}.txt``.")

    web_content = f"""
# Modification made at {TODAY}.
{web_content}
    """.strip() + "\n"
    with project_file.open(
        encoding = 'utf-8',
        mode     = 'w',
    ) as f:
        project_rules = f.write(web_content)
