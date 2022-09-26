#!/usr/bin/env python3

from mistool.os_use import PPath as Path


# ----------- #
# -- TOOLS -- #
# ----------- #

def getcontent(path: Path) -> str:
    with path.open(
        encoding = 'utf-8',
        mode     = 'r',
    ) as f:
        content = f.read()

    return content


def rulesfrom(content: str) -> set:
    rules = set()

    for line in content.splitlines():
        if(
            not line
            or
            line[0] in ['#']
        ):
            continue

        rules.add(line)

    return rules
