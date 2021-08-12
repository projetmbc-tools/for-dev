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

project = BaseCom(
    Problems(
        Speaker(
            logfile = Path('mylog.log'),
            style   = GLOBAL_STYLE_COLOR,
        )
    )
)

project.timestamp(kind = 'start')

project.new_warning(
    what = Path('one/strange/file.txt'),
    info = "some strange behaviors."
)

print(f'>>>>>>>> sucess = {project.success}')

project.new_error(
    what = Path('one/bad/file.txt'),
    info = "bad things appear."
)

print(f'>>>>>>>> sucess = {project.success}')

project.recipe(
    NL,
    'One basic showcase.',
    FORTERM,
        {VAR_STEP_INFO: 'ONLY FOR THE TERMINAL OUPUT!',
         VAR_LEVEL    : 1},
    FORLOG,
        {VAR_STEP_INFO: 'ONLY IN THE LOG FILE!',
         VAR_LEVEL    : 1},
)
    
project.resume()

project.recipe(NL)
project.timestamp(kind = 'end')
