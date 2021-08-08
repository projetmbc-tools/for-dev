#! /usr/bin/env python3

from speaker import *
from problems import *

speaker  = Speaker(
    logfile = Path('mylog.log'),
    style   = GLOBAL_STYLE_COLOR
)

problems = Problems(speaker)

problems.new_warning(
    what = Path('one/strange/file.txt'),
    info        = "Some strange behaviors."
)

problems.new_error(
    src_relpath = Path('one/bad/file.txt'),
    info        = "Bad things appear."
)

speaker.recipe(
    NL,
    'One basic showcase.',
    FORTERM,
        {VAR_STEP_INFO: 'Write just on the terminal',
         VAR_LEVEL    : 1},
    FORLOG,
        {VAR_STEP_INFO: 'Only in the log?',
         VAR_LEVEL    : 1},
)
    
problems.resume()
