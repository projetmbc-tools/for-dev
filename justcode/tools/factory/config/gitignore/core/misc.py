#!/usr/bin/env python3

from typing import Tuple


# ----------------- #
# -- NAME & KIND -- #
# ----------------- #

def build_kindname(kind: str, name: str) -> str:
    return f"{kind}/{name}"


def extract_kindname(kindname: str) -> Tuple[str, str]:
    return kindname.split('/')


# -------------------------- #
# -- "BY HAND" MANAGEMENT -- #
# -------------------------- #

def keep_thisrules(kindname: str) -> bool:

    return False
