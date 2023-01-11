#!/usr/bin/env python3

import              os
from pathlib import Path

import click
from click.testing import CliRunner

from cbdevtools.addfindsrc import addfindsrc

# ! -- DEBUGGING -- ! #
# Clear the terminal.
# print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

JINJANG_DIR = addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src.jngcli import jng_CLI

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

DATA_TESTS = THIS_DIR / 'data'

data     = DATA_TESTS / 'post' / '01-latex' / 'data.json'
template = DATA_TESTS / 'post' / '01-latex' / 'template.tex'
output   = DATA_TESTS / 'post' / '01-latex' / 'output_found.tex'


def test_CLI_hooks():
    print(template.is_file())
    runner = CliRunner()
    result = runner.invoke(
        cli = jng_CLI,
        args =
        [
            f'"{data}"',
            f'"{template}"',
            f'"{output}"',
        ]
    )

    assert result.exit_code == 0, result.output
