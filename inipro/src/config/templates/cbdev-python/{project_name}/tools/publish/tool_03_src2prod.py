#!/usr/bin/env python3

from pathlib import *

from src2prod import *

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

SRC_DIR = Path(__file__).parent

while SRC_DIR.name != "cbdevtools":
    SRC_DIR = SRC_DIR.parent

README_DIR = 'readme'
SOURCE_DIR = 'src'
TARGET_DIR = 'cbdevtools'

project = Project(
    # safemode = False,
    project  = SRC_DIR,
    source   = 'src',
    target   = 'cbdevtools',
    ignore   = '''
        tool_*/
        tool_*.*
    ''',
    usegit = True,
    readme = 'readme',
)

project.update()
