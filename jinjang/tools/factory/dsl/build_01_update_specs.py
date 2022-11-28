#!/usr/bin/env python3

from mistool.os_use import PPath as Path
from yaml import (
    safe_load as yaml_load,
    dump      as yaml_dump
)

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


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR


SPECS_SRC_DIR  = PROJECT_DIR / 'src' / 'config' / 'flavour'
SPECS_SRC_FILE = SPECS_SRC_DIR / 'specs.py'

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
    name    = specdir.name

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
        allspecs[name] = {
            'dir'   : specdir,
            'status': yaml_load(f)['status'],
        }


# ---------------------- #
# -- TOOLS FOR SOURCE -- #
# ---------------------- #

SPECHARS = {
    (TAG_INSTR  := 'instruction'): ':',
    (TAG_COMMENT:= 'comment'    ): '_',
}


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

def update_src(options):
    print('SRC - OPTIONS >',options)

    exit()


# ------------------- #
# -- TOOLS FOR DOC -- #
# ------------------- #

def update_doc(hardspec):
    print('DOC >',hardspec)


# ------------------------ #
# -- THE SPECS ACCEPTED -- #
# ------------------------ #

for name, infos in allspecs.items():
    print(f"{TAB_1}* {name}.")

    if infos['status'] != 'ok':
        print(f"{TAB_2}+ {infos['status'].title()}.")

        continue

    specdir = infos['dir']

    with (specdir / 'specs.yaml').open(
        mode     = "r",
        encoding = "utf-8"
    ) as f:
        hardspec = yaml_load(f)


    print(f"{TAB_2}+ Analyzing the hard specs.")

    options = specs2options(hardspec)

    print(f"{TAB_2}+ Updating the source code.")

    update_src(options)

    print(f"{TAB_2}+ Updating the doc.")

    update_doc(options)
