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
    logfile = Path('mylog.log'),
    style   = GLOBAL_STYLE_COLOR,
    silent  = True,
)

problems = Problems(speaker)

problems.new_warning(
    what = Path('one/strange/file.txt'),
    info = "some strange behaviors."
)

problems.new_error(
    what = Path('one/bad/file.txt'),
    info = "bad things appear."
)

speaker.recipe(
    NL,
    'One basic showcase.',
    FORTERM,
        {VAR_STEP_INFO: 'ONLY FOR THE TERMINAL OUPUT!',
         VAR_LEVEL    : 1},
    FORLOG,
        {VAR_STEP_INFO: 'ONLY IN THE LOG FILE!',
         VAR_LEVEL    : 1},
)
    
problems.resume()
