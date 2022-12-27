#!/usr/bin/env python3

###
# This module implements a Comand Line Interface.
###

import click

from .jngbuild import *


# --------- #
# -- CLI -- #
# --------- #

###
# prototype::
#     message : ????
#
#     :action: YYY
###
def _exit(message: str) -> None:
    print(
f"""
Try 'python -m jinjang --help' for help.

Error: {message}
""".strip()
    )

    exit(1)

###
# prototype::
#     datas    :
#     template :
#     output   :
#     dto      :
#     pydto    :
#     fl       :
#     cfg      :
#
#     :action: YYY
###
@click.command()
@click.argument('datas')
@click.argument('template')
@click.argument('output')
@click.option('--dto',
              is_flag = True,
              default = False,
              help    = "This flag is mandatory if ``--pydto`` is not used. "
                        'It is to work with JSON or YAML datas. ')
@click.option('--pydto',
              is_flag = True,
              default = False,
              help    = 'TO USE WITH A LOT OF CAUTION! '
                        "This flag is mandatory if ``--dto`` is not used. "
                        'It is to use datas from a Python file: '
                        'use a dictionary named ``JNG_DATAS`` for '
                        'the Jinja variables and their value. ')
@click.option('--fl',
              default = AUTO_FLAVOUR,
              help    = "A flavour to use if you don't want to let "
                        'jinjaNG detect automatically the dialect '
                        'of the template. '
                        'Possible values: '
                        + ', '.join(ALL_FLAVOURS[:-1])
                        + f', or {ALL_FLAVOURS[-1]}'
                        + '.')
@click.option('--cfg',
              default = '',
              help    = 'COMING SOON...      '
                        'TO USE WITH A LOT OF CAUTION! '
                        'The value ``auto`` authorizes jinjaNG to use a ``cfg.jng.yaml`` file, if it exists. You can also indicate the path of a specific YAML configuration file.')
def jngcli(
    datas   : str,
    template: str,
    output  : str,
    dto     : bool,
    pydto   : bool,
    fl      : str,
    cfg     : str,
) -> None:
    """
    Produce a file by filling in a Jinja template.

    DATAS: the path of the file containing the datas.

    TEMPLATE: the path of the template.

    OUTPUT: the path of the output built by jinjaNG.
    """
# DTO or PYDTO?
    if(
        not(dto or pydto)
        or
        (dto and pydto)
    ):
        _exit("You must used either ``--dto``, or ``--pydto``.")

    if pydto:
        print('WARNING: Using a Python file can be dangerous.')

# Lets' work...
    mybuilder = JNGBuilder(
        pydatas = pydto
    )

    try:
        mybuilder.render(
            datas    = Path(datas),
            template = Path(template),
            output   = Path(output)
        )

        print(f'File {output} has been built.')

    except Exception as e:
        _exit(repr(e))


# -------------------------------------------- #
# --- Entry point for ``python -m jinjang`` -- #
# -------------------------------------------- #

jngcli()
