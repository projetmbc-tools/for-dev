#!/usr/bin/python3

from os      import chdir
from pathlib import Path
from shlex   import split as shlexsplit
import              subprocess

from justcode import (
    TAG_MAIN,
    TAG_PROJECT_PATH,
    Params,
)


projdir  = Params[TAG_MAIN][TAG_PROJECT_PATH]
projrepo = Params[TAG_MAIN]["project_repo"]

initial_workdir = Path.cwd()

chdir(projdir)

for command in [
     "git init",
    f"git remote add origin {projrepo}",
]:
    subprocess.call(
        shlexsplit(command)
    )

chdir(initial_workdir)
