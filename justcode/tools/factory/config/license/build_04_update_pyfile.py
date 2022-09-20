#!/usr/bin/env python3

from json import load

from mistool.os_use import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR

LICENSE_DIR       = PROJECT_DIR / 'src' / 'config' / 'license'
LICENSE_DATAS_DIR = LICENSE_DIR / 'datas'
PYFILE            = LICENSE_DIR / 'license.py'


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


# --------------------------- #
# -- UPDATE ``licence.py`` -- #
# --------------------------- #

print(f"{TAB_1}* Preparing the code of ``licence.py``.")

code = []

allpaths = [p for p in LICENSE_DATAS_DIR.walk("file::**.txt")]
allpaths.sort()

for p in allpaths:
    lic_filename  = p.stem
    lic_file_JSON = p.parent / f"{lic_filename}.json"

    with lic_file_JSON.open(
        encoding = 'utf8',
        mode     = 'r',
    ) as jsfile:
        infos = load(jsfile)

    lic_ID  = infos['shortid'].lower()
    lic_TAG = lic_filename.replace('-', '_')

    if infos['urls']['official'] is None:
        url = infos['urls']['content']

    else:
        url = infos['urls']['official']

    code += [
        f"# {infos['fullname']}",
        f"#     + See: {url}",
        " "*4 + f'TAG_LICENSE_{lic_TAG} := "{lic_ID}",',
    ]



code = '\n'.join(code)


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

# ALL THE TAGS

ALL_LICENSES = [
{code}
]
        """.strip()
        +
        '\n'
    )


print(f"{TAB_1}* ``licence.py`` updated.")
