#!/usr/bin/python3

from os      import chdir
from pathlib import Path
from shlex   import split as shlexsplit
import              subprocess

from justcode import (
    TAG_GLOBAL,
    TAG_PROJECT_PATH,
    Params,
)

PROJECT_DIR  = Params[TAG_GLOBAL][TAG_PROJECT_PATH]
PROJECT_REPO = Params[TAG_GLOBAL]["project_repo"]

prev_cwd = Path.cwd()

chdir(PROJECT_DIR)

for command in [
     "git init",
    f"git remote add origin {PROJECT_REPO}",
]:
    subprocess.call(
        shlexsplit(command)
    )

chdir(prev_cwd)


# ----------------- #
# -- QUICK DEBUG -- #
# ----------------- #

if __name__ == '__main__':
    chdir(PROJECT_DIR)

    subprocess.call(
        shlexsplit("git remote -v")
    )

    chdir(prev_cwd)
