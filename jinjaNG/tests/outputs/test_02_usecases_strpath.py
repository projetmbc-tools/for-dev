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

USECASES_DATA = build_tests_data(
    data_dir = THIS_DIR / 'usecases'
)


# -------------------------------------------- #
# -- USECASES (CONTRIB.) - NON-STRICT TESTS -- #
# -------------------------------------------- #

def test_contrib_usecases_strpath_NON_STRICT():
    for data, template, output in USECASES_DATA:
        output_wanted = minimize_content(output)
        output_found  = minimize_content(
            build_output_strpath(
                MY_BUILDER,
                data,
                template
            )
        )

        assert output_wanted == output_found, message(template)

        remove_output_found(template.parent, Path(template.name))


# ---------------------------------------- #
# -- USECASES (CONTRIB.) - STRICT TESTS -- #
# ---------------------------------------- #

def test_contrib_usecases_strpath_STRICT():
    for data, template, output in USECASES_DATA:
        output_wanted = content(output)
        output_found  = content(
            build_output_strpath(
                MY_BUILDER,
                data,
                template
            )
        )

        assert output_wanted == output_found, message(template)

        remove_output_found(template.parent, Path(template.name))
