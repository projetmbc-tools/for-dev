#!/usr/bin/env python3

from datetime    import date
from collections import defaultdict
from json        import load

import black

from mistool.os_use import PPath as Path

from scraping import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

UPDATE_CREATIVE = UPDATE_OPENSOURCE = True

UPDATE_OPENSOURCE = False # Debug mode.
UPDATE_CREATIVE   = False # Debug mode.


TODAY = date.today()


THIS_FILE = Path(__file__)

PROJECT_DIR = Path(THIS_FILE).parent

while(PROJECT_DIR.name != 'inipro'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR

LICENSE_DIR        = PROJECT_DIR / 'src' / 'config' / 'license'
LICENSE_ONLINE_DIR = LICENSE_DIR / 'online'
PYFILE             = LICENSE_DIR / 'license.py'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ------------------------------------------ #
# -- UPDATES FROM ``creativecommons.org`` -- #
# ------------------------------------------ #

if UPDATE_CREATIVE:
    print(f"{TAB_1}* Licenses on ``creativecommons.org``.")

    myCC = CreativeCommons(
        decotab_1   = f"{TAB_2}+",
        decotab_2   = f"{TAB_3}-",
        license_dir = LICENSE_ONLINE_DIR,
    )
    myCC.build()


# ------------------------------------- #
# -- UPDATES FROM ``opensource.org`` -- #
# ------------------------------------- #

if UPDATE_OPENSOURCE:
    print(f"{TAB_1}* Licenses on ``opensource.org``.")

    myOpenSrc = OpenSource(
        decotab_1   = f"{TAB_2}+",
        decotab_2   = f"{TAB_3}-",
        license_dir = LICENSE_ONLINE_DIR,
    )
    myOpenSrc.build()


# --------------------------- #
# -- UPDATE ``licence.py`` -- #
# --------------------------- #

print(f"{TAB_1}* Updating ``licence.py``.")

exit()
license_found   = set()
license_by_kind = defaultdict(list)

for f in LICENSE_DIR.walk("file::**.txt"):
    if f.ext == 'json':
        continue

    lic_file_TXT_name = f.stem

    kind = f'__{f.parent.name}__'

    assert not lic_file_TXT_name in license_found, \
           (
            f"name ``{lic_file_TXT_name}`` already used somewhere."
             "\n"
            f"See the folder ``{kind.replace('_', '')}``."
           )

    lic_file_JSON = f.parent / f"{lic_file_TXT_name}.json"

    with lic_file_JSON.open(
        encoding = 'utf8',
        mode     = 'r',
    ) as sf:
        specs = load(sf)

    license_found.add(lic_file_TXT_name)

    license_by_kind[kind].append(
        (lic_file_TXT_name, specs)
    )


code_EACH_TAG = []

ALL_LICENSES = []

TAG_ONLINE  = '__online__'
TAG_SPECIAL = '__special__'

ALL_TAGS = [
    TAG_ONLINE,
    TAG_SPECIAL,
]

for kind in ALL_TAGS:
    sortednames = sorted(license_by_kind[kind])

    ALL_LICENSES.append(kind)
    ALL_LICENSES += [n for n, _ in sortednames]

    code_EACH_TAG.append(kind)

    code_EACH_TAG = []

    for (n, hn) in sortednames:
        code_EACH_TAG.append(
            f'TAG_LICENSE_{n.replace("-", "_")} = "{hn}"'
        )

    code_EACH_TAG.append('')


code_ALL_TAGS = f"{ALL_LICENSES = }"

code_ALL_TAGS = black.format_file_contents(
    code_ALL_TAGS,
    fast = False,
    mode = black.FileMode()
)


code_EACH_TAG = '\n'.join(code_EACH_TAG)


for kind in ALL_TAGS:
    ctitle = kind.replace('_', '').title()

    code_ALL_TAGS = code_ALL_TAGS.replace(
        ' '*4 + f'"{kind}",',
        f"# {ctitle}"
    )

    code_EACH_TAG = code_EACH_TAG.replace(
        kind,
        f"# {ctitle}"
    )

for n in ALL_LICENSES:
    code_ALL_TAGS = code_ALL_TAGS.replace(
        f'"{n}"',
        f'TAG_LICENSE_{n.replace("-", "_")}'
    )


with PYFILE.open(
    encoding = 'utf8',
    mode     = 'w',
) as f:
    f.write(
        f"""
#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``{THIS_FILE_REL_PROJECT_DIR}``

# EACH TAG

{code_EACH_TAG}

# ALL THE TAGS

{code_ALL_TAGS}
        """.strip()
        +
        '\n'
    )
