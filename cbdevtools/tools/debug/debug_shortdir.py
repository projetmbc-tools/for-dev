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


print("shortdir(1) =")
pprint(shortdir(1))
print()

for toignore in [
    [],
    ['imag', 'real'],
    ['as_.+', 'from_.+']
]:
    toignore = [re_compile(s) for s in toignore]

    if toignore:
        toignore.append(PATTERN_UNDERSCORE)

    print(f"{toignore = }")

    print("shortdir(1, toignore) =")
    pprint(shortdir(1, toignore))
    print()
