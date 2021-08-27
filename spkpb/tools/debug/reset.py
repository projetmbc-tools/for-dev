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
            logfile   = Path('mylog.log'),
            termstyle = GLOBAL_STYLE_COLOR,
        )
    )
)

project.new_warning(
    what = Path('one/strange/file.txt'),
    info = "some strange behaviors."
)

project.reset()

project.new_error(
    what = Path('one/bad/file.txt'),
    info = "bad things appear."
)

project.resume()
