#!/usr/bin/env python3

from pathlib import Path
from yaml    import safe_load as yaml_load

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

MY_BUILDER = JNGBuilder(
    pydatas = True
)


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR = Path(__file__).parent

TO_TEST_YAML = THIS_DIR / 'docexa.yaml'


with TO_TEST_YAML.open(
    encoding = 'utf-8',
    mode     = 'r'
) as f:
    DOCEXA_TOTEST = yaml_load(f)

DOC_CONTENT_DIR = Path(DOCEXA_TOTEST['docdir'])
DOCEXA_TOTEST   = DOCEXA_TOTEST['totest']


# ----------- #
# -- TOOLS -- #
# ----------- #

def remove_output_found(subdir, template):
    (subdir / f"output_found{template.suffix}").unlink()


def message(subdir, datas, template):
    return (
        "\n"
        f"See: {datas} and "
        f"{subdir.relative_to(DOC_CONTENT_DIR)}/{template.name}"
        "\n"
    )


# -------------------------------------- #
# -- DOC. EXAMPLES - NON-STRICT TESTS -- #
# -------------------------------------- #

def test_doc_examples_non_strict():
    for subdir, datas, template in DOCEXA_TOTEST:
        subdir   = DOC_CONTENT_DIR / subdir
        template = Path(template)

        output_wanted = minimize_content(
            subdir / f"output{template.suffix}"
        )

        output_found  = minimize_content(
            build_output(
                MY_BUILDER,
                subdir / datas,
                subdir / template
            )
        )

        assert output_wanted == output_found, message(subdir, datas, template)

        remove_output_found(subdir, template)


# ---------------------------------- #
# -- DOC. EXAMPLES - STRICT TESTS -- #
# ---------------------------------- #

def test_doc_examples_strict():
    for subdir, datas, template in DOCEXA_TOTEST:
        subdir   = DOC_CONTENT_DIR / subdir
        template = Path(template)

        output_wanted = content(
            subdir / f"output{template.suffix}"
        )

        output_found  = content(
            build_output(
                MY_BUILDER,
                subdir / datas,
                subdir / template
            )
        )

        assert output_wanted == output_found, message(subdir, datas, template)

        remove_output_found(subdir, template)
