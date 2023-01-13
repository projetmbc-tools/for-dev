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

HOOKS_DATA = build_tests_data(
    data_dir = THIS_DIR / 'hooks'
)


# ---------------------------------------- #
# -- USECASES (CONTRIB.) - STRICT TESTS -- #
# ---------------------------------------- #

def test_CLI_hooks_STRICT_slow():
    runner = CliRunner()

    for data, template, output in HOOKS_DATA:
        output_found = template.parent / f"output_found{template.suffix}"
        whatwewant   = what_we_want(data, template, output_found)

        result = runner.invoke(
            cli              = jng_CLI,
            catch_exceptions = False,
            args             = [
                 '--config', 'auto',
                f'{data}',
                f'{template}',
                f'{output_found}',
            ]
        )

        assert result.exit_code == 0, message(template, result.output)

        output_wanted = content(output)
        output_found  = content(output_found)

        assert output_wanted == output_found, message(template, result.output)

        for p in whatwewant['files']:
            p = Path(p)

            assert p.is_file(), message(
                template,
                f"\nMissing expected file:\n+ {p}"
            )

        remove_output_found(template.parent, Path(template.name))
        remove_xtra_hooks  (whatwewant)
