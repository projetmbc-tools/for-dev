#!/usr/bin/env python3

from typing import Tuple

from collections import defaultdict

from cbdevtools.addfindsrc import addfindsrc

from common import *


# -------------------- #
# -- PACKAGE TESTED -- #
# -------------------- #

addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src import *

MY_BUILDER = JNGBuilder()


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR = Path(__file__).parent

DATAS_DIR = THIS_DIR / 'datas'


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


# ----------- #
# -- TOOLS -- #
# ----------- #

def message(template):
    return (
         "\n"
        f"See: {template.parent.name}/{template.name}"
         "\n"
    )

# -------------------- #
# -- USECASES DATAS -- #
# -------------------- #

def extract_dto(pdir: Path) -> Tuple[Path, Path, Path]:
    dto = {
        n: []
        for n in ['datas', 'template', 'output']
    }

    for pfile in pdir.glob('*'):
        name = pfile.stem

        if name in dto:
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

def test_contrib_usecases_non_strict():
    for flavour, test_name, datas, template, output in USECASES_DATAS:
        output_wanted = minimize_content(output)
        output_found  = minimize_content(
            build_output(
                MY_BUILDER,
                datas,
                template
            )
        )

        assert output_wanted == output_found, message(template)


# ---------------------------------------- #
# -- USECASES (CONTRIB.) - STRICT TESTS -- #
# ---------------------------------------- #

def test_contrib_usecases_strict():
    for flavour, test_name, datas, template, output in USECASES_DATAS:
        output_wanted = content(output)
        output_found  = content(
            build_output(
                MY_BUILDER,
                datas,
                template
            )
        )

        assert output_wanted == output_found, message(template)
