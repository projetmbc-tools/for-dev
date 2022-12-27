#!/usr/bin/env python3

from mistool.os_use import PPath as Path


# ----------- #
# -- TOOLS -- #
# ----------- #

def build_output(
    builder,
    datas,
    template
):
    output_found = template.parent / f"output_found{template.suffix}"

    builder.render(
        datas    = datas,
        template = template,
        output   = output_found
    )

    return output_found


# ------------------------ #
# -- NON-STRICT CONTENT -- #
# ------------------------ #

def minimize_content(path):
    return [
        lstripped
        for l in path.read_text(encoding = 'utf-8').split('\n')
        if (lstripped:= l.rstrip())
    ]


# -------------------- #
# -- STRICT CONTENT -- #
# -------------------- #

# Verbatim equivalences of the contents except for the final empty lines that are striped.

def content(path):
    return path.read_text(encoding = 'utf-8').rstrip().split('\n')
