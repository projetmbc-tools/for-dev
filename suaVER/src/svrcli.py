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
def svr_CLI(
    config  : str,
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
