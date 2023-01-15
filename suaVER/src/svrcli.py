#!/usr/bin/env python3

###
# This module implements the [C]-ommand [L]-ine [I]-nterface of ¨suaver.
###


import click



# --------- #
# -- CLI -- #
# --------- #

###
# prototype::
#     message : this text is to indicate one error.
#
#     :action: an error message is printed, then the script exits
#              with a ``1`` error.
###
def _exit(message: str) -> None:
    print(
f"""
Try 'suaver --help' for help.

Error: {message}
""".strip()
    )

    exit(1)


###
# prototype::
#     XXXX : ????
#
#     :action: ????
###
@click.command(
    context_settings = dict(
        help_option_names = ['--help', '-h']
    )
)
@click.argument('config',
                 type = click.Path())
@click.option('--unsafe', '-u',
              is_flag = True,
              default = False,
              help    = '\033[91m\033[1m'
                            '** TO USE WITH A LOT OF CAUTION! ** '
                        '\033[0m'
                        'This flag allows ????')
def svr_CLI(
    config: str,
    unsafe: bool,
) -> None:
    """
    ???

    CONFIG: the path of the YAML file ???
    """
# Unsafe mode used?
    ...

    try:
        ...

    except Exception as e:
        _exit(repr(e))
