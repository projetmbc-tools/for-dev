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
#     message : this text indicates one error.
#
#     :action: an error message is printed, then the script exits
#              with a ``1`` error.
###
def _exit(message):
    print(
f"""
Try 'python -m jinjang --help' for help.

Error: {message}
""".strip()
    )

    exit(1)


###
# prototype::
#     data     : the file containing the data to feed the template.
#                path::``YAML``, path::``JSON``, and path::``PY``
#                files can be used.
#     template : the template file.
#     output   : the path for the output built by ¨jinjaNG.
#     unsafe   : only the value ``True`` allows to launch
#                a path::``PY`` file to build data.
#     fl       : this indicates either to use the automatic
#                detection of the flavour if ``fl = AUTO_FLAVOUR``,
#                or the flavour of the template.
#     cfg      : COMING SOON...
#
#     :action: the ``output`` file is constructed using the data
#              and template while applying any parameters specified.
###
@click.command()
@click.argument('data')
@click.argument('template')
@click.argument('output')
@click.option('--unsafe', '-u',
              is_flag = True,
              default = False,
              help    = 'TO USE WITH A LOT OF CAUTION! '
                        'This flag allows to use data from a Python '
                        'file to launch: use a dictionary named '
                        '``JNGDATA`` for the Jinja variables and '
                        'their value. ')
@click.option('--fl', '-f',
              default = AUTO_FLAVOUR,
              help    = "A flavour to use if you don't want to let "
                        'jinjaNG detect automatically the dialect '
                        'of the template. '
                        'Possible values: '
                        + ', '.join(ALL_FLAVOURS[:-1])
                        + f', or {ALL_FLAVOURS[-1]}'
                        + '.')
@click.option('--cfg', '-c',
              default = '',
              help    = 'COMING SOON... '
                        'TO USE WITH A LOT OF CAUTION! '
                        'The value ``auto`` authorizes jinjaNG to use '
                        'a ``cfg.jng.yaml`` file, if it exists. '
                        'You can also indicate the path of a specific '
                        'YAML configuration file.')
def jng_CLI(
    data    : str,
    template: str,
    output  : str,
    unsafe  : bool,
    fl      : str,
    cfg     : str,
) -> None:
    """
    Produce a file by filling in a Jinja template.

    DATA: the path of the file containing the data.

    TEMPLATE: the path of the template.

    OUTPUT: the path of the output built by jinjaNG.
    """
# Unsafe mode used?
    if unsafe:
        print('WARNING! Using a Python file can be dangerous.')

# Lets' work...
    mybuilder = JNGBuilder(
        flavour   = fl,
        launch_py = unsafe,
        # config    = cfg
    )

    try:
        mybuilder.render(
            data     = Path(data),
            template = Path(template),
            output   = Path(output)
        )

        print(
             'File successfully built:'
             '\n'
            f'  + {output}'
        )

    except Exception as e:
        _exit(repr(e))


# -------------------------------------------- #
# --- Entry point for ``python -m jinjang`` -- #
# -------------------------------------------- #

jng_CLI()
