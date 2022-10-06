#!/usr/bin/env python3

from typing import List

from mistool.os_use import PPath as Path

from .misc import *


# ------------------- #
# -- WRITING RULES -- #
# ------------------- #

def writerules(
    dirpath  : Path,
    kind_name: str,
    rules    : List[str],
    header   : str = ""
) -> None:
    _, name = extract_kindname(kind_name)
    name    = f'{name}.txt'

    content = '\n'.join(rules).strip() + '\n'

    if header:
        content = f"{header}\n\n{content}"

    (dirpath / name).write_text(
        data     = content,
        encoding = 'utf-8'
    )
