#!/usr/bin/python3

from os      import chdir
from pathlib import Path
from shlex   import split as shlexsplit
import              subprocess

from justcode import (
    GLOBAL_TAG,
    PROJECT_PATH_TAG,
    Params,
)

PROJECT_DIR  = Params[GLOBAL_TAG][PROJECT_PATH_TAG]
PROJECT_REPO = Params[GLOBAL_TAG]["project_repo"]

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
