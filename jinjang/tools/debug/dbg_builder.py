#! /usr/bin/env python3

from pprint import pprint

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

template = """
One small {{ txt_example }} with automatic calculations.

{#: for i in range(1, max_i + 1) :#}
    {{ i }}) I count using squares: {{ i**2 }}.
{#: endfor :#}
""".strip()

datas = {}

output = mybuilder.render_fromstr(
    datas    = datas,
    template = template,
)

print("\033c", end="")

for kind in [
    'datas',
    'template',
    'output',
]:
    if kind != 'datas':
        print()

    print(f'--- {kind} ---')
    print()

    toprint = globals()[kind]

    if kind == 'datas':
        pprint(toprint)

    else:
        print(toprint)

print()
