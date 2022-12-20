#!/usr/bin/env python3

from typing import Tuple

from collections import defaultdict
from pathlib     import Path

from cbdevtools.addfindsrc import addfindsrc


# -------------------- #
# -- PACKAGE TESTED -- #
# -------------------- #

addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src import *


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR = Path(__file__).parent

DATAS_DIR = THIS_DIR / 'datas'

FLAVOURS_SETTINGS = config.flavour.SETTINGS
TAG_EXT           = config.flavour.TAG_EXT


# ---------------------- #
# -- USECASES FOLDERS -- #
# ---------------------- #

def yielddirs(pdir: Path) -> Path:
    if not pdir.is_dir():
        raise Exception(
            f"one dir expected, see:\n{pdir}"
        )

    for subdir in pdir.glob('*'):
        if(
            subdir.is_dir()
            and
            not subdir.name.startswith('.')
            and
            not subdir.name.startswith('x-')
        ):
            yield subdir


USECASES_FOLDERS = defaultdict(list)

for pdir in yielddirs(DATAS_DIR):
    flavour = pdir.name

    for ucdir in yielddirs(pdir):
        USECASES_FOLDERS[flavour].append(ucdir)

# ! -- DEBUGGING -- ! #
# from pprint import pprint
# pprint(dict(USECASES_FOLDERS))
# ! -- DEBUGGING -- ! #


# ------------------------------------- #
# -- USECASES FROM THE CONTRIBUTIONS -- #
# ------------------------------------- #

def extract_dto(
    flavour: str,
    pdir   : Path
) -> Tuple[Path, Path, Path]:
    flavours_exts = FLAVOURS_SETTINGS[flavour][TAG_EXT]

    dto = {
        n: []
        for n in ['datas', 'output', 'template']
    }

    for pfile in pdir.glob('*'):
        name = pfile.stem

        if(
            not pfile.is_file()
            or
            not name in dto
        ):
            continue

        ext = pfile.suffix[1:] if pfile.suffix else ""

        if name == 'datas':
            if ext != 'json':
                continue

        else:
            keepthis = False

            for gext in flavours_exts:
                if pfile.match(gext):
                    keepthis = True
                    break

            if not keepthis:
                continue

        dto[name].append(pfile)

    for name, pathsfound in dto.items():
        if len(pathsfound) != 1:
            raise Exception(
                f"one file, and only one, can be named ''{name}'': "
                f"{len(pathsfound)} file(s) found. Look at the folder:\n{pdir}"
            )

    return tuple(
        p[0]
        for _, p in dto.items()
    )


def test_contrib_usecases():
    for flavour, usecases in USECASES_FOLDERS.items():
        for ucdir in usecases:
            datas, template, output = extract_dto(flavour, ucdir)

            print(f'--- {flavour} ---')
            print(datas.name)
            print(template.name)
            print(output.name)

test_contrib_usecases()
