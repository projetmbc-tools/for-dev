#!/usr/bin/env python3

LOCAL_TEST = False
LOCAL_TEST = True


from pprint import pprint

if LOCAL_TEST:
    from cbdevtools import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

if LOCAL_TEST:
    MODULE_DIR = addfindsrc(
        file    = __file__,
        project = 'cbdevtools',
    )


# -------------- #
# -- LET'S GO -- #
# -------------- #

if LOCAL_TEST:
    from src.shortdir import shortdir, re_compile, PATTERN_UNDERSCORE

else:
    from cbdevtools.shortdir import shortdir, re_compile, PATTERN_UNDERSCORE
