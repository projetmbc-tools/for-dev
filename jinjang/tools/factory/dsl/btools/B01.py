#!/usr/bin/env python3

import                  black
from collections import defaultdict
from yaml        import (
    safe_load as yaml_load,
    dump      as yaml_dump
)

from mistool.os_use import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

DEFAULT_STATUS_CONTENT = {
    "status" : 'on hold',
    "comment": (
        'Specs on hold.'
        ' '
        'The author of jinjaNG will contact you later.'
    )
}


# ---------------------- #
# -- TOOLS FOR SOURCE -- #
# ---------------------- #

# Placeholders
README_TOOLS      = "<:TOOLS:>"
README_TOOLS_LONG = "<:TOOLS_LONG:>"

# Specilas chars.
SPECHAR_INSTR   = ':'
SPECHAR_COMMENT = '_'

# Vars
TAG_VAR_START = 'variable_start_string'
# Vars
TAG_VAR_START = 'variable_start_string'
TAG_VAR_END   = 'variable_end_string'
# Instructions.
TAG_BLOCK_INSTR_START = 'block_start_string'
TAG_BLOCK_INSTR_END   = 'block_end_string'
TAG_INLINE_INSTR      = 'line_statement_prefix'
# Comments.
TAG_BLOCK_COMMENT_START = 'comment_start_string'
TAG_BLOCK_COMMENT_END   = 'comment_end_string'
TAG_INLINE_COMMENT      = 'line_comment_prefix'


GRP_TAGS = {
    (TAG_ABOUT:= 'about'): [
        TAG_AUTHOR:= 'author',
        TAG_DESC  := 'desc',
        TAG_DATE  := 'date',
        TAG_TOOLS := 'tools',
    ],
    (TAG_SRC_COMMENT:= 'src-comment'): [
        TAG_BLOCK := 'block',
        TAG_INLINE:= 'inline',
    ],
    None: [
        TAG_EXT:= 'ext',
        TAG_VAR:= 'var',
        # TAG_PARAM:= 'param',
    ]
}


TAG_1ST_NAME  = '1st name'
TAG_LAST_NAME = 'last name'
TAG_EMAIL     = 'email'


TAG_JINJA = "jinja2"


def build_authorinfos(text):
    firstname, lastname = text.split(',')
    lastname, email = lastname.split('[')

    email = email.strip()[:-1]

    infos = {
        TAG_1ST_NAME : firstname,
        TAG_LAST_NAME: lastname,
        TAG_EMAIL    : email,
    }

    return {
        k: v.strip()
        for k,v in infos.items()
    }


def build_startend(text):
    start, end = text.split('...')

    return start.strip(), end.strip()


def build_before(text):
    bef, _ = text.split('...')

    return bef.strip()


# # Ici, on change de gestion car on vcréer une regex qui va récupérer just la variable utilisée MYVAR mais aussi tout la commende JNPARAM pour passer à JNVAR(MYVAR) pour la gestion esnsuite par jinja

# def build_paramregex(text):
#     print('TODO >', text)
#     exit()


FORMATERS = {
    TAG_AUTHOR: build_authorinfos,
    TAG_BLOCK : build_startend,
    TAG_INLINE: build_before,
    TAG_VAR   : build_startend,
    # TAG_PARAM : build_paramregex,
}


def specs2options(hardspec):
    options = {}

    for grptag, subtags in GRP_TAGS.items():
        if grptag is None:
            dict2use = hardspec.copy()

        else:
            dict2use = hardspec[grptag]

        for tag, val in dict2use.items():
            if not tag in subtags:
                raise Exception(
                    f"unknown key: {tag}.")

            if tag in FORMATERS:
                val = FORMATERS[tag](val)

            options[tag] = val

            if grptag is None:
                del hardspec[tag]

        if not grptag is None:
            del hardspec[grptag]

    if options.get(TAG_TOOLS, False) == True:
        options[TAG_TOOLS] = True

    else:
        options[TAG_TOOLS] = False

    return options


# ---------------------- #
# -- TOOLS FOR SOURCE -- #
# ---------------------- #

CODE_TEMPL = """
{about}

SETTINGS[TAG_FLAVOUR_{name_up}] = {settings}
""".lstrip()


def build_settings(options):
    if not TAG_VAR in options:
        raise Exception('Missing var...')

    settings = {
        TAG_TOOLS: options[TAG_TOOLS],
        TAG_EXT  : [
            p
            if p == "*" else
            f"*.{p}"
            for p in options[TAG_EXT]
        ],
    }

    forjinja = {
        TAG_VAR_START: options[TAG_VAR][0],
        TAG_VAR_END  : options[TAG_VAR][1],
    }


    if not(
        TAG_BLOCK in options
        or
        TAG_INLINE in options
    ):
        raise Exception('No comment!')

    if TAG_INLINE in options:
        forjinja[TAG_INLINE_COMMENT] = options[TAG_INLINE] + SPECHAR_COMMENT
        forjinja[TAG_INLINE_INSTR]   = options[TAG_INLINE] + SPECHAR_INSTR

    if TAG_BLOCK in options:
        block_start, block_end = options[TAG_BLOCK]

        if not TAG_INLINE in options:
            forjinja[TAG_INLINE_COMMENT] = None
            forjinja[TAG_INLINE_INSTR]   = None

    else:
        block_start = block_end = options[TAG_INLINE] + options[TAG_INLINE][-1]

    forjinja[TAG_BLOCK_COMMENT_START] = block_start + SPECHAR_COMMENT
    forjinja[TAG_BLOCK_COMMENT_END]   = SPECHAR_COMMENT + block_end

    forjinja[TAG_BLOCK_INSTR_START] = block_start + SPECHAR_INSTR
    forjinja[TAG_BLOCK_INSTR_END]   = SPECHAR_INSTR + block_end

    settings[TAG_JINJA] = forjinja

    return settings


def build_src(name, options):
    date   = options[TAG_DATE]
    author = options[TAG_AUTHOR]
    author = (
          author[TAG_1ST_NAME]
        + " " +
          author[TAG_LAST_NAME]
    )

    deco = '-'*(2*3 + len(name))

    about = f"""
# {deco} #
# -- {name.upper()} -- #
# {deco} #
#
# {options[TAG_DESC]}
#
# Last change: {date}
# Author     : {author}
    """.strip()

    pycode = CODE_TEMPL.format(
        name     = name,
        name_up  = name.upper(),
        about    = about,
        settings = build_settings(options),
    )

    return pycode
