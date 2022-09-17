#!/usr/bin/env python3


from datetime            import date

from mistool.os_use import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TODAY = date.today()


THIS_FILE = Path(__file__)

PROJECT_DIR = Path(THIS_FILE).parent

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR

GITIGNORE_DIR       = PROJECT_DIR / 'src' / 'config' / 'gitignore'
GITIGNORE_DATAS_DIR = GITIGNORE_DIR / 'datas'
PYFILE              = GITIGNORE_DIR / 'gitignore.py'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

def pyname(name):
    cname = ""

    for c in name:
        if c in "-+":
            c = "_"

        cname += c

    cname = cname.upper()

    if cname == "C__":
        cname = "CPP"

    elif cname == "TLA_":
        cname = "TLA_PLUS"

    return cname


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ----------------------------- #
# -- UPDATE ``gitignore.py`` -- #
# ----------------------------- #

print(f"{TAB_1}* Preparing the code of ``gitignore.py``.")

code = []

allpaths = [p for p in GITIGNORE_DATAS_DIR.walk("file::**.txt")]
allpaths.sort()

for p in allpaths:
    lic_filename  = p.stem

    lic_ID  = lic_filename.lower()
    lic_TAG = pyname(lic_filename)

    code.append(
        " "*4 + f'TAG_GITIGNORE_{lic_TAG} := "{lic_ID}",',
    )



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

ALL_GITIGNORES = [
{code}
]
        """.strip()
        +
        '\n'
    )


print(f"{TAB_1}* ``gitignore.py`` updated.")
