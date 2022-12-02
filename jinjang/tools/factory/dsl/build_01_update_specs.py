#!/usr/bin/env python3

from btools.B01 import *


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

THIS_FILE_REL_SRC_PATH    = Path(__file__) - PROJECT_DIR
THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR


SPECS_SRC_FILE = PROJECT_DIR / 'src' / 'config' / 'flavour.py'

CONTRIB_DSL_DIR   = PROJECT_DIR / 'contribute' / 'api' / 'dsl'
SPECS_STATUS_YAML = THIS_DIR / 'validated.yaml'

EXTRA_TOOLS_DIR = PROJECT_DIR / 'jng-extra-tools'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


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


# ------------------------ #
# -- THE SPECS ACCEPTED -- #
# ------------------------ #

final_pycode = []
ALL_FLAVOURS = []
ALL_TOOLS    = []
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

    if options[TAG_TOOLS]:
        print(f"{TAB_2}+ Referencing new tools.")

        ALL_TOOLS.append(flavour)


# -------------------- #
# -- UPDATE PYFILES -- #
# -------------------- #

print(f"{TAB_1}* Updating the source code.")


ALL_FLAVOURS = [
    f"(TAG_FLAVOUR_{flvr.upper()}:= '{flvr}'),"
    for flvr in ALL_FLAVOURS
]


ALL_TAGS = []

final_pycode = '\n'.join(final_pycode)

myglobals = globals().copy()

for name, val in myglobals.items():
    if not name.startswith('TAG_'):
        continue

    pykey = f"'{val}':"

    if pykey in final_pycode:
        ALL_TAGS.append(
            f"({name}:= '{val}'),"
        )

        final_pycode = final_pycode.replace(pykey, f'{name}:')

ALL_TAGS.sort()


final_pycode = f"""
# Lines automatically build by the following file.
#
#     + ``{THIS_FILE_REL_SRC_PATH}``

SETTINGS = dict()


# -------------- #
# -- ALL TAGS -- #
# -------------- #

ALL_TAGS = {ALL_TAGS}


# ------------------ #
# -- ALL FLAVOURS -- #
# ------------------ #

ALL_FLAVOURS = {ALL_FLAVOURS}

{final_pycode}
""".lstrip()

final_pycode = black.format_file_contents(
    final_pycode,
    fast = False,
    mode = black.FileMode()
).strip()

for old, new in [
    ('"(TAG_', '(TAG_'),
    ('),"', ')'),
]:
    final_pycode = final_pycode.replace(old, new)

with SPECS_SRC_FILE.open(
    encoding = 'utf8',
    mode     = 'w'
) as f:
    f.write(final_pycode)


# ------------------ #
# -- UPDATE TOOLS -- #
# ------------------ #

if ALL_TOOLS:
    print(f"{TAB_1}* Updating the tools.")

    for flavour in ALL_TOOLS:
        tools_files = [
            p
            for p in (CONTRIB_DSL_DIR / flavour).glob("*")
            if p.stem.lower() == "tools"
        ]

        for path in tools_files:
            if path.ext != 'md':
                toolsname      = f'jng{flavour}'
                toolsname_long = f'{toolsname}.{path.ext}'
                break

        for path in tools_files:
            if path.stem.islower():
                dest = f'{toolsname}.{path.ext}'

            else:
                dest = 'README.md'

            dest = EXTRA_TOOLS_DIR / flavour / dest

            path.copy_to(
                dest,
                safemode = False
            )

            if dest.ext == 'md':
                content = dest.read_text(encoding = 'utf-8')

                for old, new in [
                    (README_TOOLS     , toolsname     ),
                    (README_TOOLS_LONG, toolsname_long),
                ]:
                    content = content.replace(old, new)

                dest.write_text(
                    data     = content,
                    encoding = 'utf-8')


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
