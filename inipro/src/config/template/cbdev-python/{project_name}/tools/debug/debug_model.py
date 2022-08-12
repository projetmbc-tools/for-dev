#!/usr/bin/env python3

# ----------------------------- #
# -- WHICH CODE IS DEBUGGED? -- #
# ----------------------------- #

TESTIG_SRC = False
# To test the installed package instead of the source code,
# comment the line below.
TESTIG_SRC = True


# ---------------------------------- #
# -- WHICH FEATURES ARE DEBUGGED? -- #
# ---------------------------------- #

if TESTIG_SRC:
    from cbdevtools import *

    MODULE_DIR = addfindsrc(
        file    = __file__,
        project = '{name}',
    )

    from src.{name} import *

else:
    from {name} import *


# -------------- #
# -- LET'S GO -- #
# -------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #

# Just write your debugging code here.
