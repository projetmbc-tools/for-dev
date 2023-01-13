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

MY_BUILDER = JNGBuilder(
    launch_py = True
)


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR = Path(__file__).parent

DOC_CONTENT_DIR, DOCEXA_TOTEST = build_docexas_data(
    docexa_yaml = THIS_DIR / 'docexa.yaml'
)


# -------------------------------------- #
# -- DOC. EXAMPLES - NON-STRICT TESTS -- #
# -------------------------------------- #

def test_doc_examples_strpath_NON_STRICT():
    for subdir, data, template in DOCEXA_TOTEST:
        subdir   = DOC_CONTENT_DIR / subdir
        data     = subdir / data
        template = subdir / Path(template)

        output_wanted = minimize_content(
            subdir / f"output{template.suffix}"
        )

        output_found = minimize_content(
            build_output_strpath(
                MY_BUILDER,
                data,
                template
            )
        )

        assert output_wanted == output_found, message(template)

        remove_output_found(subdir, template)


# ---------------------------------- #
# -- DOC. EXAMPLES - STRICT TESTS -- #
# ---------------------------------- #

def test_doc_examples_strpath_STRICT():
    for subdir, data, template in DOCEXA_TOTEST:
        subdir   = DOC_CONTENT_DIR / subdir
        data     = subdir / data
        template = subdir / Path(template)

        output_wanted = content(
            subdir / f"output{template.suffix}"
        )

        output_found = content(
            build_output_strpath(
                MY_BUILDER,
                data,
                template
            )
        )

        assert output_wanted == output_found, message(template)

        remove_output_found(subdir, template)
