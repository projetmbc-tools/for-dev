#!/usr/bin/env python3

from cbdevtools import *


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'spkpb',
)


# -------------- #
# -- LET'S GO -- #
# -------------- #

from src import *

speaker = Speaker(
    logfile = Path('mylog.log')
)

timestamp(
    speaker = speaker,
    kind    = 'start 1',
)

timestamp(
    speaker = speaker,
    kind    = 'start 2',
    with_NL = False,
)

timestamp(
    speaker = speaker,
    kind    = 'start 3',
)
