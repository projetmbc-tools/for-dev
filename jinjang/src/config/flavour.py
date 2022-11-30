# Lines automatically build by the following file.
#
#     + ``tools/factory/dsl/build_01_update_specs.py``

SETTINGS = dict()


# -- ALL FLAVOURS -- #

ALL_FLAVOURS = [(TAG_FLAVOUR_ASCII:= 'ascii'), (TAG_FLAVOUR_LATEX:= 'latex')]


# -- ASCII -- #
#
# Use -> Generic behaviour of `jinjaNG`.
#
# Last change: 2022-11-28
# Author     : Christophe Bal

SETTINGS[TAG_FLAVOUR_ASCII] = {
    "ext": ["*.*"],
    "variable_start_string": "{{",
    "variable_end_string": "}}",
    "line_comment_prefix": "#_",
    "line_statement_prefix": "#:",
    "comment_start_string": "{#_",
    "comment_end_string": "_#}",
    "block_start_string": "{#:",
    "block_end_string": ":#}",
}


# -- LATEX -- #
#
# Use -> ??? avec une bibliothèque dédiée !!!
#
# Last change: 2022-11-???
# Author     : Christophe Bal

SETTINGS[TAG_FLAVOUR_LATEX] = {
    "ext": ["*.tex", "*.sty", "*.tkz"],
    "variable_start_string": "\\\\JNGVAR{",
    "variable_end_string": "}",
    "line_comment_prefix": "%_",
    "line_statement_prefix": "%:",
    "comment_start_string": "%%_",
    "comment_end_string": "_%%",
    "block_start_string": "%%:",
    "block_end_string": ":%%",
}