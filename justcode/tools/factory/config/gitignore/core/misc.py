#!/usr/bin/env python3

from typing import Tuple


# -------------------------- #
# -- "BY HAND" MANAGEMENT -- #
# -------------------------- #

WOTKING_ON = """
PYTHON
TEX
""".upper() \
   .strip() \
   .split('\n')


def keep_thisrules(kindname: str) -> bool:
    _, name = extract_kindname(kindname)

    if name in WOTKING_ON:
        return True

    return False


# ----------------- #
# -- NAME & KIND -- #
# ----------------- #

def build_kindname(kind: str, name: str) -> str:
    return f"{kind}/{name}"


def extract_kindname(kindname: str) -> Tuple[str, str]:
    return kindname.split('/')
