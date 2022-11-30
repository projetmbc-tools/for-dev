#!/usr/bin/env python3

import                  black
from collections import defaultdict
from yaml        import (
    safe_load as yaml_load,
    dump      as yaml_dump
)

from mistool.os_use import PPath as Path


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'jinjaNG'):
   PROJECT_DIR = PROJECT_DIR.parent

THIS_FILE_REL_SRC_PATH = Path(__file__) - PROJECT_DIR

THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR


SPECS_SRC_FILE = PROJECT_DIR / 'src' / 'config' / 'flavour.py'

CONTRIB_DSL_DIR   = PROJECT_DIR / 'contribute' / 'api' / 'dsl'
SPECS_STATUS_YAML = THIS_DIR / 'validated.yaml'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


DEFAULT_STATUS_CONTENT = {
    "status" : 'on hold',
    "comment": (
        'Specs on hold.'
        ' '
        'The author of jinjaNG will contact you later.'
    )
}


# ----------------------- #
# -- THE SPECS DEFINED -- #
# ----------------------- #

if not SPECS_STATUS_YAML.is_file():
    SPECS_STATUS_YAML.touch()


allspecs = {}

for specfile in CONTRIB_DSL_DIR.rglob("*/*specs.yaml"):
    specdir = specfile.parent
    flavour    = specdir.name

    specstatus_yaml = specdir / "status.yaml"

    if not specstatus_yaml.is_file():
        specstatus_yaml.touch()

        with specstatus_yaml.open(
            mode     = "w",
            encoding = "utf-8"
        ) as f:
            yaml_dump(DEFAULT_STATUS_CONTENT, f)

    with specstatus_yaml.open(
        mode     = "r",
        encoding = "utf-8"
    ) as f:
        allspecs[flavour] = {
            'dir'   : specdir,
            'status': yaml_load(f)['status'],
        }


# ---------------------- #
# -- TOOLS FOR SOURCE -- #
# ---------------------- #

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
    (TAG_ABOUT := 'about'): [
        TAG_AUTHOR:= 'author',
        TAG_DESC  := 'desc',
        TAG_DATE  := 'date',
    ],
    (TAG_SRC_COMMENT:= 'src-comment'): [
        TAG_BLOCK := 'block',
        TAG_INLINE:= 'inline',
    ],
    None: [
        TAG_EXT  := 'ext',
        TAG_VAR  := 'var',
        # TAG_PARAM:= 'param',
    ]
}


TAG_1ST_NAME  = '1st name'
TAG_LAST_NAME = 'last name'
TAG_EMAIL     = 'email'


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
        TAG_EXT      : [f"*.{p}" for p in options[TAG_EXT]],
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
        settings[TAG_INLINE_COMMENT] = options[TAG_INLINE] + SPECHAR_COMMENT
        settings[TAG_INLINE_INSTR]   = options[TAG_INLINE] + SPECHAR_INSTR

    if TAG_BLOCK in options:
        block_start, block_end = options[TAG_BLOCK]

        if not TAG_INLINE in options:
            settings[TAG_INLINE_COMMENT] = None
            settings[TAG_INLINE_INSTR]   = None

    else:
        block_start = block_end = options[TAG_INLINE] + options[TAG_INLINE][-1]

    settings[TAG_BLOCK_COMMENT_START] = block_start + SPECHAR_COMMENT
    settings[TAG_BLOCK_COMMENT_END]   = SPECHAR_COMMENT + block_end

    settings[TAG_BLOCK_INSTR_START] = block_start + SPECHAR_INSTR
    settings[TAG_BLOCK_INSTR_END]   = SPECHAR_INSTR + block_end

    return settings


def build_src(name, options):
    date   = options[TAG_DATE]
    author = options[TAG_AUTHOR]
    author = (
          author[TAG_1ST_NAME]
        + " " +
          author[TAG_LAST_NAME]
    )

    about = f"""
# -- {name.upper()} -- #
#
# Use -> {options[TAG_DESC]}
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


# ------------------- #
# -- TOOLS FOR DOC -- #
# ------------------- #

def update_doc(hardspec):
    print('DOC >',hardspec)


# ------------------------ #
# -- THE SPECS ACCEPTED -- #
# ------------------------ #

final_pycode = []
ALL_FLAVOURS = []
not_ok       = defaultdict(list)

for flavour in sorted(allspecs):
    infos = allspecs[flavour]

    if infos['status'] != 'ok':
        not_ok[infos['status']].append(flavour)

        continue

    print(f"{TAB_1}* {flavour}.")

    ALL_FLAVOURS.append(flavour)

    specdir = infos['dir']

    with (specdir / 'specs.yaml').open(
        mode     = "r",
        encoding = "utf-8"
    ) as f:
        hardspec = yaml_load(f)


    print(f"{TAB_2}+ Analyzing the hard specs.")

    options = specs2options(hardspec)

    print(f"{TAB_2}+ Building the source code.")

    final_pycode += [
        '',
        build_src(flavour, options),
    ]

    print(f"{TAB_2}+ Building the doc.")

    update_doc(options)


# -------------------- #
# -- UPDATE PYFILES -- #
# -------------------- #

print(f"{TAB_1}* Updating the source code.")


ALL_FLAVOURS = [
    f"(TAG_FLAVOUR_{flvr.upper()}:= '{flvr}'),"
    for flvr in ALL_FLAVOURS
]


final_pycode = '\n'.join(final_pycode)
final_pycode = f"""
# Lines automatically build by the following file.
#
#     + ``{THIS_FILE_REL_SRC_PATH}``

SETTINGS = dict()


# -- ALL FLAVOURS -- #

ALL_FLAVOURS = {ALL_FLAVOURS}

{final_pycode}
""".lstrip()

final_pycode = black.format_file_contents(
    final_pycode,
    fast = False,
    mode = black.FileMode()
).strip()

for old, new in [
    ('"(TAG_FLAVOUR', '(TAG_FLAVOUR'),
    ('),"', ')'),
]:
    final_pycode = final_pycode.replace(old, new)

with SPECS_SRC_FILE.open(
    encoding = 'utf8',
    mode     = 'w'
) as f:
    f.write(final_pycode)


# ------------------ #
# -- SPECS NOT OK -- #
# ------------------ #

if not_ok:
    print(f"{TAB_1}* Specs not accepted.")

    for kind in sorted(not_ok):
        print(f"{TAB_2}+ Specs tagged ''{kind}''.")

        flavours = sorted(not_ok[kind])
        flavours = ' , '.join(flavours)

        print(f"{TAB_3}--> {flavours}")
