#!/usr/bin/env python3

###
# This module implements the [C]-ommand [L]-ine [I]-nterface of ¨jinjang.
###


import click

from .jngbuild import *


# --------- #
# -- CLI -- #
# --------- #

###
# prototype::
#     err : one exception.
#
#     :action: an error message is printed, then the script exits
#              with a ``1`` error.
###
def _exit(err: Exception) -> None:
    print(
f"""
Try 'jinjang --help' for help.

\033[91m\033[1m{type(err).__name__}: {err}\033[0m
""".strip()
    )

    exit(1)


###
# prototype::
#     data     : the path of the file containing the data to feed
#                the template.
#                path::``YAML``, path::``JSON``, and path::``PY``
#                files can be used.
#     template : the path of the template file.
#     output   : the path for the output built by ¨jinjang.
#     unsafe   : same usage as the attribut/parameter ``launch_py``
#                of the method ``jngbuild.JNGBuilder.render``,
#                :see: jngbuild.JNGBuilder.render
#     erase    : :see: jngbuild.JNGBuilder.render
#     flavour  : :see: jngbuild.JNGBuilder.render
#     config   : :see: jngconfig.build_config.render
#     short    : opposite usage of the argument ``verbose`` of
#                the method ``jngbuild.JNGBuilder.render``,
#                :see: jngconfig.build_config.render
#
#     :action: :see: jngbuild.JNGBuilder.render
###
@click.command(
    context_settings = dict(
        help_option_names = ['--help', '-h']
    )
)
@click.argument('data',
                 type = click.Path())
@click.argument('template',
                 type = click.Path())
@click.argument('output',
                 type = click.Path())
@click.option('--unsafe', '-u',
              is_flag = True,
              default = False,
              help    = '\033[91m\033[1m'
                            '** TO USE WITH A LOT OF CAUTION! ** '
                        '\033[0m'
                        'This flag allows Python file to build data: use '
                        'a dictionary named ``JNGDATA`` for the Jinja '
                        'variables and their value. ')
@click.option('--erase', '-e',
              is_flag = True,
              default = False,
              help    = '\033[91m\033[1m'
                            '** TO USE WITH A LOT OF CAUTION! ** '
                        '\033[0m'
                        'This flag allows the erasing of the output file '
                        'if it already exists.')
@click.option('--flavour', '-f',
              default = AUTO_FLAVOUR,
              help    = "A flavour to use if you don't want to let "
                        'jinjaNG detect automatically the dialect '
                        'of the template. '
                        'Possible values: '
                      + ', '.join(ALL_FLAVOURS[:-1])
                      + f', or {ALL_FLAVOURS[-1]}'
                      + '.')
@click.option('--config', '-c',
              default = NO_CONFIG,
              help    = '\033[91m\033[1m'
                            '** TO USE WITH A LOT OF CAUTION! ** '
                        '\033[0m'
                        'The value ``auto`` authorizes jinjaNG to use '
                        'a ``cfg.jng.yaml`` file detected automatically '
                        'relatively to the parent folder of the template. '
                        'You can also indicate the path of a specific '
                        'YAML configuration file.')
@click.option('--short', '-s',
              is_flag = True,
              default = False,
              help    = "This flag asks to hide the output of user's "
                        "commands runned by jinjaNG.")
def jng_CLI(
    data    : str,
    template: str,
    output  : str,
    unsafe  : bool,
    erase   : bool,
    flavour : str,
    config  : str,
    short   : bool,
) -> None:
    """
    Produce a file by filling in a Jinja template.

    DATA: the path of the file containing the data.

    TEMPLATE: the path of the template.

    OUTPUT: the path of the output built by jinjaNG.
    """
# Unsafe mode used?
    if unsafe:
        print(
            '\033[91m\033[1m'
                'WARNING! Using a Python file can be dangerous.'
            '\033[0m'
        )

# Internal tag for auto config.
    if config == 'auto':
        config = AUTO_CONFIG

# Lets' work...
    mybuilder = JNGBuilder(
        flavour   = flavour,
        erase     = erase,
        launch_py = unsafe,
        config    = config,
        verbose   = not short
    )

    try:
        mybuilder.render(
            data     = data,
            template = template,
            output   = output
        )

        print(
             'File successfully built:'
             '\n'
            f'  + {output}'
        )

    except Exception as e:
        _exit(e)
