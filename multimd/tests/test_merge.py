#!/usr/bin/env python3

from cbdevtools import *


# ------------------------------------ #
# -- FUNCTION(S) / CLASS(ES) TESTED -- #
# ------------------------------------ #

THIS_DIR = Path(__file__).parent

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'multimd',
)

from src import *


# ------------------------ #
# -- MERGING - NO ABOUT -- #
# ------------------------ #

def test_merge_no_about():
    ...


# -------------------------- #
# -- MERGING - WITH ABOUT -- #
# -------------------------- #

def test_merge_with_about():
    ...