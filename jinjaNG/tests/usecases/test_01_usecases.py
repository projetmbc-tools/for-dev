#!/usr/bin/env python3

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

USECASES_DATAS = build_usecases_datas(
    datas_dir = THIS_DIR / 'datas'
)


# ----------- #
# -- TOOLS -- #
# ----------- #

def message(template):
    return (
         "\n"
        f"See: {template.parent.name}/{template.name}"
         "\n"
    )


# -------------------------------------------- #
# -- USECASES (CONTRIB.) - NON-STRICT TESTS -- #
# -------------------------------------------- #

def test_contrib_usecases_NON_STRICT():
    for _, _, datas, template, output in USECASES_DATAS:
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

def test_contrib_usecases_STRICT():
    for _, _, datas, template, output in USECASES_DATAS:
        output_wanted = content(output)
        output_found  = content(
            build_output(
                MY_BUILDER,
                datas,
                template
            )
        )

        assert output_wanted == output_found, message(template)
