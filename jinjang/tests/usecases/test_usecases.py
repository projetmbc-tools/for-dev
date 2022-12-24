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

AUTO_FROM_EXT = config.flavour.AUTO_FROM_EXT


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


# -------------------- #
# -- USECASES DATAS -- #
# -------------------- #

def extract_dto(pdir: Path) -> Tuple[Path, Path, Path]:
    dto = {
        n: []
        for n in ['datas', 'template', 'output']
    }

    for pfile in pdir.glob('*'):
        dto[pfile.stem].append(pfile)

    for name, pathsfound in dto.items():
        if len(pathsfound) != 1:
            nbpaths = len(pathsfound)

            howmany = 'no' if nbpaths == 0 else nbpaths
            plural  = ''   if nbpaths == 0 else 's'

            raise Exception(
                f"one file, and only one, can be named ''{name}'': "
                f"{howmany} file{plural} found. Look at the folder:\n{pdir}"
            )

    return tuple(
        p[0]
        for _, p in dto.items()
    )


USECASES_DATAS = []

for flavour, usecases in USECASES_FOLDERS.items():
    for ucdir in usecases:
        jngdatas, template, output = extract_dto(ucdir)
        test_name               = ucdir.name

        USECASES_DATAS.append(
            (
                flavour,
                test_name,
                jngdatas,
                template,
                output
            )
        )


# -------------------------------------------- #
# -- USECASES (CONTRIB.) - NON-STRICT TESTS -- #
# -------------------------------------------- #

# The lines are stripped to the right, and
# empty lines are ignored.

def test_contrib_usecases_non_strict():
    for flavour, test_name, datas, template, output in USECASES_DATAS:
        output_wanted = [
            lstripped
            for l in output.read_text(encoding = 'utf-8').split('\n')
            if (lstripped:= l.rstrip())
        ]
        print(f'--- {flavour}:{test_name} ---')
        print(output_wanted)

        # output_found

test_contrib_usecases_non_strict()

exit()


# ---------------------------------------- #
# -- USECASES (CONTRIB.) - STRICT TESTS -- #
# ---------------------------------------- #

# Verbatim equivalences of the contents.

def test_contrib_usecases_strict():
    for flavour, test_name, datas, template, output in USECASES_DATAS:
        output_wanted = output.read_text(encoding = 'utf-8').split('\n')
        print(f'--- {flavour}:{test_name} ---')
        print(output_wanted)

        # output_found

test_contrib_usecases_strict()
