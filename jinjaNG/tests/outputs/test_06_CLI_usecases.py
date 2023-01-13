#!/usr/bin/env python3

import click
from click.testing import CliRunner

from common import *


# -------------------- #
# -- PACKAGE TESTED -- #
# -------------------- #

addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src.jngcli import jng_CLI


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR = Path(__file__).parent

USECASES_DATA = build_tests_data(
    data_dir = THIS_DIR / 'usecases'
)


# ---------------------------------------- #
# -- USECASES (CONTRIB.) - STRICT TESTS -- #
# ---------------------------------------- #

def test_CLI_contrib_usecases_STRICT():
    runner = CliRunner()

    for data, template, output in USECASES_DATA:
        output_found = template.parent / f"output_found{output.suffix}"

        result = runner.invoke(
            cli              = jng_CLI,
            catch_exceptions = False,
            args             = [
                f'{data}',
                f'{template}',
                f'{output_found}',
            ]
        )

        assert result.exit_code == 0, message(template, result.output)

        output_wanted = content(output)
        output_found  = content(output_found)

        assert output_wanted == output_found, message(template)

        remove_output_found(template.parent, Path(template.name))
