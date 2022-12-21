#! /usr/bin/env python3

from cbdevtools import *


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)


# -------------- #
# -- LET'S GO -- #
# -------------- #

from src.build import *

mybuilder = Builder()
