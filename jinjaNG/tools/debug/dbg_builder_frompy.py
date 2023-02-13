#! /usr/bin/env python3

from pprint import pprint

from cbdevtools import *


# Clear the terminal.
print("\033c", end="")


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src.jngbuild import *


# -------------- #
# -- LET'S GO -- #
# -------------- #

mybuilder = JNGBuilder(flavour = FLAVOUR_ASCII)

template = """
One small {{ txt_example }} with automatic calculations.

#: for i in range(1, max_i + 1)
    {{ i }}) I count using squares: {{ i**2 }}.
#: endfor
""".strip()

data = {
    "txt_example": 'example',
    "max_i"      : 4,
}

output = mybuilder.render_frompy(
    data    = data,
    template = template,
)

print("\033c", end="")

for kind in [
    'data',
    'template',
    'output',
]:
    if kind != 'data':
        print()

    print(f'--- {kind} ---')
    print()

    toprint = globals()[kind]

    pprint(toprint) if kind == 'data' else print(toprint)

print()
