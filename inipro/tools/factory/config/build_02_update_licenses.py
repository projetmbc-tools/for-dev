#!/usr/bin/env python3

from datetime import date
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


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# --------------------------- #
# -- UPDATES FROM WEBSITES -- #
# --------------------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #
