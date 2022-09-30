#!/usr/bin/env python3

from mistool.os_use import PPath as Path

from .constants import (
    PT_EXT_GITIGN,
    PT_EXT_PATCH
)


# ----------- #
# -- TOOLS -- #
# ----------- #

def rulesfrom(content: str) -> set:
    rules = set()

    for line in content.splitlines():
        line = line.strip()

        if(
            not line
            or
            line[0] in ['#']
        ):
            continue

        rules.add(line)

    return rules


def usefulrulesfrom(path: Path) -> set:
    rules = rulesfrom(
        path.read_text(
            encoding = 'utf-8'
        )
    )

    if len(rules) == 1:
        for therule in rules:
            if therule.endswith((PT_EXT_GITIGN, PT_EXT_PATCH)):
# ! -- DEBUGGING -- ! #
                # print(path.stem)
# ! -- DEBUGGING -- ! #

                rules = set()

    return rules
