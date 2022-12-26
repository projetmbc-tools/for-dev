#!/usr/bin/env python3

from btools.B01 import *


SRC_DIR = addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src.config.jngflavours import *


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

README_DIR       = PROJECT_DIR / 'readme'
FLAVOURS_MD_FILE = README_DIR / 'flavours.md'


FLAVOURS_PY_CONTENT = (
    SRC_DIR / "src" / "config" / "jngflavours.py"
).read_text(
    encoding = 'utf-8'
)

TEMPL_BEFORE = """
# -- {flname} -- #
# {deco} #
#
""".strip()

AFTER = """
#
# Last change:
""".strip()


TEMPL_ONE_FLAVOUR = """
#### Flavour `{flname}`

> **Short description:** {desc}

  1. **Extensions for the auto-detection, and possible tools for the templates.**

      * {exts}

      * {tools}

  1. **Variables** are typed `{var}`.

  1. **Using `jinja` instructions.**

      * {instr_inline}

      * {instr_block}

  1. **Writing comments.**

      * {comment_inline}

      * {comment_block}
""".strip()


# ----------- #
# -- TOOLS -- #
# ----------- #

def instr_comment_text(
    isinline,
    kind,
    desc,
    tag_start,
    tag_end = ""
):
    style = 'inline' if isinline else 'block'

    if tag_start is None:
        text = f"No {style} {kind} are available."

    else:
        if tag_end:
            tag_end       = f' {tag_end}'
            several_lines = ', on several lines if needed'

        else:
            several_lines = ''

        text = (
            f"{style.title()} {kind} are typed "
            f"`{tag_start} ...{tag_end}` where "
            f"`...` symbolizes {desc}{several_lines}."
        )

    return text


# ----------------- #
# -- THE CONTENT -- #
# ----------------- #

print(f'{TAB_1}* README - "flavours.md" - Building the content.')

content = []

for flname, specs in JINJA_TAGS.items():
    print(f'{TAB_2}+ Flavour "{flname}" found.')

# Description.
    _, desc, _ = between(
        text = FLAVOURS_PY_CONTENT,
        seps = [
            TEMPL_BEFORE.format(
                flname = flname.upper(),
                deco   = '-'*(2*3 + len(flname))
            ),
            AFTER
        ]
    )

    desc = desc.strip()
    desc = desc[1:].strip()
    desc = desc[0].lower() + desc[1:]

# Extensions.
    exts = AUTO_FROM_EXT[flname]

    if exts == ['*']:
        exts = (
            "Any extension not associated to any other flavour is "
            "associated to this flavour which is like a default one."
        )

    else:
        plurals = (len(exts) != 1)

        exts = ", ".join(f"`{e[2:].upper()}`" for e in exts)

        if plurals:
            i    = exts.rfind(',') + 1
            exts = exts[:i] + ' or' + exts[i:]

        exts = (
            f"Files having extensions {exts} are "
             "associated to this flavour."
        )

# Tools.
    tools = (
        (
             "Tools to assist in typing templates are available: "
            f"see the folder `jng-extra-tools/{flname}`."
        )
        if WITH_EXTRA_TOOLS[flname] else
        "No tools are available to assist in typing templates."
    )

# Variables.
    var = f"{specs[TAG_VAR_START]} one_jinja_var {specs[TAG_VAR_END]}"

# Instructions.
    instr_inline = instr_comment_text(
        isinline  = True,
        kind      = 'instructions',
        desc      = 'some `Jinja` instructions',
        tag_start = specs[TAG_INLINE_INSTR]
    )

    instr_block = instr_comment_text(
        isinline  = False,
        kind      = 'instructions',
        desc      = 'some `Jinja` instructions',
        tag_start = specs[TAG_BLOCK_INSTR_START],
        tag_end   = specs[TAG_BLOCK_INSTR_END]
    )

# Comments.
    comment_inline = instr_comment_text(
        isinline  = True,
        kind      = 'comments',
        desc      = 'comments only for the template',
        tag_start = specs[TAG_INLINE_COMMENT]
    )

    comment_block  = instr_comment_text(
        isinline  = False,
        kind      = 'comments',
        desc      = 'comments only for the template',
        tag_start = specs[TAG_BLOCK_COMMENT_START],
        tag_end   = specs[TAG_BLOCK_COMMENT_END]
    )

# New piec of content.
    content.append(
        TEMPL_ONE_FLAVOUR.format(
            flname         = flname,
            desc           = desc,
            exts           = exts,
            tools          = tools,
            var            = var,
            instr_inline   = instr_inline,
            instr_block    = instr_block,
            comment_inline = comment_inline,
            comment_block  = comment_block
        )
    )

content = '\n\n'.join(content)


# ---------------------------- #
# -- UPDATING "flavours.md" -- #
# ---------------------------- #

print(f'{TAB_1}* README - "flavours.md" - Updating the content.')

before, _ , after = between(
    text = FLAVOURS_MD_FILE.read_text(encoding = 'utf-8'),
    seps = [
        '<!-- FLAVOURS - TECH. DESC. - START -->',
        '<!-- FLAVOURS - TECH. DESC. - END -->'
    ],
    keepseps = True,
)

FLAVOURS_MD_FILE.write_text(
    data     = f"{before}\n\n{content}\n\n{after}",
    encoding = 'utf-8'
)
