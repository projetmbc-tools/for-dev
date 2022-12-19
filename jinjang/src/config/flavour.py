# Lines automatically build by the following file.
#
#     + ``tools/factory/dsl/build_01_update_specs.py``

SETTINGS = dict()


# -------------- #
# -- ALL TAGS -- #
# -------------- #

ALL_TAGS = [
    (TAG_BLOCK_COMMENT_END:= 'comment_end_string'),
    (TAG_BLOCK_COMMENT_START:= 'comment_start_string'),
    (TAG_BLOCK_INSTR_END:= 'block_end_string'),
    (TAG_BLOCK_INSTR_START:= 'block_start_string'),
    (TAG_EXT:= 'ext'),
    (TAG_INLINE_COMMENT:= 'line_comment_prefix'),
    (TAG_INLINE_INSTR:= 'line_statement_prefix'),
    (TAG_JINJA:= 'jinja2'),
    (TAG_TOOLS:= 'tools'),
    (TAG_VAR_END:= 'variable_end_string'),
    (TAG_VAR_START:= 'variable_start_string'),
]


# ------------------ #
# -- ALL FLAVOURS -- #
# ------------------ #

ALL_FLAVOURS = [
    (FLAVOUR_ASCII:= 'ascii'),
    (FLAVOUR_HTML:= 'html'),
    (FLAVOUR_LATEX:= 'latex'),
]


# ----------- #
# -- ASCII -- #
# ----------- #
#
# Generic behaviour of `jinjaNG`.
#
# Last change: 2022-11-28
# Author     : Christophe Bal

SETTINGS[FLAVOUR_ASCII] = {
    TAG_TOOLS: False,
    TAG_EXT: ["*"],
    TAG_JINJA: {
        TAG_VAR_START: "{{",
        TAG_VAR_END: "}}",
        TAG_INLINE_COMMENT: "#_",
        TAG_INLINE_INSTR: "#:",
        TAG_BLOCK_COMMENT_START: "{#_",
        TAG_BLOCK_COMMENT_END: "_#}",
        TAG_BLOCK_INSTR_START: "{#:",
        TAG_BLOCK_INSTR_END: ":#}",
    },
}


# ---------- #
# -- HTML -- #
# ---------- #
#
# Useful settings and tools for HTML templating.
#
# Last change: 2022-12-02
# Author     : Christophe Bal

SETTINGS[FLAVOUR_HTML] = {
    TAG_TOOLS: True,
    TAG_EXT: ["*.html"],
    TAG_JINJA: {
        TAG_VAR_START: "{{",
        TAG_VAR_END: "}}",
        TAG_INLINE_COMMENT: None,
        TAG_INLINE_INSTR: None,
        TAG_BLOCK_COMMENT_START: "<!--_",
        TAG_BLOCK_COMMENT_END: "_-->",
        TAG_BLOCK_INSTR_START: "<!--:",
        TAG_BLOCK_INSTR_END: ":-->",
    },
}


# ----------- #
# -- LATEX -- #
# ----------- #
#
# Useful settings and tools for LaTeX templating.
#
# Last change: 2022-12-01
# Author     : Christophe Bal

SETTINGS[FLAVOUR_LATEX] = {
    TAG_TOOLS: True,
    TAG_EXT: ["*.tex", "*.sty", "*.tkz"],
    TAG_JINJA: {
        TAG_VAR_START: "\\\\JNGVAR{",
        TAG_VAR_END: "}",
        TAG_INLINE_COMMENT: "%_",
        TAG_INLINE_INSTR: "%:",
        TAG_BLOCK_COMMENT_START: "%%_",
        TAG_BLOCK_COMMENT_END: "_%%",
        TAG_BLOCK_INSTR_START: "%%:",
        TAG_BLOCK_INSTR_END: ":%%",
    },
}
