#!/usr/bin/env python3

from datetime import date
from operator import is_
from pathlib  import Path
from requests import get as getfile

# --------------- #
# -- CONSTANTS -- #
# --------------- #

TODAY = date.today()


SRC_DIR = Path(__file__).parent

while(SRC_DIR.name != 'inipro'):
   SRC_DIR = SRC_DIR.parent

SRC_DIR /= 'src'

LICENSES_DIR = SRC_DIR / 'config' / 'licenses' / 'online'
