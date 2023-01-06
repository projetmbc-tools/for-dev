#!/usr/bin/env python3

from datetime import date
from pathlib  import Path

from cbdevtools.addfindsrc import addfindsrc
from mistool.string_use    import between


# --------------- #
# -- CONSTANTS -- #
# --------------- #

JINJANG_DIR = addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src import JNGBuilder


THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

DOC_FILE = JINJANG_DIR / "doc" / "content" / "how-to" / "python" / "files2files.txt"

MAGIC_COMMENT = "// -- RENDER - LOCAL VARS - AUTO LIST - {kind} -- //"


# -------------- #
# -- SPEAKING -- #
# -------------- #

TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ---------------- #
# -- LET'S WORK -- #
# ---------------- #

print(f'{TAB_1}* Doc of the method JNBuilder.render.')

last_content = DOC_FILE.read_text(encoding = "utf-8")

before, _, after = between(
    text     = last_content,
    keepseps = True,
    seps     = [
        MAGIC_COMMENT.format(kind = 'START'),
        MAGIC_COMMENT.format(kind = 'END'),
    ]
)

tab = " "*8

last_list = [
    tab + f"* python::``{lv}``\n"
    for lv in sorted(JNGBuilder._RENDER_LOC_VARS)
]
last_list = '\n'.join(last_list)
last_list = f"\n\n{last_list}\n"

new_content = before + last_list + after

if new_content == last_content:
    print(f'{TAB_2}+ No update needed.')

else:
    print(f'{TAB_2}+ New list added.')

    before, _, after = between(
        text     = new_content,
        keepseps = True,
        seps     = [
            "this::\n    date =",
            "==",
        ]
    )

    today = date.today()

    print(f'{TAB_2}+ New date for the doc file: {today}.')

    new_content = before + f" {today}\n\n\n" + after

    DOC_FILE.write_text(
        data     = new_content,
        encoding = "utf-8"
    )
