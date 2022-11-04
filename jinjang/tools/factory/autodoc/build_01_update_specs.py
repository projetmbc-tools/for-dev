#!/usr/bin/env python3

TODO

from distutils.log import info
from mistool.os_use     import PPath as Path
from mistool.string_use import between
from mistool.term_use   import DirView, PPath


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR


CONTRIB_DIR = PROJECT_DIR / 'contribute'
README_FILE = 'README.md'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# --------------- #
# -- LET'S GO! -- #
# --------------- #

def keepthis(info):
    # if info['depth'] == 2:
    #     print(info)

    if info['ppath'].name == '.DS_Store':
        return False

    if (
        info['depth'] == 2
        and
        not info['ppath'].is_dir()
        and
        info['ppath'].parent.name == 'changes'
    ):
        return True

    if info['depth'] > 1:
        return False

    return True


def shortdirview(folder):
    dirview = DirView(
        ppath   = folder,
        sorting = "filefirst",
    )
    dirview.buildviews()

    shortlisview = [
        info
        for info in dirview.listview
        if keepthis(info)
    ]

    dirview.listview = shortlisview

    return dirview.ascii


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ---------------------- #
# -- RULES OF THE API -- #
# ---------------------- #

print(f"{TAB_1}* Contributions: working on ``README`` files.")

for folder in CONTRIB_DIR.glob('*'):
    if not folder.is_dir():
        continue

    name = folder.name

    readmefile = folder / README_FILE


    if not readmefile.is_file():
        print(f"{TAB_2}+ Dir ``{name}`` : no ``README`` file.")
        continue


    asciidirview = shortdirview(folder)


    before, _, after = between(
        text = readmefile.read_text(
            encoding = 'utf-8'
        ),
        seps = [
            '<!-- FOLDER STRUCT. AUTO - START -->',
            '<!-- FOLDER STRUCT. AUTO - END -->',
        ],
        keepseps = True
    )

    asciidirview = asciidirview.replace('\n', '\n' + ' '*4)

    content = f"""
{before}

    {asciidirview}

{after}
""".strip() + '\n'*2

    readmefile.write_text(
        data     = content,
        encoding = 'utf-8'
    )

    print(f"{TAB_2}+ Dir ``{name}`` :``README`` file updated.")
