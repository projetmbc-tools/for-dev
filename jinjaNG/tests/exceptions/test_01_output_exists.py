#!/usr/bin/env python3

from pytest import raises as pyt_raises

from cbdevtools.addfindsrc import addfindsrc


# -------------------- #
# -- PACKAGE TESTED -- #
# -------------------- #

addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src import *

MY_BUILDER = JNGBuilder()


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR = Path(__file__).parent

FOLDER_TESTED = THIS_DIR / 'fake' / 'all-good-files'

DATA     = FOLDER_TESTED / 'data.yaml'
TEMPLATE = FOLDER_TESTED / 'template.txt'
OUTPUT   = FOLDER_TESTED / 'output.txt'


# ------------------------------ #
# -- OUTPUT CAN NOT BE ERASED -- #
# ------------------------------ #

def test_output_not_erasable():
    with pyt_raises(Exception) as exc_info:
        MY_BUILDER.render(
            data     = DATA,
            template = TEMPLATE,
            output   = OUTPUT
        )


# -------------------------- #
# -- OUTPUT CAN BE ERASED -- #
# -------------------------- #

def test_output_erasable():
    MY_BUILDER.render(
        erase    = True,
        data     = DATA,
        template = TEMPLATE,
        output   = OUTPUT
    )
